#coding=utf-8
import sys
import os
base_path = os.path.abspath('..') + '\\util'
sys.path.append(base_path)
sys.path.append('..')
from util.find_element import FindElement

class LoginHandle:
	def __init__(self,driver,filename):
		self.fd = FindElement(driver,filename)

	def usernameElement(self):
		return self.fd.get_element('login','username')

	def passwordElement(self):
		return self.fd.get_element('login','password')

	def loginBtElement(self):
		return self.fd.get_element('login','loginButton')

	def toRegisterElement(self):
		return self.fd.get_element('login','toRegister')

	def forgetPwdElement(self):
		return self.fd.get_element('login','forgetPwd')

	def homePageMyName(self):
		return self.fd.get_element('home','myname')

	def sendUsername(self,username):
		self.usernameElement().clear()
		self.usernameElement().send_keys(username)

	def sendPassword(self,password):
		self.passwordElement().clear()
		self.passwordElement().send_keys(password)

	def clickLoginBt(self):
		self.loginBtElement().click()

	def clickToRegister(self):
		self.toRegisterElement().click()

	def clickForgetPwd(self):
		self.forgetPwdElement().click()


		

if __name__ == '__main__':
	from selenium import webdriver
	from time import sleep
	driver = webdriver.Chrome()
	driver.get('http://www.18crm.com')
	a = LoginHandle(driver,'../config/LocalElement.ini')
	a.sendUsername('亚克@test')
	a.sendPassword('61075058')
	a.clickLoginBt()
	sleep(2)
	driver.switch_to_alert().accept()
	print(a.homePageMyName().text)
	