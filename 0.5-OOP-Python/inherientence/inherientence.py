## ---> Logics behind Override <----

class Pet:
    def __init__(self, name, age):

        self.name = name
        self.age = age

    def show(self):
        print(f"I'm {self.name} and my age is {self.age}.")

    def speak(self):
        print("I do not know how to talk")


class DD(Pet):
    def __init__(self, name, age, origin):
        super().__init__(name, age)
        self.origin = origin

    def speak(self):
        print("Hau-Hau...")

class Pagla(Pet):
    # def speak(self):
    #     # super().speak()
    #     print("test line")

    pass

    


d = DD("Md Al Amin", 27, "BD")
print(d.name)
d.speak()

p = Pagla("AAA", 40)
p.speak()