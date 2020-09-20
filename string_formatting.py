def print_formated(number):
    for i in range(1,n+1):
        print("\n",i, end="\t")
        def decimaltooctal(n):
            if n>8:
                decimaltooctal(n//8)
            print(n%8, end="")

        def decimaltohexa(n):
            hexa = {10:'A', 11:'B',12:'C',13:'D',14:'E',15:'F'}
            if n>15:
                decimaltohexa(n//16)
            if n%16>9:
                print(hexa[n%16], end="")
            else:
                print(n%16,end="")

        def decimaltobinary(n):
            if n>1:
                decimaltobinary(n//2)
            print(n%2, end="")


        decimaltooctal(i)
        print("\t", end="")
        decimaltohexa(i)
        print("\t", end="")
        decimaltobinary(i)


if __name__ == '__main__':
    n = int(input())
    print_formated(n)