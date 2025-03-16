2.	Print list of odd/even numbers from 1-n, where n is input. E.g.  n = 10 even_nums = [2, 4, 6, 8, 10] odd_nums = [1, 3, 5, 7, 9] 
def get_odd_even(n):
    evens = [i for i in range(1, n + 1) if i % 2 == 0]
    odds = [i for i in range(1, n + 1) if i % 2 != 0]
    return evens, odds

n = int(input("Enter a number: "))
even_nums, odd_nums = get_odd_even(n)

print("Even numbers:", even_nums)
print("Odd numbers:", odd_nums)
