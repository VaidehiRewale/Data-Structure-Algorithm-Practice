WAP to print following pattern (use while loop): 
3 2 1 
  2 1 
    1 

def pattern2(n):
    i = n
    while i > 0:
        spaces = (n - i) * 2 
        print(" " * spaces, end="")  
        
        j = i
        while j > 0:
            print(j, end=" ")
            j -= 1
        
        print()
        i -= 1

n = int(input("Enter a number: "))
pattern2(n)
