# 1. 导包
from time import sleep
# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
# 驱动管理器
from webdriver_manager.chrome import ChromeDriverManager


class TestCase(object):

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        sleep(1)
        self.driver.get(self.url)
    
    def test_webelement_prop(self, element_class, element_name):
        # 使用find_element 定位元素后，会返回一个WedElement对象
        # 该对象用来描述Web页面的一个元素
        e = self.driver.find_element(element_class, element_name)
        print(type(e)) # 一个element 类
        print(e.id) # 元素id 唯一值
        print(e.tag_name) # 标签名
        print(e.size) # 元素宽高
        print(e.rect) # 元素宽高与坐标
        print(e.text) # 元素的文本内容

    def test_webelement_method(self, element_class, element_name):
        e = self.driver.find_element(element_class, element_name)
        sleep(1)
        # 输入内容
        e.send_keys('input by selenium')
        # 常用
        # 输出获取元素的值
        print(e.get_attribute('value'))
        # 输出获取元素的类型
        print(e.get_attribute('type'))
        # 输出获取元素的名称
        print(e.get_attribute('name'))
        
        # 少用
        # 输出获取元素的css字体
        print(e.value_of_css_property('font'))
        # 输出获取元素的css颜色
        print(e.value_of_css_property('color'))
        
        sleep(3)
        # 清空输入内容
        e.clear()

    def test_windows(self):
        self.driver.find_element(By.LINK_TEXT, '新闻').click()
        windows = self.driver.window_handles

        while 1:
            for w in windows:
                self.driver.switch_to.window(w)
                sleep(2)


if __name__ == '__main__':
    demo_case = TestCase('http://sahitest.com')
    demo_case.test_webelement_prop(By.LINK_TEXT, 'demo')
    
    Link_text_case = TestCase('http://sahitest.com/demo/linkTest.htm')
    Link_text_case.test_webelement_prop(By.ID, 't1')
    Link_text_case.test_webelement_method(By.ID, 't1')

    windows_case = TestCase('http://www.baidu.com')
    windows_case.test_windows()
