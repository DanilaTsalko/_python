# -*- coding: utf-8 -*-
class Student:
    # Атрибут класса
    students_quantity = 0

    def __init__(self, name, course, grades):
        self.name = name
        self.course = course
        self.grades = grades

        # Увеличиваем счётчик студентов при создании нового объекта
        Student.students_quantity += 1

    def is_honors_student(self):
        """
        Возвращает True, если средний балл по всем предметам больше 8.5
        """
        total_score = 0
        total_subjects = 0

        for subject, scores in self.grades.items():
            total_score += sum(scores)
            total_subjects += len(scores)

        average_score = total_score / total_subjects
        return average_score > 8.5

    def avg_score_by_subject(self, subject):
        """
        Возвращает средний балл по указанному предмету
        """
        if subject not in self.grades:
            raise ValueError(f"Subject '{subject}' not found.")

        scores = self.grades[subject]
        average_score = sum(scores) / len(scores)
        return f"Average score for {subject} = {average_score:.2f}"

# Пример использования
student = Student("Anna", 2, {"programming": [9, 8, 2, 3, 1], "FE": [9, 2, 3, 1, 8]})
print(student.is_honors_student())  # True
print(student.avg_score_by_subject("programming"))  # Average score for programming = 9.00