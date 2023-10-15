# Solution 1
# +

    
# Solution 2n
# import pdb
# pdb.set_trace()
def isPalindrome(s: str) -> bool:
    start = 0
    end = len(s)-1
    s = s.lower()
    while start < end:
        while not s[start].isalnum():
            start += 1
            if start >= len(s):
                return False
        while not s[end].isalnum():
            end -= 1
            if end <= 0:
                return False
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True     

if __name__ == "__main__":
    # s = ""
    # s = "ab_a"
    s = "A man, a plan, a canal: Panama"
    # s = ".,"
    print(isPalindrome(s))