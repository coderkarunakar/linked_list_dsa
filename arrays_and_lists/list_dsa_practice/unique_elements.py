# Write a python program to print all unique elements in the list.
# converting list to set and set to list
arr=[1,2,1,2,7]
s=set(arr)
unique=list(s)
print(unique)


#using inbuilt function counter but it wont give inside a list simply it gives z
# from collections import Counter
# print(*Counter(arr))




#3rd approach

# Python program to check if two
# to get unique values from list
# using traversal
 
# function to get unique values
 
 
def unique(list1):
 
    # initialize a null list
    unique_list = []
 
    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not(mana list lo leni values ni e list lo add chestamu unnavi cheyamu so not in used)
        if x not in unique_list:
            unique_list.append(x)
    # print list
    #last lo mana list lo leni values em em unayo avvi anni final ga print chestamu..
    for x in unique_list:
        print (x)
 
 
# driver code
list1 = [10, 20, 10, 30, 40, 40]
print("the unique values from 1st list is")
unique(list1)
 
 
list2 = [1, 2, 1, 1, 3, 4, 3, 3, 5]
print("\nthe unique values from 2nd list is")
unique(list2)