#just this shows how return print and without print for the return works..that's it so simple concept...

# def increment(a):
#     a=a+2
#     return a
# a=2
# a=(increment(a))
# print(a)


# case 2 :here it prints only the new a created not the return function a since it is not printed
# def increment(a):
#     a=a+2
#     return a
# a=2
# increment(a)
# print(a)


# #case 3:
# def increment(a):
#     a=a+2
#     return a
# a=2
# print(increment(a)) #this is return function a and 
# print(a)   #this is newly created a at the top...


#here return is not there so no need to print it just simply call it that is enough for it ..
def change(li):
    li[1]=li[1]+2
    return
li=[1,2,3,4,5]
change(li)
print(li)