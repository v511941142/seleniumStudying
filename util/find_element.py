#coding=utf-8
import sys
sys.path.append('..')
from read_ini import ReadIni

class FindElement:
	def __init__(self,driver,filename):
		self.driver = driver
		self.rd = ReadIni(filename)

	def get_element(self,section,key):
		ele_info = self.rd.get_value(section,key)
		by = ele_info.split('>')[0]
		value = ele_info.split('>')[1]
		if by == 'id':
			element = self.driver.find_element_by_id(value)
		elif by == 'xpath':
			element = self.driver.find_element_by_xpath(value)
		elif by == 'class':
			element = self.driver.find_element_by_class_name(value)
		elif by == 'link_text':
			element = self.driver.find_element_by_link_text(value)
		return element

if __name__ == '__main__':

	from selenium import webdriver
	driver = webdriver.Chrome()
	driver.get('http://www.18crm.com')

	a = FindElement(driver,'../config/LocalElement.ini').get_element('login','toRegister')
	a.click()
	print(a)