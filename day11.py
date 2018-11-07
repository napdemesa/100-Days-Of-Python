
if __name__ == "__main__":
    n = int(input())

    student_marks = {}

    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

    query_name = input()

    sumMarks = 0

    for x in range(0, 3):
        sumMarks = sumMarks + student_marks[query_name][x]

    avg = sumMarks / 3

    print(avg)
