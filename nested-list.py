# Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([score, name])
    
    records.sort()
    last = records[0][0]
    names = []
    second_last = 0

    for element in records:
        if not element[0] == last:
            second_last = element[0]
            break

    for element in records:
        if second_last == element[0]:
            names.append(element[1])
        
    names.sort()
    for name in names:
        print(name)
    