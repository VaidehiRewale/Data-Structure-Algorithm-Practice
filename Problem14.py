 Write a function that implements the binary search algorithm using iteration. 

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid 
        elif arr[mid] < target:
            left = mid + 1 
        else:
            right = mid - 1 
    
    return -1 


arr = [1, 3, 5, 7, 9, 11]
target = 7
index = binary_search(arr, target)

if index != -1:
    print(f"Element found at index {index}")
else:
    print("Element not found")
