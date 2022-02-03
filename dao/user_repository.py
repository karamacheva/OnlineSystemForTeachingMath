from dao.repository import Repository
from entity.user import User
from util.func_util import find

class UserRepository(Repository):

    """Child class for UserRepository"""

    def find_by_username(self, username: str) -> User | None:
        users_list = self.find_all()
        results = find(lambda user: user.username == username, users_list)
        return results