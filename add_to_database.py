import json
import re
import sqlite3
from datetime import datetime
import requests
import os

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

    # Если нету папки для фото, создаем её
    if not os.path.exists('photos'):
        os.makedirs('photos')

    list_of_identical_products = []

    for category, category_id in categories.items():
        with open(f'test.{category}.json', 'r') as file:
            json_content = json.loads(file.read())
            data = json_content['data']['catalog']['category']['productsWithMetaData']['list']

            number_suffix = 2

            for product in data:
                # Создаем нужный слаг
                slug = re.sub(r'(^-|-$)|[^a-z0-9]+', '-', product['name'].lower().replace('\'', ''))

                # Текущее время
                now = datetime.now()
                formatted_date = now.strftime("%Y-%m-%d %H:%M:%S.%f")

                while slug in list_of_identical_products:
                    if number_suffix > 10:
                        raise Exception("Exceeded maximum number of suffix attempts")
                    number_suffix += 1
                    slug = f"{slug}-{number_suffix}"

                list_of_identical_products.append(slug)
                number_suffix = 1

                try:
                    cursor.execute('''
                        INSERT INTO store_product (name, slug, price, time_create, brand_id, category_id, gender_id, type_id)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                    ''', (product['name'], slug, product['price'], formatted_date, 0, category_id, 2, 0))
                except sqlite3.IntegrityError:
                    # Обработка ошибки IntegrityError
                    cursor.execute('''
                        INSERT INTO store_product (name, slug, price, time_create, brand_id, category_id, gender_id, type_id)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                    ''', (product['name'], slug, product['price'], formatted_date, 0, category_id, 2, 0))
                except sqlite3.Error as error:
                    # Обработка других ошибок SQLite
                    print("Ошибка SQLite:", error)

                product_id = cursor.lastrowid
                print("Присвоенный ID продукта:", product_id)
                media = product['media']
                image_number = 1

                for id in range(len(media)):
                    cursor.execute('''INSERT INTO store_productphotos (image) VALUES (?)''', (f'photos/product/{slug}_{image_number}.jpg',))

                    image_id = cursor.lastrowid

                    cursor.execute('''INSERT INTO store_product_photos (product_id, productphotos_id) VALUES (?, ?) ''',
                                   (product_id, image_id))

                    # Получаем фото по ссылке
                    link = f"https://static.wixstatic.com/media/{media[id]['url']}/v1/fill/w_500,h_500,al_c,q_80,usm_0.66_1.00_0.01,enc_auto/{media[id]['url']}"

                    # Формируем имя для фото
                    filepath = os.path.join('photos', f'{slug}_{image_number}.jpg')

                    # Отправляем GET-запрос для загрузки фото
                    response = requests.get(link)
                    response.raise_for_status()

                    # Сохраняем фото на диск
                    with open(filepath, 'wb') as f:
                        f.write(response.content)

                    print(f"Фото {slug}_{image_number}.jpg успешно скачано и сохранено в папке 'photos'")
                    image_number += 1
                    print('list_of_identical_products', list_of_identical_products)
    # Фиксируем изменения в базе данных
    conn.commit()
    # Закрываем соединение с базой данных
    conn.close()


def main():
    add_to_database()


if __name__ == '__main__':
    main()
