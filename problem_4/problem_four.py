



def is_palindrome(val):
    if str(val) == ''.join((reversed(str(val)))):
        return True
    else:
        return False
def main(digits):
    max_res = 0
    initial = int('9'* digits)
    other = int(initial)
    lowest = int('1'+'0'*(digits-1))
    for left in range(lowest,initial):
        for right in range(lowest,left):
            if is_palindrome(left*right):
                max_res = max(max_res, left*right)
    print(max_res) 


main(3)