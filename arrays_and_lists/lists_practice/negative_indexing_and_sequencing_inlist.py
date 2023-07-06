
li=[3.3,2,'karunakar','anjali','raghuvaran btech',9,7]


#Negative indexing..
#in this list we can access through the negative indexing as well 
#the negative indexing starts from -1,-2,-3...and goes on.... note:-1 means last element and -2 means second last  element..

#case 1:
#Negative means from the last..     and if u give the negative index which is not in the list gives u the error out of index...
# print(li[-1:])  #as this single : gives u the single element only if u give 2 colon's :: then it goes till end ..
# print(li[-2])

#case 2:
# print(li[-1:-3]) #and this wont work here it simply gives u and empty list ... for the negative index we need to give  like  this

print(li[-4:-1])  #note:in negative index also goes till end-1  only 
print(li[-4:])   #if u want till end i.e len of  list simply leave like this u wil get all the elements....



#   Sequencing...

#Note:as like our range function we have sequencing in list...
#in range function  we have (start,end,step)
#in list function we have[start:end:step] just give the index number..



#case 3:
# #note:here also it goes from start ,end-1,with step difference..
# print(li[1:3:1])  #as this works only for the positive indexing it wont work for the negative indexing..and here also it goes till the end -1...remember it..


#case 4:
# print(li[1:5:2])   #note:here also last element is end -1



#case 5:
# print(li[1:])   #this prints from the index 1 to till last ,note :here the end element is by default length of the list..and step will be by default is 1,...

# print(li[0::])  #this prints from the index 0 to till last..  as we gave :: 2colon's...



# print(li[0::2])  #note:this :: wil run the loop till end and with an difference of 2 i.e step 2


# #case 6:
# print(li[:4])  #this gives u the start index from the 0 index and goes till the end i.e 3 only as it works end-1
# # and the default step is 1 only


