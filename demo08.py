# 导包
# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
# 驱动管理器
from webdriver_manager.chrome import ChromeDriverManager
# os
import os
from time import sleep


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = 'file:///'+path+'/test_alert.html'
        self.driver.get(file_path)
    
    def tets_alert(self):
        # 定位元素
        self.driver.find_element(By.ID, 'alert').click()
        # 切换到alert
        alert = self.driver.switch_to.alert
        print(alert.text)
        sleep(3)
        alert.accept()

    def tets_confirm(self):
        # 定位confirm
        self.driver.find_element(By.ID, 'confirm').click()
        # 切换到cofrim
        confirm = self.driver.switch_to.alert
        print(confirm.text)
        # confirm 内有两种方法 accept同意删除 dismiss取消
        # confirm.accept()
        sleep(3)
        confirm.dismiss()

    def tets_prompt(self):
        # 定位
        self.driver.find_element(By.ID, 'prompt').click()
        # 切换prompt
        prompt = self.driver.switch_to.alert
        print(prompt.text)
        sleep(3)
        prompt.accept()


if __name__ == '__main__':
    case = TestCase()
    # case.tets_alert()
    # case.tets_confirm()
    case.tets_prompt()
