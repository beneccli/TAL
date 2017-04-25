from people import People

class ChatBotEngine:

    # Va lire une phrase et en sortir les tokens
    def tokenize(self, str):
        return False

    @staticmethod
    def talk(str):
        tokens = ChatBotEngine.tokenize(str)
        return "Je ne comprends pas ce que tu dis, désolé..."