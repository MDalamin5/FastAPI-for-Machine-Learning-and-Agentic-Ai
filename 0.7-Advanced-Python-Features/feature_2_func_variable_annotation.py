##
name: str = "Md Al Amin"
age: int = 27
is_student: bool = False


## functions Annotations

def greet(person: str, age: int) -> str:
    """
    Greets a person by name and age

    :param person: The name of the person (expected to be a string)
    :param age: The age of the person (expected to be an integer)
    :return: A greeting message (Expected to be a string)
    """

    return f"Hello, {person}! You are {age} years old."