#READ AND PRINT ALL ELEMENTS IN A GIVEN LIST 

#1.USING FOR LOOP,this will give all elements in a new line
a=[1,2,3,4,5]
for index in range(len(a)):
    print (a[index])

#2.WIHTOUT USING FOR LOOP and using a * operator,this will give in a same line
print(*a)
#printting using seperated by a comma ,
print(*a,sep=',')
#if u want in new line simply use '\n' with a sep
print(*a,sep='\n')

#3.

# Python program to print list
# print the list by converting a list of 
# integers to string using map,here simply map is converting integers which is in the given list a to string and joining with a space and printing,
  
a = [1, 2, 3, 4, 5]
print(' '.join(map(str, a)))