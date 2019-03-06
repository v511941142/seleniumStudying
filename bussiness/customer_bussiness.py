import sys
sys.path.append('..')
from time import sleep
from common.common_util import CommonUtil
from handle.custom_handle import CustomHandle
from common.webdriver_util import WebdriverUtil

class CustomerBussiness:
	def __init__(self,driver):
		self.driver = driver
		self.custom_h = CustomHandle(self.driver)
		self.base = CommonUtil()
		self.util = WebdriverUtil()

	def addCustom(self,userName='',notNullText=''):
		self.custom_h.addCustom(userName,notNullText)
		sleep(2)	
		alertText = self.base.getAlertText(self.driver)
		sleep(2)
		self.base.acceptAlert(self.driver)

		#切换回原先的窗口,并切换到主表单,获取最新的客户姓名,来确认是否新增成功
		oldHandle = self.driver.current_window_handle
		allHandle = self.driver.window_handles
		self.util.switchWindow(self.driver,oldHandle,allHandle)

		#若失败可能是需要等待---> sleep(1)
		self.util.switchFrame(self.driver,'frame','mainframe')
		return alertText


if __name__ == '__main__':
	from common.common_util import CommonUtil
	driver = CommonUtil().login()
	print(CustomerBussiness(driver).addCustom(userName='222',notNullText='11'))