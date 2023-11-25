def palindrome(name):
    reverse = ""
    word = name
    for i in range (len(word)-1,-1,-1):
        reverse = reverse + word[i]
    if name == reverse:
        print("Palindrome")
    else:
        print("Not Palindrome")
name = input("Enter A String:")
palindrome(name)