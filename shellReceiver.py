# Used for testing the stories

import logic
import storage

def startConversation():
    print("Press Ctrl-C to quit")
    userData = storage.UserData("+1234567890")
    while True:
        userMessage = input("send pretend SMS:")
        userData.addUserMessage(userMessage)
        (newState, serverMessage) = logic.getNextStateAndMessage(userData, userMessage)
        userData.state = newState
        print(serverMessage)

if __name__ == "__main__":
    startConversation()
