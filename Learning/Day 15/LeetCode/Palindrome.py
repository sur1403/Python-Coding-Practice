x = 121
y = -121
z = 10

class Palindrome(object):
    def palindrome(self, x):
        str_x = str(x)
        if str_x == str_x[::-1]:
            return True
        else:
            return False 
palindrome = Palindrome()

result = palindrome.palindrome(x)
print("x", result)
result = palindrome.palindrome(y)
print("y",result)
result = palindrome.palindrome(z)
print("z", result)


  