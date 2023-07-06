# Write a python program to count total number of duplicate elements in an list.
#converting list to set and finding both the len difference is the total count of duplicate 
arr=[1,2,1,2,5,6,6,7,0]
s=set(arr)
l=list(s)
length=len(l)
arr_length=len(arr)
no_of_dup=arr_length-length
print(no_of_dup)