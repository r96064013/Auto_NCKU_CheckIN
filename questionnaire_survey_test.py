# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 11:46:44 2021

@author: Chi-Yee
"""

from selenium import webdriver
import random
import time
from time import sleep
import getpass
import csv
from datetime import datetime
import requests

headers = {"Authorization": "Bearer " + "DFFr19CQ6rd4UY9jjemSxyBtqoWtIDn8TNlWDPlpBjn","Content-Type": "application/x-www-form-urlencoded"}

def line_broadcast(text):
    params = {"message": text}
    requests.post("https://notify-api.line.me/api/notify",headers=headers, params=params)

def main():    
    driver = webdriver.Chrome()
    #driver.minimize_window()
    driver.get('https://app.pers.ncku.edu.tw/ncov/index.php?auth')
    user_id = driver.find_element_by_xpath("//*[@id='user_id']")
    user_id.send_keys("R96064013")
    user_id = driver.find_element_by_xpath("//*[@id='passwd']")
    user_id.send_keys("")
    
    try:
        submit_bottom = driver.find_element_by_xpath("//*[@id='submit_by_acpw']")
        submit_bottom.click()
    except Exception as e:
        line_broadcast("新型冠狀病毒（COVID-19）資訊平台專區登入button有誤")
    sleep(2)
    b = driver.find_elements_by_xpath("//*[contains(text(), '回報今日健康資訊')]")
    if len(b) > 0:
        print("正在填寫健康聲明書.........")
        text = "正在填寫健康聲明書"
        line_broadcast(text)
        answers = driver.find_elements_by_css_selector("div[class='form-control2 input-group']")
        for answer in answers:
            try:
                #print(answer)
                ans = answer.find_elements_by_css_selector('label')
                #li = random.choice(ans)
              
                if(len(ans)>10):
                    li = ans[15]
                    li.click()
                    time.sleep(0.1)
                else:
                    li = ans[0]
                    li.click()
                    time.sleep(0.1)
                #eee = eee + 300
                #$driver.execute_script(c+str(eee)+d)
            except Exception as e:
                #print("click error: " ,e)
                pass
            try:
                text = answer.find_element_by_css_selector("input[name='stay_1_other'][type='text']")
                text.send_keys("交管系")
            except Exception as c:
                #print("send_keys error: ",c)
                pass
        
        try:
            submit_bottom = driver.find_element_by_xpath("//*[@id='arch_grid']/div[3]/form/div/div/div[3]/button[1]")
            submit_bottom.click()                                          
            text = "健康聲明填寫完畢"
            line_broadcast(text)
        except:
            text = "健康聲明填寫異常"
            line_broadcast(text)
       
if __name__ == '__main__':
   main()
   

    

