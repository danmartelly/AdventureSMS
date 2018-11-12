# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

import storage
import logic

app = Flask(__name__)

@app.route("/sms", methods=["GET", "POST"])
def sms_respond():
    # get message and update user data
    userMessage = request.values.get("Body", None)
    phoneNumber = request.values.get("From", None)
    fp = open("/home/pi/Documents/AdventureSMS/log.txt", "a")
    fp.write("phone number " + phoneNumber + ": " + userMessage + "\n")
    fp.close()
    userData = storage.getUserData(phoneNumber)
    userData.addUserMessage(userMessage)
    storage.saveUserData(userData)

    # use logic to send response
    #resp = MessagingResponse()
    logic.updateUser(userData)
    
    return None

if __name__ == "__main__":
    app.run(debug=True)
