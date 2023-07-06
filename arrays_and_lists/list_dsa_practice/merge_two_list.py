
# Write a python program to merge two list to third list.
list1=[1,2,3]
list2=["karunakar","simran"]
x=list(list1)  #compulsory to convert to list first
x.extend(list2)
print(x)

list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c', 'd']
merged_list = list(list1)
merged_list.extend(list2)
print(merged_list)