from datetime import date


class Student():
    def __init__(self, s, n, d, c):
        self.__studentID = s
        self.__name = n
        self.__DOB = d
        self.__classification = c

    def age(self):
        dob = self.__DOB.split('/')
        dob_year = int(dob[2])
        today = date.today()
        self.__age = today.year - dob_year

    def registration(self):
        registration_days = {

            "Senior": '4/1 - 4/3',
            "Junior": '4/4 - 4/6',
            "Sophomore": '4/7 - 4/9',
            "Freshman": '4/10 - 4/12'
        }
        self.registration_day = registration_days[self.__classification]

    def get_age(self):
        return self.__age

    def get_registration(self):
        return self.registration_day
