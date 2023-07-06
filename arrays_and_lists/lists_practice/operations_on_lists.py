
# #Note:list is created usign square brackets..

#case1:
# #creating an empty lists
# li=[] 
# print(li)  #this gives u an empty list...



#case2:
# ki=[3,59.3,5]
# print(ki)

# print (type(ki))





#case 3:
# #note:list [] is an heterogeneous type we can store different type of elements.. like string,int,float,  etc...

# l=[3,9.7,'karun']  #here int,float,and string is stored...
# print(l)






# #case 4:
# #Access and change the elements in the list...
# m=[8,7.0,'karunakar']
# print(m[0],end=' ')
# print(m[1])  #this is the format of accesing the elements of the arrays..but need to give only square braces.. only
# #since if we give other than square braces it gives error since lists can be access only through square
# #if u try to give more index number which is not in the list then it might give u list index out of range..



# #case 5:
# #changing the list elements..
# n=[3,8.0,'karun','hyderabad']
# print(n)
# n[2]='ramya'  #this is the simple format to change the list elements.. in a particular elements.. if u want to give multiple simply give same format in the next line..  and we cannot change index which is not in the present list...

# print(n) 


# #case 6:
# #slicing of a list...
# list=[1,2,'karunakar',9.0]
# print(list[1:])  #this gives list from index 1 to till end since we didn't gave last number..
# print(list[1:3])  #this prints the list 2,'karunakar'  and here what ever the last index u give like n it print s till n-1 only since that is the reason we got here only till index 2.
# print(list[:])   #this gives all the elements in the list as we didn't mention anything
# print(list[1:10])  #this gives u all the elements present in the list and it wont give any error even if u give
#                     #out of index here. in slicing we dont get index out of range error we get only in the access and
#                     #and change the elements...


  #case 7:
#insert and append the elements in the list..


# #note:in this append it will try to add as an last element..
# box=[1,2,3.5,'karunkar']
# box.append('ram')    #this is the format to append the element dont try to put in the print as it gives None this is the format
# print(box)

# #this is the format for inserting elements .. at a  specific index..

# box1=[2,3,'karan bhai']
# box1.insert(2,"ramcharan")  #this specifies (index no) and (what u want to add) this is the format to insert..and it wont delete what actually we have it just changes the index no what actually we have before...
# print(box1)


# box1.insert(8,'prabhas')  #here we tried to give the index more which is not in our list .it wont give error simply it try to give at the last...
# print(box1)



# #case 8:
# #trying to add multiple elements once at a time

# box1 .append([9,9,9])   #if we use this append (with square  braces) sice with out square brace it wont take multiple it takes only one element with open braces..it tries to give u like an extra list inside the available list  .once execute and look it once
# print(box1)

# box1.extend([9,8,9])
# print(box1)

#case 9
#removing elements from the list...
# box2=[5,5,5,'karan','ram',9,4]
# box2.remove(5)  #this tries to remove 5 from the given list and note:if we have multiple 5's then it removes the first element which is in the list...
# print(box2)

#Note:if u try to remove the element which is not present in the list then it try to give u the value error that's it



#case10:
# pop is used to remove the  last element from the list

# box2.pop()
# print(box2)

# #u can remove the particular element from the index as well
# box2.pop(2)  #this specifies the particular index number... if u try  to give index which is not there then it gives index out of range...
# print(box2)


#note:len() it is a fucntion it is used to find out the length....