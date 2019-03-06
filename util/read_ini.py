#coding=utf-8

import configparser

class ReadIni:
	def __init__(self,filename):
		self.fp = configparser.ConfigParser()
		self.fp.read(filename)

	def get_value(self,section,key):
		return self.fp.get(section,key)

if __name__ == '__main__':
	a = ReadIni('../config/LocalElement.ini').get_value('login','toRegister')
	print(a)
