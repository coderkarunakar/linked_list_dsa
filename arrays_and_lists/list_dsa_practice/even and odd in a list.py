# 17. Write a python program to put even and odd elements of list in two separate list.
arr=[1,2,2,3,4,5]
even=[]
odd=[]
for index in arr:
   
    if index%2==0:
        even.append(index)
    else:
        odd.append(index)

print(even)
print(odd)