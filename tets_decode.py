import urllib.parse

# URL-адрес с закодированными значениями переменных
with_name = 'https://www.golfstore.lu/_api/wix-ecommerce-storefront-web/api' \
            '?o=getData&s=WixStoresWebClient&q=query,getData($externalId:String!,$compId:String,$mainCollectionId:String,$limit:Int!,$sort:ProductSort,$filters:ProductFilters,$offset:Int,$withOptions:Boolean,=,false,$withPriceRange:Boolean,=,false){appSettings(externalId:$externalId){widgetSettings}catalog{category(compId:$compId,categoryId:$mainCollectionId){id,name,visible,productsWithMetaData(limit:$limit,onlyVisible:true,sort:$sort,filters:$filters,offset:$offset){list{id,options{id,key,title,@include(if:$withOptions),optionType,@include(if:$withOptions),selections,@include(if:$withOptions){id,value,description,key,linkedMediaItems{url,fullUrl,thumbnailFullUrl:fullUrl(width:50,height:50),mediaType,width,height,index,title,videoFiles{url,width,height,format,quality}}}}productItems,@include(if:$withOptions){id,optionsSelections,price,formattedPrice,formattedComparePrice,availableForPreOrder,inventory{status,quantity}isVisible,pricePerUnit,formattedPricePerUnit}customTextFields(limit:1){title}productType,ribbon,price,comparePrice,sku,isInStock,urlPart,formattedComparePrice,formattedPrice,pricePerUnit,formattedPricePerUnit,pricePerUnitData{baseQuantity,baseMeasurementUnit}itemDiscount{discountRuleName,priceAfterDiscount}digitalProductFileItems{fileType}name,media{url,index,width,mediaType,altText,title,height}isManageProductItems,productItemsPreOrderAvailability,isTrackingInventory,inventory{status,quantity,availableForPreOrder,preOrderInfoView{limit}}subscriptionPlans{list{id,visible}}priceRange(withSubscriptionPriceRange:true),@include(if:$withPriceRange){fromPriceFormatted}discount{mode,value}}totalCount}}}}&v=%7B%22externalId%22%3A%222d0335de-a636-4cd3-8b1f-b1e8d12b166d%22%2C%22compId%22%3A%22comp-kw3gihbc%22%2C%22limit%22%3A62%2C%22sort%22%3Anull%2C%22filters%22%3Anull%2C%22offset%22%3A100%2C%22withOptions%22%3Afalse%2C%22withPriceRange%22%3Afalse%2C%22mainCollectionId%22%3Anull%7D'
wout_name = 'https://www.golfstore.lu/_api/wix-ecommerce-storefront-web/api' \
            '?o=getFilteredProducts&s=WixStoresWebClient&q=query,getFilteredProducts($mainCollectionId:String!,$filters:ProductFilters,$sort:ProductSort,$offset:Int,$limit:Int,$withOptions:Boolean,=,false,$withPriceRange:Boolean,=,false){catalog{category(categoryId:$mainCollectionId){numOfProducts,productsWithMetaData(filters:$filters,limit:$limit,sort:$sort,offset:$offset,onlyVisible:true){totalCount,list{id,options{id,key,title,@include(if:$withOptions),optionType,@include(if:$withOptions),selections,@include(if:$withOptions){id,value,description,key,linkedMediaItems{url,fullUrl,thumbnailFullUrl:fullUrl(width:50,height:50),mediaType,width,height,index,title,videoFiles{url,width,height,format,quality}}}}productItems,@include(if:$withOptions){id,optionsSelections,price,formattedPrice,formattedComparePrice,availableForPreOrder,inventory{status,quantity}isVisible,pricePerUnit,formattedPricePerUnit}customTextFields(limit:1){title}productType,ribbon,price,comparePrice,sku,isInStock,urlPart,formattedComparePrice,formattedPrice,pricePerUnit,formattedPricePerUnit,pricePerUnitData{baseQuantity,baseMeasurementUnit}itemDiscount{discountRuleName,priceAfterDiscount}digitalProductFileItems{fileType}name,media{url,index,width,mediaType,altText,title,height}isManageProductItems,productItemsPreOrderAvailability,isTrackingInventory,inventory{status,quantity,availableForPreOrder,preOrderInfoView{limit}}subscriptionPlans{list{id,visible}}priceRange(withSubscriptionPriceRange:true),@include(if:$withPriceRange){fromPriceFormatted}discount{mode,value}}}}}}&v=%7B%22mainCollectionId%22%3A%220c8104f6-3b98-2b15-95cb-06f382d5a778%22%2C%22offset%22%3A100%2C%22limit%22%3A62%2C%22sort%22%3Anull%2C%22filters%22%3Anull%2C%22withOptions%22%3Afalse%2C%22withPriceRange%22%3Afalse%7D'

# Раскодирование URL-кодированных значений
decoded_url_1 = urllib.parse.unquote(with_name)
decoded_url_2 = urllib.parse.unquote(wout_name)

print(decoded_url_1)
print(decoded_url_2)

from fake_useragent import UserAgent

# Создание экземпляра класса UserAgent
user_agent = UserAgent()

# Генерация случайного User-Agent
random_user_agent = user_agent.random

# Использование случайного User-Agent в вашем запросе
headers = {'User-Agent': random_user_agent}
print(headers)
print(random_user_agent)