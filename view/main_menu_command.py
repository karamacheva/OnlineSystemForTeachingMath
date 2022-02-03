from controller.login_controller import LoginController
from entity.user import User
from exception.invalid_username_or_password import InvalidUsernameOrPassword
from view.menu import Command

class RegisterCommand(Command):
    """Register"""

    def __init__(self, login_controller: LoginController):
        self.login_controller = login_controller

    def run(self) -> str:
        first_name = input("Enter first name:")
        second_name = input("Enter second name:")
        last_name = input("Enter last name:")
        username = input("Enter username:")
        password = input("Enter password:")
        age = int(input("Enter age:"))
        gender = input("Enter gender:")
        email = input("Enter email:")
        telephone_number = int(input("Enter telephone number:"))
        user = self.login_controller.register(User(first_name, second_name, last_name, username, password, age, gender,
                                                   email, telephone_number))
        return f"You are successfully registered as: {user.first_name} {user.second_name} {user.last_name} with" \
               f" your username: [{user.username}]"

class LoginCommand(Command):

    """Login"""

    def __init__(self, login_controller: LoginController):
        self.login_controller = login_controller

    def run(self) -> str:
        username = input("Enter username:")
        password = input("Enter password:")
        try:
            user = self.login_controller.login(username, password)
        except InvalidUsernameOrPassword as ex:
            return str(ex)
        return f"Hello, {user.first_name} {user.last_name} [{user.username}]!"

class LogoutCommand(Command):

    """Logout"""

    def __init__(self, login_controller: LoginController):
        self.login_controller = login_controller

    def run(self) -> str:
        self.login_controller.logout()
        return f"You have successfully logged out."

class GetLoggedUserCommand(Command):

    """Get logger user"""

    def __init__(self, login_controller: LoginController):
        self.login_controller = login_controller

    def run(self) -> str:
        user = self.login_controller.get_logged_user()
        if user is not None:
            return f"You are logged as: {user.first_name} {user.last_name} [{user.username}]."
        else:
            return "No user logged in."
