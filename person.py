from datetime import date

class Person:
    firstname = ''
    lastname = ''
    birthday = ''
    birthday_place = ''
    weight = ''
    size = ''
    place = ''
    relatives = []

    def __init__(self):
        return

    def __init__(self, firstname, lastname,  birthday, birthday_place, weight, size, place):
        self.firstname = firstname
        self.lastname = lastname
        self.birthday = birthday
        self.birthday_place = birthday_place
        self.weight = weight
        self.size = size
        self.place = place