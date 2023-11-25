def max_heapify(arr,n,i):
    largest = i
    left = (2*i) + 1
    right = (2*i) + 2
    if i < n and arr[left] > arr[largest]:
        largest = arr[left]
    if i < n and arr[right] > arr[largest]:
        largest = arr[right]
    if i != largest:
        arr[i],arr[largest] = arr[largest],arr[i]
    max_heapify(arr,n,largest)
        
        
def heapsort(arr):
    l = len(arr)
    for i in range(l // 2,0,-1):
        max_heapify(arr,l,arr[i])
        
    for i in range(len,0,-1):
        arr[0],arr[i] = arr[i],arr[0]
        max_heapify(arr,l,0)
        
    return arr

array = [10,3,5,6,87,90]
print(heapsort(array))