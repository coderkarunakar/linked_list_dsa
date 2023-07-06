# #Note:lists are mutable
# def increment(li):
#     li=[3,3,4]
#     return
# li=[1,2,3,4]
# print(li)  #this not refers to the main list it refers to only newly created list only

def increment(li):
    li=[3,3,4]
    return li
li=[1,2,3,4]
li=increment(li)  #this refers to main list as we are here created an interlink so it refers to main list...
print(li)

#in python lists ,set,dictionary,..are mutable remember we can change its value and it's id remains same before and after creation of list but where as that is not the case in the primary data typed like int ,float,string,bool... 