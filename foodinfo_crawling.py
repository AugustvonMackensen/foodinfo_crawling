from selenium.common import NoSuchElementException
from selenium import webdriver as wd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

driver = wd.Chrome(service=Service(ChromeDriverManager().install()))

food_dict = {}

def run():
    # 전통향토음식 음식정보 크롤링
    # selenium 업그레이드 된 이후 driver 등록 코드
    # chromedriver.exe 굳이 프로젝트 폴더에 안 넣어도 됨
    # 가나다순으로 크롤링, 페이징 관련 문제로 있어 ㄱ~ㅎ으로 나눠서 처리.
    get_item(27, 'ㄱ')
    get_item(4, 'ㄴ')
    get_item(18, 'ㄷ')
    get_item(18, 'ㅁ')
    get_item(14, 'ㅂ')
    get_item(20, 'ㅅ')
    get_item(20, 'ㅇ')
    get_item(12, 'ㅈ')
    get_item(7, 'ㅊ')
    get_item(4, 'ㅋ')
    get_item(2, 'ㅌ')
    get_item(4, 'ㅍ')
    get_item(9, 'ㅎ')

    return food_dict

# 페이지 최종 숫자와 한글 자음 입력받아 메소드 실행
def get_item(n, ch):
    for page in range(1, n+1):
        food_title = ""
        food_info = ""
        # 사이트 접속
        url = 'https://terms.naver.com/list.naver?cid=42701&categoryId=42708&so=st3.asc&viewType= \
              &categoryType=&index='+ ch + '&page='+ str(page) + "'"
        driver.get(url)
        info_elements = driver.find_elements(By.CSS_SELECTOR, 'div.list_wrap > ul > li')
        info_num = len(info_elements)
        for item in range(1, info_num + 1):
            try:
                # selenium.common.exceptions.ElementClickInterceptedException 방지위해 send_keys() 메소드 사용
                driver.find_element(By.CSS_SELECTOR, 'div.list_wrap > ul > li:nth-child(' + str(item) + ') > div > \
                                    div.subject > strong > a:nth-child(1)').send_keys(Keys.ENTER)
                food_title = driver.find_element(By.CSS_SELECTOR, 'div.section_wrap > div.headword_title > h2').text
                # 개행문자 제거
                food_info = driver.find_element(By.CSS_SELECTOR, '#size_ct > p').text.replace('\n', '')
                driver.back()  # 뒤로 가기
                if(item == info_num):
                    break
            except NoSuchElementException:
                driver.back()
                continue
            else:
                # 음식설명이 있는 데이터만 딕셔너리에 저장
                if food_info is not None:
                    food_dict[food_title] = food_info


