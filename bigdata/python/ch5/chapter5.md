# Chapter 5: Data Structures

## Lists
Python knows a number of _compound_ data types, used to group together other values. 

The most versatile is the <span style="color:rgb(0, 176, 240)">list</span>, which can be written as a list of comma-separated values (items) between square brackets. 
Lists are **0-indexed** and **mutable**.
## Methods

Lists might contain items of different types, but usually the items all have the same type.

```python
nums = [1,2,3,4,5]
print(nums)
```
### Indexing 
Like strings (and all other built-in sequence types), lists can be indexed and sliced:

```python
print(nums[0:3])
```

### Concatentation
Lists also support operations like concatenation:
```python
more_nums = [6,7,8]
print(more_nums + nums)
```

### Assignment
Simple assignment in Python never copies data. 
When you assign a list to a variable, the variable refers to the **_existing list**_.

Any changes you make to the list through one variable will be seen through all other variables that refer to it.

```python
nums_assign = nums
print(id(nums_assign) == id(nums)) # They reference the same object
nums_assign.append([0,0]) # changes occur are reflected in both
print(nums_assign) 
print(nums)
```

All slice operations return a new list containing the requested elements. This means that the following slice returns a [[References#Shallow Copy |shallow copy]] of the list:
```python
colors = ["Red", "Brown", "Yellow","Silver"]
less_colors = colors[0:2]
print(colors)
print(less_colors)
```

##### Slice Assignment
Assignment to slices is also possible, and this can even change the size of the list or clear it entirely:
```python
letters = ['C', 'D','E','F']
letters[0:2] = ['A','B']
print(letters)
```

## More Methods

```python {pre}
l = [1,2,3,4,5,6]
```
#### append(_x_)
Add an item to the end of the list. 
Equivalent to `a[len(a):] = [x]`.
```python
l.append(7)
print(l)
```
#### extend(*iterable*)
Extend the list by appending all the items from the iterable. 
Equivalent to `a[len(a):] = iterable`.
```python
more_nums = [8,9,10]
l.extend(more_nums)
print(l)
```
#### insert(_i_,_x_)
Insert an item at a given position. 
The first argument is the index of the element before which to insert, so `a.insert(0, x)` inserts at the front of the list, and `a.insert(len(a), x)` is equivalent to `a.append(x)`.

```python
l.insert(0,0)
print(l)
```
#### remove(_x_)
Remove the first item from the list whose value is equal to _x_. 
It raises a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") if there is no such item.
```python
l.remove(3)
print(l)
```
#### pop([i])
Remove the item at the given position in the list, and return it. 
If no index is specified, `a.pop()` removes and returns the last item in the list. 
It raises an [`IndexError`](https://docs.python.org/3/library/exceptions.html#IndexError "IndexError") if the list is empty or the index is outside the list range.
```python
l.pop()
print(l)
l.pop(2)
print(l)
```
#### clear()
Remove all items from the list. 
Equivalent to `del a[:]`.
```python
l.clear()
print(l)
```
#### index(_x_[, _start_[, _end_]])
Return zero-based index in the list of the first item whose value is equal to _x_. 
Raises a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") if there is no such item.

The optional arguments _start_ and _end_ are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. 
The returned index is computed relative to the beginning of the full sequence rather than the _start_ argument.

```python
print(l.index(1))
```
#### count(_x_)
Return the number of times _x_ appears in the list.
```python
print(l.count(3))
```
#### sort(*, key=None, reverse=False)
Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).
```python
people = ["Sarah", "John", "Harry","Howie"]
print(people.sort(reverse=True))
```
#### reverse
Reverse the elements of the list in place.
```python
rv_string = 'string to reverse'
print(rv_string.reverse())
```

#### copy
Return a shallow copy of the list. Equivalent to ``a[:]``.

```python {post}
l = []
print(l)
c = [-1,0,-1]
l = c.copy()
print(l)
```


#### len() 
The size of the list can be known by calling ``len`` similar to strings.
```python
l = [1,2,3]
print(len(l))
```


## List Comprehensions
List comprehensions provide a concise way to create lists. 

Common applications are to make new lists where each element is the result of some operations applied to each member of another sequence or iterable, or to create a subsequence of those elements that satisfy a certain condition.

```python
squares = [x**2 for x in range(0,8)]
```

You can add ``if statements`` to to the for clauses.
The order of clauses is ``for clause`` then ``if statement``.
```python
points = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
```

