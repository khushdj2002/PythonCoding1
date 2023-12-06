import textwrap

str = "ABCda"
print(str.upper())
stri = ""
stri+=str[1]
stri+=stri
print(stri)
print(str.count('a',0,3))
print(str.index('a',1,5))
print(str.find('a'))
print(str.find('ac'))
s="a"
st = s.partition('a')
print(type(st))
print(str.capitalize())
print(str.swapcase())
print(str.casefold())
print(str.center(10,"-"))
print(str.isalnum())
print(str.__add__("bcd"))

original_string = "Hello, World!"

# Encode the string using UTF-16 encoding
encoded_bytes = original_string.encode(encoding='UTF-16')

print(encoded_bytes)




string1 = "Staße"
string2 = "stasse"

# Using casefold() for case-insensitive comparison
if string1.casefold() == string2.casefold():
    print("Equal")
else:
    print("Not Equal")


print(str.endswith("BC",0,3))
print(str)

original_string = "Hello\tWorld!"

# Replace tabs with spaces, using a custom tab size of 4
expanded_string = original_string.expandtabs(tabsize=4)

print(expanded_string)


name = "John"
age = 25

# Using str.format() to format a string with placeholders
formatted_string = "Name: {}, Age: {}".format(name, age)

print(formatted_string)

# Define a dictionary with key-value pairs
person_info = {'name': 'John', 'age': 25, 'city': 'New York'}

# Use format_map() to format a string with placeholders
formatted_string = "Name: {name}, Age: {age}, City: {city}".format_map(person_info)

print(formatted_string)

print("123$世界".isascii())

print(str.isdigit())
print(str.isdecimal())
print("1/2".isnumeric())

print(str.istitle())
print(str.isspace())
words = ["Hello", "world", "!"]
separator = " "
result = separator.join(words)
print(result)

text = "Hello"
width = 30
padded_text = text.ljust(width, '*')
print(padded_text)
import textwrap
soln = textwrap.wrap(str,1)
# soln = textwrap.wrap(str,placeholder="abc")
print(soln)
s = "Hello   World   lol"
str = s.split()
for i in range(len(str)):
    str[i] = str[i].capitalize()
print(" ".join(str))
print(str)
string1.strip()

my_list = ['apple', 'banana', 'orange']
for index, element in enumerate(my_list):
    print(f"Index: {index}, Element: {element}")

lis=[1,2,3]
li = []
li.append(3)
print(li)
print((2+3)/2)

str="abcgfdsbcfgsdf"
print(str.partition("bc"))
str = "asfwas gfsd gfsd. adfafds"
print(str.capitalize())

str = "hello"
print(str.ljust(10,"-"))
print(str.rjust(10,"-"))
str = "he\tgfds"
print(str.expandtabs(7))

print(str.removesuffix("d"))
print(str.__len__())
print(len(str))

str1 = "abcabcabc"
str1=str1.replace("a","e",2)
print(str1)

print(str1.rpartition("c"))

str2 = ".|."
l = [""]*7
print(l)
for i in range(len(l)//2+1):
    if i==len(l)//2:
        l[i] = "WELCOME".center(21,"-")
    else:
        l[i]=l[len(l)-i-1]=str2.center(21,"-")
        str2=str2+str2

print(l)
print(7//2+1)


print(bin(5)+" "+hex(10)+" ")
list=[1,2,3]
print(list)