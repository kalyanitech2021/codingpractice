# Given a string without spaces, the task is to remove duplicates from it.
# Note: The original order of characters must be kept the same. 

# Example:
# Input: S = "zvvo"
# Output: "zvo"
# Explanation: Only keep the first
# occurrence

# Expected Time Complexity: O(|s|)
# Expected Auxiliary Space: O(constant)

def removeDuplicate(str, n):
    index = 0

    for i in range(n):
        for j in range(0, i + 1):
            if str[i] == str[j]:
                break
        if j == i:
            str[index] = str[i]
            index += 1
             
    return "".join(str[:index])

str= "geeksforgeeks"
n = len(str)
print(removeDuplicate(list(str), n))