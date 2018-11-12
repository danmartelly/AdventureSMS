# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import pickle

filename = "/home/pi/Documents/secretInfo.pickle"
fp = open(filename, "rb")
secretInfo = pickle.load(fp)
fp.close()

def sendSMS(phone_to, message):
    # Your Account Sid and Auth Token from twilio.com/console
    account_sid = secretInfo["account_sid"]
    auth_token = secretInfo["auth_token"]
    client = Client(account_sid, auth_token)

    message = client.messages \
                .create(
                     body=message,
                     from_=secretInfo["twilioPhoneNumber"],
                     to=phone_to
                 )
    return message.sid
