def string_mutations(string, position, character):
    string_l = list(string)
    string_l[position] = character
    string_new = ''.join(string_l)
    return string_new

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    new_string = string_mutations(s,int(i),c)
    print(new_string)
