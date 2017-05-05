import re
from ChatBotEngine import ChatBotEngine
from datetime import date
from person import Person
from people import People
import nltk
import os

chappie = ChatBotEngine();

person = Person("Obama", "Barrack", 'M', date.today(), "Missouri", 82, 174, "New York")
People.add(person)


str = 'Salut ! Quel est l\'âge de Barrack Obama ?'
print(chappie.talk(str))


###############################
# Exemple utilisation de ntlk #
###############################

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

nltk.data.path.append(BASE_DIR + '/nltk_data/')

talk = "Salut ! Tu es très beau. Voilà je voulais te le dire. M. Enzo Hamelin nous a bien aidé. Haha, ça fonctionne bien... C'est drôle non ? Ok."

s = nltk.sent_tokenize(talk, "french") # On découpe en phrase
for si in s:
    print(nltk.word_tokenize(si, "french")) # Pour chaque phrase on recupère les tokens
