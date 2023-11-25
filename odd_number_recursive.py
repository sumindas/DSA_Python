def odd_sum_recursive(num):
    if num < 0:
        return 0
    elif num%2 == 0:
        return odd_sum_recursive(num-1)
    else:
        return num + odd_sum_recursive(num-2)
limit = 17
print(odd_sum_recursive(limit))
