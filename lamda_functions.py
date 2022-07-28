# # lamda function to calculate square value 
# f=lambda x: x**2
# value=f(6)
# print('square of 4=', value)

# a= lambda x:x**2
# value=a(8)
# print('square of 5=',value)

# def  gm():
#  '''author: python 9am 
# today i am not attend to the python class 
# because my another work'''
#  print(gm._doc_)

# example program for default argument
# def info(name="hey" ,age=45):
#     print('name:' ,name)
#     print('age :',age)
# info( )
# # info('python')
# info(name="moulali")
# info(age=25)

# add of two numbers using function
# def s(a,b):
#     c=a+b
#     d=a+b
#     print('sum is' ,c)
#     print('sum is' ,d)
# s(10,20) 
# s(20,44.5)   

# def sum(a,b):
#     c=a+b
#     return c
# x=sum(10,20)
# print('sum is',x)    
# y=sum(10.5,5.5)
# print("sum is:",y)

# add of two numbwrs by using functions

# def x(a,b):
#  c=a+b
#  d=a-b
#  return c
# c=x(142,1)
# d=x(144,1) 
# print("sum is:", c) 
# print("sum is:", d) 
# c=x(142,1)
# d=x(144,1) 

# def eo(num):
#     if num%2==0:
#         print(num, "is even")
#     else:
#         print(num,"is odd")
# n=int(input("enter the value of num: "))       
# eo(n)
# eo(15)
# eo(29)


# filter() function that returns even numbers from a list
# def even(x):
#     if x%2==0:
#         return True
#     else:
#         return False
# z=[int(x) for x in input().split()]
# q=list(filter(even,z))    
# print("from the z the even value are :",q)    

# a lambda function to calculate sum of two numbers
f=lambda x,y,z: x+y+z
s= lambda x,y,z: x*y*z
r=f(3,10,2)
z=s(2,3,5)
print('sum=',r)
print('mul=',z)