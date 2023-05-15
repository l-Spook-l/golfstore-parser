import json
import re
import sqlite3
from datetime import datetime

categories = {
    'Golf clubs': 2,
    'Clothing': 1,
    'Shoes': 3,
    'Golf Bags': 5,
    'Accessories': 6,
    'Balls': 4,
}


def add_to_database():
    # Устанавливаем соединение с базой данных
    conn = sqlite3.connect('db.sqlite3')
    # Создаем курсор для выполнения SQL-запросов
    cursor = conn.cursor()

    for category, category_id in categories.items():
        with open(f'test.{category}.json', 'r') as file:
            json_content = json.loads(file.read())
            balls = json_content['data']['catalog']['category']['productsWithMetaData']['list']
            for product in balls:
                # print(product['price'])
                # print(product['name'])
                print(product['media'])
                slug = re.sub(r'(^-|-$)|[^a-z0-9]+', '-', product['name'].lower().replace('\'', ''))
                now = datetime.now()
                formatted_date = now.strftime("%Y-%m-%d %H:%M:%S.%f")

                cursor.execute('''
                    INSERT INTO store_product (name, slug, price, time_create, brand_id, category_id, gender_id, type_id)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ''', (product['name'], slug, product['price'], formatted_date, 0, category_id, 2, 0))

                cursor.execute('''
                        INSERT INTO store_productphotos (image)
                        VALUES (?)
                    ''', (product['media']))

    # Фиксируем изменения в базе данных
    conn.commit()
    # Закрываем соединение с базой данных
    conn.close()


def main():
    add_to_database()


if __name__ == '__main__':
    main()
