import time

from selenium.common import NoSuchElementException
from selenium import webdriver as wd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = wd.ChromeOptions
driver = wd.Chrome(options=options(), service=Service(ChromeDriverManager().install()))

food_dict = {}

def run():
    # 전통향토음식 음식정보 크롤링
    # selenium 업그레이드 된 이후 driver 등록 코드
    # chromedriver.exe 굳이 프로젝트 폴더에 안 넣어도 됨

    folder_list =['가래떡', '가지구이', '갈비구이', '갈비찜', '갈비탕', '개피떡', '게장', '경단', '계란말이', '고갈비',
                  '고등어구이', '고추장불고기', '곱창전골', '국수', '김밥', '김치찌개', '낚지볶음', '냉면', '닭갈비', '닭찜',
                  '돼지갈비찜', '돼지고기구이', '돼지고기볶음', '된장국', '된장찌개', '떡갈비', '떡만둣국', '떡볶이', '만두',
                  '만둣국', '명란젓', '배추김치', '보쌈', '부대찌개', '북엇국', '삼겹살구이', '삼계탕', '새우구이', '송편', '순대',
                  '순대국밥', '순대볶음', '순두부찌개', '아귀찜', '알밥', '양념치킨', '오리구이', '오이소박이', '왕만두',
                  '유과', '육포', '육회', '육회비빔밥', '잡채', '장어구이', '족발', '주먹밥', '죽', '찐빵', '찹쌀떡',
                  '총각김치', '추어탕', '콩국수', '통닭', '파전', '팥빙수', '팥죽', '해물찜', '해물탕', '해장국',
                  '호두과자', '훈제오리']


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
            pass

    print(food_dict)
    return food_dict




