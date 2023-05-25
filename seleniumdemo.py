# 一个简单的selenium程序
 
# 1. 导入包
# selenium 4
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# 2. 创建webdriver驱动
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
sleep(1)

# 3. 获取url
driver.get("https://www.baidu.com/")
sleep(1)

# 4. 定位输入元素，并使用send_keys方法输入keywords
driver.find_element("id", "kw").send_keys("selenium")
sleep(1)

# 5. 定位搜索元素, 并使用click方法点击
driver.find_element("id", "su").click()
sleep(5)

# 6. 自动化结束，关闭浏览器
driver.quit()

