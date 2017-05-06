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


str = 'Combien a d\'enfants Ryan Gosling ?'
print(chappie.talk(str))


###############################
# Exemple utilisation de ntlk #
###############################

#talk = "Salut ! Tu es très beau. Voilà je voulais te le dire. M. Enzo Hamelin nous a bien aidé. Haha, ça fonctionne bien... C'est drôle non ? Ok."
#talk = 'Salut ! Connais-tu l\'âge de Pierre ?'

#s = nltk.sent_tokenize(talk, "french") # On découpe en phrase
#for si in s:
#    tokens = nltk.word_tokenize(si, "french")
#    print(tokens) # Pour chaque phrase on recupère les tokens