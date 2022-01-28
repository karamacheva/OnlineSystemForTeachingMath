from entity.person import Person

class Student(Person):

    """Child class Student for one of users in the online system"""

    next_id = 0 # unique id sequence

    @classmethod
    def get_next_id(cls):
        cls.next_id += 1
        return cls.next_id

    def __init__(self, first_name: str, second_name: str, last_name: str, age: int, gender: str, email: str,
                 telephone_number: int, username: str, password: str, class_grade: int,
                 number_in_class: int):
        super().__init__(first_name, second_name, last_name, age, gender, email, telephone_number)
        self.student_id = self.__class__.get_next_id()
        self.username = username
        self.password = password
        self.class_grade = class_grade
        self.number_in_class = number_in_class

    def __str__(self):
        return f"| {self.student_id:<12d} {super().__str__()} {self.username:<15.15s} | " \
               f"{self.password:<12.12s} | {self.class_grade:<2d} | {self.number_in_class:<2d} |"





