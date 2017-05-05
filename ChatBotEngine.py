from people import People
import re

class ChatBotEngine:

    def __init__(self):
        return

    def findIntent(self, tokens):
        return 'NoIntent'

    def talk(self, str):
        intent = self.findIntent([])
        return tokens