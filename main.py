import requests
from fake_useragent import UserAgent


categories = {
    # Категория, id, количество товара
    'Golf clubs': ["0c8104f6-3b98-2b15-95cb-06f382d5a778", 99],
    'Clothing': ["7b716bef-d59a-7d97-36ee-994ad180e7d3", 99],
    'Shoes': ["5cdf8a7f-3347-97a2-21f9-192f6a9bc22f", 80],
    'Golf Bags': ["9e2c9222-0e43-7ffc-121a-0b7ccebbc554", 17],
    'Accessories': ["b93590b0-d8d0-6eae-31e5-ed5570f2615c", 60],
    'Balls': ["4839cba0-7843-3dc0-7ff2-9dcc64ff9e9f", 17],
}


def golf_parser():
    url = 'https://www.golfstore.lu/_api/wix-ecommerce-storefront-web/api'

    # Создание экземпляра класса UserAgent
    user_agent = UserAgent()
    # Генерация случайного User-Agent
    random_user_agent = user_agent.random

    headers = {
        'Authorization': "VhBcHwkNDr7L7fpOi_W7L4AswzosUf557IVNrPz0Npg.eyJpbnN0YW5jZUlkIjoiZDYxZmY2MTUtZTkzMS00ZDlkLWFl"
                         "MTktM2Q4YjdjNzMxM2FiIiwiYXBwRGVmSWQiOiIxMzgwYjcwMy1jZTgxLWZmMDUtZjExNS0zOTU3MWQ5NGRmY2QiLCJt"
                         "ZXRhU2l0ZUlkIjoiMTQ5NGZkNzgtNzA5Ni00Mjc5LTg3MjQtMjU0MDAyYzQyMWRmIiwic2lnbkRhdGUiOiIyMDIzLTA2"
                         "LTIwVDEyOjQ0OjMwLjU3MVoiLCJ2ZW5kb3JQcm9kdWN0SWQiOiJzdG9yZXNfc2lsdmVyIiwiZGVtb01vZGUiOmZhbHNl"
                         "LCJvcmlnaW5JbnN0YW5jZUlkIjoiM2FmOGQ3MDYtYTcxYS00NjlhLTk1NjYtMjhhNTdlNDZkMjgwIiwiYWlkIjoiMTY4"
                         "OGMwMjEtNTJhMy00ZDVlLWI1NmEtY2YzYzRjMjc4OTQ1IiwiYmlUb2tlbiI6ImMyOGIwYjZkLTk5YTctMGZlNC0yOTNk"
                         "LTE4Y2I3ZWI3MzI3NCIsInNpdGVPd25lcklkIjoiNTk3ZjUzODMtZTZjNy00MzkzLWI2MWItM2M1YzU3ZDk5ZjliIn0",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "User-Agent": random_user_agent,
    }

    for category, id in categories.items():
        query = {
            "query": f"query {{catalog {{category(categoryId:\"{id[0]}\")"
                     f"{{numOfProducts productsWithMetaData(filters:{{}}, limit:{id[1]}, sort:null, offset:0, onlyVisible:true) "
                     "{totalCount list {id options {id key title optionType selections "
                     "{id value description key linkedMediaItems {url fullUrl thumbnailFullUrl:fullUrl(width:50, height:50)"
                     "mediaType width height index title videoFiles {url width height format quality}}}} productItems "
                     "{id optionsSelections price formattedPrice formattedComparePrice availableForPreOrder inventory "
                     "{status quantity} isVisible pricePerUnit formattedPricePerUnit} customTextFields (limit:1) {title} "
                     "productType ribbon price comparePrice sku isInStock urlPart formattedComparePrice formattedPrice "
                     "pricePerUnit formattedPricePerUnit pricePerUnitData {baseQuantity baseMeasurementUnit} itemDiscount"
                     " {discountRuleName priceAfterDiscount} digitalProductFileItems {fileType} name media {url index width"
                     " mediaType altText title height} isManageProductItems productItemsPreOrderAvailability "
                     "isTrackingInventory inventory {status quantity availableForPreOrder preOrderInfoView {limit}} "
                     "subscriptionPlans {list {id visible}} priceRange (withSubscriptionPriceRange:true) "
                     "{fromPriceFormatted} discount {mode value}}}}}}"
        }

        session = requests.session()
        response = session.post(url=url, headers=headers, json=query)

        with open(f'test.{category}2.json', 'w') as file:
            file.write(response.text)

        print(f'category: {category} id: {id}')


def main():
    golf_parser()


if __name__ == '__main__':
    main()
