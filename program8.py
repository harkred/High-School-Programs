#To check if a sting is palindrome or not
def is_palindrome(stri):
    x = 'Palindrome' if stri == stri[::-1] else 'Not palindrome'
    return x

stri = 'eye'
print(is_palindrome(stri))
