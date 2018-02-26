# coding:utf-8

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest

class TestCheckAds(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.dr = cls.load_chrome()

    @classmethod
    def tearDownClass(cls):
        cls.dr.quit()

    @classmethod
    def load_chrome(cls, option='headless'): # option = headless or normal
        options = Options()
        options.add_argument('disable-infobars')
        if option == 'headless':
            options.add_argument('--headless')  # 无界面模式
            options.add_argument('--disable-gpu')
        return webdriver.Chrome(chrome_options=options)


    def check_keyward(self, keyward, ads_title, page_title):
        # dr = webdriver.Chrome()
        options = Options()
        options.add_argument('disable-infobars')   
        options.add_argument('--headless')  # 无界面模式
        options.add_argument('--disable-gpu')
        dr = webdriver.Chrome(chrome_options=options)

        dr.get("http://m.sm.cn/s?q=%s&from=ws&by=submit&snum=6" % keyward)
        try:
            dr.find_element_by_partial_link_text(ads_title).click()
        except NoSuchElementException:
            print('关键字: \'%s\', 无法定位到广告标题！' % keyward)
        # print(page_title,type(page_title))
        # print(dr.title,type(page_title))
        if page_title in dr.title:
            print('关键字: \'%s\', 广告正常展示！' % keyward)
        else:
            print('关键字: \'%s\', 广告页面标题与参数不符！'% keyward)


    def load_data(self, data_file):
        try:
            # if not python3, need import codecs and use codecs.open(data_file, encoding='utf-8-sig')
            with open(data_file,encoding='utf-8') as f:
                return f.readlines()
        except IOError:
            print("数据文件 \'%s\', 打开失败" % data_file)


    def test_ads(self, data_file='data.txt'):
        
        for line in self.load_data(data_file):
            if line[-1] == '\n':
                line = line[:-1]
            line = line.split(',')
            # print(line)
            self.check_keyward(line[0], line[1], line[2])


if __name__ == '__main__':  
    unittest.main(verbosity=1)