#Line seperated input...
n=int(input("enter the n of an element"))

li=[]  #here an empty list was created 
for i in range(n):  #this loop runs till n,since only for loop means end's at n-1 and list also does the same but this range goes till n not n-1 so here we are getting till n point....
    current=int(input())  #here simply taking user input as an integer 
    li.append(current)   #here just appending the current element in the  empty list ...


#in this line simply prints the elements present in the list...what we gave above..

for ele in li:
    print(ele)