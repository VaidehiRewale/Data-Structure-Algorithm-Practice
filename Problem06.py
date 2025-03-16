WAP to print following pattern 
1 
1 2 
1 2 3 

def pattern1(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

n = int(input("Enter the number of rows: "))
pattern1(n)
