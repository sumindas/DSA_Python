def replace_char(name,element,replace):
    result = " "
    for i in name:
        if i == element:
            result = result + replace
        else:
            result = result + i
    return result


name = "my name is sumindas"
replace = '*'
element = 's'
print(replace_char(name,element,replace))
