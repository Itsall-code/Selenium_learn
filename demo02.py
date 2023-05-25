# 1. 导入包
from time import sleep
# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
# 驱动管理器
from webdriver_manager.chrome import ChromeDriverManager


# 2. 创建一个测试类
class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        ## 传递url
        self.driver.get('http://www.baidu.com')
        sleep(1)
    
    # 3.1 id元素定位
    def test_click(self):
        self.driver.find_element('id', 'su').click()
        sleep(2)
        self.driver.quit()

    def find_id(self):
        # 通过id查找可以获得唯一值
        self.driver.find_element('id', 'kw').send_keys('Selenium')

    def test_id(self):
        self.find_id()
        self.test_click()

    # 3.2. name元素定位
    def test_name(self):
        # 通过name 查找可能会返回多个元素，返回第一个值
        # find_elements方法 会返回一个集合
        self.driver.find_element('name', 'wd').send_keys('selfnium')
        self.test_click()

    # 3.3. link_text元素定位
    def test_link_text(self):
        self.find_id()
        self.driver.find_element('id', 'su').click()
        sleep(2)
        self.driver.find_element('link text', '百度首页').click()
        sleep(3)
        self.driver.quit()

    # 3.4. partial_link_text 部分文本连接定位
    def test_partial_link_text(self):
        self.find_id()
        self.driver.find_element('id', 'su').click()
        sleep(2)
        self.driver.find_element('partial link text', '首页').click()
        sleep(3)
        self.driver.quit()

    # 3.5. xpath 定位
    def test_xpath(self):
        self.driver.find_element('xpath', '//*[@id="kw"]').send_keys('selenium')
        self.test_click()

    # 3.6 tag 定位
    # tag 定位一般少用，因为难定位
    def test_tag(self):
        input0 = self.driver.find_element('tag name', 'input')[0]
        print(input0)

    # 3.7 csS_selector 定位
    def test_css_selector(self):
        self.driver.find_element('css selector', '#kw').send_keys('selenium')         
        self.test_click()

    # 3.8 class_name 定位
    def test_class_name(self):
        self.driver.find_element('class name', 's_ipt').send_keys('selenium')
        self.test_click()


if __name__ == '__main__':
    case = TestCase()
    # case.test_id()
    # case.test_name()
    # case.test_link_text()
    # case.test_partial_link_text()
    # case.test_xpath()
    # case.test_tag()
    # case.test_css_selector()
    case.test_class_name()
