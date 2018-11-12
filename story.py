import unittest

class SMSStory:
    stateTransitions = {
        None: lambda x: (None, "no story here"),
        }
    def __init__(self, currentState=None):
        self.currentState = currentState

    # returns the server's response message if any
    def transitionGivenUserMessage(self, userMessage):
        transitionFunction = self.stateTransitions[self.currentState]
        (newState, serverMessage) = transitionFunction(userMessage)
        self.currentState = newState
        return serverMessage

    def _messageContainsOneOf(self, message, stringArr):
        for string in stringArr:
            if string in message:
                return True
        return False

    def _messageContainsAllOf(self, message, stringArr):
        for string in stringArr:
            if string not in message:
                return False
        return True

class JokeStory(SMSStory):
    def __init__(self, currentState=None):
        super().__init__(currentState)
        self.stateTransitions = {
            None: lambda x: (0, "What's the difference between a panda and a hungry bank robber?"),
            0: self._userGuess
        }
    
    def _userGuess(self, message):
        repeatSetupStrings = [
            "again"
            ]
        giveUpStrings = [
            "give up",
            "don't know",
            "idk",
            "tell me"
            ]
        correctStrings = [
            "eat",
            "shoot",
            "leaves"
            ]
        message = message.lower()
        if self._messageContainsAllOf(message, correctStrings):
            (nextState, serverMessage) = (0, "Yeah that's right! One eats shoots and leaves; the other eats, shoots, and leaves. :)")
        elif self._messageContainsOneOf(message, repeatSetupStrings):
            (nextState, serverMessage) = (0, "The question is: What's the difference between a panda and a hungry bank robber?")
        elif self._messageContainsOneOf(message, giveUpStrings):
            (nextState, serverMessage) = (0, "One eats shoots and leaves; the other eats, shoots, and leaves. :)")
        else:
            (nextState, serverMessage) = (0, "huh?")
        return (nextState, serverMessage)

###### TESTS #####

class TestBaseStory(unittest.TestCase):
    def test_Transition(self):
        story = SMSStory()
        for i in range(5):
            serverMessage = story.transitionGivenUserMessage("howdy")
            self.assertEqual(serverMessage, "no story here")

class TestJokeStory(unittest.TestCase):
    def test_Transition(self):
        story = JokeStory()
        userMessage = "howdy"
        serverMessage = story.transitionGivenUserMessage(userMessage)
        self.assertEqual(serverMessage, "What's the difference between a panda and a hungry bank robber?")
        userMessage = "I don't know"
        serverMessage = story.transitionGivenUserMessage(userMessage)
        self.assertEqual(serverMessage, "One eats shoots and leaves; the other eats, shoots, and leaves. :)")

    def test_dontKnowTransition(self):
        story = JokeStory(0)
        userMessage = "I give up"
        serverMessage = story.transitionGivenUserMessage(userMessage)
        self.assertEqual(serverMessage, "One eats shoots and leaves; the other eats, shoots, and leaves. :)")

    def test_giveAnswerTransition(self):
        story = JokeStory(0)
        userMessage = "Eats shoots and leaves. Eats, shoots, and leaves"
        serverMessage = story.transitionGivenUserMessage(userMessage)
        self.assertEqual(serverMessage, "Yeah that's right! One eats shoots and leaves; the other eats, shoots, and leaves. :)")
        
if __name__ == "__main__":
    unittest.main()        
