# Selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
# 驱动管理器
from webdriver_manager.chrome import ChromeDriverManager
# 系统参数
import os
from time import sleep, strftime, localtime, time

# Selenium 屏幕截图
class TestCase(object):
    def __init__(self, url):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get(url)

    def test1(self):
        self.driver.find_element(By.ID, 'kw').send_keys('selenium')
        self.driver.find_element(By.ID, 'su').click()
        sleep(2)
        # 使用 save_screenshot 截图，截图文件在当前文件所在路径
        # self.driver.save_screenshot('baidu.png')
        # 一般为了可读性，会使用测试时间作为测试截图的名字
        # 调用 strftime() 格式化时间
        st = strftime("%Y-%m-%d-%H-%M-%S", localtime(time()))
        file_name = st + '.png'
        self.driver.save_screenshot(file_name)
        
        # 使用 save_screenshot_as_file 截图，参数文件路径
        # 使用专门文件夹存放截图
        # 获取当前路径
        path = os.path.abspath('screenshot')
        # 生成截图路径
        file_path = path + '/' + file_name
        self.driver.get_screenshot_as_file(file_path)
        
if __name__ == '__main__':
    case = TestCase('https://baidu.com/')
    case.test1()
