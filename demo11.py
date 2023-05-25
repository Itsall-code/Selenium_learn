# Selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
# 驱动管理器
from webdriver_manager.chrome import ChromeDriverManager
# os
from time import sleep


class TestCase(object):
    def __init__(self, url):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get(url)

    def test_mourse(self):
        # 单击
        btn = self.driver.find_element(By.XPATH, '/html/body/form/input[3]')
        ActionChains(self.driver).click(btn).perform()
        sleep(2)

        # 双击
        btn = self.driver.find_element(By.XPATH, '/html/body/form/input[2]')
        ActionChains(self.driver).double_click(btn).perform()

        # 右键
        btn = self.driver.find_element(By.XPATH, '/html/body/form/input[4]')
        ActionChains(self.driver).context_click(btn).perform()
        sleep(5)

    def test_move(self):
        ele = self.driver.find_element(By.ID, 's-usersetting-top')
        sleep(1)
        # 鼠标移动
        ActionChains(self.driver).move_to_element(ele).perform()
        sleep(2)
        self.driver.find_element(By.LINK_TEXT, '高级搜索').click()
        sleep(3)

    def test_drop(self):
        dragger = self.driver.find_element(By.ID, 'dragger')
        item2 = self.driver.find_element(By.XPATH, '/html/body/div[3]')
        item3 = self.driver.find_element(By.XPATH, '/html/body/div[4]')
        # 使用drag_and_drop(起点元素，终点元素),实现拖拽
        ActionChains(self.driver).drag_and_drop(dragger, item3).perform()
        sleep(1)
        # 使用click_and_hold(起点元素).release(终点元素),实现拖拽
        ActionChains(self.driver).click_and_hold(dragger).release(item2).perform()
        sleep(2)

    def test_key(self):
        kw = self.driver.find_element(By.NAME, 't2')
        sleep(1)
        # 输入
        kw.send_keys('selenium')
        sleep(1)
        # Ctrl + A
        kw.send_keys(Keys.CONTROL, 'a')
        sleep(1)
        # Ctrl + X
        kw.send_keys(Keys.CONTROL, 'x')
        sleep(1)
        # Ctrl + V
        kw.send_keys(Keys.CONTROL, 'v')
        sleep(1)


if __name__ == '__main__':
    # case_mourse = TestCase('https://sahitest.com/demo/clicks.htm')
    # case_mourse.test_mourse()

    # case_move = TestCase('https://baidu.com/')
    # case_move.test_move()

    # case_drop = TestCase('https://sahitest.com/demo/dragDropMooTools.htm')
    # case_drop.test_drop()

    case_key = TestCase('https://sahitest.com/demo/keypress.htm')
    case_key.test_key()
