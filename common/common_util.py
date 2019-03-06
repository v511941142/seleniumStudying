import sys
import os
base_path = os.path.abspath('..') + '\\util'
sys.path.append(base_path)
sys.path.append('..')
import inspect
import datetime
import string
import random
from selenium import webdriver
from util.read_ini import ReadIni
from util.find_element import FindElement

class CommonUtil:

	def login(self,broswer='Chrome'):
		'''
		公用登录方法
		'''
		if broswer == 'Chrome':
			driver = webdriver.Chrome()
		driver.get('http://www.18crm.com')
		driver.maximize_window()
		fd = FindElement(driver,'../config/LocalElement.ini')
		rd = ReadIni('../config/TestData.ini')
		fd.get_element('login','username').send_keys(rd.get_value('public_login','username'))
		fd.get_element('login','password').send_keys(rd.get_value('public_login','password'))
		fd.get_element('login','loginButton').click()
		self.acceptAlert(driver)
		return driver

	def acceptAlert(self,driver):
		try:
			driver.switch_to_alert().accept()
		except:
			return 'No alert display'

	def getAlertText(self,driver):
		try:
			return driver.switch_to_alert().text
		except:
			return 'No alert text display'

	def verifyTextMatch(self,driver,actualText,expectText):
		if actualText == expectText:
			return inspect.stack()[1][3] + ' ----->>> pass' 
		else:
			self.screenShot(driver)
			return inspect.stack()[1][3] + ' ----->>> fail'  + ' : screenshot done'

	def verifyTextContain(self,driver,actualText,expectText):
		if expectText.lower() in actualText.lower():
			return inspect.stack()[1][3] + ' ----->>> pass' 
		else:
			self.screenShot(driver)
			return inspect.stack()[1][3] + ' ----->>> fail'  + ' : screenshot done'

	def screenShot(self,driver):
		now_time = datetime.datetime.now().strftime('%Y-%m-%d')
		pic_path = '..\\screenshot\\' + inspect.stack()[2][3] + '----' + now_time + '.png'
		driver.get_screenshot_as_file(pic_path)

	def getAlphaNumeric(self,length,type='letter'):
		CaseList = []
		if type == 'lower':
			case = string.ascii_lowercase
		elif type == 'upper':
			case = string.ascii_uppercase
		elif type == 'digits':
			case = string.digits
		elif type == 'mix':
			case = string.ascii_letters + string.digits
		else:
			case = string.ascii_letters
		for i in range(length):
			CaseList.append(random.choice(case))
		return ''.join(CaseList)

	def getUniqueName(self,charCount=6,type='mix'):
		return self.getAlphaNumeric(charCount,type)



		


if __name__ == '__main__':
	#from selenium import webdriver
	#from time import sleep
	#driver = webdriver.Chrome()
	#driver.get('http://www.18crm.com')
	#driver.find_element_by_id('usercode').send_keys('13080661661')
	#driver.find_element_by_id('loginbtn').click()
	print(CommonUtil().getUniqueName(10))
	#CommonUtil().getAlphaNumeric(3,'lower')