Print Factorial of n 
E.g n=4, output=24 (1*2*3*4=24) 

def factorial(num):
    return 1 if num ==0 else num*factorial(num-1)
num = int(input("enter a number:"))
print(f"FACTORIAL:", factorial(num))
