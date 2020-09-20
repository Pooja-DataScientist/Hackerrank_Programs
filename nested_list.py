if __name__ == '__main__':
    grade = []
    names=[]
    for i in range(int(input())):
        name = input()
        score = float(input())
        j = name,score
        j=list(j)
        grade.append(j)
    grade.sort(key=lambda x: x[1])
    lowest = grade[0].__getitem__(1)
    second_lowest = 0
    for l in grade:
        if l[1]==lowest:
            lowest = l[1]
        elif l[1] >lowest:
            second_lowest = l[1]
            break
    for l in grade:
        if l[1] == second_lowest:
            names.append(l[0])
            names.sort()
    for i in names:
        print(i)
