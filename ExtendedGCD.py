def egcd(x, y):
    print('x:', x, 'y:', y)
    if y > x:
        print("Flip x, y for purpose of algorithm ")
        return egcd(y,x)
    if y == 0:
        return (x, 1, 0)
    else:
        d, a, b = egcd(y, x % y)
        print('d:', d, 'a:', a, 'b:', b)
        print(str(a) + "-" +str(x) + "//"+str(y) + "*"+str(b))
        return (d, b, a - (x // y)*b)

print(egcd(7,20))
