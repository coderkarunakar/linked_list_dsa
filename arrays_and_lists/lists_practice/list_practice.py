# 1. Write a python program to read and print elements of list


#SPACE SEPERATED... LISTS...
#with this we can take the elements in the list in a space seperated... like 1 2 3 ...like  infinty u can give..
# li=[int (x) for x in input('enter the elements').split()]
# print(li)

# # this line is for printing the each element at specific index 
# for i in range(len(li)):
#     print('the elements at the index ',i,li[i])

#LINE SEPERATED ...LISTS
# like  
# 1
# 2
# 3
# 4

# # for this we need to take 2 times user input pls do remember
# li=[]
# n=int(input("enter the no of elements u want to enter .. "))
# for x in range(n):  #note:range function starts from 1,2,3....
#     li.append(int(input()))  #this line is for inserting the each value in it..,this line #makes us to take the int as input elements
# print(li)  #and finally printing those elements



#just taking the string as the list elements...since already default it takes as string..
li=[]
n=int(input("enter the no of elements u want to enter .. "))
for x in range(n):  #note:range function starts from 1,2,3....
    li.append((input()))  #this line is for inserting the each value in it..
print(li)  #and finally printing those elements




#note:just this input() makes us to take  the input as string if we put int then it takes int as the input ,same for float..




# 2.question:
#print negative elements in a list..
# Write a python program to print all negative elements in an list.

#LOGIC ALL NUMBERS <0 COMES UNDER NEGATIVE NUMBERS..

#A BIG NOTE :THAT IF WE DONT GIVE .SPLIT IN THE LIST USER INPUT THEN IT MIGHT GIVES U ERROR..



# li=[int (x)for x in input("enter the list of inputs please").split()]
# for i in li:
#     if i<0:
#         print(i,end=" ")



# li=[int (x)for x in input("enter the list of inputs please").split()]
# for i in range(0,len(li)):
#     if li[i]<0:   #since here list is an square bracket one...so used is square bracket..
#         print(li[i],end=" ")

#using a while loop 


# li=[int (x) for x in input('enter the input').split()]

# i=0
# while i<len(li):
#     if li[i]<0:  #this is how we can fetch values in the list using while loop
#         print(li[i],end=' ')
#     i=i+1




#3.Write a python program to find sum of all list elements.


# total=0
# li=[int(x) for x in input("enter the elements of list please").split()]
# for i in range (0,len(li)):
#     total=total+li[i]

# print("The sum of all the elemets of the list is ",total)

#4. Write a python program to find maximum and minimum element in an list.

#LOGIC SIMPLY USE THE MIN AND MAX FUNCTION..



# li=[]
# n=int(input("enter the no of elements u want to enter .. "))
# for x in range(n):  #note:range function starts from 1,2,3....
#     li.append((input('enter the elements one by one')))  #this line is for inserting the each value in it..
# print(li)  #and finally printing those elements
# print("the smallest element is ",min(li))
# print("the largest element is ",max(li))

# #4.finding minimun and maximum of a number in a given list
# li=[]
# n=int(input("enter the input of the elements please"))

# for k in range(1 ,n+1):
#     li.append(int(input("enter the elements one by one")))
# smallest=largest=li[0]

# for l in range(1,n):
#     if smallest>li[l]:  #first manam asign chesina no checking no kante pedadi itey a checking no  samllest loki tiskovali ledante mana asign no a untadi and elage mana code for loop lo unna condition fail iye daka pani chestune untundiii and deni vice versa largest ante logic
#         smallest=li[l]
#         min=l
#     if largest<li[l]:
#         largest=li[l]
#         max=l
# print("the smallest of the list is ",min,smallest)
# print("the largest of the list is ",max,largest)

#2.negative no in between the given range here we get like -4,-3,-2,-1
# def negativenumbers(a,b):
#   # Checking condition for negative numbers
#   # single line solution
#   out=[i for i in range(a,b+1) if i<0]
#   # print the all negative numbers
#   print(*out)
 
# # driver code
# # a -> start range
# a=-4
# # b -> end range
# b=5
# negativenumbers(a,b)


# Python program to find sum of all
# elements in list using recursion
 
# # creating a list
# list1 = [11, 5, 17, 18, 23]
 
# # creating sum_list function
 
 
# def sumOfList(list, size):
#     if (size == 0):
#         return 0
#     else:
#         return list[size - 1] + sumOfList(list, size - 1)
 
 
# # Driver code
# total = sumOfList(list1, len(list1))
 
# print("Sum of all elements in given list: ", total)

