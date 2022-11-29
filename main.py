import foodinfo_crawling as crawling
import common.oracle_db as oradb

if __name__ == '__main__':
    food_dict = crawling.run()
    conn = ''
    cursor = ''
    try:
        oradb.oracle_init()
        conn = oradb.connect()
        cursor = conn.cursor()

        query = 'insert into foodinfo(food_name, food_content) values(%s, %s)'
        food_val = list(food_dict.items())
        cursor.executemany(query, food_val)
        oradb.commit()
        
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


