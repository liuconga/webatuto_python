# coding=utf-8
import unittest
import sys, os
print(sys.path)
sys.path.append(os.getcwd() + '/scripts/test_unittest.py')
print(sys.path)
from scripts.test_unittest import TestDemo
from tool import HTMLTestRunner

a = 3
if a == 1:
    """TestSuite添加测试用例"""
    suite = unittest.TestSuite()
    # 添加单个测试方法
    suite.addTest(TestDemo('test_add1'))
    # 添加多个测试方法
    # suite.addTests([TestDemo('test_add'), TestDemo('test_logger')])
    # 添加所有测试方法
    # suite.addTest(unittest.makeSuite(TestDemo))
    # 运行测试套件
    unittest.TextTestRunner().run(suite)

elif a == 2:
    """TestLoader添加测试用例"""
    # 方式1：
    suite = unittest.TestLoader().discover("./", pattern='test_unittest.py')
    # 运行搜到的测试用例组成的测试套件
    unittest.TextTestRunner().run(suite)

    # 方式2：
    # suite = unittest.defaultTestLoader.discover("./", pattern='test_unittest.py')
    # unittest.TextTestRunner().run(suite)
elif a == 3:

    """TestLoader添加测试用例并生成HTML测试报告"""
    suite = unittest.TestLoader().discover("./scripts/", pattern='test_ddt.py')
    # 运行搜到的测试用例组成的测试套件
    with open('./report/HTMLTestRunner.html', 'wb') as f:
        HTMLTestRunner(stream=f, verbosity=1, title=u'unittest测试报告', description=u'unittest-ddt测试报告').run(suite)
