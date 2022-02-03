from entity.user import User

class Teacher(User):

    """Child class Teacher for one of users in the online system"""

    next_id = 0 # unique id sequence

    @classmethod
    def get_next_id(cls):
        cls.next_id += 1
        return cls.next_id

    def __init__(self, first_name: str, second_name: str, last_name: str, username: str, password: str, age: int,
                 gender: str, email: str, telephone_number: int, internship: int, professional_degree: str):
        super().__init__(first_name, second_name, last_name, username, password, age, gender, email, telephone_number)
        self.teacher_id = self.__class__.get_next_id()
        self.internship = internship
        self.professional_degree = professional_degree

    def __str__(self):
        return f"| {self.teacher_id:<12d} {super().__str__()} | {self.internship:<2d} |" \
               f" {self.professional_degree:<15.15s} |"
