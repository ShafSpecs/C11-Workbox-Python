import string

abc = string.ascii_lowercase
test_string = "hello"
key = 5

cipher = test_string.translate(test_string.maketrans(abc, abc[key:] + abc[:key]))
print(cipher)
