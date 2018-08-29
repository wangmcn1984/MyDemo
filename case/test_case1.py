#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
测试用例1
"""
from selenium import webdriver
import unittest

class Test1(unittest.TestCase):
    '''测试用例1测试'''
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_01(self):
        '''失败用例'''
        self.driver.get('https://www.baidu.com')
        self.driver.find_element_by_id('kw1').send_keys('百度一下')
        self.assertTrue(True)

    def test_02(self):
        '''失败用例'''
        self.driver.get('https://mail.126.com/')
        self.assertIn('163',self.driver.title)

    def test_03(self):
        '''成功用例'''
        self.driver.get('https://cn.bing.com/')
        self.assertIn('Bing',self.driver.title)

if __name__ == '__main__':
    unittest.main(verbosity=2)
