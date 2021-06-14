# Given two strings a and b consisting of lowercase characters. 
# The task is to check whether two given strings are an anagram of each other or not. 
# An anagram of a string is another string that contains the same characters, 
# only the order of characters can be different. 
# For example, “act” and “tac” are an anagram of each other.

# Example:
# Input:
# a = geeksforgeeks, b = forgeeksgeeks
# Output: YES
# Explanation: Both the string have same
# characters with same frequency. So, 
# both are anagrams.

# Expected Time Complexity: O(|a|+|b|).
# Expected Auxiliary Space: O(Number of distinct characters).

def isAnagram(str1, str2):
    n1 = len(str1)
    n2 = len(str2)

    if n1 != n2:
        return False

    str1 = sorted(str1)
    str2 = sorted(str2)

    for i in range(n1):
        if str1[i] == str2[i]:
            return True
        else:
            return False

str1 = "geeksforgeeks"
str2 = "forgeeksgeeks"
print("Output: ", isAnagram(list(str1), list(str2)))
