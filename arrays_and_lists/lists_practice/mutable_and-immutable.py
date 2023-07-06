#note:list,set,dictionary are mutable(changable) in python that means we can add elements like see down
li=[2,3,4]
print(li)  #2,3,4
print(id(li))

li[1]=7
print(li)  #2,7,4 here we are able to change the values in it so it is called mutable 
#same follows for the set,dictionary as well
print(id(li))

#in list set,tuple even after u change it's value also ur id will be same previously and new
#but that is not the case in int,float,string,bool


# #note:all primary datatypes in python are immutable (can't be changed)
# a='karunakar'
# a[0]='r'
# print(a)  #this gives an type error cant be changed so this concept is called immutable 
# #same happens with the int,float,







# # #note:please look in our class notes as well what i wrote....

# #only one thing remember that variables in python are immutable and list are mutable that's it dont run out of it it takes u to confusion..leave it just remember this

# # #Note:variables in python are immutable i.e only it's reference get changed not it's original memory .only reference get changed..


# # #imMutable(i.e cannot be changed)
# # x=3
# # a=3
# # print(x)
# # print(id(x))
# # print(id(a))
# # a=4
# # print(id(a))
# # print(id(x))
# # print(x)
# # print(a)

# #here:in variables if they  are having same reference no intially (sicne having same no's can give same reference id)if u change in 1 variable that will not be reflecting to other variable..


# # #mutable in lists(i.e can be changed)
# #case 1:
# # li=[1,2,3,4]
# # li2=li
# # li2[1]=4
# # print(li)


# #case 2:
# li=[1,2,3,4]
# li2=li  #here even though referign to same it get changed in newly asigned only but where as in variable it is not like that it get asigned to it's old one only

# li2=[3,3,4]
# li2[1]=4
# print(li)
# print(li2)


#we can take one by one elements in list like this pls run this...

# # change this to how many items your list you want to have
# li = []
# length = int(input('enter'))
# for i in range(length):
#     #enter numbers one at a time
#     number = int(input('>> '))
#     li.append(number)
# print(li)