from itertools import permutations

string,num = input().split()
permutations_list = list(permutations(string, int(num)))
permutations_list.sort()
for i in range(len(permutations_list)):
    print("".join(permutations_list[i]))
