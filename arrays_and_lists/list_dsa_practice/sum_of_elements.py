# Write a python program to find sum of all list elements.

#simple method 
li=[2,3,5]
sum=0
for index in range(len(li)):
    #by accessing each and every element...
    sum=sum+li[index]
print(sum)


#2nd approach using enumerate

li=[1,2,3,9];s=0
#using enumerate
for i ,a in enumerate(li): #here i is index , a is index count
    #this is our main logic..
    s=s+a
print(s)

#using inbuilt sum()
li=[1,1,2]
total=sum(li)
print(total)