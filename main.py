from ChatBotEngine import ChatBotEngine
from datetime import date
from person import Person
from people import People


People.add(Person("Obama", "Barrack", date.today(), "Missouri", 82, 174, "New York"))
#People.find("firstname", "Obama")

str = 'Salut ! Connais-tu Barrack Obama ?'
print(ChatBotEngine.talk(str))

