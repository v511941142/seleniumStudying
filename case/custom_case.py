import sys
sys.path.append('..')
from bussiness.customer_bussiness import CustomerBussiness
from common.common_util import CommonUtil
from handle.custom_handle import CustomHandle

class CustomCase:
	def __init__(self):
		self.driver = CommonUtil().login()
		self.customer_b = CustomerBussiness(self.driver)
		self.custom_h = CustomHandle(self.driver)
		self.base = CommonUtil()
		

	def custom_test01(self):
		# 不输入姓名保存
		result = self.customer_b.addCustom(userName='',notNullText='123')
		return self.base.verifyTextMatch(self.driver,result,'客户姓名不能为空')

	def custom_test02(self):
		# 不输入必填项保存
		result = self.customer_b.addCustom(userName='123',notNullText='')
		return self.base.verifyTextMatch(self.driver,result,'必填测试不能为空')

	def custom_test03(self):
		# 新增成功
		userName = self.base.getUniqueName()
		notNullText = self.base.getUniqueName()
		result = self.customer_b.addCustom(userName,notNullText)
		return self.base.verifyTextContain(self.driver,result,'新增成功')



#新增成功
#必填测试不能为空
if __name__ == '__main__':
	print(CustomCase().custom_test01())
	print(CustomCase().custom_test02())
	print(CustomCase().custom_test03())
