# #16.lecture :

# #insert at i th position Recursively
# #our problem is u are given a linked list ,and u are given a head of the linked list in which u want to insert ,u are given a position where u will insert     and u are given a data through which u are given a node and insert that node in the linked list and u have to do it recursively

# #example : given  data    1->2->4->7->6 and index 2 ,need to insert data 8
# #expected output is 1->2->8->4->7->6 

# #steps for doing  it in recursive manner 
# #let our function is insert(head,i,data)
# #the induction hypothesis is that 

# #17th lecture :
# #  insert at ith  Recursively code:
# #we will have head ,i  , and data


# #for the normal approach the time complexity  of the code is O(n)
# #printLL traverse the linked list   and prints each node takes O(N)
# #length  traverses the linked list and count the number of nodes which takes O(n)
# #insertAtI function iterarates through the linked list to find the insertion position which takes O(n ) 
# #therefore the overall time complexity is O(n) here n is the nodes in the linked list


# # for normal approach the space complexity is as follows
# #the memory required to store the linked list is proportional  to the number of nodes,so it is O(n) where n is number of nodes in the linked list

# # here  we have used some fewer variables i.e count ,prev,curr ,newNode but these variables have only const space   and do not depend on the size of the linked list there fore overall space complexity is O(n)


# class Node:
#    def __init__(self,data):
#       #actually a node consist of data and next value i.e ref of next value so here we are storing next
#       #value as None..
#       self.data=data
#       self.next=None
#       #to get the head of the linked list
# def printLL(head):
#    #performs on head is not none
#    while head is not None:
#    #here we are converting it to string since it head is an int and we need output in the form of
#    #-> arrow function and the printLL is an string and head is an integer so we can not do like that so we are simply converting it to string ...
#       print(str(head.data) + "->",end="")
#       head =head.next
#       #by the above the loop was done and finally we need to print None and simply return 
#    print("None")
#    return 

# #insert at the ith position of a linked list and whose head is provided ,at the position which u want to insert i.e i and the data at which the new node is created,
# # if the i<0 and i>len (linked list) then we need to return same linked list

# #if i need to insert at i th position first i need to reach that i the position first
# #for reaching the i th position i need to maintain the count ,initially am at zero th position and i will traverse till i reach the i th position i.e keep on traversing till am lesser than the i th position,and keep on incrementing the count ,when the count becomes i then i will come out of the loop that means i need to insert at the i th position

# def length(head):
#    count=0
#    while head is not None:
#       count=count+1
#       head=head.next
#    return count

# def insertAtIR(head,i,data):

#     #if index is less than 0 means i.e negative  here u dont need  to do anything just simply return the same linked list
#    if i<0:
#       return head
#    #when i come to any element i.e head of the linked list,the induction hypothesis is lets insert at ith position recursively,call this function to insert at i-1 position ,of the next part of the linked list
#    if i==0:
#       newNode = Node(data)
#       #since am inserting at the 0th position i.e new node .next should be the head
#       newNode.next=head
#       return newNode
   
#    #if at any point if our head becomes none that means our i  was more than the length of the linked list ,here we cannot do anything just simply return none,at an empty linked list you nee d to insert at zero th position that is allowed  ,so u need to write i=0 before head  is none,so u will write i=0 before none
#    if head is None:
#       return None

          



  
   
#    #this below line does that u will get head of the linked list after inserting at i-1 position of that part  of the linked list
#    smallHead=insertAtIR(head.next,i-1,data)
#    head.next = smallHead
#    #need to return our head of the linked list our head remains same 
#    return head

# def insertAtI(head,i,data):
#    if i<0 or i >length(head):
#       return head
   
#    count=0
#    prev=None
#    curr=head
#    while count<i:
#       prev=curr
#       #we are maintaining the curr because we dont want to loose the reference of head and in the end we need to return the head of the linked list 
#       curr=curr.next
#       count=count+1
#       #with this our new node will be created

#    newNode= Node(data)
#    if prev is not None:
#       prev.next=newNode
#    else:
#       head=newNode
#    newNode.next=curr
#    return head




# #if i need to insert at i th position first i need to reach that i the position first
# #for reaching the i th position i need to maintain the count ,initially am at zero th position and i will traverse till i reach the i th position i.e keep on traversing till am lesser than the i th position,and keep on incrementing the count ,when the count becomes i then i will come out of the loop that means i need to insert at the i th position




# def takeInput():
#    # below is splitted based on space seperated 
#    inputList =[int(ele) for ele in input("please enter input").split()]

#    #initializing head to be None
#    head =None
#    #initializing the tail to be none-
#    tail=None  #since initially we are not taking any element so head and tail to be none

#    # a for loop is used to iterate through the above inputList
#    for currentData in inputList:
#       #a simple condition if our current data is -1 then break i.e terminates and exits the loop
#       if currentData ==-1:
#          break
#       #if our current data is not equal to -1  then create  a new node,with the below statement a node is created
#       newNode = Node(currentData)
# #this means no node has been created i.e first node
#       if head is None:
#          #then our node should to point newNode,here head is assigned in the first out only
#          head =newNode
#          tail=newNode #because for a single element a head and tail should be same for the first time
#       #except for the first node u will not work on head,if it is not the first node ,start from head keep on traversing till next becomes not none
#       else:
#          tail.next=newNode
#          tail=newNode



#    return head


# #below takeInput is inbuilt function
# #this is main.head 
# head =takeInput()
# printLL(head)
# printLL(head)  #with this only a simple copy of above code is created... thats it nothing changes
# head=insertAtIR(head,2,6)
# printLL(head)
# head=insertAtIR(head,0,9)
# printLL(head)

# #checking by inserting at the last position i.e length of the linked list
# head=insertAtIR(head,7,10)
# printLL(head)



                #19.Deleting node recursively

#we will get an linked list from the user like 
#head->1->2->3->4->5->null
#i=2
#here in this case we need to delete at the index  2 i.e which is 3


#Approach :first we need to brake our problem into 2 problems i.e n-1

#Base case:if our head becomes null then simply we need to return and come out 
 #if head ==null then simply return null and come out 
#our calculation part:when i=0 then simply update the head and return the updated head,this should be our recursion calculation part

#Recursion call->head->head->next
#in place of i we need to pass i-1
#here required node will be deleted and we will get the updated head
#by this required node get deleted and we will get the updated head...

#THIS IS OUR ASSIGNMENT DELETE A NODE IN THE GIVEN LINKED LIST..
