#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
执行用例
"""
import unittest, time
import os
from plugins import HTMLTestRunner

# 或者将HTMLTestRunner文件拷贝到Python安装目录里的Lib文件夹下
# import HTMLTestRunner

# 获取路径
cur_path = os.path.dirname(os.path.realpath(__file__))
# 测试用例路径
case_path = os.path.join(cur_path, 'case')
# 测试报告路径
report_path = os.path.join(cur_path, 'report')

if __name__ == "__main__":
    # 构造测试集
    suite = unittest.defaultTestLoader.discover(case_path,'test*.py')
    # 获取当前时间
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    # 定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(title='自动化测试报告',
                                          description='用例执行情况：',
                                          stream=open(report_path + '\\' + now + ' HTMLReport.html', 'wb'),
                                          verbosity=2
                                          )
    # 运行测试用例
    runner.run(suite)
