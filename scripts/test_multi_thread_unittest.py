"""1.python多线程实现并发执行测试用例
   2.基于unittest框架
       unittest本身不支持多线程所以需要二次开发
   3.java的testNg和python的pytest支持多线程（非常鉴定单）
   4.注意运行要用 python test_multi_thread_unittest.py 在命令行运行

   """
import threading
import unittest
from time import sleep

from selenium import webdriver


class TestMultiThreading(unittest.TestCase):
    def __init__(self, methodName, browser=None):
        super().__init__(methodName=methodName)
        self.browser = browser

    def test_browser1(self):
        """测试多浏览器"""
        if self.browser == 'chrome':
            print("chrome+++++")
            driver = webdriver.Chrome()
            driver.get("http://www.baidu.com")
            sleep(2)
            driver.quit()
        elif self.browser == 'firefox':
            print("firefox+++++")
            driver = webdriver.Firefox()
            driver.get("http://www.baidu.com")
            sleep(2)
            driver.quit()

    def test_browser2(self):
        if self.browser == 'chrome':
            print("bbbbbbb++++chrome")
            driver = webdriver.Chrome()
            driver.get("http://www.baidu.com")
            sleep(2)
            driver.quit()
        elif self.browser == 'firefox':
            print("bbbbbb+++++firefox")
            driver = webdriver.Firefox()
            driver.get("http://www.baidu.com")
            sleep(2)
            driver.quit()


def suite1(browser):
    """测试套件1"""
    suite = unittest.TestSuite()
    suite.addTest(TestMultiThreading('test_browser1', browser=browser))
    unittest.TextTestRunner().run(suite)


def suite2(browser):
    """测试套件2"""
    suite = unittest.TestSuite()
    suite.addTest(TestMultiThreading('test_browser2', browser=browser))
    unittest.TextTestRunner().run(suite)


def create_thread(target, args):
    t = threading.Thread(target=target, args=args)
    t.start()
    return t


if __name__ == '__main__':
    """运行不能直接点if的运行，要通过unittest运行"""
    # t_chrome = threading.Thread(target=suite, args=('chrome',))
    # t_chrome1 = threading.Thread(target=suite1, args=('chrome',))
    # t_firefox = threading.Thread(target=suite, args=('firefox',))
    # t_firefox1 = threading.Thread(target=suite1, args=('firefox',))
    # # t_chrome.start()
    # t_firefox.start()
    # t_chrome1.start()
    # t_firefox1.start()
    # t_chrome.join()
    # t_firefox.join()
    # t_chrome1.join()
    # t_firefox1.join()
    lists = [(suite1, ('chrome',)), (suite1, ('firefox',)), (suite2, ('chrome',)), (suite2, ('firefox',))]
    lists_thread = list()
    for i in lists:
        lists_thread.append(create_thread(*i))
    # for i in lists_thread:
    #     i.start()
    for i in lists_thread:
        i.join()
