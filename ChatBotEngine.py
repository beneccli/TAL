from people import People

class ChatBotEngine:

    # Va lire une phrase et en sortir les tokens
    @staticmethod
    def tokenize(str):
        return False

    @staticmethod
    def talk(str):
        tokens = ChatBotEngine.tokenize(str)
        return "Je ne comprends pas ce que tu dis, désolé..."