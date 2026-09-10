def palindrome(s):
    if s[::-1]==s:
        return 'y'
    else:
        return 'n'
a=input('Enter a string:')
print(palindrome(a))
