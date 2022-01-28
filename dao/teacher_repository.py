from dao.repository import Repository
from entity.teacher import Teacher

class TeacherRepository(Repository):

    """Child class for TeacherRepository"""

    def find_by_internship(self, internship: int) -> list[Teacher]:
        """find teacher from input internship"""
        teacher_list = self.find_all()
        results = [teacher for teacher in teacher_list if internship == teacher.internship]
        return results

    def find_by_professional_degree(self, professional_degree: str) -> list[Teacher]:
        """find teacher from input professional_degree"""
        professional_degree = professional_degree.lower()
        teacher_list = self.find_all()
        results = [teacher for teacher in teacher_list if professional_degree == teacher.professional_degree]
        return results
