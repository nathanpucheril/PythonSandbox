def does_contain(n, digit):
    if n % 10 == digit:
        return True
    if not n // 10 == 0:
        return does_contain(n//10, digit)
    return False

def pingpong(n):
    #1 for up, -1 for down
    def help_me_PLEASE(val,k, op):
        if k == n:
            return val
        elif does_contain(k, 7) or k % 7 == 0:
            return help_me_PLEASE(val - op, k + 1, -(op))
        return help_me_PLEASE(val + op, k + 1, op)
    return help_me_PLEASE(1, 1, 1)

print(pingpong(69))
