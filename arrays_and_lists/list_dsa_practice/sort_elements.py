# Write a python program to sort list elements in ascending or descending order.
a=[1,2,5,3,4]
a.sort()
print(a)


#ascending order(chinna nunchi pedda)
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
print(a)
#descending order(pedda nunchi chinna)
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]<a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
print(a)





#checking...
nums=[1,2,3,4]
x=sum(nums)
print(x)