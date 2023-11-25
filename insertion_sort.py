def insertion_sort(array):
    for i in range(1,len(array)):
        j = i
        while array[j-1] > array[j] and j > 0:
            array[j-1] , array[j] = array[j],array[j-1]
            j -= 1
    return array

my_array = [4,88,8,23,13,12,17]
print(f"Orginal Array is {my_array}")
print("Array After Sort",insertion_sort(my_array))
        