import unittest

from scripts.test_unittest import TestDemo

a = 1
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

if a == 2:
    """TestLoader添加测试用例"""
    # 方式1：
    suite = unittest.TestLoader().discover("./", pattern='test_unittest.py')
    # 运行搜到的测试用例组成的测试套件
    unittest.TextTestRunner().run(suite)

    # 方式2：
    # suite = unittest.defaultTestLoader.discover("./", pattern='test_unittest.py')
    # unittest.TextTestRunner().run(suite)
