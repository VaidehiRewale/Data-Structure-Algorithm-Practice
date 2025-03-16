Write a code to achieve below pattern 
5 4 3 2 1 
D C B A 
3 2 1 
B A 
1 
def print_pattern():
    
    for i in range(5, 0, -1):
        print(i, end=" ")
    print()
   
    for i in range(68, 64, -1): 
        print(chr(i), end=" ")
    print()

    for i in range(3, 0, -1):
        print(i, end=" ")
    print()

    for i in range(66, 64, -1):
        print(chr(i), end=" ")
    print()

    print(1)


print_pattern()
