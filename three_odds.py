def three_odds(array):
    for i in range(0,len(array)):
        if array[i]%2!=0:
            if i < len(array)-2:
                if array[i+1]%2!=0 and array[i+2]%2!=0:
                    print("True")

arr = [2,6,4,1,3]
three_odds(arr)