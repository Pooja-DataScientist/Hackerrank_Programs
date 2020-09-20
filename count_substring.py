
def count_substring(string, substring):
    count = 0
    for i in range(0, len(string)):
        if string[i:].startswith(substring):
            count=count+1
    return count


if __name__ == '__main__':
    string = input().strip()
    substring = input().strip()
    substring_count = count_substring(string, substring)
    print(substring_count)





