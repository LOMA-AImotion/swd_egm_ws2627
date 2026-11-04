def is_palindrome(s: str) -> bool:
    return s == s[::-1]
 
print("anna", is_palindrome("anna"))
print("Anna", is_palindrome("Anna"))
print("otto", is_palindrome("otto"))
print("gnubelebung", is_palindrome("gnubelebung"))