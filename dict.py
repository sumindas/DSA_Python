my_dict = {
    "apple": 3,
    "banana": 5,
    "orange": 2
}

for key in my_dict:
    print(key)

for value in my_dict.values():
    print(value)
    
for key,value in my_dict.items():
    print(key,value)
    
    
print("-------------------")
my_dict = {
    "name": "John",
    "age": 30,
    "country": "USA"
}

name = my_dict["name"]
age = my_dict["age"]

print("Name:", name)
print("Age:", age)


print("--------------")

data_dict = {
    'key1': 42,
    'key2': 87,
    'key3': 199,
    'key4': 63,
    'key5': 91
}

highest_value = None

for value in data_dict.values():
    if highest_value is None or value > highest_value:
        highest_value = value

print("Highest value:", highest_value)



list1 = [1,2,3,4,5,6,7,8]
result = [ x for x in list1 if x%2 != 0]
print(result)
dict1 = {x: x**2 for x in list1}
print(dict1)

dict2 = {x: x**2 for x in list1 if x%2 != 0}
print(dict2)
