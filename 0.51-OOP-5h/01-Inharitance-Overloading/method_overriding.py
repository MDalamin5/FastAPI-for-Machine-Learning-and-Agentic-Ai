class User:
    def __init__(self):
        self.name = "Md Al Amin"
        self.age = 44

    def display_info(self):
        print("This is user class method...")


class Person(User):
    # Constructor overloading
    def __init__(self, profession):
        super().__init__()
        self.profession = profession


    # Method overriding...
    def display_info(self):
        print("I'm From Person Class")



if __name__ == "__main__":
    obj = Person("SwE")
    obj.display_info()