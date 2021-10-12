#sebastian mertins programming 11 test scores project
#the program goes through the list, takes certain numbers out, then averages them, and then prints the average.

assignment_list = [[34, 12], [45, 78], [67, 89], [20, 97]]

for i in range(len(assignment_list)):
    for j in range(len(assignment_list[i])):
        average1 = (assignment_list[i][0] + assignment_list[i][1])/2
    if i == 0:
        print(f"average for assignment 1: {average1}")
    if i == 1:
        print(f"average for assignment 2: {average1}")
    if i == 2:
        print(f"average for assignment 3: {average1}")
    if i == 3:
        print(f"average for assignment 4: {average1}")

for i in range(len(assignment_list)):
    for j in range(len(assignment_list[i])):
        average2 = (assignment_list[0][j] + assignment_list[1][j] + assignment_list[2][j] + assignment_list[3][j])/4
        if j == 0:
            print(f"average for student 1: {average2}")
        if j == 1:
            print(f"average for student 2: {average2}")
    if j == 1:
        break