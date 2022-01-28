from dao.repository import Repository
from entity.administartor import Administrator

class AdministatorRepository(Repository):

    """Child class for AdministatorRepository"""

    def find_by_internship(self, internship: int) -> list[Administrator]:
        """find admins from input internship"""
        admin_list = self.find_all()
        results = [administrator for administrator in admin_list if internship == administrator.internship]
        return results

    def find_by_responsibility(self, responsibility_part: str) -> list[Administrator]:
        """find admins from input responsibility"""
        responsibility_part = responsibility_part.lower()
        admin_list = self.find_all()
        results = []
        for administrator in admin_list:
            for responsibility in administrator.responsibility:
                if responsibility_part in responsibility.lower():
                    results.append(administrator)
        return results
