#copying elements from one array to another array
a=[1,2,2]
x=a.copy()
print(a)
print(x)
old_list=[1,2,3]
new_list=old_list
new_list.append('a') #since it is an copy so we are getting this in both the old and new array
print(new_list)
print(old_list)