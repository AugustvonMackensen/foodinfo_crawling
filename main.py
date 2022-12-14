import foodinfo_crawling as crawling
import common.oracle_db as oradb
from PIL import Image
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from konlpy.tag import Okt
from collections import Counter


if __name__ == '__main__':
    food_dict = crawling.run()
    # ----- 보고서용 시각화 처리 코드 ------------------------
    with open('food_info.txt', 'w', encoding='utf-8') as f:
        for title,content in food_dict.items():
            f.write(f'{title} : {content}\n')

    crawling_txt = open('food_Info.txt', 'rt', encoding='utf-8').read()

    okt = Okt()
    line = []
    line = okt.pos(crawling_txt)

    nlist = []
    for word, tag in line:
       if tag in ['Noun']:
           nlist.append(word)

    print(nlist)

    stop_words = '매우 늘 것 반드시 것 고 랭 그 그것 것 음 과 결 퇴 가내 굳이 수도 의 속 자 끝 후'
    stop_words = set(stop_words.split(' '))

    # 불용어 제외
    nlist = [word for word in nlist if not word in stop_words]

    counts = Counter(nlist)
    tags = counts.most_common(100)

    img = Image.open('heart.png')
    imgArray = np.array(img)
    print(imgArray)

    wordcloud = WordCloud(font_path='malgun.ttf', background_color='white', width = 400, height = 400,
            max_font_size = 100,  # 빈도수가 가장 큰 글자의 크기 지정
            mask = imgArray).generate_from_frequencies(dict(tags))

    plt.figure(figsize=(10, 10))
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()

    # --------------------- DB 저장 처리 구문 -------------------------------------------------
    conn = ''
    cursor = ''
    try:
        oradb.oracle_init()
        conn = oradb.connect()
        cursor = conn.cursor()

        query = 'insert into foodinfo(food_name, food_content) values(:1, :2)'
        food_val = list(food_dict.items())
        cursor.executemany(query, food_val)
        oradb.commit(conn)

        # 삽입결과 확인
        resultset = cursor.execute('select * from foodinfo').fetchall()

        for row in resultset:
            print(row) # 행 단위 출력
    except Exception as msg:
        oradb.rollback(conn)
        print(conn)
        print('크롤링 데이터 삽입 실패 : ', msg)
    finally:
        cursor.close()
        oradb.close(conn)


