def my_func(*kids):
    print(kids[1])

def my_func2(**kids):
    print(kids["a"])

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

# print("\n\nRecursion Example Results")
# tri_recursion(6)
'''
6
result = 6 + 5 + 4 + 3 + 2 + 1 + 0
5
result = 5 + 4 + 3 + 2 + 1 + 0
4
result = 4 + 3 + 2 + 1 + 0
3
result = 3 + 2 + 1 + 0
2
result = 2 + 1 + 0
1
result = 1 + 0
0
'''

# x = lambda a : a + 10
# print(x(5))

def f(n):
    return lambda x : x*n

# mydoubler = f(2)
# print(mydoubler(11))

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def myfunc(self):
#         print("Hello my name is " + self.name)

# # p1 = Person("John", 36)
# # p1.myfunc()

# class Car:
#     def __init__(self,name,cost):
#         self.name = name
#         self.cost = cost
#     def myfunc(self):
#         print("Hello ", self.name)

# c1 = Car("ferrari", 100000)
# c1.myfunc()

# del c1
# c1.myfunc()

# class Person:
#     def __init__(self, fname,lname):
#         self.firstname = fname
#         self.lastname = lname
    
#     def printname(self):
#         print(self.firstname, self.lastname)

# p = Person("John", "Lee")
# p.printname()

# class Student(Person):
#     def __init__(self, fname, lname, year):
#         super().__init__(fname,lname)
#         self.graduationyear = year
    
#     def welcome(self):
#         print("Hi", self.firstname, self.lastname, self.graduationyear)

# s = Student("Jay","You",2019)
# s.printname()
# s.welcome()

# mytuple = ("apple", "banana", "cherry")
# myit = iter(mytuple)

# print(next(myit))
# print(next(myit))
# print(next(myit))

# mystr = "banananananana"
# myit = iter(mystr)

# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))

# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self
    
#     def __next__(self):
#         x = self.a
#         self.a += 1
#         return x

# myclass = MyNumbers()
# myiter = iter(myclass)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self
#     def __next__(self):
#         if self.a <= 20:
#             x = self.a
#             self.a += 1
#             return x
#         else:
#             raise StopIteration

# myclass = MyNumbers()
# myiter = iter(myclass)

# for x in myiter:
#     print(x)

# x = 300
# def myfunc():
#     print(x)

# myfunc()
# print(x)

# x = 300

# def myfunc():
#   global x
#   x = 200

# myfunc()

# print(x)

# import platform
# x = dir(platform)
# print(x)

import datetime
x = datetime.datetime.now()
print(x.year, x.strftime("%A"))