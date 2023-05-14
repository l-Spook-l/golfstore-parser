import requests


def golf_parser():
    url = 'https://www.golfstore.lu/_api/wix-ecommerce-storefront-web/api'

    categories = {
        'Golf clubs': "0c8104f6-3b98-2b15-95cb-06f382d5a778",
        'Clothing': "7b716bef-d59a-7d97-36ee-994ad180e7d3",
        'Shoes': "5cdf8a7f-3347-97a2-21f9-192f6a9bc22f",
        'Golf Bags': "9e2c9222-0e43-7ffc-121a-0b7ccebbc554",
        'Accessories': "b93590b0-d8d0-6eae-31e5-ed5570f2615c",
        'Balls': "4839cba0-7843-3dc0-7ff2-9dcc64ff9e9f",
    }

    # query = {
    #     "query": "query {catalog {category(categoryId:\"7b716bef-d59a-7d97-36ee-994ad180e7d3\") "
    #              "{numOfProducts productsWithMetaData(filters:{}, limit:18, sort:null, offset:0, onlyVisible:true) "
    #              "{totalCount list {id options {id key title optionType selections "
    #              "{id value description key linkedMediaItems {url fullUrl thumbnailFullUrl:fullUrl(width:50, height:50)"
    #              "mediaType width height index title videoFiles {url width height format quality}}}} productItems "
    #              "{id optionsSelections price formattedPrice formattedComparePrice availableForPreOrder inventory "
    #              "{status quantity} isVisible pricePerUnit formattedPricePerUnit} customTextFields (limit:1) {title} "
    #              "productType ribbon price comparePrice sku isInStock urlPart formattedComparePrice formattedPrice "
    #              "pricePerUnit formattedPricePerUnit pricePerUnitData {baseQuantity baseMeasurementUnit} itemDiscount"
    #              " {discountRuleName priceAfterDiscount} digitalProductFileItems {fileType} name media {url index width"
    #              " mediaType altText title height} isManageProductItems productItemsPreOrderAvailability "
    #              "isTrackingInventory inventory {status quantity availableForPreOrder preOrderInfoView {limit}} "
    #              "subscriptionPlans {list {id visible}} priceRange (withSubscriptionPriceRange:true) "
    #              "{fromPriceFormatted} discount {mode value}}}}}}"
    # }

    headers = {
        'Authorization': "w62tobLjOeEeoOyBM2hhHuOISICuleRW54EJOQBMLZE.eyJpbnN0YW5jZUlkIjoiZDYxZmY2MTUtZTkzMS00ZDlkL"
                         "WFlMTktM2Q4YjdjNzMxM2FiIiwiYXBwRGVmSWQiOiIxMzgwYjcwMy1jZTgxLWZmMDUtZjExNS0zOTU3MWQ5NGRmY2QiL"
                         "CJtZXRhU2l0ZUlkIjoiMTQ5NGZkNzgtNzA5Ni00Mjc5LTg3MjQtMjU0MDAyYzQyMWRmIiwic2lnbkRhdGUiOiIyMDIzL"
                         "TA1LTE0VDEzOjM3OjMzLjQwMVoiLCJ2ZW5kb3JQcm9kdWN0SWQiOiJzdG9yZXNfc2lsdmVyIiwiZGVtb01vZGUiOmZhbH"
                         "NlLCJvcmlnaW5JbnN0YW5jZUlkIjoiM2FmOGQ3MDYtYTcxYS00NjlhLTk1NjYtMjhhNTdlNDZkMjgwIiwiYWlkIjoiMTY"
                         "4OGMwMjEtNTJhMy00ZDVlLWI1NmEtY2YzYzRjMjc4OTQ1IiwiYmlUb2tlbiI6ImMyOGIwYjZkLTk5YTctMGZlNC0yOTNk"
                         "LTE4Y2I3ZWI3MzI3NCIsInNpdGVPd25lcklkIjoiNTk3ZjUzODMtZTZjNy00MzkzLWI2MWItM2M1YzU3ZDk5ZjliIn0",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    }

    # session = requests.session()
    # response = session.post(url=url, headers=headers, json=query)
    # data = response.json()

    # with open('test.json', 'w') as file:
    #     file.write(response.text)

    for category, id in categories.items():
        query = {
            "query": f"query {{catalog {{category(categoryId:\"{id}\")"
                     "{numOfProducts productsWithMetaData(filters:{}, limit:18, sort:null, offset:0, onlyVisible:true) "
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

        with open(f'test.{category}.json', 'w') as file:
            file.write(response.text)

        # print(response.text)
        print(f'category: {category} id: {id}')

    # print(response)
    # print(response.text)
    # print(data)


def main():
    golf_parser()


if __name__ == '__main__':
    main()
