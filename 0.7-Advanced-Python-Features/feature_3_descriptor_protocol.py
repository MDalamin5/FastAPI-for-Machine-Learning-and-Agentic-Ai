class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        """
        __repr__ is meant to 
        """

        return f"Person(name={self.name!r}, age: {self.age})"
    

    def __repr__(self):
        """
        __str__ its presents readable string of the object.
        """
        return f"{self.name}, age: {self.age}"
    

    
person = Person("Md Al Amin", 27)
print(repr(person))
print(person)