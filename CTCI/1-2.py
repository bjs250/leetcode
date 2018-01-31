def reverseString(s):
    ans = ""
    for i in range(0, len(s)):
        ans += s[len(s)-1-i]
    return ans

s = "abcd"
print(reverseString(s))
