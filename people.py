# Database of people
class People:
    people = []

    @staticmethod
    def add(person):
        People.people.append(person)

    @staticmethod
    def findByName(fullname): #Should be improved, like looking for firstname, lastname and both
        results = []
        for person in People.people:
            if person.firstname == fullname:
                results.append(person)
        return results

    @staticmethod
    def find(attr, value):
        results = []
        for person in People.people:
            if     attr == 'firstname' and person.firstname == value \
                or attr == 'lastname' and person.lastname == value \
                or attr == 'birthday' and person.birthday == value \
                or attr == 'birthday_place' and person.birthday_place == value \
                or attr == 'weight' and person.weight == value \
                or attr == 'size' and person.size == value \
                or attr == 'place' and person.place == value:
                results.append(person)
        return results