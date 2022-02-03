from dao.user_repository import UserRepository
from entity.user import User
from exception.invalid_username_or_password import InvalidUsernameOrPassword


class LoginController:

    """Login Controller class"""

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
        self._logged_user = None

    def register(self, user: User) -> User:
        """To register user"""
        created = self.user_repository.create(user)
        return created

    def login(self, username: str, password: str) -> User:
        """To login user"""
        user = self.user_repository.find_by_username(username)
        if user is not None and user.password == password:
            self._logged_user = user
            return user
        raise InvalidUsernameOrPassword("Invalid username or password. Try again.")

    def logout(self) -> User:
        """To logout user"""
        self._logged_user = None

    def get_logged_user(self) -> User | None:
        """To get logged user"""
        return self._logged_user
