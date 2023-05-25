# 1. 导包
# 1. 导入包
from time import sleep
# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
# 驱动管理器
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


# 2. 使用类进行封装测试对象
class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def test(self):
        self.driver.get('http://www.baidu.com')
        sleep(1)
        self.driver.find_element("id", "kw").send_keys('selenium')
        sleep(2)
        self.driver.find_element("id", "su").click()
        sleep(3)
        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()
    case.test()
