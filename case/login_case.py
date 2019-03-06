import sys
sys.path.append('..')
from bussiness.login_bussiness import LoginBussiness
from handle.login_handle import LoginHandle
from common.common_util import CommonUtil
from util.read_ini import ReadIni
from selenium import webdriver

class LoginCase:
	def __init__(self):
		self.driver = webdriver.Chrome()
		self.driver.get('http://www.18crm.com')
		self.login_b = LoginBussiness(self.driver,'../config/LocalElement.ini')
		self.login_h = LoginHandle(self.driver,'../config/LocalElement.ini')
		self.rd = ReadIni('../config/TestData.ini')
		self.base = CommonUtil()
	
	def login_test01(self):
		'''
		不输入用户名、密码登录
		提示：用户账号格式为： 用户名@公司简称
		'''
		result = self.login_b.loginTest(self.rd.get_value('login','test01_username'),self.rd.get_value('login','test01_password'))
		return self.base.verifyTextMatch(self.driver,result,self.rd.get_value('login','test01_expect'))

	def login_test02(self):
		'''
		手机格式错误登录：130
		提示：输入的手机号格式不正确!
		'''
		result = self.login_b.loginTest(self.rd.get_value('login','test02_username'),self.rd.get_value('login','test02_password'))
		return self.base.verifyTextMatch(self.driver,result,self.rd.get_value('login','test02_expect'))

	def login_test03(self):
		'''
		用户名、密码错误：manager@test , 123456
		提示：用户名或密码错误
		'''
		result = self.login_b.loginTest(self.rd.get_value('login','test03_username'),self.rd.get_value('login','test03_password'))
		return self.base.verifyTextMatch(self.driver,result,self.rd.get_value('login','test03_expect'))

	def login_test04(self):
		'''
		企业号未开通登录:manager@999 , 123
		提示：企业号：999 不正确，或者您还没有开通软件，请点击“我要购买”进行开通
		'''
		result = self.login_b.loginTest(self.rd.get_value('login','test04_username'),self.rd.get_value('login','test04_password'))
		return self.base.verifyTextMatch(self.driver,result,self.rd.get_value('login','test04_expect'))

	def login_test05(self):
		'''
		登陆成功:manager@test , 123
		进入首页,姓名 == manager
		'''
		self.login_b.loginTest(self.rd.get_value('login','test05_username'),self.rd.get_value('login','test05_password'))
		try:
			result = self.login_h.homePageMyName().text
		except:
			result = ''
		return self.base.verifyTextMatch(self.driver,result,self.rd.get_value('login','test05_expect'))
	

if __name__ == '__main__':

	#print(LoginCase().login_test01())
	#print(LoginCase().login_test02())
	#print(LoginCase().login_test03())
	#print(LoginCase().login_test04())
	print(LoginCase().login_test05())
	#print(LoginCase().test())


