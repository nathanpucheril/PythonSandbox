memory = {}
def memo_fib(x):
    if x in memory:
        return memory[x]
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        val = memo_fib(x-2) + memo_fib(x-1)
        memory[x] = val
        return val

def memo_fib_iter(x):
    if x in memory:
        return memory[x]
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        curr, prev = 1, 0
        count = 1
        val = 0
        while count < x:
            val = curr + prev
            curr, prev = val, curr
            count += 1
        return val

print(memo_fib_iter(12334))
# print(memo_fib(7))
