# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from tools import cur_file_dir


class RENSHEN_GAME_AUTOMATION():
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option('useAutomationExtension',False)
        self.chrome_options.add_experimental_option("excludeSwitches",['enable-automation'])
        self.browser = webdriver.Chrome(options=self.chrome_options)
    def get_url(self,url='http://liferestart.syaro.io/view/index.html'):
        # print(url)
        self.browser.get(url)

    def load_json(self,update_exe_file_path='C:/Users/1/PycharmProjects/python_selenium_rensheng/update.exe',json_file_path = '"C:\\Users\\1\\PycharmProjects\\python_selenium_rensheng\\Remake_save.json"'):
        self.browser.implicitly_wait(3)
        # 加载参数
        self.browser.find_element(By.ID, 'load').click()
        time.sleep(1)
        # 这里可以对传参进行参数化
        os.system(update_exe_file_path+' '+json_file_path)
        time.sleep(2)

    def click_from_id(self,id,out_time,sleep_time):
        """
        通过id，点击元素
        :param id: 需要点击的网页id
        :param out_time: 等待查找id的时间
        :param sleep_time: 点击完成等待时间
        :return: None
        """
        self.browser.implicitly_wait(out_time)
        restart_b = self.browser.find_element(By.ID, id)
        restart_b.click()
        time.sleep(sleep_time)

    def await_click_from_id(self,await_out_time,check_time,id,sleep_time):
        """
        等待页面元素出现 通过id，点击元素
        :param await_out_time: 等待页面元素出现时间
        :param check_time: 检查时间 多长时间检查一次页面
        :param id: 需要点击的网页id
        :param sleep_time: 点击完成等待时间
        :return: None
        """
        self.browser.implicitly_wait(await_out_time)
        summary_b = WebDriverWait(self.browser, check_time).until(EC.presence_of_element_located((By.ID,id)))# 'summary'
        summary_b.click()
        time.sleep(sleep_time)

    def start_game(self):
        while True:
            # 重启人生
            self.click_from_id('restart',1,1)
            # 10连抽
            self.click_from_id('random', 1, 1)

            self.browser.implicitly_wait(3)
            # 选择天赋
            talents = self.browser.find_element(By.ID, 'talents')
            # 优先选择好的天赋 （可能吧）
            self.tag_num = 0
            a3 = talents.find_elements(By.CLASS_NAME, "grade3b")
            if a3:
                for i in a3:
                    i.click()
                    self.tag_num += 1
            no_list = ["不孕不育（你生不出孩子）","阴阳之外（天生无性别）" ]
            if self.tag_num < 3:
                a2 = talents.find_elements(By.CLASS_NAME, "grade2b")
                if a2:
                    for i in a2:
                        if i.text in no_list:
                            i.click()
                            self.tag_num += 1

            if self.tag_num < 3:
                a1 = talents.find_elements(By.CLASS_NAME, "grade1b")
                if a1:
                    for i in a1:
                        i.click()
                        self.tag_num += 1

            if self.tag_num < 3:
                a0 = talents.find_elements(By.CLASS_NAME, "grade0b")
                if a0:
                    for i in range(3 - self.tag_num):
                        a0[i].click()
                        self.tag_num += 1

            time.sleep(1)
            # next
            self.click_from_id('next', 3, 1)

            # random
            self.click_from_id('random', 1, 1)

            # start
            self.click_from_id('start', 1, 1)

            try:
                self.click_from_id('auto', 1, 1)
            except:
                pass
            # summary
            self.await_click_from_id(3000,3,"summary",1)

            # again
            self.click_from_id('again',1,0)
            self.tag_num = 0


if __name__ == '__main__':
    renshen_game_automation = RENSHEN_GAME_AUTOMATION()
    renshen_game_automation.get_url("http://liferestart.syaro.io/view/index.html")
    update_exe_file_path = os.path.join(cur_file_dir(),"update.exe")
    json_file_path = os.path.join(cur_file_dir(),"Remake_save.json")
    renshen_game_automation.load_json(update_exe_file_path,json_file_path)
    renshen_game_automation.start_game()