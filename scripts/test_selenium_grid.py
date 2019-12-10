import threading
from time import sleep

from selenium import webdriver


class TestSeleniumGrid(object):

    def test_firefox(self):
        caps = {}
        caps['platform'] = 'ANY'
        caps['browserName'] = 'firefox'
        caps['version'] = '70'
        driver = webdriver.Remote('http://127.0.0.1:4444/wd/hub', desired_capabilities=caps)
        driver.implicitly_wait(5)
        driver.get('http://www.jd.com')
        sleep(3)
        # driver.find_element_by_id('kw').send_keys('你好')
        # driver.find_element_by_id('su').click()
        driver.quit()

    def test_chrome(self):
        caps = {}
        caps['platform'] = 'ANY'
        caps['browserName'] = 'chrome'
        driver = webdriver.Remote('http://127.0.0.1:4444/wd/hub', desired_capabilities=caps)
        driver.implicitly_wait(5)
        print(driver.session_id)
        driver.get('http://www.baidu.com')
        driver.find_element_by_id('kw').send_keys('你好')
        driver.find_element_by_id('su').click()
        driver.quit()
    def test_chrome1(self):
        caps = {}
        caps['platform'] = 'ANY'
        caps['browserName'] = 'chrome'
        driver = webdriver.Remote('http://127.0.0.1:4444/wd/hub', desired_capabilities=caps)
        driver.implicitly_wait(5)
        print(driver.session_id)
        driver.get('http://www.baidu.com')
        driver.find_element_by_id('kw').send_keys('你好')
        driver.find_element_by_id('su').click()
        driver.quit()

    def test_firefox1(self):
        caps = {}
        caps['platform'] = 'ANY'
        caps['browserName'] = 'firefox'
        caps['version'] = '71'
        driver = webdriver.Remote('http://127.0.0.1:4444/wd/hub', desired_capabilities=caps)
        driver.implicitly_wait(5)
        driver.get('http://www.baidu.com')
        driver.find_element_by_id('kw').send_keys('你好')
        driver.find_element_by_id('su').click()
        driver.quit()

    # def test_browser(self, browser):
    #     caps = {}
    #     caps['platform'] = 'ANY'
    #     caps['browserName'] = browser
    #     self.driver = webdriver.Remote('http://127.0.0.1:4444/wd/hub', desired_capabilities=caps)
    #     self.driver.implicitly_wait(5)
    #     self.driver.get('http://www.baidu.com')
    #     self.driver.find_element_by_id('kw').send_keys('你好')
    #     self.driver.find_element_by_id('su').click()
    #     self.driver.quit()
    #
    # def test_bingfa(self):
    #     t1 = threading.Thread(target=self.test_browser, args=('chrome',) )
    #     t2 = threading.Thread(target=self.test_browser, args=('chrome',) )
    #     t3 = threading.Thread(target=self.test_browser, args=('chrome',) )
    #     t1.start()
    #     t2.start()
    #     t3.start()
    #     t1.join()
    #     t2.join()
    #     t3.join()
    # def test_bingfa(self):
    #     t1 = threading.Thread(target=self.test_firefox )
    #     t2 = threading.Thread(target=self.test_firefox1)
    #     t3 = threading.Thread(target=self.test_chrome)
    #     t4 = threading.Thread(target=self.test_chrome1)
    #     t1.start()
    #     t2.start()
    #     t3.start()
    #     t4.start()
    #     t1.join()
    #     t2.join()
    #     t3.join()
    #     t4.join()
