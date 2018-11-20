import unittest
import storage
import story
import sender

def getNextStateAndMessage(userData, userMessage):
    userStory = story.loadStory(userData.storyName, userData.state)
    serverMessage = userStory.transitionGivenUserMessage(userMessage)
    return (userStory.currentState, serverMessage)

def updateUser(userData):
    # check if last message is from the server
    if userData.getLastSender() != "user":
        return
    userMessage = userData.getLastMessage()
    (newState, serverMessage) = getNextStateAndMessage(userData, userMessage)
    if serverMessage == None:
        return
    # send and save message
    sender.sendSMS(userData.phoneNumber, serverMessage)
    userData.addServerMessage(serverMessage)
    userData.state = newState
    storage.saveUserData(userData)

class TestLogic(unittest.TestCase):
    def test_Next():
        pass
