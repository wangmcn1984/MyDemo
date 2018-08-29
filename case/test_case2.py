#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
测试用例2
"""
from selenium import webdriver
import unittest

class Test2(unittest.TestCase):
    '''测试用例2测试'''
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_01(self):
        '''成功用例'''
        self.driver.get('https://www.baidu.com')
        self.driver.find_element_by_id('kw').send_keys('百度一下')

    def test_02(self):
        '''成功用例'''
        self.driver.get('https://cn.bing.com/')

if __name__ == '__main__':
    unittest.main(verbosity=2)
