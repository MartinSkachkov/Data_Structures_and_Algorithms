def reverse_integer(n):
    rev_num = 0
    is_nagative = n < 0
    n = abs(n)

    while n != 0:
        last_digit = n % 10
        rev_num = rev_num * 10 + last_digit
        n //= 10

    if is_nagative:
        rev_num = -rev_num
    
    return rev_num

print(reverse_integer(-1234))