def hailstone_repeater(k):
    def hailstone(n):
        i = 0
        while i < k + n:
            print(n)
            i+=1
        if n == 1:
            return
        if n % 2 == 0:
            hailstone(n//2)
        else:
            hailstone(3*n + 1)
    return hailstone

fn = hailstone_repeater(2)
fn(5)
