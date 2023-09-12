import requests

# headers = {
#         'Accept': 'application/json',
#         'Content-Type': 'application/json',
#         'Authorization': f'Bearer {merchant_token}',
#     }
#     data = {
#         "requestId": requestid,
#         "phone": phone,
#         "accountId": accountid
#     }
#     response = requests.post(f'https://api.qiwi.com/partner/payin-tokenization-api/v1/sites/{siteId}/token-requests',
#                              json=data, headers=headers).json()

headers = {
    'accept': 'application/json',
}


if __name__ == '__main__':
    response = requests.get('https://alexbobr.ru/table/', headers=headers)
    response = response.json()
    print(response[0]['point_begin'])