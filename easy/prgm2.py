# Given a string S, check if it is palindrome or not.

# Example:
# Input: S = "abba"
# Output: 1
# Explanation: S is a palindrome

# Input: S = "abc" 
# Output: 0
# Explanation: S is not a palindrome

# Expected Time Complexity: O(Length of S) 
# Expected Auxiliary Space: O(1)

def isPalindrome(str):
    return str == str[::-1]
        
str = "madam"
result = isPalindrome(str)

if result:
    print(1)
else:
    print(0)

