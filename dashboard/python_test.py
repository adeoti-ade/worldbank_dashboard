# try:
#     age = int(input("Please enter your age: "))
#     if age < 0:
#         raise ValueError("%d is not a valid age. \
#             Age must be positive or zero.")
# except ValueError as err:
#     print("You entered incorrect age input: %s" % err)
# else:
#     print("I see that you are %d years old." % age)

import datetime # we will use this for date objects
class Person:
    def __init__(self, name, surname, birthdate, address, telephone, email, age):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.address = address
        self.telephone = telephone
        self.email = email
        self._age = age

    def age(self):
        if hasattr(self, "_age"):
            return self._age
        today = datetime.date.today()
        age = today.year - self.birthdate.year
        if today < datetime.date(today.year, self.birthdate.month,
                                 self.birthdate.day):
            age -= 1

        return age
