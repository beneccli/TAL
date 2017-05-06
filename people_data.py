# Database of people
import datetime
from person import Person
from people import People

people = []
ryanGosling = Person("Ryan","Gosling",'M',datetime(1980, 12, 1),"london",184)
tomCruise = Person("Tom","Cruise",'M',datetime(1962,7,3),"Syracuse",170)
markWahlberg = Person("Mark","Wahlberg",datetime(1971,6,5),"Boston",173)
vinDiesel = Person("Vin","Diesel",datetime(1967,7,18),"Comté d'Alameda CA",182)
kimKardashian = Person("Kim","Kardashian",datetime(1980,10,21),"Los Angeles",158)

ryanGosling.children.append(tomCruise)
ryanGosling.parents.append(vinDiesel)

people.append(ryanGosling)
people.append(tomCruise)
people.append(markWahlberg)
people.append(vinDiesel)
people.append(kimKardashian)


for person in people :
    People.people.add(person)