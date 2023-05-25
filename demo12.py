# Selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
# 驱动管理器
from webdriver_manager.chrome import ChromeDriverManager
# os
from time import sleep

# Selenium 执行 Js 脚本
class TestCase(object):
    def __init__(self, url):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get(url)
    
    # 使用execute_script 同步执行（常用）
    def test1(self):
        self.driver.execute_script("alert('test')")
        sleep(1)
        self.driver.switch_to.alert.accept()
    
    # 使用 Js 脚本获取标题名 
    def test2(self):
        js = 'return document.title'
        title = self.driver.execute_script(js)
        sleep(1)
        print(title)
    
    # 使用 Js 脚本修改元素属性
    def test3(self):
        js = 'var q = document.getElementById("kw"); q.style.border="2px solid red"'
        self.driver.execute_script(js)
        sleep(1)

    # 使用 Js 脚本实现操作滚动条
    def test4(self):
        self.driver.find_element(By.ID, 'kw').send_keys('selenium')
        sleep(1)
        self.driver.find_element(By.ID, 'su').click()
        sleep(1)
        js = 'window.scrollTo(0, document.body.scrollHeight)'
        self.driver.execute_script(js)
        sleep(1)


if __name__ == '__main__':
    case = TestCase('https://baidu.com/')
    case.test1()
    case.test2()
    case.test3()
    case.test4()
