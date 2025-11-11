def is_palindrome(word: str) -> bool:
    if len(word) <= 1:
        return True
    
    if word[0] is not word[-1]:
        return False

    rest = word[1:-1]
    return is_palindrome(rest)

print(is_palindrome('ANA'))
print(is_palindrome("MADEIRA"))
