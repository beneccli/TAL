from people import People
import re
import nltk
import os

class ChatBotEngine:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    nltk.data.path.append(BASE_DIR + '/nltk_data/')
    dict_tags = {} # Dictionary

    def __init__(self):
        # Get all known tags
        tmp = open("french.tagger", "r").read()
        lines = tmp.split('\n')
        for l in lines:
            if l != '':
                l = l.split(':')
                self.dict_tags[l[0]] = l[1]

        return

    # Try to find the intent of a list of tokens = sentence (is it a question etc)
    def find_intent(self, tokens):
        tokens_tagified = self.tagify(tokens)
        print(tokens_tagified)

        # Find a question
        if tokens_tagified[0][1] == 'VERB' and tokens_tagified[1][1] == 'PRON':
            return 'question'
        for token_tagified in tokens_tagified:
            if token_tagified[1] == 'IADJ':
                return 'question'

        return 'unknown'

    # Try to understand the question and then to answer it
    def answer_question(self, tokens):


        return 'Trying to answer your question...'

    # Search for tags of each token
    def tagify(self, tokens):
        tags = []
        for token in tokens:
            if token.lower() in self.dict_tags:
                tags.append([token.lower(), self.dict_tags[token.lower()]])
            else:
                # Tag is not found doesn't mean we can't find tags inside the token
                # So let's try to find some way to tag it
                if '\'' in token:
                    tmp = token.split('\'')
                    if len(tmp) == 2:
                        if tmp[0] == 'd':
                            tags.append(['de', self.dict_tags['de']])
                            self.find_tag(tmp[1], tags)
                        elif tmp[0] == 'l':
                            tags.append(['le', self.dict_tags['le']])
                            self.find_tag(tmp[1], tags)
                    else:
                        tags.append([token.lower(), 'X'])

                elif '-' in token:
                    # /?\ All tokens like "rez-de-chaussée" has already been found before so here we're safe about words
                    # that use a '-' inside (assuming we have all words in our dict)
                    tmp = token.split('-')
                    for tk in tmp:
                        self.find_tag(tk, tags, True)

                else:
                    tags.append([token.lower(), 'X'])

        return tags

    def find_tag(self, token, tags, lowercase = False):
        if lowercase and token.lower() in self.dict_tags:
            tags.append([token.lower(), self.dict_tags[token.lower()]])
        elif not lowercase and token in self.dict_tags:
            tags.append([token, self.dict_tags[token]])
        else:
            tags.append([token, 'X'])

    # Core method where all mechanics are involved
    def talk(self, str):
        sentences = nltk.sent_tokenize(str, "french")  # On découpe en phrase
        tokens = []
        for sentence in sentences:
            tokens.append(nltk.word_tokenize(sentence, "french"))
            intent = self.find_intent(tokens[-1])

            if intent == 'question':
                print(self.answer_question(tokens[-1]))

        return ''