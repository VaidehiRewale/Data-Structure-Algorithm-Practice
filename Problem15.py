Write a function to solve the Two Sum problem, a popular interview question. Given an 
array of integers and a target sum, return the indices of the two numbers that add up to 
the target. For example, given the array [2, 7, 11, 15] and the target sum 9, the function 
should return [0, 1] because 2 + 7 = 9. 

def two_sum(nums, target):
    for i in range(len(nums)):  
        for j in range(i + 1, len(nums)):  
            if nums[i] + nums[j] == target:  
                return [i, j]  
    return []  

nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target)) 
 
