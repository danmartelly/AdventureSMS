import unittest
import random
import string
import pickle
import os.path

saveBasePath = "/home/pi/Documents/smsSaveData/"

class UserData:
    def __init__(self, phoneNumber):
        self.phoneNumber = phoneNumber
        self.messageData = []
        self.state = None
        self.storyName = "TeenageLoveStory"

    def addServerMessage(self, msg, timestamp=None):
        self.messageData.append({"sender":"server", "message":msg})

    def addUserMessage(self, msg):
        self.messageData.append({"sender":"user", "message":msg})

    def _filterMessages(self, filterFunc):
        return [msgData["message"] for msgData in self.messageData if filterFunc(msgData)]

    def getServerMessageHistory(self):
        return self._filterMessages(lambda msgData: msgData["sender"] == "server")

    def getUserMessageHistory(self):
        return self._filterMessages(lambda msgData: msgData["sender"] == "user")

    def getAllMessages(self):
        return self._filterMessages(lambda x: True)

    def getLastSender(self):
        if len(self.messageData) > 0:
            return self.messageData[-1]["sender"]
        else:
            return None

    def getLastMessage(self):
        if len(self.messageData) > 0:
            return self.messageData[-1]["message"]
        else:
            return None

def getUserData(phoneNumber):
    filename = saveBasePath + phoneNumber.replace("+","")
    if os.path.isfile(filename):
        fp = open(filename, "rb")
        userData = pickle.load(fp)
        fp.close()
        return userData
    else:
        return UserData(phoneNumber)

def saveUserData(userData):
    filename = saveBasePath + userData.phoneNumber.replace("+","")
    fp = open(filename, "wb")
    pickle.dump(userData, fp, 2)
    fp.close()
    
###### TESTS #####

class TestUserData(unittest.TestCase):
    def test_rememberNumber(self):
        phoneNumber = "+123456789"
        userData = UserData(phoneNumber)
        self.assertEqual(phoneNumber, userData.phoneNumber)

    def test_rememberServerHistory(self):
        phoneNumber = "+123456789"
        userData = UserData(phoneNumber)
        messages = ["hello world", "goodbye cruel world"]
        for msg in messages:
            userData.addServerMessage(msg)
        self.assertEqual(userData.getServerMessageHistory(), messages)

    def test_rememberUserHistory(self):
        phoneNumber = "+123456789"
        userData = UserData(phoneNumber)
        messages = ["amazing", "grace"]
        for msg in messages:
            userData.addUserMessage(msg)
        self.assertEqual(userData.getUserMessageHistory(), messages)

    def test_rememberMixedHistory(self):
        phoneNumber = "+123456789"
        userData = UserData(phoneNumber)
        serverMessages = ["hello world", "goodbye cruel world"]
        userMessages = ["amazing", "grace"]
        userData.addServerMessage(serverMessages[0])
        userData.addUserMessage(userMessages[0])
        userData.addUserMessage(userMessages[1])
        userData.addServerMessage(serverMessages[1])
        self.assertEqual(userData.getUserMessageHistory(), userMessages)
        self.assertEqual(userData.getServerMessageHistory(), serverMessages)
        
class TestStorage(unittest.TestCase):
    def makeRandomMessage(self):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(10))
    
    def test_saveAndRetrieve(self):
        phoneNumber = "+123456789"
        userData = UserData(phoneNumber)
        messages = [self.makeRandomMessage() for i in range(10)]
        for msg in messages:
            userData.addServerMessage(msg)
        saveUserData(userData)
        retrievedUserData = getUserData(phoneNumber)
        self.assertEqual(retrievedUserData.getServerMessageHistory(),
                         userData.getServerMessageHistory())
                       
        

if __name__ == "__main__":
    unittest.main()

