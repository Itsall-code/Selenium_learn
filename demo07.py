# 导包
# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
# 驱动管理器
from webdriver_manager.chrome import ChromeDriverManager
# os
import os
from time import sleep


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = 'file:///'+path+'/forms3.html'
        self.driver.get(file_path)
    
    def test_select(self):
        # 单选
        se1 = self.driver.find_element(By.ID, 'provise')
        select1 = Select(se1)
        # 根据索引选中
        select1.select_by_index(1)
        sleep(1)
        # 根据元素值
        select1.select_by_value('sh')
        sleep(1)
        # 根据文本内容
        select1.select_by_visible_text('BeiJing')
        sleep(1)

        #  多选
        se2 = self.driver.find_element(By.ID, 'skill')
        select2 = Select(se2)
        # 实现方法1
        for i in range(3):
            select2.select_by_index(i)
            sleep(1)
        sleep(2)
        select2.deselect_all()
        sleep(2)
        # 实现方法2
        # select2.options 存放了元素的所有选项，以列表的形式实现
        for option in select2.options:
            option.click()
            sleep(1)
        # option的一些属性
        # 所有选项
        print(select2.all_selected_options)
        print('\n')
        # 一个选项
        print(select2.first_selected_option)


if __name__ == '__main__':
    case = TestCase()
    case.test_select()
 
