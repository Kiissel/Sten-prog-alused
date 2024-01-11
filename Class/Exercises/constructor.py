"""Constructor exercise."""


class Empty:
    """An empty class without constructor."""


class Person:
    """Represent person with firstname, lastname and age."""

    def __init__(self):
        self.firstname = ""
        self.lastname = ""
        self.age = 0


class Student:
    """Represent student with firstname, lastname and age."""

    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age


if __name__ == '__main__':

    empty_constructor = Empty()

# 3 x person usage
person1 = Person.firstname = "Mati"
person1 = Person.lastname = "Kurikas"
person1 = Person.age = 20

person2 = Person.firstname = "Kati"
person2 = Person.lastname = "Kapsas"
person2 = Person.age = 22

person3 = Person.firstname = "Tiit"
person3 = Person.lastname = "Teet"
person3 = Person.age = 24

# 3 x student usage
student1 = Student("Madli", "Kurikas", 21)
student2 = Student("Kristo", "Mutter", 22)
student3 = Student("Kadri", "Peet", 23)