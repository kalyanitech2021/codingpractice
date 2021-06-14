# Geek lost the password of his super locker. 
# He remembers the number of digits N as well as the sum S of all the digits of his password. 
# He know that his password is the largest number of N digits that can be made with given sum S. 
# As he is busy doing his homework, help him retrieve his password.

# Example:
# Input:
# N = 5, S = 12
# Output:
# 93000
# Explanation:
# Sum of elements is 12. Largest possible 
# 5 digit number is 93000 with sum 12.

# Example:
# Input:
# N = 3, S = 29
# Output:
# -1
# Explanation:
# There is no such three digit number 
# whose sum is 29.

# Expected Time Complexity : O(N)
# Expected Auxilliary Space : O(1)

def largestNumber(n, s):
    if s == 0:
        if n == 1:
            print("largest number is: " , "0") 
        else:
            print("not possible")
        return

    if s > 9 * n:
        print("not possible")
        return

    result = [0] * n

    for i in range(n):
        if s >= 9:
            result[i] = 9
            s = s - 9
        else:
            result[i] = s
            s = 0

    print("largest number is: ", end= "")
    
    for i in range(0, n) :
        print(result[i], end = "")

n = 5
s = 12
largestNumber(n, s)