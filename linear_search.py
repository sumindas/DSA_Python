
def linear_search(res,k):
    pos = -1
    for i in range(len(res)):
        if res[i] == k:
            pos = i
            break
    if pos !=-1:
        print("Item Found At position",pos+1)
    else:
        print("Item Not found")

array = [32,76,87,89,80,788,56]
key = int(input("Enter The Key:"))
linear_search(array,key)
            
            



