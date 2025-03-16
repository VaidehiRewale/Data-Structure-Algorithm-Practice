3.	Use while loop and print following pattern: n = 19 
1 2 3 4 5 * * * * * 11 12 13 14 15 * * * * 
 
Here sets are divided by 5, first set prints numbers where next set prints * so on and so forth 
 
If n=12, output: 1 2 3 4 5 * * * * * 11 12 
If n=4, output: 1 2 3 4 


def print_pattern(n):
    i = 1
    count = 0  

    while i <= n:
        if count % 2 == 0:  
            for _ in range(5):
                if i > n:
                    break
                print(i, end=" ")
                i += 1
        else: 
            for _ in range(5):
                if i > n:
                    break
                print("*", end=" ")
                i += 1
        
        count += 1 

print_pattern(int(input("Enter a number: ")))
