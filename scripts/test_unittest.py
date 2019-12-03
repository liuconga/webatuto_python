# coding=utf-8
"""unittest"""
import json
import sys
import time

import yaml
from parameterized import parameterized

from tool import HTMLTestRunner

sys.path.append('../')
import unittest
import tool


class TestDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('Class----->Start')

    @classmethod
    def tearDownClass(cls):
        print('Class------>End')

    def setUp(self):
        # self.driver = tool.DriverUtil.get_driver()
        # self.driver.get('http://www.baidu.com')
        print('Method------->Start')

    def tearDown(self):
        tool.DriverUtil.quit_driver()
        print('Method-------->End')

    def test_logger(self):
        """测试日志工具方法"""
        logger = tool.Logger.get_logger()
        logger.error("error+++++++++-------")

    def test_assert(self):
        """测试unittest的断言"""
        self.assertEqual(1, 2)
        self.assertIn(1, [1, 2, 3])
        self.assertTrue(1 == 2)
        self.assertIsNone(None)

        # 以下为通过assert关键字进行断言
        assert 1 in [1, 2, 3, 4]
        assert 1 == 2

        # 以下为捕获异常并截图
        try:
            assert 1 == 2
        except Exception as e:
            # 将捕获错误截图保存到image中
            self.driver.get_screenshot_as_file('../image/{}.png'.format(time.strftime('%Y-%m-%d_%H:%M:%S')))
            # 将不获的异常抛出
            raise e

    # 1.@parameterized.expand(['1','2','3'])
    # 2.@parameterized.expand(data())
    # 3.data=['1','2','3']
    #   @parameterized.expand(data)
    data = ['1', '2', '3']

    @parameterized.expand(data)
    def test_parameterized(self, x):
        """使用parameterized实施参数化"""
        """unittest本身不支持参数化所以使用parameterized"""
        print("我执行了", x)

    @unittest.skip('未完成所以跳过啦')
    # @unittest.skipIf(1>2,'条件满足跳过啦')
    def test_skip(self):
        """测试跳过"""
        print("我没被跳过")

    def test_htmlTestRunner(self):
        """测试生成html测试报告"""
        suite = unittest.TestSuite()
        suite.addTest(TestDemo('test_add1'))
        with open('../report/a.html', 'wb') as f:
            HTMLTestRunner(f, 1, '我是测试报告', '你好我是描述').run(suite)

    def test_data_json(self):
        """测试读取json文件之数据驱动"""
        # 1.读取json中数据
        with open('../data/data.json') as f:
            data = json.load(f)
            # data的类型由json文件来决定：如果json中是对象会解析成字典类型
            # 如果json中是数组形式，会解析成列表类型；
            print(type(data[1]))
        # 2.将数据写入json文件
        a = {1: 2, 3: 4}  # 会自动将字典转换成json形式，比如json中键必须是字符串
        with open('../data/data_ddt.json', 'w') as f:
            json.dump(a, f)

        # 3.将字典转换成json以字符串形式输出
        dict1 = {1: 2, 3: 4}
        data = json.dumps(dict1)
        print(data)  # type(data)为字符串

        # 4.将json转换成字典
        str1 = '{"1":2,"3":4,"bool3":false}'
        data = json.loads(str1)
        print(data)  # {'1': 2, '3': 4, 'bool3': False}
        """python中false为首字母大写，json中首字母是小写"""

    def test_txt(self):
        """测试读取txt文件"""
        txt: list = []
        new_txt: list = []
        with open('../data/data.txt') as f:
            # 通过readlines读取所有行
            txt = f.readlines()
            # 拆解字符串
            i: str
            for i in txt:
                new_txt.append(tuple(i.strip().split(',')))
        new_txt = new_txt[1:]
        print(new_txt)

    def test_yaml(self):
        # 将列表或字典写入yaml
        dict1 = [{"username1": {'name': '刘聪', 'age': 18}, "username2": {'name': 'ccc', 'age': 18}},
                 {"username3": {'name': 'aaa', 'age': 18}, "username4": {'name': 'bbbb', 'age': 18}}]
        with open('../data/data.yaml', 'w')as f:
            # encoding:如果有中文的情况要写,allow_unicode:如果不写，中文会以unicode码形式写入yaml文件
            yaml.dump(dict1, f, allow_unicode=True, encoding='utf-8')

        # 读取yaml中内容
        with open('../data/data.yaml', 'r')as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            print(data, type(data), sep='--')  # 输出为列表类型


if __name__ == '__main__':
    """此为执行方式2："""
    print(sys.path)
    unittest.main()
