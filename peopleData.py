# Database of people
import datetime
import Person
import People

people = []
ryanGosling = Person("ryan","gosling",'M',datetime(1980, 12, 1),"london",184)
tomCruise = Person("tom","cruise",'M',datetime(1962,7,3),"Syracuse",170)
markWahlberg = Person("mark","wahlberg",datetime(1971,6,5),"Boston",173)
vinDiesel = Person("vin","diesel",datetime(1967,7,18),"Comté d'Alameda CA",182)
kimKardashian = Person("kim","kardashian",datetime(1980,10,21),"Los Angeles",158)

ryanGosling.children.append(tomCruise)
ryanGosling.parents.append(vinDiesel)

people.append(ryanGosling)
people.append(tomCruise)
people.append(markWahlberg)
people.append(vinDiesel)
people.append(kimKardashian)


for person in people :
    People.people.add(person)
    

