import sys
import os
sys.path.append('..')
from time import sleep
from common.common_util import CommonUtil
from selenium.webdriver import ActionChains
from common.webdriver_util import WebdriverUtil

driver = CommonUtil().login()
ActionChains(driver).move_to_element(driver.find_element_by_link_text('客户')).perform()
sleep(2)
driver.find_element_by_link_text('我的客户').click()

xf = driver.find_element_by_xpath('//*[@id="mainframe_18crm"]')
driver.switch_to.frame(xf)


driver.find_element_by_xpath(r"//*[@id='table_maindata']/tbody/tr[3]/td[1]/input[1]").click()
