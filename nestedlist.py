if __name__ == '__main__':
    n = int(input())
    students = []
    for _ in range(n):
        name = input()
        score = float(input())
        students.append((name, score))
    students.sort(key=lambda x: (x[1], x[0]))
    second_lowest_score = None
    lowest_score = students[0][1]
    for student in students:
        if student[1] > lowest_score:
            second_lowest_score = student[1]
            break
    second_lowest_students = [name for name, score in students if score == second_lowest_score]
    for name in sorted(second_lowest_students):
        print(name)
