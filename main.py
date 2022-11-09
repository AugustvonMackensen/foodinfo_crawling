import foodinfo_crawling as crawling
import common.oracle_db as oradb

if __name__ == '__main__':
    food_dict = crawling.run()
    # oradb.oracle_init()
    # conn = oradb.connect()
    # cursor = conn.cursor()

    print(food_dict)

