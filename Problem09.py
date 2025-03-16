Given a string of 0s and 1s print the value of string, where val(0)=1, val(1)=2 
Input: 00010110 
Output: 11 

def calculate_value(binary_string):
    total = 0
    for char in binary_string:
        total += 1 if char == '0' else 2
    return total

binary_string = input("Enter a binary string: ")
print(calculate_value(binary_string))
