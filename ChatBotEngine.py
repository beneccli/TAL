from people import People
import re
import nltk
import os

class ChatBotEngine:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    nltk.data.path.append(BASE_DIR + '/nltk_data/')
    tags = {}

    def __init__(self):
        # Get all known tags
        tmp = open("french.tagger", "r").read()
        lines = tmp.split('\n')
        for l in lines:
            if l != '':
                l = l.split(':')
                self.tags[l[0]] = l[1]

        return

    # Try to find the intent of a list of tokens = sentence (is it a question etc)
    def findIntent(self, tokens):
        tokens_tagified = self.tagify(tokens)
        return 'NoIntent'

    # Search for tags of each token
    def tagify(self, tokens):
        tags = []
        for token in tokens:
            if token.lower() in self.tags:
                tags.append([token.lower(), self.tags[token.lower()]])
            else:
                # Tag is not found doesn't mean we can't find tags inside the token
                # So let's try to find some way to tag it
                if '\'' in token:
                    tmp = token.split('\'')
                    if len(tmp) == 2:
                        if tmp[0] == 'd':
                            tags.append(['de', self.tags['de']])
                            if tmp[1] in self.tags: # Don't use lower() here coz this token can't be the start of the
                                                    # sentence, so if there is a uppercase is must be a proper noun
                                tags.append([tmp[1], self.tags[tmp[1]]])
                            else:
                                tags.append([tmp[1], 'X'])
                        elif tmp[0] == 'l':
                            tags.append(['le', self.tags['le']])
                            if tmp[1] in self.tags: # Don't use lower() here coz this token can't be the start of the
                                                    # sentence, so if there is a uppercase is must be a proper noun
                                tags.append([tmp[1], self.tags[tmp[1]]])
                            else:
                                tags.append([tmp[1], 'X'])
                    else:
                        tags.append([token.lower(), 'X'])

                elif '-' in token:
                    # /?\ All tokens like "rez-de-chaussée" has already been found before so here we're safe about words
                    # that use a '-' inside (assuming we have all words in our dict)
                    tmp = token.split('-')
                    for tk in tmp:
                        if tk.lower() in self.tags:
                            tags.append([tk.lower(), self.tags[tk.lower()]])
                        else:
                            tags.append([tk, 'X'])

                else:
                    tags.append([token.lower(), 'X'])

        print(tags)
        return

    def findTag(self, token):
        return

    # Core method where all mechanics are involved
    def talk(self, str):
        sentences = nltk.sent_tokenize(str, "french")  # On découpe en phrase
        tokens = []
        intent = []
        for sentence in sentences:
            tokens.append(nltk.word_tokenize(sentence, "french"))
            intent.append(self.findIntent(tokens[-1]))
        return