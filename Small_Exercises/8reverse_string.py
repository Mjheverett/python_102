string_forward = input("Please enter the string to reverse: ")
string_backward = ""
for i in string_forward:
    string_backward = i + string_backward
print(string_backward)