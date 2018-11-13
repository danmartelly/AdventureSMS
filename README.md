The intent of this project is to tell stories using the medium of SMS aka texting. It was written with Python 3.5.3 and run on a Raspberry Pi 3 running Raspbian.

SETUP:
This project makes use of twilio and as a result, you'll have to a twilio account for the messages to go through.

The following are the critical instructions that twilio has you do when doing the quickstart:
1. pip install twilio
2. pip install flask
3. Find a way to deploy your Flask application. You can use ngrok as suggested by twilio (https://ngrok.com/download. The instructions will assume you're using ngrok

Next you should update some file paths to represent your desired folder structure on your computer. Open storage.py and change "saveBasePath" to point to a folder where you want user's data to be saved. 

Then open "sender.py" and change the filename to a location where you are going to want to save some configuration information. To create the configuration information file, open a python shell and type in the following:
>> import pickle
>> filename = "/path/to/config/file.pickle"
>> secretInfo = "account_sid": 'getFromTwilio', "auth_token": 'getFromTwilio', "twilioPhoneNumber": 'getFromTwilio'}
>> fp = open(filename, "wb")
>> pickle.dump(secretInfo, fp, 2)
>> fp.close()

RUN:
You should now be ready to run. You can do this by running twilioReceiver.py in one terminal. And run "./ngrok http 5000" in another terminal.
You'll have to set up twilio to forward text messages to your ngrok instance. You can do this by copying the forwarding URL e.g. https://49sdfker.ngrok.io to the message webhook in the Twilio dashboard. You have to append "/sms" to the URL. e.g. https://49sdfker.ngrok.io/sms

Start texting your twilio number and you should get a response!
