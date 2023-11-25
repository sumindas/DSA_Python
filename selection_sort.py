def selection_min_sort(array):
    for i in range(len(array)):
        min_value = min(array[i:])
        min_index = array.index(min_value) 
        array[i] , array[min_index] = array[min_index] , array[i]
    return array

def selection_sort(array):
    for i in range (len(array)):
        min_index = i
        for j in range (i+1, len(array)):
            if array [j] < array[min_index]:
                min_index = j
        array[i] , array [min_index] = array[min_index] , array[i]
    return array
            

my_array = [45,87,98,23,13,12,11]
print(f"Orginal Array is {my_array}")
print("Array After Sort",selection_sort(my_array))