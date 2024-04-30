import sys
print(sys.executable)
import unittest
import time
from ..client import RainbowClientWrapper
from ..wrapper import RainbowWrapper

class TestKVWrapper(unittest.TestCase):
	def setUp(self) -> None:
			self.client = RainbowClientWrapper(app_id="",
			                                   user_id='', secret_key='')
			self.kv = RainbowWrapper(self.client,
													group="spark.public_kv_test")
			self.tb = RainbowWrapper(self.client,
														group="spark.public_table_test")
			self.files = RainbowWrapper(self.client,
														group="spark.public_file_test")


	def test_get_kv_value(self):
			v1 = self.kv.get_kv_value(
					'test_date', 
     			default_value='test')
			v2 = self.kv.get_kv_value(
								'test_json', 
								default_value='test')
			v3 = self.kv.get_kv_value(
								'test_number', 
								default_value='test')
			v4 = self.kv.get_kv_value(
								'test_string', 
								default_value='test')
			v5 = self.kv.get_kv_value(
								'test_text', 
								default_value='test')
			v6 = self.kv.get_kv_value(
								'test_xml', 
								default_value='test')
			v7 = self.kv.get_kv_value(
								'test_yaml', 
								default_value='test')
			print(f"type: {type(v1)}, value: {v1}")
			print(f"type: {type(v2)}, value: {v2}")
			print(f"type: {type(v3)}, value: {v3}")
			print(f"type: {type(v4)}, value: {v4}")
			print(f"type: {type(v5)}, value: {v5}")
			print(f"type: {type(v6)}, value: {v6}")
			print(f"type: {type(v7)}, value: {v7}")
   
	def test_get_tb_value(self):
		print(self.tb.get_tb_value("test"))
  
	def test_get_file_value(self):
			def hello_world(data):
				print('hello world')
			def goodbay(data):
				print('goodbay')
			self.files.add_listener(hello_world)
			self.files.add_listener(goodbay)
			file_data = self.files.get_file_value(default_value="test")
			print(file_data.file_datas[0].data)
			time.sleep(1)
   
	# def test_get_file_value_callbacks(self):
	# 		def hello_world(data):
	# 				print('hello world')
	# 		def goodbay(data):
	# 			print('goodbay')
	# 		self.files.add_listener(hello_world)
	# 		self.files.add_listener(goodbay)
	# 		max_retries = 20  # 设置最大重试次数
	# 		for i in range(max_retries):
	# 				try:
	# 						file_data = self.files.get_file_value(default_value="test")
	# 						print(file_data.file_datas[0].data)
	# 						time.sleep(5)  # 休眠5秒
	# 						# 可以在这里添加更多的逻辑来决定是否继续循环
	# 				except Exception as e:
	# 						print(f"An error occurred: {e}")
	# 						if i < max_retries - 1:
	# 								time.sleep(1)  # 等待一段时间后重试
	# 						else:
	# 								raise  # 重试失败，抛出异常


   
			














