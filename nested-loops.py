M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# original list
school = [["Mary", "Jack", "Tiffany"],
          ["Brad", "Claire"],
          ["Molly", "Andy", "Carla"]]

student_list = []
for class_group in school:
    for student in class_group:
        student_list.append(student)
print(student_list)

student_list = [student for class_group in school for student in class_group]
print(student_list)

matrix = []

for i in range(2):

    # create empty row (a sublist inside our list)
    matrix.append([])  # two empty lists inside matrix are created

    for j in range(5):
        # populate the list
        matrix[i].append(j)
