# Дополнительное практическое задание по модулю: "Базовые структуры данных."

# На вход даны следующие данные:
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]     # Список grades содержит списки оценок для каждого ученика в алфавитном порядке.
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}                           # Множество students содержит неупорядоченную последовательность имён всех учеников в классе.

# Напишите программу, которая составляет словарь, используя grades и students, где ключом будет имя ученика, а значением - его средний балл.
average_grades = [sum(grade)/len(grade) for grade in grades]
sort_students = sorted(students)
my_dict = dict(zip(sort_students, average_grades))
print(my_dict)