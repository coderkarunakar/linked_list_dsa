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





          #Linked List Node: some coding part
#a linked list is a collection of nodes
#every node has its data value and next data reference node
#if no data is present then next reference is none
#imp note:every node has 2 things i.e data(current value) and next (i.e ref of next node)
#note:when ever we want to initialize a node we provide data with that
#if we create data then by default automatically next is none






class Node:
   def __init__(self,data):
      self.data=data
      self.next=None
a=Node(13)
b=Node(15)
a.next=b
    
print(a.data)#13
print(b.data)#15
print(a.next.data)#15 because a.next.data  here next data refers to the b so it is 15(first it goes to a i.e 13 then next.data i.e 15)
print(a)
print(a.next)
print(b)
# print (b.next.data) this gives error none type has no attribute data it means it stores it data value and next ref i.e none so its next ref is not there so we get and error here

    
    
 


 




