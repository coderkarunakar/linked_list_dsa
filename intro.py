            #LINKED LIST NOTES

# 1.INTRO TO LINKED LIST
# 2.all the elements are connected in non continous manner
#3.there will a link btw the elements
#4.each element of the linked list is known as node
#5.node will be storing 2 things i.e 
   #i.data of the current value
   #ii. reference to the next node value
  #EXAMPLE:CONSTRUCTION OF LINKED LIST WITH THE GIVEN VALUES
#IF WE HAVE THE VALUES LIKE

# DATA 1 REF (200)
# DATA 5 REF (100)
#DATA  4 REF (300)
#DATA  3 REF (900)
#DATA  2 REF (500)

#THEN WITH THE ABOVE Data we can create a linked list by  current data+ ref of next data

#current data ref of next data
#1 100
#5 300
#4 900
#3 500
#2 None (since next data reference is not available so it is none)



#Note:every data and its current ref value is known as Node


#WHAT WE NEED INCASE OF A LINKED LIST
#i. head of the linked list stores the reference to the first node
#ii. Tail of the linked list stores the reference of the last node in the linked list
#iii. maximum we deal with head only not much with tail (very less)
#note:if we have ref of the head of the linked list then we have a complete linked list,because 
#with that only we can move to last node in the linked list


#EXAMPLE:

# DATA  REF  ....
# 1     400         5  600    4 800   3  1000   

                                    #   2   none     

#if we have  a head of the linked list then we have a complete linked list
  
