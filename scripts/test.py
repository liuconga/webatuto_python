from selenium import webdriver

if __name__ == '__main__':
        caps = {}
        caps['platform'] = 'ANY'
        caps['browserName'] = 'chrome'
        driver = webdriver.Remote('http://127.0.0.1:4445/wd/hub', desired_capabilities=caps)
        driver.implicitly_wait(5)
        driver.get('http://www.baidu.com')
        driver.find_element_by_id('kw').send_keys('你好')
        driver.find_element_by_id('su').click()
        driver.quit()