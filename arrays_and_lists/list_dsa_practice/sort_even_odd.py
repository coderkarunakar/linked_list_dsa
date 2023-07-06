# Write a python program to sort even and odd elements of list separately.
a=[1,2,3,4,0,9,8,7,6]
even=[]
odd=[]
for i in range(len(a)):
    if a[i]%2==0:
        even.append(a[i])
    else:
        odd.append(a[i])

print(even)
print(odd)

for i in range(len(even)):
    for j in range(i+1,len(even)):
        if even[i]<even[j]:
            temp=even[i]
            even[i]=even[j]
            even[j]=temp
print(even)
for i in range(len(odd)):
    for j in range(i+1,len(odd)):
        if odd[i]<odd[j]:
            temp=odd[i]
            odd[i]=odd[j]
            odd[j]=temp
print(odd)


#question adding +1 to the given integer..
# from typing import List

# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         carry = 1
#         for i in range(len(digits)-1, -1, -1):
#             digits[i] += carry
#             if digits[i] <= 9:
#                 carry = 0
#                 break
#             digits[i] = 0
#         if carry == 1:
#             digits.insert(0, 1)
#         return digits
# s = Solution()
# digits = [4, 3, 2, 1]
# print(s.plusOne(digits))  # output: [4, 3, 2, 2]



#pushing zerores to the end

class UserMainCode:
    @classmethod
    def PushZeroesEnd(cls, input1, input2):
        # Count the number of zeros in the input list
        num_zeros = input1.count(0)
        
        # Remove the zeros from the input list
        input1 = [num for num in input1 if num != 0]
        
        # Append the required number of zeros to the end of the input list
        input1 += [0] * num_zeros
        
        # Return the input list
        return tuple(input1)
input1 = (1,0,3,0,6)
input2 = 5
output = UserMainCode.PushZeroesEnd(input1, input2)
print(output)
