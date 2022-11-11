import foodinfo_crawling as crawling
import common.oracle_db as oradb

if __name__ == '__main__':
    food_dict = crawling.run()
    oradb.oracle_init()
    conn = oradb.connect()
    cursor = conn.cursor()

    query = 'insert into foodinfo(food_name, food_content) values(%s, %s)'

    foodname_list = list(food_dict.keys())
    foodinfo_list = list(food_dict.items())

    for item in range(len(food_dict)):
        foodinfo_val = (foodname_list[item], foodinfo_list[item])
        cursor.execute(query, foodinfo_val)

    print(food_dict)

