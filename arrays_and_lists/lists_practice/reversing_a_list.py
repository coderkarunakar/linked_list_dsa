# #reversing a list
# def reverse(li):
#     length=len(li)
#     for i in range(length//2):  #since we need integer part not the float (i.e in decimals )so we took // 
#         li[i],li[length-1-i]=li[length-1-i],li[i]  #this line is the swapping part...
# li=[int (x) for x in input('enter inputs').split()]
# reverse(li)
# print(li)


#instead of this we can use the negative indexing as well 
# like li[i]=li[-i-1]


# #reversing a list
# def reverse(li):
#     length=len(li)
#     for i in range(length//2):  #since we need integer part not the float (i.e in decimals )so we took // 
#         li[i],li[-i-1]=li[-1-i],li[i]  #this line is the swapping part...
# li=[int (x) for x in input('enter inputs').split()]
# reverse(li)
# print(li)



# #we can use the slicing operation as well
n=int(input('enter n'))
li=[int (x) for x in input('enter inputs of n').split()]
# x=len(li)
# print(li[x::-1]) #here no end point so goes till end...

print(li[::-1])  #this works since no end point and no start point...