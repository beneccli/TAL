from ChatBotEngine import ChatBotEngine
from datetime import date
from person import Person
from people import People


person = Person("Obama", "Barrack", 'M', date.today(), "Missouri", 82, 174, "New York")
People.add(person)

#People.find("firstname", "Obama")

str = 'slt ! Cmt ça va ?'
print(ChatBotEngine.talk(str))
