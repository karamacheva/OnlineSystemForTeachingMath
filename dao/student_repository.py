from dao.repository import Repository
from entity.student import Student

class StudentRepository(Repository):

    """Child class for StudentRepository"""

    def find_by_class_grade(self, class_grade: int) -> list[Student]:
        """find student from input class_grade"""
        student_list = self.find_all()
        results = [student for student in student_list if class_grade == student.class_grade]
        return results

    def find_by_age(self, age: int) -> list[Student]:
        """find student from input age"""
        student_list = self.find_all()
        results = [student for student in student_list if age == student.age]
        return results



