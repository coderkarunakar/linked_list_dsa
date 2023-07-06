#IN THIS WE WILL BE DISCUSSING ONLY THE INBUILT FUNCTIONS(PARAMETERS IN PYTHON)

# 1.end="" simply prints next line and current line in single line with something like space,nothing,or special character
# 2. .join() joins 2 strings with a special character
#3.map() simply performs given function on the given iteration..
#4.enumerate() this will give the index and value
#5  arr.count('what value') this gives a specific value count
#6  arr.copy()  it makes the copy of the elements...
#7. array.insert(index,element) it inserts the element in a particular index
#8   del arrayname[index no] it  deletes an specified index value
#9    array.remove(value) it removes the specified value in the index..
#10.  extend() it extends two lists



#1.end="" this is used to print the next line into the same line 


# a='karunakar'
# b='anu'
# #using a space 
# print(a,end='')
# print(b)

# #using @ symbol moreover we can use comma , #,%  any symbol
# a='welcome to gfg'
# b='karunakar'
# print(a,end='@')
# print(b)





# # 2..join():this will ignore with what it has joined initially it will join with what u will give ,if u give '', '' then it will join only in this if no multiple '', then it will join only with what u have on every letter

# #here it was joined with the commas i.e , 
# a='k','a','r','u','n','a','k','a','r'
# #joining with empty string
# print("".join(a))

# #joining a string
# print("$".join(a))


# b='karun','akar'
# #joining with - character
# print("&".join(b))

# print('-#-'.join(a))





# #3.MAP() it performs given function on the given iteration.. here str function with a as iteration..

# a = [1, 2, 3, 4, 5]
# print(' *'.join(map(str, a)))





# #4.enumerate() this will give index and value its syntax is
# #enumerate(iterable, start=0)
# l=["karunakar","anu","manisha"]
# print(list(enumerate(l)))

# #in enumerate u can give a specific index as well,from that it will show ..like  3,4,5,6,....
# print(list(enumerate(l,3)))

# for ele in enumerate(l):
#     print(ele)

# for count ,ele in enumerate(l,100): #with a specified index 
#     print(count,ele)




#5.count()
fruits = ['apple', 'banana', 'cherry']

x = fruits.count("cherry")
print(x) #it just shows the no of times an item is appearing..

#6.copy()
a=[1,2,2]
x=a.copy()
print(a)
print(x)


#7.inset()
arr=["geeks" ,"geeks"]
arr.insert(1,"for") #index and element
print(arr)

r=[1,2,4]
r.insert(2,3) #inserting index and element
print(r)


# #8.del()
# del() : Element to be deleted is mentioned using list name and index.
# Syntax: del <ListName>[index]
# Example:
l1=[ 1 , 1 , 12 , 3 ]
del l1[ 2 ] #it deletes an specified index...
print(l1)

#9.remove()
l1=[ 1 , 1 , 12 , 3 ]
l1.remove( 12 )
print(l1)

#10.extend()