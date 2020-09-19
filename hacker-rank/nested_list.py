n = int(input())
student = []
score = set()
for i in range(n):
    s = input()
    x = float(input())
    score.add(x)
    student.append([s, x])
score = list(score)
name = []
for st in student:
    if st[1] == score[1]:
        name.append(st[0])
print(name[1])