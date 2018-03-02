#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
Created on 20180301
@author:wyl QQ635864540
python version 2.7
'''
__author__ = 'wyl QQ635864540'

import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sudokusolver

class ClsGetDetailSudoku:
	def __init__(self):
		self.filename = 'fromurl.txt'
		self.setUp()
		self.solver = sudokusolver.ClsSudokuSolver()
		self.username = 'email'
		self.pwd = 'password'
		self.loginurl = 'https://www.oubk.com/login'
		self.needsearchall = False
		
	def __del__(self):
		self.tearDown()
		
	def setUp(self):
		self.driver = webdriver.Chrome('c:\\python27\\scripts\\chromedriver.exe')
		
	def tearDown(self):
		raw_input('Press Enter key to end this process.\n')
		self.driver.close()
			
	def GetDetail(self):
		#time.sleep(460)
		self.Login()
		#time.sleep(200)
		if self.needsearchall:
			with open(self.filename,'r') as f:
				origurl = f.read()
			f.close()
			origurl = origurl.strip()
			for i in range(1, 148):
				url = origurl
				if url == '':
					continue
				url = url.format(i)
				print url
				try:
					driver = self.driver
					driver.get(url)
					array = []
					for lineindex in range(1,10):
						line = ''
						for columnindex in range(1,10):
							name = 'k{}s{}'
							name = name.format(columnindex,lineindex)
							element = driver.find_element_by_name(name)
							#element.send_keys(3)
							value = element.get_attribute('value')
							#print name
							if value == '':
								line += '.'
								#print '.'
							else:
								#print value
								line += value.strip()
						array.append(line)
					print array
					results = self.solver.Solver(array)
					print results
					if results is None:
						return
					for lineindex2 in range(1,10):
						for columnindex2 in range(1,10):
							name = 'k{}s{}'
							name = name.format(columnindex2,lineindex2)
							element = driver.find_element_by_name(name)
							#element.send_keys(3)
							value = element.get_attribute('value')
							#print name
							if value == '':
								ele = results[lineindex2-1][columnindex2-1]
								s = str(ele)
								#print ele
								element.click()
								element.send_keys(s)
					savebtn = driver.find_element_by_id('btSave')
					savebtn.click()
					time.sleep(1)
				except Exception as e:
					print 'Exception in GetDetail, error info:',str(e)
		else:
			with open(self.filename,'r') as f:
				results = f.readlines()
			f.close()
			for url in results:
				url = url.strip()
				if url == '':
					continue
				print url
				try:
					driver = self.driver
					driver.get(url)
					array = []
					for lineindex in range(1,10):
						line = ''
						for columnindex in range(1,10):
							name = 'k{}s{}'
							name = name.format(columnindex,lineindex)
							element = driver.find_element_by_name(name)
							#element.send_keys(3)
							value = element.get_attribute('value')
							#print name
							if value == '':
								line += '.'
								#print '.'
							else:
								#print value
								line += value.strip()
						array.append(line)
					print array
					results = self.solver.Solver(array)
					print results
					if results is None:
						return
					for lineindex2 in range(1,10):
						for columnindex2 in range(1,10):
							name = 'k{}s{}'
							name = name.format(columnindex2,lineindex2)
							element = driver.find_element_by_name(name)
							#element.send_keys(3)
							value = element.get_attribute('value')
							#print name
							if value == '':
								ele = results[lineindex2-1][columnindex2-1]
								s = str(ele)
								#print ele
								element.click()
								element.send_keys(s)
					savebtn = driver.find_element_by_class_name('btn_save')
					savebtn.click()
					time.sleep(1)
				except Exception as e:
					print 'Exception in GetDetail, error info:',str(e)
			
			
	def Login(self):
		try:
			driver = self.driver
			driver.get(self.loginurl)
			nameElement = driver.find_element_by_name('login_name')
			nameElement.send_keys(self.username)
			pwdElement = driver.find_element_by_name('password')
			pwdElement.send_keys(self.pwd)
			loginButton = driver.find_element_by_class_name('btn-large')
			loginButton.click()
		except Exception as e:
			print 'Exception in Login, error info:',str(e)
		
		
		
if __name__=='__main__':
	cls = ClsGetDetailSudoku()
	cls.GetDetail()
	#cls.Login()