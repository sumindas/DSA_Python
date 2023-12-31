def partition(arr,low,high):
    pivot = arr[low]
    i = low + 1
    j = high
    while True:
        while i <=j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
            
        if i <= j:
            arr[i],arr[j] = arr[j],arr[i]
        else:
            break
        
    arr[low],arr[j] = arr[j],arr[low]
    return j
   

def quicksort(arr,low,high):
   if low < high:
       pivot_index = partition(arr,low,high)
       quicksort(arr,low,pivot_index-1)
       quicksort(arr,pivot_index+1,high)
   


array = [23,76,98,90,34,23,12,46,1]
print(f"Array Bfore Sort:{array}")
quicksort(array,0,len(array)-1)
print("Array After Sort:",array)

    
            