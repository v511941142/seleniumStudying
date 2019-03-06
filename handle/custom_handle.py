#coding=utf-8
import sys
import os
base_path = os.path.abspath('..') + '\\util'
sys.path.append(base_path)
sys.path.append('..')
from common.webdriver_util import WebdriverUtil
from util.find_element import FindElement
from selenium.webdriver import ActionChains
from time import sleep
class CustomHandle:
	def __init__(self,driver):
		self.fd = FindElement(driver,'../config/LocalElement.ini')
		self.util = WebdriverUtil()
		self.base = CommonUtil()
		self.driver = driver

	def toCustom(self):
		#点击"我的客户"
		ActionChains(self.driver).move_to_element(self.fd.get_element('custom','custom')).perform()
		self.fd.get_element('custom','myCustom').click()
		#切换到主Frame
		self.util.switchFrame(self.driver,'frame','mainframe')
		return self.driver

	def clickAdd(self):
		self.driver = self.toCustom()
		#点击新增按钮
		oldHandle = self.driver.current_window_handle
		self.fd.get_element('custom','add').click()
		#切换到新弹出的"新增客户"页面
		allHandle = self.driver.window_handles
		self.util.switchWindow(self.driver,oldHandle,allHandle)
		return self.driver

	def addCustom(self,username,notnull):
		self.driver = self.clickAdd()
		#输入姓名、必填项，点击确定 ,username,notnull
		self.fd.get_element('custom','customName').send_keys(username)
		self.fd.get_element('custom','notNullText').send_keys(notnull)
		self.fd.get_element('custom','save').click()

	def getFirstCustom(self):
		return self.fd.get_element('custom','fistCustom').text

	def getSecondCustom(self):
		return self.fd.get_element('custom','secondCustom').text

	def getCountCustom(self):
		element = self.fd.get_element('custom','totalCustom')
		return element.get_attribute('value')

	def deleteCustom(self):
		print(self.getCountCustom())
		self.fd.get_element('custom','checkCustom').click()
		self.fd.get_element('custom','deleteCustom').click()
		self.base.acceptAlert(self.driver)
		sleep(5)
		self.base.acceptAlert(self.driver)
		sleep(5)
		print(self.getCountCustom())

		
		



		

if __name__ == '__main__':
	from common.common_util import CommonUtil

	driver = CommonUtil().login()
	a = CustomHandle(driver)
	a.toCustom()
	print(a.deleteCustom())

	