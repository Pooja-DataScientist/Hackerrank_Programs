def merge_the_tools(string, k):
    split_string = []
    for i in range(0, len(string), k):
        split_string.append(string[i:i+k])
    for j in range(len(split_string)):
       split_string[j] = list(dict.fromkeys(split_string[j]))
       print(''.join(split_string[j]))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)