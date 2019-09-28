# Dictionary comprehension

# <variable> = { key:new_value for (key, value) in <dictionary>.items() }
grades = {'Nora': 90, 'Lulu': 15, 'Gino': 60}

double_grades = {key: value*2 for (key, value) in grades.items()}
print(double_grades)
# {'Nora': 180, 'Lulu': 30, 'Gino': 120}

# We can also add a condition in dict comprehension
grades_2 = {key: value*2 for (key, value) in grades.items() if value % 2 == 0}
print(grades_2)
# {'Nora': 180, 'Gino': 120}
