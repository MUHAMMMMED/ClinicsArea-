

# Create your tests here.
# import pyautogui
# from time import sleep

# msg = input("Enter Your Msg >> :")
# num_msg = int(input("Chose Your Numbr of Msg >> :"))
# time_msg = float(input("Chose Your Time Of Msg >> :"))

# for num in range(num_msg + 1 ):
#     pyautogui.typewrite(msg)
#     sleep(time_msg)
#     pyautogui.press('enter')
#     sleep(time_msg)


# import http.client
# import ssl 

# conn = http.client.HTTPSConnection("api.ultramsg.com",context = ssl._create_unverified_context())

# payload = "token={TOKEN}&to=&body="
# payload = payload.encode('utf8').decode('iso-8859-1') 

# headers = { 'content-type': "application/x-www-form-urlencoded" }

# conn.request("POST", "/{INSTANCE_ID}/messages/chat", payload, headers)

# res = conn.getresponse()
# data = res.read()

# print(data.decode("utf-8"))

# import requests

# url = "https://api.ultramsg.com/{INSTANCE_ID}/messages/chat"

# payload = "token={TOKEN}&to=&body="
# payload = payload.encode('utf8').decode('iso-8859-1')
# headers = {'content-type': 'application/x-www-form-urlencoded'}

# response = requests.request("POST", url, data=payload, headers=headers)

# print(response.text)

# import os

# from twilio.rest import Client

# from dotenv import load_dotenv
# load_dotenv()

# ACCOUNT_SID = os.environ.get('ACCOUNT_SID')
# AUTH_TOKEN = os.environ.get('AUTH_TOKEN')
# FROM = os.environ.get('FROM')

# client = Client(ACCOUNT_SID, AUTH_TOKEN)

# def sendMessage(senderId, message):

#     res = client.messages.create(
#         body=message,
#         from_=FROM,
#         to=f'whatsapp:+{senderId}'
#     )
#     return res


# def whatsapp():
#     print(request.get_data())
#     message = request.form['Body']
#     senderId = request.form['From'].split('+')[1]
#     print(f'Message --> {message}')
#     print(f'Sender id --> {senderId}')
#     res = sendMessage(senderId=senderId, message=message)
#     print(f'This is the response --> {res}')
#     return '200'