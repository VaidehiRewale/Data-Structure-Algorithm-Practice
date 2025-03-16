 Write a function that generates the first n numbers of the Fibonacci sequence. The 
Fibonacci sequence is a series of numbers where each number is the sum of the two 
preceding ones, usually starting with 0 and 1. For example, the first 10 numbers in the 
Fibonacci sequence are: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.

def fib(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2, n):
            c = a + b
            a = b
            b = c
            print(c)

fib(10)
