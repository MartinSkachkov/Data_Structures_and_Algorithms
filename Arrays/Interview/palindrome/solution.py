def is_palindrome(s):
    l = 0
    r = len(s) - 1

    while l < r:
        if s[l] != s[r]:
            print("not palindrome")
            return
        l += 1
        r -= 1

    print("palindrome")

is_palindrome("racecar")
is_palindrome("hello") 