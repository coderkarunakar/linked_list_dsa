li=[1,23,'karunkar','ramsita',8,'alluarjun','sneha','anupuma']


#case 1: using range function..
# for i in range(len(li)):
#     print(li[i])  #this prints the li 's each index...


#case 2: using range and starts at a particular index..
# for i in range (2,len(li)):  #this starts from the index 2 and goes till the length of the loop
#     print(li[i])


#case 3:  using simple looping
# for ele in li:  #here we haven't used the range function range run's on the indexing and here ele fetches each element in the li
#     print(ele)


# #case 4: using the slicing part
# for i in li[2:]:
#     print(i)

    #case 5:using the slicing part and goes till a specific part

for i in li[2:4]:  #NOTE:this works  from 2 to 3 only as we know for loop skips the last index if we specify an index no..
    print(i)