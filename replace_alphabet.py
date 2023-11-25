def replace_alphabet(string,n):
    result = ""
    for char in string:
        if char.isalpha():
            if char.islower():
                base = ord('a')
            else:
                base = ord('A')
            new_char = chr((ord(char) - base + n) % 26 + base)
            result += new_char
        else:
            result += char
    return result
print(replace_alphabet("sumindas",1))
