if __name__ == '__main__':
    number_of_students = int(input('Enter the number of students'))
    records = []
    for _ in range(number_of_students):
        name = input()
        score = float(input())
        records.append([name, score])
    records.sort(key=lambda x: x[0])
    records.sort(key=lambda x: x[1])
    scores = []
    for i in range(len(records)):
        scores.append(records[i][1])
    scores = list(set(scores))
    finding_score = scores[1]
    for i in range(len(records)):
        if records[i][1] == finding_score:
            print(records[i][0])


