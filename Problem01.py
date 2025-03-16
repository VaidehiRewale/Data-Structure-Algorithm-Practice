Print sum of first n numbers 
E.g. n=5, output=15 (1+2+3+4+5=15) 

def sum_of_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

n = int(input("Enter a number: "))
print("Sum of first", n, "numbers is:", sum_of_n(n))
