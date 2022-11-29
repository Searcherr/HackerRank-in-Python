if __name__ == '__main__':
    n = int(input('Input number of students'))
    if n < 2 or n > 10:
        print('We need more then 1 and less than 11 students')
    else:
        student_marks = {}
        for _ in range(n):
            name, *line = input().split()
            scores = list(map(float, line))
            student_marks[name] = scores
        query_name = input('Input name of the student: ')
        if query_name not in student_marks.keys():
            print('There is no student with given name')
        else:
            mean_score = sum(student_marks[query_name]) / len(student_marks[query_name])
            format_mean_score = "{:.2f}".format(mean_score)
            print(format_mean_score)