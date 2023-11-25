def max_heapify(array,n,i):
    largest = i
    left = (2*i) + 1
    right = (2*i) + 2
    if left < n and array[left] > array[largest]:
        largest = left
    if right < n and array[right] > array[largest]:
        largest = right
    if largest != i:
        array[i],array[largest] = array[largest],array[i]
        max_heapify(array,n,largest)
        
def heap_sort(array):
    n = len(array)
    for i in range(n // 2-1 , -1 , -1):
        max_heapify(array,n,i)
    
    for i in range(n-1 , 0 , -1):
        array[i],array[0] = array[0],array[i]
        max_heapify(array,i,0)
    
    return array
        
array = [12,87,9,2,34,54,76]
data = heap_sort(array)
print("Sorted Array:",data)