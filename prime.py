def is_prime(number):
    if number <= 1:
        return False
    
    for i in range(1,int(number**0.5)+1):
        if number % 2 == 0:
            return False
    
    return True

array = [12,54,1,2,3,4,5,6,11,65,78]
print("prime numbers in array")
for i in array:
    if is_prime(i):
        print(i)
    
