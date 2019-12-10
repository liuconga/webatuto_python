"""pytest实现多线程
   1.pip install pytest-xdist
   2.xdist是多进程运行的，因为python的GLI所以多线程无意义
   3. 在pytest.ini 中配置参数： -n 并发数
   4.还可以通过写一个方法实现多线程
    """
import multiprocessing
import threading
import time
from time import sleep

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities


class TestMultiPyTest(object):

    def test_firefox(self):
        """测试多浏览器-火狐浏览器"""
        driver = webdriver.Firefox()
        driver.get("http://www.baidu.com")
        sleep(2)
        driver.quit()

    def test_firefox1(self):
        """测试多浏览器-火狐浏览器"""
        driver = webdriver.Firefox()
        driver.get("http://www.baidu.com")
        sleep(2)
        driver.quit()

    def test_chrome(self):
        """测试多浏览器-谷歌浏览器"""
        driver = webdriver.Chrome()
        driver.get("http://www.baidu.com")
        sleep(2)
        driver.quit()

    def test_chrome1(self):
        """测试多浏览器-谷歌浏览器"""
        driver = webdriver.Chrome()
        driver.get("http://www.baidu.com")
        sleep(2)
        driver.quit()

    # def test_browser(self, browser):
    #     """测试多浏览器"""
    #     if browser == 'chrome':
    #         print("chrome+++++")
    #         driver = webdriver.Chrome()
    #         driver.get("http://www.baidu.com")
    #         sleep(2)
    #         driver.quit()
    #     elif browser == 'firefox':
    #         print("firefox+++++")
    #         driver = webdriver.Firefox()
    #         driver.get("http://www.baidu.com")
    #         sleep(2)
    #         driver.quit()
    #
    # def test_multi_threading(self):
    #     """多线程-通过此测试方法实现多用例并行执行"""
    #     t1 = threading.Thread(target=self.test_browser, args=('chrome',))
    #     t2 = threading.Thread(target=self.test_browser, args=('firefox',))
    #     t1.start()
    #     t2.start()
    #     t1.join()
    #     t2.join()
    #
    # def test_multi_processing(self):
    #     """多进程-通过此测试方法实现多用例并行执行 python中多进程才能调到多核cpu"""
    #     t1 = multiprocessing.Process(target=self.test_browser, args=('chrome',))
    #     t2 = multiprocessing.Process(target=self.test_browser, args=('firefox',))
    #     t1.start()
    #     t2.start()
    #     t1.join()
    #     t2.join()
    #
    # def test_docker(self):
    #     desired_caps=DesiredCapabilities.CHROME
    #
    #     driver=webdriver.Remote('http://127.0.0.1:4444/wd/hub',desired_capabilities=desired_caps)
    #     driver.get('http://www.baidu.com')
    #     driver.find_element_by_id('kw').send_keys('你好')
    #     print("我打印了呀")
    #     driver.get_screenshot_as_file('error.png')
    #     time.sleep(2)
    #
    #     driver.quit()