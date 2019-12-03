from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


class DriverUtil(object):
    # 给driver指定类型
    driver: WebDriver = None

    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            cls.driver = webdriver.Chrome()
            cls.driver.maximize_window()
        return cls.driver

    @classmethod
    def quit_driver(cls):
        if cls.driver is not None:
            cls.driver.quit()
            DriverUtil.driver = None
