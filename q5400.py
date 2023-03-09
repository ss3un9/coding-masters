n = int(input())
students = []

for i in range(n):
    name, iq = input().split()
    students.append((name, int(iq)))

sorted_students = sorted(students, key=lambda x: -x[1])  # IQ 역순으로 정렬

for i in range(3):
    print(sorted_students[i][0])  # 상위 3명의 이름 출력