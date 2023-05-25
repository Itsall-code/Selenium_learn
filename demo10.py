# 导包
# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait # 显式等待
from selenium.webdriver.support import expected_conditions as EC # 期望结果
# 驱动管理器
from webdriver_manager.chrome import ChromeDriverManager
# os
import os


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = 'file:///'+path+'/test_wait.html'
        self.driver.get(file_path)

    def test(self):
        self.driver.find_element(By.ID, 'btn').click()
        wait = WebDriverWait(self.driver, 3)

        wait.until(EC.text_to_be_present_in_element((By.ID, 'id2'), 'id 2'))
        print(self.driver.find_element(By.ID, 'id2').text)
        print('ok')


if __name__ == '__main__':
    case = TestCase()
    case.test()
