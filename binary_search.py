def binary_search(num_list,key):
    start = 0
    end = len(num_list)-1
    while start <= end:
        mid = start + end //2
        if num_list[mid] == key:
            print("The Item Found At Position",mid+1)
            return
        elif num_list[mid] < key:
            start = mid+1
        elif num_list[mid] > key:
            end = mid-1
    print("The Key Not Found")
    
num_list = [12,34,36,45,78,98,99,100,108,110,112]
key = int(input("Enter The Key:"))
binary_search(num_list,key)
