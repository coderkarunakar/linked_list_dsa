#in this concept our main concept is to split a list based on the space  that's it using split () method we can serate it...

#case 1:

# str=input('please enter')  #here if u give comma (,)then it splits according to the , basis..note:this split method is mainly for spliting purpose it splits based on what u give and by default is white space remember it is very important..
# str_split=str.split(',')

# li=[]
# for ele in str_split:
#     li.append(int(ele))
# print(li)  #this gives u an space seperated list i.e based on the , as we gave according to the split i.e(,)


# #case 2:doing all this in one line is possible in python okay let us see... and dont forger to open the created empty list...
# li=[]
# li=[int(x) for x in input('enter').split(',')]#note:if u give , comma here and splits based on the space then it will definetely gives u an error 
# for ele in li:
#     print(ele)


#case 3:  this is like how many inputs u want to take in the first line and in the second line just simply give the input values....that's it ...

# li=[]
# n=int(input('enter the total inputs u want to take'))
# li=[int (x) for x in input().split()]
# for ele in li:
#     print(ele)