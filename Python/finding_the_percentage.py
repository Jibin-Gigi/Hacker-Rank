if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    score_list = student_marks[query_name]
    result = 0
    count = 0
    for score in score_list:
        result += score
        count += 1
    average = result / count
    print(f"{average:.2f}")
