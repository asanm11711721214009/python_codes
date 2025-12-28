
# If check the palindrome or not
# It gives the result is True or False

def is_palindrome(s):
    s=s.lower()
    return s==s[::-1]
print(is_palindrome("Racecar"))