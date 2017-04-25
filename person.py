from datetime import date

class Person:
    firstname = ''
    lastname = ''
    gender = ''
    birthday = ''
    birthday_place = ''
    weight = ''
    size = ''
    place = ''
    parents = []
    children = []

    def __init__(self):
        return

    def __init__(self, firstname, lastname, gender, birthday, birthday_place, weight, size, place):
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.birthday = birthday
        self.birthday_place = birthday_place
        self.weight = weight
        self.size = size
        self.place = place