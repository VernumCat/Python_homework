grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
students.sort()
grades_average = list()
for ball in grades:
    ball = sum(ball) / len(ball)
    grades_average.append(ball)
journal = {st:gr_a for st, gr_a in zip(students, grades_average)}
print(journal)