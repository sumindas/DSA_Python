def bubble_sort(array):
    for i in range(len(array)):
        for j in range(0,len(array)-i-1):
            if array[j]>array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
    return array
                
my_array = [45,87,98,23,13,12,11]
print(f"Orginal Array is {my_array}")
print("Array After Sort",bubble_sort(my_array))