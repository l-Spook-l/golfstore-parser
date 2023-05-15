import json
import re
import sqlite3
from datetime import datetime
from main import categories
# https://static.wixstatic.com/media/597f53_deca6a99f24a4d548fc45f0b2288a4c6~mv2.jpg/v1/fill/w_500,h_500,al_c,q_80,usm_0.66_1.00_0.01,enc_auto/597f53_deca6a99f24a4d548fc45f0b2288a4c6~mv2.jpg

def add_to_database():
    # for category in categories
        # with open(f'test.{category}.json', 'r') as file:
        # json_content = json.loads(file.read())
        # balls = json_content['data']['catalog']['category']['productsWithMetaData']['list']
        # for product in balls:
            # print(product['price'])
            # print(product['name'])
            # print(product['media'])
            # category
            # slug = re.sub(r'(^-|-$)|[^a-z0-9]+', '-', product['name'].lower().replace('\'', ''))

    with open('test.Golf clubs.json', 'r') as file:
        json_content = json.loads(file.read())
        # print(json_content)
        # print(json_content['data'])
        # print(json_content['data']['catalog'])
        # print(json_content['data']['catalog']['category'])
        # print(json_content['data']['catalog']['category']['productsWithMetaData'])
        # print(json_content['data']['catalog']['category']['productsWithMetaData']['list'])
        balls = json_content['data']['catalog']['category']['productsWithMetaData']['list']
        # print(type(balls), len(balls))
        # print(json_content['data']['catalog']['category']['name'])

        for product in balls:
            # print(product)
            # print(product['price'])
            print(product['name'], len(product['media']))
            print(product['media'][0])

            slug = re.sub(r'(^-|-$)|[^a-z0-9]+', '-', product['name'].lower().replace('\'', ''))
            # print(slug)

            now = datetime.now()
            formatted_date = now.strftime("%Y-%m-%d %H:%M:%S.%f")
            # print(formatted_date)

    # # ==========================================
    # # ==========================================
    # # Устанавливаем соединение с базой данных
    # conn = sqlite3.connect('db.sqlite3')
    #
    # # Создаем курсор для выполнения SQL-запросов
    # cursor = conn.cursor()
    #
    # # Открываем JSON-файл
    # with open('test.Balls.json') as f:
    #     data = json.load(f)
    #
    # # Перебираем объекты в JSON и выполняем операцию вставки
    # for item in data:
    #     # Извлекаем нужные поля из объекта item
    #     поле1 = item['поле1']
    #     поле2 = item['поле2']
    #     ...
    #
    #     # Выполняем операцию вставки в таблицу
    #     cursor.execute('''
    #         INSERT INTO store_product (поле1, поле2, ...)
    #         VALUES (?, ?, ...)
    #     ''', (поле1, поле2, ...))
    #
    # # Фиксируем изменения в базе данных
    # conn.commit()
    # # Закрываем соединение с базой данных
    # conn.close()


def main():
    add_to_database()


if __name__ == '__main__':
    main()
