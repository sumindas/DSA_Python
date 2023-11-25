def binary_recursive(arr,target,low,high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid+1
    elif arr[mid] < target:
        return binary_recursive(arr,target,mid + 1,high)
    else:
        return binary_recursive(arr,target,low,mid-1)

numbers = [12,34,54,65,76,87,99,100,124]
key = int(input("Enter The Key:"))
index = binary_recursive(numbers,key,0,len(numbers)-1)
if index != -1:
    print(f"Key Found At position {index}")
else:
    print("Key Not Found")
    