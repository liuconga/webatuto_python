import pytest
import allure
from allure.pytest_plugin import AllureHelper

from tool.read_data import ReadData


class TestPyTest(object):
    @classmethod
    def setup_class(cls):
        """类级别开始"""
        print('class-->start----')

    @classmethod
    def teardown_class(cls):
        """类级别结束"""
        print('class-->end----')

    def setup(self):
        """方法级别开始"""
        print('method-->start----')

    def teardown(self):
        """方法级别结束"""
        print('method-->end----')

    """测试方法顺序"""
    @pytest.mark.run(order=2)
    def test2(self):
        # 给allure添加描述
        allure.description(description='我是描述')
        print('我是测试方法1111')

    # @AllureHelper.step(title="我是步骤。。。。。")
    @allure.step(title="我是描述。。。。你们好呀")
    @pytest.mark.run(order=1)
    def test1(self):
        allure.attach("我是测试步骤", "1")
        print('我是测试方法22222')
        allure.attach("我是步骤","2")

    @pytest.mark.parametrize("username,password,yzm", ReadData.read_xml('data.xml'))
    def test_xml(self, username, password, yzm):
        print(username + password + yzm)
