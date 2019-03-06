import sys
sys.path.append('..')
from handle.login_handle import LoginHandle
from common.common_util import CommonUtil
from time import sleep
class LoginBussiness:
	def __init__(self,driver,filename):
		self.login_h = LoginHandle(driver,filename)
		self.util = CommonUtil()
		self.driver = driver

	def loginTest(self,username,password):
		self.login_h.sendUsername(username)
		self.login_h.sendPassword(password)
		self.login_h.clickLoginBt()
		alertText = self.util.getAlertText(self.driver)
		self.util.acceptAlert(self.driver)
		return alertText


if __name__ == '__main__':
	from selenium import webdriver
	from time import sleep
	driver = webdriver.Chrome()
	driver.get('http://www.18crm.com')
	print(LoginBussiness(driver,'../config/LocalElement.ini').loginTest('',''))
	print(LoginBussiness(driver,'../config/LocalElement.ini').loginTest('130',''))
	print(LoginBussiness(driver,'../config/LocalElement.ini').loginTest('130@616856',''))
	print(LoginBussiness(driver,'../config/LocalElement.ini').loginTest('123@999',''))