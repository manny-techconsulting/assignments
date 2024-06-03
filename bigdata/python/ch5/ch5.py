#DATA STRUCTUTRES

#LISTS

#PRE
nums = [0,1,23,4,5,6,7,8,9,10]

#METHODS

#LEN
print(len(nums))

#APPEND
print(nums.append(11))

#EXTEND
print(nums.extend([12,13,14]))

#INSERT
print(nums.insert(0,-1))

#REMOVE
print(nums.remove(14))

#POP
print(nums.pop())

#CLEAR
print(nums.clear())
nums = [0,0,1,2,3,0,0 ]

#INDEX
print(nums.index(0))

#COUNT
print(nums.count(0))

#SORT
print(nums.sort(reverse=True))

#COPY
c_num = nums.copy()
print(c_num)

#LIST COMPREHENSIONS
squares = [x**2 for x in range(0,11,1)]
print(squares)

#LIST COMPREHENSIONS WITH IF STATEMENTS
points = [(x, y) for x in [1,2,3] for y in [4,2,1] if x != y]
print(points)