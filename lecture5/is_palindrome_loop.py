def is_palindrome(s: str) -> bool:
    # if we find a mismatch, it's not a palindrome
    for i in range(0, len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True

print("anna", is_palindrome("anna"))
print("Anna", is_palindrome("Anna"))
print("otto", is_palindrome("otto"))
print("gnubelebung", is_palindrome("gnubelebung"))