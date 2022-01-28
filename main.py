from entity.student import Student
from entity.teacher import Teacher
from entity.administartor import Administrator
from entity.anonymous_user import AnonymousUser
from dao.student_repository import StudentRepository
from dao.teacher_repository import TeacherRepository
from dao.admin_repository import AdministatorRepository
from dao.anonymous_repository import AnonymousUserRepository

if __name__ == '__main__':

    s1 = Student("Ekaterina", "Radoslavova", "Karamacheva", 16, "Female", "kati_kar@abv.bg", 359893592908,
                 "ekaramac", "KaTi1810", 10, 13)
    #print(s1)

    s2 = Student("Darina", "Ivanova", "Nikolova", 15, "Female", "dari_nik@abv.bg", 359895689542,
                 "dinikol", "dart1154", 10, 6)
    #print(s2)

    t1 = Teacher("Elizabet", "Evgenieva", "Arnaudova", 46, "Female", "elizabet.arnaudova@gmail.com", 359879606628,
                 "earnaud", "beti1503", 22, "master")
    #print(t1)

    t2 = Teacher("Kristina", "Dimitrova", "Kasabova", 41, "Female", "kristina.kasabova@gmail.com", 359879554268,
                 "kkasabova", "kris5489", 15, "Bachelor")
    #print(t2)

    a1 = Administrator("Ivan", "Georgiev", "Petrov", 32, "Male", "ivan.petrov@gmail.com", 359878568935, "ivanadmin",
                       "adminmanage1", "It Manager", 9, ("manage admin team", "set up new employee in admin team"))
    #print(a1)

    a2 = Administrator("Vladimir", "Petrov", "Gerdanov", 28, "Male", "vlad.gerdan@gmail.com", 359878684869, "vladiadm",
                       "adminsupport1", "Desktop Support", 5, ("support",))
    #print(a2)

    au1 = AnonymousUser("Gabriel", "Nikolov", "Aleksandrov", 21, "Male", "gabi_al@abv.bg", 359899625471, "student",
                        ("math", "swimming"))
    #print(au1)

    au2 = AnonymousUser("Mariya", "Antonova", "Yordanova", 29, "Female", "mariya_yo@abv.bg", 359895262843, "designer",
                        ("driving", "cooking", "math"))
    #print(au2)

    students = (s1, s2)
    students_repo = StudentRepository()

    for student in students:
        students_repo.create(student)

    print("\nStudents are:")
    for student in students_repo.find_all():
        print(student)

    print("\nStudents from 10th grade:")
    for student in students_repo.find_by_class_grade(10):
        print(student)

    print("\nStudents which are 15 years old:")
    for student in students_repo.find_by_age(15):
        print(student)

    teachers = (t1, t2)
    teachers_repo = TeacherRepository()

    print("\nTeachers are:")
    for teacher in teachers:
        teachers_repo.create(teacher)

    for teacher in teachers_repo.find_all():
        print(teacher)

    print("\nTeachers with 15 years internship:")
    for teacher in teachers_repo.find_by_internship(15):
        print(teacher)

    print("\nTeachers with master degree:")
    for teacher in teachers_repo.find_by_professional_degree("Master"):
        print(teacher)

    administrators = (a1, a2)
    administrators_repo = AdministatorRepository()

    print("\nAdministrators are:")
    for administrator in administrators:
        administrators_repo.create(administrator)

    for administrator in administrators_repo.find_all():
        print(administrator)

    print("\nAdministrators with 5 years internship:")
    for administrator in administrators_repo.find_by_internship(5):
        print(administrator)

    print("\nAdministrators with manage responsibility:")
    for administrator in administrators_repo.find_by_responsibility("manage"):
        print(administrator)

    anonymous_users = (au1, au2)
    anonymous_users_repo = AnonymousUserRepository()

    print("\nAnonymous users are:")
    for anonymous_user in anonymous_users:
        anonymous_users_repo.create(anonymous_user)

    for anonymous_user in anonymous_users_repo.find_all():
        print(anonymous_user)

    print("\nAnonymous users which are 29 years old")
    for anonymous_user in anonymous_users_repo.find_by_age(29):
        print(anonymous_user)

    print("\nAnonymous users with interests for math:")
    for anonymous_user in anonymous_users_repo.find_by_interests("Math"):
        print(anonymous_user)





