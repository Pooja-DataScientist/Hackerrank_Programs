n = int(input("Enter numbers of students:"))
score = []
names=[]
for i in range(n):
    name = input("Enter name: ")
    grade = float(input("Enter grade: "))
    j = name,grade
    j=list(j)
    score.append(j)
score.sort(key=lambda x: x[1])
lowest = score[0].__getitem__(1)
second_lowest = 0
for l in score:
    if l[1]==lowest:
        lowest = l[1]
    elif l[1] >lowest:
        second_lowest = l[1]
        break
for l in score:
    if l[1] == second_lowest:
        names.append(l[0])
        names.sort()
for i in names:
    print(i)

