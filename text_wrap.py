import textwrap

def text_wrap(string, max_width):
    s = ""
    for i in range(0, len(string), max_width):
        s = s + string[i:i+max_width] + "\n"
    return s


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = text_wrap(string, max_width)
    print(result)