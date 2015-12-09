def count_digits(num, d):
    count = 0
    while num > 0:
        num , curr_digit = num//10, num%10
        if curr_digit == d:
            count += 1
    return count

def get_index(num, d):
    k = 0
    last = 0
    while k < num:
        num , curr_digit = num//10, num%10
        if curr_digit == d:
            last = k
        k+=1
    return last

print("Hello".find("ll"))
