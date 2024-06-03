#CHAPTER 3.3    LISTS

#LIST INDEXING

nums = [1,2,3,4,5]
print(nums)

#ASSIGNMENT
#
#Simple assignment in Python never copies data. 
#When you assign a list to a variable, the variable refers to the _existing list_. 
#Any changes you make to the list through one variable will be seen through all other variables that refer to it.
###
nums_reference_copy = nums
print("Do these two objects reference the same object")
print(id(nums_reference_copy) == id(nums))
#Changes occur in both
nums_reference_copy[0] = 0
nums[1] = 1
print(nums_reference_copy)
print(nums)

#SLICES
#REGULAR SLICE
print(nums[0:len(nums)]) #a[start:stop]
print(nums[0:]) #a[start:] 
print(nums[:3]) #a[:stop]
print(nums[:]) #a copy of the whole array

#EXTENDED SLICE
print(nums[0::2]) #a[start:stop:step]
print(nums[::-1]) # reverse access of a list