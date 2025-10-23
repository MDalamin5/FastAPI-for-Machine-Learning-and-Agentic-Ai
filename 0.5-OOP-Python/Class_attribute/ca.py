class Person:
    number_of_object = 0 # this is class attribute.

    def __init__(self, name):
        self.name = name
        Person.number_of_object += 1


    # class Method
    @classmethod
    def number_of_people(cls):
        return cls.number_of_object
    
    @classmethod
    def add_person(cls):
        cls.number_of_object += 1


o1 = Person("Md Al Amin")
print(o1.number_of_object)

o2 = Person("Aminul")
print(o1.number_of_object)

print(Person.number_of_people())