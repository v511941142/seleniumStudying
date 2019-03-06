import sys
import os
base_path = os.path.abspath('..') + '\\util'
sys.path.append(base_path)
sys.path.append('..')
from selenium import webdriver
from util.find_element import FindElement

class WebdriverUtil:

	def switchWindow(self,driver,oldHandle,allHandle):
		for handle in allHandle:
			if handle != oldHandle:
				driver.switch_to.window(handle)
				return driver

	def switchFrame(self,driver,section,key):
		fd = FindElement(driver,'../config/LocalElement.ini')
		driver.switch_to.frame(fd.get_element(section,key))
		return driver