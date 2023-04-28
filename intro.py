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

    
    
 
            # topic:--
            # #Linked list input

#A Node is something which stores current value and next reference data
 
#taking input from the linked list
#we need to take input untill u get -1

               #Task :to take input of the linked list

               #a linked list has head(first node) and tail (last node)





class Node:
   def __init__(self,data):
      #actually a node consist of data and next value i.e ref of next value so here we are storing next
      #value as None..
      self.data=data
      self.next=None
      #to get the head of the linked list
def printLL(head):
   #performs on head is not none
   while head is not None:
   #here we are converting it to string since it head is an int and we need output in the form of
   #-> arrow function and the printLL is an string and head is an integer so we can not do like that so we are simply converting it to string ...
      print(str(head.data) + "->",end="")
      head =head.next
      #by the above the loop was done and finally we need to print None and simply return 
   print("None")
   return 
def takeInput():
   # below is splitted based on space seperated 
   inputList =[int(ele) for ele in input("please enter input").split()]

   #initializing head to be None
   head =None
   #initializing the tail to be none-
   tail=None  #since initially we are not taking any element so head and tail to be none

   # a for loop is used to iterate through the above inputList
   for currentData in inputList:
      #a simple condition if our current data is -1 then break i.e terminates and exits the loop
      if currentData ==-1:
         break
      #if our current data is not equal to -1  then create  a new node,with the below statement a node is created
      newNode = Node(currentData)
#this means no node has been created i.e first node
      if head is None:
         #then our node should to point newNode,here head is assigned in the first out only
         head =newNode
         tail=newNode #because for a single element a head and tail should be same for the first time
      #except for the first node u will not work on head,if it is not the first node ,start from head keep on traversing till next becomes not none
      else:
         tail.next=newNode
         tail=newNode



   return head


#below takeInput is inbuilt function
#this is main.head 
head =takeInput()
printLL(head)
printLL(head)  #with this only a simple copy of above code is created... thats it nothing changes

#after optimizing the code we get the time complexity as O(N)

#scenario of output happens like this
# 1 2 3 4 5 6 -1
#1->2->3->4->5->6->None
#1->2->3->4->5->6->None



#pls use  chatgpt or codingninja linked list course lecture 5 for dry run understanding


#for the above take input elements as 1 2 3 4 5 -1 --->1->2-> 3-> 4-> 5 None
#and take some rememberable reference our wish


#Topic:
#print a linked list
#the  code is done in the above lines only please do check


#Time comlexity analysis 
#for the above code the time complexity is O(n2)
#the only step is taking the time  is traversing for the elements for the n th elements u need 
#to traverse for the n-1 elements for n-1 elements u need to traverse for  the n-2 elements  this is the step taking time and we can optimize it



#1 2 3 4 5 -1 output 1->2->3->4->5 
#0 +1 +2+3+....+(n-1)  #here for the first element u have done is no iteration so it is 0 th step


#  n(n-1)/2 =n^2-n/2  =n^2/2
#so our time complexity for the above code is O(n^2)



#Linked list input 2:in this session we are going to optimize the taking input part of the linked list 


#in our code when ever a new element is need to be inserted we start from the head and reach till the last 


#example:
#1-> 2-> 3-> 4-> 5 ->None

#if supppose we have numbers like 1->2->3->None
#here we want to  add 4 we need to traverse from the begining from 1 and till none and we can add None
#even this happens for all the elements in the what ever u want to add u need to simply traverse from the begining so this makes our t.c to be O(n^2)



                     #8 lecture Number
#Optimizing the taking input from the part of the linkedlist
 
                  #IN OUR PREVIOUS CODE
 #till now our code has functionality like when ever a new node is inserted we start at the 
 #begging and we need to reach till last (i.e when we reach curr.next is None if it is not none then we keep on iterating the code untill we get curr.next is None)


#in order to optimize this above code we can simply  stop iterating over the all elements and simply we can give like finding the last reference of the node and we can insert it,just we need reference of the last node i.e tail and as we know the reference of the first node is head


#we can follow the above process by using only 3 steps 
#1.create new node
#2.tail.next=new node
#tail=new node
#just by following the above steps we can simply optimize our code

#at each iteration we need to maintain the reference of the last node and that u have maintained to the tail  ,this is an O(N ) only,for the code simply refer the above code..






#lecture 11
#print i the node in a given linked list
#given head pointer and from the head we can traverse any node and an i pointer and the i can 0,1,2,....anything with this we can traverse in the given linked list and i have to go to that i th  node and print that node   the indexing starts from zero

#Approach :we would start from head and we would traverse in the forward direction and trying to reach the i th node
#we wil be having a current which would be pointing a head node and we would traverse the node one by one and we would keep on increasing the count where in the count would be zero ,and in each iteration i would increase the count and the current pointer so that i reach the i th node,i need to ensure that my current should not be null because if my curr is null i cant go forward and my count should be less than  i ,because if my count is equal i am at the i th node and i can come out of the loop ,till the movement where the curr is <i and the curr is not null i need to traverse 
#only 2 conditions 1.count <i 2.curr!=null




#Insert at the i th position in a  linked list 
# Question :u are given a linked list 3->4->5->1->2
#Task is to implement the function u are given a linked list (i.e u are given a head of the linked list in which u have to insert an element)  the position is the ith is given to u and the data through which the new node will be inserted to u is given to u (insert (head ,i,data)) and have to return the head as well because the head of the linked list can be changed..

#we can insert the elements from the range of 0  to length of linked list  this is the range of i 



#example explaination


#here i is the index position
#3(i=0) 4(i=1) 5(i=2) 1(i=3) 2(i=4)

#given data we need to insert i=2 and data is 6
#step 1:first we need to create a node for 6       

#then our given linked list get changed like this 3 4 6 5 1 2 
#so inorder to do this we need a pointer at 4 and 5 i.e 2 pointers and at which position u want to insert lets say i.e current and its previous position is important lets say it is prev     and curr this 2 pointers are needed to insert any element



#when the count reaches i then i will do this steps
#steps to insert 
# 1st :create a new node with data 6 ,
#then prev.next=new node
# new node.next=curr    

#if we have to insert at the index 0  then our test case would fail for the above approach
#because in step 2 prev.next if no prev then it would point to none i.e none .next is attribute error
#so inorder to pass this test case we need to create a condition that if prev is none then head is new node


#with this all the test cases will be passed
#approach is as follows
#create a new node
#if prev is  none :
      #head is None:
#else:
      #prev.next =new node
#new node .next =curr
# return head