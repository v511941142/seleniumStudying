#coding=utf-8
import sys
import os
base_path = os.path.abspath('..') + '\\util'
sys.path.append(base_path)
sys.path.append('..')
from common.webdriver_util import WebdriverUtil
from common.common_util import CommonUtil
from util.find_element import FindElement
from selenium.webdriver import ActionChains
from time import sleep
class CustomHandle:
	def __init__(self):
		self.base = CommonUtil()
		#self.fd = FindElement(driver,'../config/LocalElement.ini')
		self.util = WebdriverUtil()

	def toCustom(self):
		driver = self.base.login()
		fd = FindElement(driver,'../config/LocalElement.ini')
		ActionChains(driver).move_to_element(fd.get_element('custom','custom')).perform()
		fd.get_element('custom','myCustom').click()
		return driver
	
	def addCustom(self):
		driver = self.toCustom()
		oldHandle = driver.current_window_handle
		fd = FindElement(driver,'../config/LocalElement.ini')
		ActionChains(driver).move_to_element(fd.get_element('custom','custom')).perform()
		fd.get_element('custom','myCustom').click()

		self.util.switchFrame(driver,'frame','mainframe')

		fd.get_element('custom','add').click()

		allHandle = driver.window_handles
		self.util.switchWindow(driver,oldHandle,allHandle)
		fd.get_element('custom','customName').send_keys('hjkl')
		sleep(2)



		

if __name__ == '__main__':

	CustomHandle().addCustom()

	