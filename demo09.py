# Selenium 的等待
## 固定等待 time.sleep
### 实际项目忌讳使用，影响性能
## 隐式等待 implicitly_wait
### 设置一个最长等待时间
### 缺点不太灵活
## 显式等待 WedDriverWait
### 由Selenium 提供 常用

# 1. 导包
# Selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 驱动管理器
from webdriver_manager.chrome import ChromeDriverManager
# sleep
from time import sleep


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        url = 'http://www.baidu.com'
        self.driver.get(url)

    def test_sleep(self):
        ## 不要在实际项目中使用
        self.driver.find_element(By.ID, 'kw').send_keys('selenium')
        sleep(2) # 线程阻塞
        self.driver.find_element(By.ID, 'su').click()
        sleep(3)

    def test_implicitly(self):
        ## 在代码开头定义
        self.driver.implicitly_wait(10)
        ## 若在项目中同时定义了显式与隐式等待，谁的时间长谁生效
        self.driver.find_element(By.ID, 'kw').send_keys('selenium')
        self.driver.find_element(By.ID, 'su').click()

    def test_wait(self):
        # WedDriverWait $1 为WebDriver类， $2 为等待时间， $3 为轮询时间默认0.5s
        wait = WebDriverWait(self.driver, 2)
        # 使用expected_conditions包进行期望等待（显式等待）
        # 在等待时间内（2s）直到出网页标题为‘百度一下。。。’，进行下一步，
        wait.until(EC.title_is('百度一下，你就知道'))
        self.driver.find_element(By.ID, 'kw').send_keys('selenium')
        self.driver.find_element(By.ID, 'su').click()
        # 显示等待 灵活 比较常用


if __name__ == '__main__':
    case = TestCase()
    # case.test_sleep()
    # case.test_implicitly()
    case.test_wait()
