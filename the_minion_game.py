def minion_game(string):
    startfromvowels, startfromconstant, t,  r = [],[],[],[]
    vowels = 'AEIOU'
    for i in range(0, len(string)):
        for j in range(i + 1, len(string) + 1):
            if string[i] in vowels:
                startfromvowels.append(string[i:j])
            else:
                startfromconstant.append(string[i:j])
    startfromvowels = list(dict.fromkeys(startfromvowels))
    startfromconstant = list(dict.fromkeys(startfromconstant))
    for i in range(len(startfromvowels)):
        substring = startfromvowels[i]
        def cousubstring(sub):
            count = 0
            for v in range(len(string)):
                if string[v:].startswith(sub):
                    count = count+1
            t.append(count)
        cousubstring(substring)
    for i in range(len(startfromconstant)):
        substring = startfromconstant[i]
        def cousubstring(sub):
            count = 0
            for v in range(len(string)):
                if string[v:].startswith(sub):
                    count = count+1
            r.append(count)
        cousubstring(substring)
    if sum(t)> sum(r):
        print('Kevin {}'.format(sum(t)))
    elif sum(r)> sum(t):
        print('Stuart {}'.format(sum(r)))
    else:
        print("Draw")


if __name__ == '__main__':
    n = input()
    minion_game(n)



