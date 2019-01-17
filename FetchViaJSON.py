import requests
import json

#Pass Headers to flipkart
headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            'X-user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36 FKUA/website/41/website/Desktop',
            'Referer' :   'https://www.flipkart.com/sellers?pid=SMWFYEZMT3VFUNUS',
            'Content-Type': 'application/json',
            'Origin': 'https://www.flipkart.com',
            'Host': 'www.flipkart.com',
            'Pragma': 'no-cache'
            }
#url of the page to get data from
url = "https://www.flipkart.com/api/3/page/dynamic/product-sellers"

#pass the productId and pincode as payLoad
payLoad = {"requestContext":{"productId":"SMWFYEZMT3VFUNUS"},"locationContext":{"pincode":"110095"}}
response = requests.post(url,headers = headers,data = json.dumps(payLoad))
response_json = json.loads(response.text)

#Print the product name, listingId and productId
print(response_json["RESPONSE"]["pageContext"]["titles"]["title"])
print(response_json["RESPONSE"]["pageContext"]["listingId"])
print(response_json["RESPONSE"]["pageContext"]["productId"])
print()

seller_details = response_json["RESPONSE"]["data"]["product_seller_detail_1"]["data"]

for data in seller_details:

    seller = data['value']
    seller_information = seller['sellerInfo']['value']

    print(seller_information['name'])
    print(seller['deliveryInfo']['primaryOption']['deliveryDate'])
    print("Delivery data : " + seller['deliveryMessages'][0]['text'])
    print("Price without delivery charges: "+ str(seller['metadata']['price']))
    print("delivery charges " + seller['pricing']['value']['deliveryCharge']['decimalValue'])
    print("Final price after delivery charges" + seller['pricing']['value']['finalPrice']['decimalValue'])

    if('rating' in seller_information):
        print(seller_information['rating']['average'])
    print()
