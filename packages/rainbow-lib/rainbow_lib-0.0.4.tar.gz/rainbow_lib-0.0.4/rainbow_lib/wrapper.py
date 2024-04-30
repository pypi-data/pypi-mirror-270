#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : wrapper.py
# Author            : kylinmiao <kylinmiao@tencent.com>
# Date              : 29.04.2024
# Last Modified Date: 29.04.2024
# coding: utf-8
import json
import time
from datetime import datetime
from enum import Enum
import xml.etree.ElementTree as ET
import random
from typing import NamedTuple, List
import traceback
from functools import wraps

import yaml
from .client import RainbowClientWrapper

class ConfigType(Enum):
    KV = 0
    TABLE = 1   
    FILE = 2
    
# 文件结构
class FileMetadata(NamedTuple):
  file_version: str
  is_editable: bool
  is_gbk: bool
  md5: str
  mtime: str
  name: str
  size: int
  type: str
  content: str
  url: str
  secret_key: str
  secret_key_md5: str
    
class FileData(NamedTuple):
  name: str
  metadata: FileMetadata
  compress: str
  type: int
  data: bytes 
    
class FileList(NamedTuple):
    file_datas: List[FileData]
    tmp_dir: str 

class RainbowWrapper:
  """
  A wrapper class for interacting with rainbow, providing a simple interface to get configs
  """
  class DataType(Enum):
    """
      different data types for kv data
    """
    DATE = 18
    JSON = 4
    NUMBER = 1
    STRING = 2
    TEXT = 3
    XML = 5
    YAML = 20     

  def __init__(self, 
              client: RainbowClientWrapper,
              group: str, 
              env_name: str ="Default",
              max_retries = 3,
              logger=None):
    """
    Initializes the RainbowWrapper

    Args:
        client (RainbowClientWrapper): An instance of RainbowClientWrapper
        group (str): Group name on rainbow site
        env_name (str, optional): Env name on rainbow site. Defaults to "Default".
        max_retries (int, optional): The maximum number of retries for fetching configurations. Defaults to 3.
        logger (_type_, optional): An optional logger instance for logging messages. Defaults to rainbow's logger.
    """
    
    self._client = client
    self._group = group
    self._env_name = env_name
    self._max_retries = max_retries
    self._data = {}
    self._version, self._version_name = None, None
    self._callbacks = []
    self._logger=logger or self._default_logger()
    self._initialize_configs()
    

  def add_listener(self, callback=None):
    """
    Add a callback to listen for config changes. When the config changes, the callback will be called according to the sequcence of adding.
    
    The callback must be a function that accepts a single argument, which will be the updated config data.
    
    Exapmle of a callback function:
      def callback(data):
        # Process the updated config data
        pass
    
    The callback will be called immediatedly after the RainbowWrapper initialized
    
    Args:
        callback (callable, optional): The function to be called when the configuration changes. Defaults to None.
    
    Raises:
        ValueError: If the provided callback is not callable.
    """
    if callable(callable):
      self._callbacks.append(callback)
    else:
      raise ValueError('Invalid callback, callback must be callable')
    
  def get_kv_value(self,
                  key: str,
                  default_value: str,
  ):
    """get kv value by key

    Args:
        key (str): key 
        default_value (str): if get failed, return default_value
        data_type (DataType, optional): _description_. Defaults to None.

    Returns:
        _type_: _description_
    """
    kv = self._data.get(key)
    if not kv:
      return default_value
    
    kv_data_type = kv.get('data_type')
    value = kv.get('value')
    return self._parse_kv_value(value, kv_data_type, default_value)
  
  def get_tb_value(self,
                   default_value: str
  ) -> list:
    return self._data
  
  def get_file_value(self,
                     default_value: str
  ) -> FileList:
    return self._data

  def _initialize_configs(self):
    self._fetch_configs()
    self._add_listener(self._update_configs_callback)

  def _default_logger(self):
    from rainbow_cpplib.utils import logger
    return logger

  def _fetch_configs(self):
    retry_num = 0
    max_retries = self._max_retries
    wait_time = 1 # 初始等待时间
    max_wait_time = 30 # 最大等待时间
    
    while retry_num < max_retries:
      try:
        raw_configs = self._client.get_configs(group=self._group, env_name=self._env_name)
        self._log_info(f'Got configs: {raw_configs}')
        if raw_configs and raw_configs.get('code') == 0:
          self._log_info('Got configs successfully')
          self._parse_configs(raw_configs)
          return
        else:
          raise ValueError("Failed to get configs with error code: {}".format(raw_configs.get('code', 'Unknown')))
      except Exception as e:
        if retry_num >= max_retries:
          err = f'Max retries exceeded while getting configs: {max_retries}'
          self._log_error(err)
          traceback.print_exc()
          raise RuntimeError(err) from e
        # 指数退避 + 随机化退避
        sleep_time = random.uniform(0, wait_time)
        time.sleep(sleep_time)
        
        # 增加重试次数与等待时间
        retry_num += 1
        wait_time *= 2
        wait_time = min(wait_time, max_wait_time)
        self._log_warn(f"Retrying get_configs after {sleep_time:.2f}s, retry times: {retry_num}")

  def _parse_configs(self, raw_configs):
      data_list = raw_configs.get('data', [])
      if data_list and isinstance(data_list, list) and isinstance(data_list[0], dict):
          struct_type = ConfigType(data_list[0].get('struct_type'))
          self._version = data_list[0].get('version')
          self._version_name = data_list[0].get('version_name')
          self._log_info(f"Got version: {self._version}, version_name: {self._version_name}, struct_type: {struct_type}")
          if struct_type == ConfigType.KV:
            self._data = {kv['key']: kv for kv in data_list[0].get('key_values', [])}
            self._log_info(f"Got kv info success : {self._data}")
          elif struct_type == ConfigType.TABLE:
            column_names = [name['column'] for name in data_list[0].get('column_types', {})]
            table_data = []
            for row in data_list[0].get('rows', []):
              row_data = {}
              row = json.loads(row)
              for name in column_names:
                row_data[name] = row.get(name, "")
              table_data.append(row_data)
            self._data = table_data
            self._log_info(f"Got table info success : {self._data}")
          elif struct_type == ConfigType.FILE:
            self._data = self._parse_file_value(data_list[0])
            self._log_info(f"Got files success : {self._data}")
          else:
            self._log_warn(f"Unsupported struct_type: {struct_type}")
      else:
          raise ValueError("Invalid configs data format")

  @property
  def version(self):
    return self._version
  
  @property
  def version_name(self):
    return self._version_name
  
  @property
  def max_retries(self):
    return self._max_retries
  
  def _update_configs_callback(self, data):
      try:
        self._fetch_configs()
        self._log_info(f"Configs updated, {datetime.now()}, callback_val: {data}, class_val: {self._data}")
        for callback in self._callbacks:
          try:
            self._log_info(f"Invoking callback {callback.__name__}")
            self._measure_exection_time(callback)(self._data)
          except Exception as e:
            err_msg = f"Failed to call callback{callback.__name__}: {e}"
            self._log_error(err_msg)
            traceback_str = traceback.format_exc()
            self._log_error(f"Traceback:\ntraceback_str{traceback_str}")
            
      except Exception as e:
        err_msg = f"Failed to update configs: {e}"
        self._log_error(err_msg)
        raise RuntimeError(err_msg) from e
      
  def _add_listener(self, 
                  callback=None):
    """when configs updated, call callback

    Args:
        callback (_type_, optional): callback. Defaults to None.
    """
    self._client.add_listener(group=self._group, env_name=self._env_name, callback=callback)
        
  def _parse_kv_value(self, 
                      value: str, 
                      data_type: int, 
                      default_value: str) :
    try:
      if data_type == self.DataType.DATE.value:
        return datetime.strptime(value, "%Y-%m-%d")
      elif data_type == self.DataType.NUMBER.value:
        return float(value)
      elif data_type in [self.DataType.STRING.value,self.DataType.TEXT.value]:
        return value
      elif data_type == self.DataType.JSON.value:
          return json.loads(value)
      elif data_type == self.DataType.XML.value:
          return ET.fromstring(value)
      elif data_type == self.DataType.YAML.value:
          return yaml.safe_load(value)
    except Exception as e:
      self._log_error(f"Failed to parse value: {e}")
      return default_value
      
  def _parse_file_value(self, data: dict) -> FileList:
    try:
      file_datas = [
          FileData(
              name=item['name'],
              metadata=FileMetadata(
                    **item['metadata']
              ),
              compress=item.get('compress', ''),  # 使用get方法提供默认值
              type=item['type'],
              data=item['data']  # 假设data字段是字节串
          )
          for item in data['file_list']['file_datas']
      ]
      tmp_dir = data['file_list']['tmp_dir']
      file_list = FileList(
        file_datas=file_datas,
        tmp_dir=tmp_dir
      )
      return file_list
    except Exception as e:
      err = f"Failed to parse file_list: {e}"
      self._log_error(err)
      raise ValueError(err) from e
    
  
  def _log_error(self, 
                  message: str):
    if self._logger:
      self._logger.error(message)
    else:        
      print(message)
      
      
  def _log_info(self, 
                  message: str):
    if self._logger:
      self._logger.info(message)
    else:        
      print(message)

  def _log_warn(self, 
                  message: str):
    if self._logger:
      self._logger.warning(message)
    else:        
      print(message)
      
  def _measure_exection_time(self, func):
    @wraps(func)
    def wrapper(*args, **kwargs):
      start_time = time.perf_counter()
      result = func(*args, **kwargs)
      end_time = time.perf_counter()
      self._log_info(f"Callback {func.__name__} executed in {end_time - start_time:.4f} seconds")
      return result
    return wrapper
  

  
    