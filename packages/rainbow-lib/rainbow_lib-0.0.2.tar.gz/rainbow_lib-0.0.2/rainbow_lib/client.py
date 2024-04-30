#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : wrapper.py
# Author            : kylinmiao <kylinmiao@tencent.com>
# Date              : 29.04.2024
from rainbow_cpplib.rainbow_client import RainbowClient

class RainbowClientWrapper:
    def __init__(self, app_id, user_id, secret_key):
        self._user_id = user_id
        self._secret_key = secret_key
        self._app_id = app_id
        self._client = None  # 将client作为实例变量
        self._init_rainbow()

    def _init_rainbow(self):
        init_param = {
            "connectStr":"api.rainbow.woa.com:8080",
            "isUsingPolaris":False,
            "fileCachePath":"./",
            "tokenConfig": {
                "isOpenSign": True,
                "app_id": self._app_id,
                "user_id": self._user_id,
                "secret_key": self._secret_key,
            },
        }
        self._client = RainbowClient(init_param)  
        
    def get_configs(self, group, env_name="Default"):
        return self._client.get_configs(group, env_name)
     
    def add_listener(self, group, env_name="Default", callback=None):
        self._client.add_listener(group, env_name, callback)
        
    @property
    def client(self):
        return self._client
	