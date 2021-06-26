# Print the average of the marks array for the student name provided, showing 2 places after the decimal.

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    sum = 0
    for score in student_marks[query_name]:
        sum += score

    average = sum / len(student_marks[query_name])
    format_float = "{:.2f}".format(average)
    print(format_float)
