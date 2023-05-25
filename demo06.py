# 1.导包
# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# 系统参数
import os
from time import sleep

class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = 'file:///'+path+'/forms2.html'
        self.driver.get(file_path)

    def test_checkbox(self):
        # 取得chekbox中的swimming元素
        swimming = self.driver.find_element(By.NAME, 'swimming')
        # 选中
        if not swimming.is_selected():
            swimming.click()
        reading = self.driver.find_element(By.NAME, 'reading')
        if not reading.is_selected():
            reading.click()
        sleep(3)
        #反选
        swimming.click()
        sleep(2)
        reading.click()
        sleep(3)
        # self.driver.quit()

    def test_radio(self):
        # 对于同名元素的查找定位使用 find_elements 方法
        gender = self.driver.find_elements(By.NAME, 'gender')
        gender[0].click()
        sleep(2)
        gender[1].click()
        sleep(3) 


if __name__ == '__main__':
    case = TestCase()
    case.test_checkbox()
    case.test_radio()