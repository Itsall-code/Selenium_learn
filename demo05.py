# 1.导包
# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
# 驱动管理器
from webdriver_manager.chrome import ChromeDriverManager
# os 包用来读取路径
import os
from time import sleep


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # 获取当前项目路径所在的文件夹
        path = os.path.dirname(os.path.abspath(__file__))
        # print(path)
        # 对字符串进行拼接，取得项目文夹的html路径)
        file_path = 'file:///'+path+'/forms.html'
        # print(file_path)
        self.driver.get(file_path)
    
    def test_login(self):
        self.driver.find_element(By.ID, 'username').send_keys('admin')
        self.driver.find_element(By.ID, 'pwd').send_keys('123')
        sleep(2)
        self.driver.find_element(By.ID, 'submit').click()
        sleep(3)


if __name__ == '__main__':
    case = TestCase()
    case.test_login()
