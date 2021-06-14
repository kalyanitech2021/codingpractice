# Given a String S, reverse the string without reversing its individual words. Words are separated by dots.

# Example:
# Input:
# S = i.like.this.program.very.much
# Output: much.very.program.this.like.i
# Explanation: After reversing the whole
# string(not individual words), the input
# string becomes
# much.very.program.this.like.i

# Expected Time Complexity: O(|S|)
# Expected Auxiliary Space: O(|S|)

def reverseWords(str, n):
    words = str.split('.')

    string = []

    for word in words:
        string.insert(0, word)
        reverseStr = '.'.join(string)
    return reverseStr

str = "i.like.this.program.very.much"
n = len(str)
print(reverseWords(str, n))
