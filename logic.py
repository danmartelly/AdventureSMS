import storage
import story
import sender

def updateUser(userData):
    # check if last message is from the server
    if userData.getLastSender() != "user":
        return
    userStory = story.JokeStory(userData.state)
    userMessage = userData.getLastMessage()
    serverMessage = userStory.transitionGivenUserMessage(userMessage)
    fp = open("/home/pi/Documents/AdventureSMS/log.txt", "a")
    fp.write("userMessage: " + userMessage)
    fp.write(" serverMessage: " + serverMessage + "\n")
    fp.close()
    if serverMessage == None:
        return
    # send and save message
    sender.sendSMS(userData.phoneNumber, serverMessage)
    userData.addServerMessage(serverMessage)
    userData.state = userStory.currentState
    storage.saveUserData(userData)
