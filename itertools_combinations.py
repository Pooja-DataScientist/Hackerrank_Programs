from itertools import combinations

string, num = input().split()
for i in range(1, int(num)+1):
    for j in (combinations(sorted(string), i)):
        print(''.join(j))

