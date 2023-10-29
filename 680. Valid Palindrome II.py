'''
We can use the standard two-pointer approach that starts at the left and right of the string and move inwards. Whenever there is a mismatch, 
we can either exclude the character at the left or the right pointer. 
We then take the two remaining substrings and compare against its reversed and see if either one is a palindrome.
'''

# 用另外一個函數來判斷是不是Palindrome
# 兩個pointer
def validPalindrome(s: str) -> bool:
    i = 0
    j = len(s)-1
    while i < j:
        if s[i] != s[j]:
            delete_i = s[i+1:j+1]
            delete_j = s[i:j]
            return _isPalindrome(delete_i) or _isPalindrome(delete_j)
        i += 1
        j -= 1
    return True

def _isPalindrome(s):
    return s == s[::-1]

import pdb
pdb.set_trace()

if __name__ == "__main__":

    s = "ebcbbececabbacecbbcbe"
    print(validPalindrome(s)) # True
    s = "eeccccbebaeeabebccceea"
    print(validPalindrome(s)) # False
    s = "atbbga"
    print(validPalindrome(s)) # False
    s = "aba"
    print(validPalindrome(s)) # True
    s = "abca"
    print(validPalindrome(s)) # True, delete c
    s = "abc"
    print(validPalindrome(s)) # False
    s = "deee"
    print(validPalindrome(s)) # True, delete d