n = int(input())
cols = (n*4)-3
string= 'abcdefghijklmnopqrstuvwxyz'
str2 = list(string[0:n])
str2.sort(reverse= True)
for i in range(1,n+1):
    l = list(str2[:i])
    k = list(str2[0:i-1])
    k.sort()
    c = '-'.join(l)
    m = '-'.join(k)
    if n!=1:
        print(((c)+'-'+m).center(cols,'-'))
    else:
        print((c+ m).center(cols, '-'))

for i in range(0,n-1):
    l = str2[0:n-1-i]
    k = str2[0:n-2-i]
    k.sort()
    c = '-'.join(l)
    m = '-'.join(k)
    if n!=1:
        print(((c)+'-'+m).center(cols,'-'))
    else:
        print(((c)+ m).center(cols, '-'))

























