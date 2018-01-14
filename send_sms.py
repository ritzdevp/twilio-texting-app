from twilio.rest import Client
from credentials import account_sid, auth_token, cell_numbers, my_twilio

client = Client(account_sid, auth_token)

my_msg = ''.join(['Your message goes here. \n' for i in range(10)])

for i in range(len(cell_numbers)):
    message = client.messages.create(to=cell_numbers[i], from_=my_twilio,
                                     body=my_msg)
