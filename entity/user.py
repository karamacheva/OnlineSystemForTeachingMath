class User:

    """A base(parent) class User"""

    def __init__(self, first_name: str, second_name: str, last_name: str, username: str, password: str, age: int,
                 gender: str, email: str, telephone_number: int):
        self.first_name = first_name
        self.second_name = second_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.age = age
        self.gender = gender
        self.email = email
        self.telephone_number = telephone_number

    def __str__(self):
        return f"| {self.first_name:<15.15s} | {self.second_name:<15.15s} | {self.last_name:<15.15s} |" \
               f" {self.username:<15.15s} | {self.password:<15.15s} | {self.age:<2d} | {self.gender:<6.6s} | " \
               f"{self.email:<30.30s} | {self.telephone_number:<15d} |"

