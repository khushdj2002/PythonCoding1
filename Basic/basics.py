name = "Kushal"
age = 21;
print("My name is :", name, );
print("My age is :", age);

# Indentation is the most significant concept of the Python programming language.
# Improper use of indentation will end up "IndentationError" in our code.

list1=[1,2,3,4,5];
for i in list1:
    if i==3:
        print("Out of for loop")
        break
    print(i)

a=50
b=a

print(id(a),id(b))
b=20
print(id(a),id(b))
a,b,c=5,10,15
print(a,b,c)
a=b=c=5
print(a,b,c)
def add(x,y):
    return x+y

print("The sum of two numbers is :",add(10,40))
print(a)
del a
# print(a)

print(type(list1))

# Python Datatypes
# 1. Numeric Value
a=5
b=10.25
c=3+4j
print("The type of variable a is ",type(a))
print("The type of variable b is ",type(b))
print("The type of variable c is ",type(c))
print("c is a complex number ",isinstance(c,complex))

# 2. String

str = "String using double quotes"
print(str)
s='''A multiline 
string'''
print(s)

str1 = "hello javatpoint"
str2 = "how are you"
print(str1[0:2]) # prints first two operator with slice operator
print(str1[4])  # prints 4th index character of the string
print(str1+" "+str2) # prints the concatenation of both string
print(str1*2) # prints the string twice

#3. List

list1 = [1,"hi","Python",2];
print(list1)
print(list1[2:]) # List slicing 2 and till end will be printed
print(list1[0:2]) #List from 0 to int=dex 2 is printed
print(list1+list1) # concat
print(list1*3) #multiple
print(list1[:2])

# #### TUPLE

tup=("hi","python",2)

print(type(tup))

print(tup[:1])
print(tup[1:])
print(tup*2)

#  ##### Dictionary

d={1:'Jimmy',2:'Alex',3:'john',4:'mike'}
print(d)
print("1st name is :",d[1])
print("2nd name is :",d[2])
print(d.keys())
print(d.values())

#  ## Boolean

print(type(True))
print(type(False))
# print(true)

# ## Set
set1 = set() # Creating Empty set
print(set1)
set2={'James',2,3,"Gowda"}
print(set2)
set2.add(10)
print(set2)
set2.remove(2)
print(set2)

# num1 = int(input("Enter the number"))
# num2 = int(input("Enter the number"))
# # num2 = input("Enter the number:")
# print(num2+num1)

import keyword

# print(keyword.kwlist)

# help("keywords")


# play with keywords

print(True==3)
print(True==1)
print(False==0)
print(True+True+True)
print(True or False) # False
print(True and False) # False
print(None ==0) # False

A=None
B=None
print(A==B)

def no_return_function():
    num1 = 10
    num2=20;
    add = num1+num2;

print(no_return_function()) # example for None

def with_return(num):
    if num%4==0:
        return False

number = with_return(81)
print(number)

print(not False)

# in keyword
cont = "javatpoint"
print("p" in cont) # true
print("P" in cont) # false

# is keyword
print(True is True) # true
print(False is True) # false
print(None is not None) # false
print((9*3) is (3*9)) # True
print((9*3) is "27") # false it also see the type

print([]==[]) # true
print([] is []) # fals
print({}=={}) # true
print({} is {}) # false

# Here we can see that two blank list is same and they are equal but as the memory allocation is
# different in different block so they are not identical.


print(()==()) # true
print(() is ()) # true
a="hello"
b="hello"
print(a==b) # true
print(a is b) # true

# Strings and tuples, unlike lists and dictionaries, are unchangeable. As a result,
# two equal strings or tuples are also identical. They're both referring to the unique memory region.


def outer_func():
    val=10
    def inner_func():
        nonlocal val
        val=20
        print(val)
    inner_func()
    print(val)

outer_func()

for i in range(10):
    if i==6:
        continue
    if i==8:
        break
    print(i, end=" ")

print()
## Exception Handling

var1=4
var2=0
try:
    print(var2/var2)
except ZeroDivisionError:
    print("We cannot divide by zero")
finally:
    print("This is inside finally block")

# assert var2!=0,"Divide by 0 error"

def function_pass(argument):
    pass
class passed_class:
    pass


def func_with_return():
    var=13
    return var

def func_with_no_return():
    var=10

print(func_with_return())
print(func_with_no_return())



list12=['A','B','C']
del list12[1]
print(list12)

t1=('A','B','C')
print(t1)
print(t1.count('D'))
print(t1.index('C'))
print(len(t1))
print((t1))

print(t1)

h='c'
if h>='a':
    if h<='z':
        print(5)


def no_catch(a: int,b: int):
    return a+b

print(no_catch(5,3))


if __name__=="__main__":
    print("hello")
else:
    print("Hello else")
a = 6
print('%.6f'%a)

print(round(28.274333882308138,6))

if __name__ == "__main__":
    print("Printing")

import NestedLists