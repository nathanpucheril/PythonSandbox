def GCD(nums):
    def gcd_help(x,y):
        x,y = map(abs, (x,y))
        if y > x:
            return gcd_help(y,x)
        if y == 0:
            return x
        return gcd_help(y, x % y)
    return reduce(gcd_help, nums)


# def extended_gcd(x, y):
#     if y > x:
#         return gcd(y,x)
#     if y == 0:
#         return (x, x//y,y)
#     return (extended_gcd(y, x % y),


print(GCD((5,-5,10)))
