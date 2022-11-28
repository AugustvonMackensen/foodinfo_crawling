import time

from selenium.common import NoSuchElementException
from selenium import webdriver as wd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import os

driver = wd.Chrome(service=Service(ChromeDriverManager().install()))

food_dict = {}

def run():
    # 전통향토음식 음식정보 크롤링
    # selenium 업그레이드 된 이후 driver 등록 코드
    # chromedriver.exe 굳이 프로젝트 폴더에 안 넣어도 됨

    folder_list =[]
    ignored_list = []
    dir = os.listdir('C:/finalProject_datasets/Training')
    for folder in dir:
        folder_list.append(folder)

    print(folder_list)
    # 사이트 접속

    for item in range(len(folder_list)):
        # 사이트 접속
        url = 'https://terms.naver.com/'
        driver.get(url)

        keyword = folder_list[item]
        time.sleep(5)
        try:
            driver.find_element(By.CSS_SELECTOR, '#term_query').send_keys(keyword)
            driver.find_element(By.CSS_SELECTOR, '#terms_search_form > fieldset > div > input.btn_search._search').click()
            driver.find_element(By.CSS_SELECTOR, '#content > div > ul > li > div > div > strong > a').click()
            food_title = keyword
            # 개행문자 제거
            food_content = driver.find_element(By.CSS_SELECTOR, '#size_ct > p').text.replace('\n', '')
            food_dict[food_title] = food_content
            print(keyword + ': ' + food_content)
            driver.back()
        except NoSuchElementException:
            print('누락될 키워드 : ' + keyword)
            ignored_list.append(keyword)
            pass


    print(food_dict)




