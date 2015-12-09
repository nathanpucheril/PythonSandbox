def gcd(x,y):
    if y > x:
        return gcd(y,x)
    if y == 0:
        return x
    return gcd(y, x % y)

def extended_gcd(x, y):
    if y > x:
        return gcd(y,x)
    if y == 0:
        return (x, x//y,y)
    return (extended_gcd(y, x % y), 

print(gcd(527, 323))
