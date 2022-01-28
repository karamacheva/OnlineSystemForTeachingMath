from dao.repository import Repository
from entity.anonymous_user import AnonymousUser

class AnonymousUserRepository(Repository):

    """Child class for AnonymousUserRepository"""

    def find_by_age(self, age: int) -> list[AnonymousUser]:
        """find Anonymous Users from input age"""
        anonymous_users_list = self.find_all()
        results = [anonymous_user for anonymous_user in anonymous_users_list if age == anonymous_user.age]
        return results

    def find_by_interests(self, interests_part: str) -> list[AnonymousUser]:
        """find Anonymous Users from input interests"""
        interests_part = interests_part.lower()
        anonymous_users_list = self.find_all()
        results = []
        for anonymous_user in anonymous_users_list:
            for interests in anonymous_user.interests:
                if interests_part in interests.lower():
                    results.append(anonymous_user)
        return results
