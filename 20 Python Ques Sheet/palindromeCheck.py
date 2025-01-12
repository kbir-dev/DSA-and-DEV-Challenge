def palindromeCheck(string):
    n = len(string)
    duplicate_str = "".join(reversed(string))
    if duplicate_str == string:
        return True
    else:
        return False

string = "Karan"
print(palindromeCheck(string))