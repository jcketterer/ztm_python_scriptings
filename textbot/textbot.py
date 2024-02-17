# from twilio.rest import Client

# account_sid = 'AC5719d34f545798cad09e067ded02b26d'
# auth_token = '196293631fb64f915e534815087fa82c'
# client = Client(account_sid, auth_token)

# message = client.messages.create(
#     from_='+18557092901',
#     body='I CANT BELIEVE THIS WORKS',
#     to='+14802290252'
# )

# print(message.sid)


import requests

requests.post("https://ntfy.sh/isKvdrqszZGRiT56",data='Can you hear me?'.encode(encoding='utf-8'))