#             #HASHTABLES AND HASH MAPS

# #1.hashtables and hash maps are the datastructure that maps the keys to its values pairs,
# #2.with this we can perform insert remove etc.. which makes easy and access fast data

# #3.hash tables stores  keyvalue pairs and the key is generated using a hash function

# #4.hash tables and hash maps are built using built in dictionary datatypes..
# #5.the keys are generated using hashing function,and the elements are not ordered and can be changed ex:mapping a students with their students id's 
# #6.can be created using a curly braces and using a dict() function

#         #CREATING A DICTIONARY USING A CURLY BRACES..
# #employee mapping with their id no's
# my_emp={'david':'001','karunakar':'002','anu':'003'}
# print(my_emp)
# print(type(my_emp))

# #CREATING A DICTIONARY USING dict() function

# #creating a empty dictionary
# new_dict=dict()
# print(new_dict)
# print(type(new_dict))

# #creating with some keys and values ,here creating will be little different using a dict() function and keys ,value..
# new_dict=dict(davin='001',raghu='002',karna='003')
# print(new_dict)
# print(type(new_dict))



# #NESTED DICTIONARIES..
# #a dictionary with in inside a dictionary..
# employee_details={
# 'employee':
# {
# 'ava':{'id':'001','salary':'20000','Desigination':'Team Lead'},
# 'Niharikha':{'id':'003','salary':'50000','Designation':'Team player'},
# 'Niharikha2':{'id':'003','salary':'50000','Designation':'Team player'},
# }
# }




# #performing operations on hash tables
# #1.Acess items
# #2.updating values
# #3.Deleting Enteries


# #Acessing values in dictionary
# #it can be accessed in many ways using key value pairs,using functions ,or implementing for loop

#             #KEYS...
# #using key values
# print(my_emp['david'])  #this fetches to the dict created above (my_emp) and gives the value associated to it ,here we need to use the square braces..

# print(my_emp)
# #we can acess using keys,values,and get() function as well...


#                     #FUNCTIONS...
# #using .keys() we can get all the keys associated to our dictionary
# print(my_emp.keys())


# #using .values() we can get all the values associated to our dictionary
# print(my_emp.values())

# #using .get() we can get all the value associated to that particular given key

# print(my_emp.get('karunakar')) #if the given key is not there then it return None




#                         #USING A FOR LOOP
# #this gives all our keys ,if we want values use .values(),and both keys,values means use .items()
# for x in my_emp:
#     print(x)

# #getting all the values of our dict() using .values() 
# for x in my_emp.values():
#     print(x)

# #this .items() gives us both  the keys and as well values side by side
# for x,y in my_emp.items():
#     print(x,y)






#     #UPDATING THE VALUES OF A DICTIONARY
#     #Note:dictionary are mutable datatypes we can update when ever it is required
# my_emp['anu']='008' #like this we can update the value
# my_emp['chris']='000'  #like this we can add new key and value
# print(my_emp)  #printing after all modifications



# #DELETING THE ITEMS FROM A DICTIONARY..
# # del,pop,pop item function,clear ..etc..

# my_dict={'karunakar':'000','rani':'009','abhi':'009'}
# my_dict.pop('rani')#this pop function simply removes the key and value if we give key
# print(my_dict)

# #popitem()
# print(my_dict.popitem())  #this gives the last value given to our dict and returns the last value..


# #del :syntax:del dictionary_name ['key']
# del my_dict['karunakar']
# print(my_dict) #this del removes the given one..



#             #converting a dictionary into a dataframe
# #dataframe :it is a 2d structure that consist of columns of various types,
# #it is very similar to python dictionary and we can even convert a dictionary into a pandas dataframe,
# #we get output as a table..
 

# #DICT TO DF(inorder to keep dict into dataframe we need to use pandas frame)
# #note:inorder to use pandas first we need to import it (pip install pandas) in our current folder directory

# # import pandas

# df=pandas.DataFrame(employee_details['employee']) #this is just an syntax
# print(df)


# import pandas

# mydataset = {
#   'cars': ["BMW", "Volvo", "Ford"],
#   'passings': [3, 7, 2]
# }

# myvar = pandas.DataFrame(mydataset)

# print(myvar)






                            #SHIFT_STRING...CONCEPT....


def shift_string(s, n):
    # Initialize an empty string to hold the shifted result
    shifted = ''
    # Loop through each character in the input string
    for char in s:
        # Check if the character is a letter
        if char.isalpha():
            # Convert the character to lowercase for easier indexing
            lower_char = char.lower()
            # Compute the index of the shifted character
            shifted_index = (ord(lower_char) - 97 + n) % 26 + 97
            # Convert the shifted index back to its corresponding letter
            shifted_char = chr(shifted_index)
            # Preserve the original case of the character
            if char.isupper():
                shifted_char = shifted_char.upper()
            # Append the shifted character to the result string
            shifted += shifted_char
        else:
            # If the character is not a letter, just append it to the result string
            shifted += char
    # Return the final shifted string
    return shifted

# Example usage:
s = 'algo123'
n = 1
shifted = shift_string(s, n)
print(shifted)  # Outputs "bmhp123"

s = 'axy'
n = 3
shifted = shift_string(s, n)
print(shifted)  # Outputs "dab"


                        #defaultdict(int): CONCEPT....

# defaultdict(int):
# defaultdict(int) is a Python function that creates a dictionary object that has a default value of zero for any missing key.

# In other words, if you try to access a key that does not exist in the dictionary, instead of raising a KeyError exception, it will return the default value of zero.


# from collections import defaultdict

# d = defaultdict(int)

# print(d["foo"])   # prints 0
# print(d["bar"])   # prints 0
# print(d)          # prints defaultdict(<class 'int'>, {'foo': 0, 'bar': 0})
