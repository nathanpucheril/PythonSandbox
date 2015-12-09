# n Choose k

def nchoosek(n, k):
    val = 1
    k_fact = 1
    for i in range(k):
        k_fact *= (i+1)
    for i in range(k):
        val *= n
        n -=1
    return val/k_fact


import math
def nchoosekNaive(n,k):
    return (math.factorial(n)/(math.factorial(k) * math.factorial(n-k)))

# print(nchoosek(500000000000000,24))
print(nchoosekNaive(500000000000000,24))
