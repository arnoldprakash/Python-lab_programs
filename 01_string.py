#demonstrate string slicing and 5 string functions
#1. string slicing
print("string slicing")
a="good moring"
print(a[0::])
print(a[1:-1:])
print(a[-3::1])
print(a[4:-1:])


#string functions
str="Hai"
print("length :",len(str))
poem="all that does flow"
print(poem[:10])
print(len(poem))
print(poem.startswith("all"))
print(poem.endswith("folks"))
print(poem.capitalize())
print(poem.upper())
