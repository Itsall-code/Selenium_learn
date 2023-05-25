# 1. 导包
# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
# 驱动管理器
from webdriver_manager.chrome import ChromeDriverManager


# 2. 创建一个测试类
class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://www.baidu.com')
    
    # 属性
    def test_prop(self):
        print(self.driver.name) # 浏览器名称
        print(self.driver.current_ur) # url
        print(self.driver.title) # 页面标题
        print(self.driver.window_handles) # 窗口句柄
        print(self.driver.page_source) # 页面源码
        self.driver.quit()

    # 控制方法
    def test_method(self):
        self.driver.find_element(By.ID, 'kw').send_keys('selenium')
        self.driver.find_element(By.ID, 'su').click()
        self.driver.back() # 后退上一页
        self.driver.refresh() # 刷新页面
        self.driver.forward() # 前进一页
      #  self.driver.close() # 关闭当前页面
        # self.driver.quit() # 退出浏览器


if __name__ == '__main__':
    case = TestCase()
    # case.test_prop()
    case.test_method()
