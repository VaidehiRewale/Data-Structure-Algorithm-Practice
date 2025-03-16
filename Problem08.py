Generate a dictionary which stores the count of appearance of character in string 
Input: aabbcdddededfg 
Output= {“a”: 2, “b”: 2, “c”: 1, “d”:5, “e”:2, “f”:1, “g”:1}

def char_count(s):
    freq = {}  
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

s = input("Enter a string: ")
print(char_count(s))
