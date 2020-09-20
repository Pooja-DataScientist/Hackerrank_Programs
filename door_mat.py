row, cols = map(int,input().split())
mid = (row+1)/2
i = 1
if row%2!=0 and cols == row*3:
    for c in range(1,row+1):
        if c < mid:
            print(('.|.'*i).center(cols,'-'))
            i = i+2
        elif c == mid:
            print('WELCOME'.center(cols,'-'))
            i = i-2
        elif c > mid:
            print(('.|.'*i).center(cols,'-'))
            i = i-2
else:
    print("Invalid Entry")