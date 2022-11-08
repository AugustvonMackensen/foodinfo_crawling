from selenium.common import NoSuchElementException
from selenium import webdriver as wd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def run():
    # selenium 업그레이드 된 이후 driver 등록 코드
    # chromedriver.exe 굳이 프로젝트 폴더에 안 넣어도 됨

    driver = wd.Chrome(service=Service(ChromeDriverManager().install()))

    for page in range(1, 155):
        # 접속할 사이트 url 연결
        main_url = 'http://terms.naver.com/list.naver?cid=42701&categoryId=42708&so=st3.asc&viewType=&categoryType=&index=%E3%84%B1&page=' \
                   + str(page) + "'"

        food_dict = {}
        food_list = []
        # 사이트 접속
        driver.get(main_url)
        info_elements = driver.find_elements(By.CSS_SELECTOR, 'div.list_wrap > ul > li')
        info_num = len(info_elements)
        food_title = ""
        food_info = ""
        for item in range(1, info_num + 1):
            try:
                driver.find_element(By.CSS_SELECTOR, 'div.list_wrap > ul > li:nth-child(' + str(item) + ') > div > \
                                    div.subject > strong > a:nth-child(1)').click()

                print(driver.find_element(By.CSS_SELECTOR, 'div.section_wrap > div.headword_title > h2').text)
                print(driver.find_element(By.CSS_SELECTOR, '#size_ct > p').text)

                food_title = driver.find_element(By.CSS_SELECTOR, 'div.section_wrap > div.headword_title > h2').text
                food_info = driver.find_elements(By.CSS_SELECTOR, '#size_ct > p')
                food_dict[food_title] = food_info
                driver.back()  # 뒤로 가기
            except NoSuchElementException:
                driver.back()
                continue


