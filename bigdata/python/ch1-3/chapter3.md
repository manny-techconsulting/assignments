# Python: Chapters 1 - 3

Chapters 1, 2, & 3 are a simple introduction to python and therefore can be combined into one section for ease of understanding.

## 3.1 Numbers

The integer numbers (e.g. 2, 4, 20) have type ``int``, the ones with a fractional part (e.g. 5.0, 1.6) have type ``float``. 


The ``=`` sign is used for assignment of a value to a variable.

#### Operators

Operators ``+``, ``-``, ``*`` and ``/`` can be used to perform arithmetic expressions.

##### Addition

```python
>>> 3 + 3
9
```

##### Subtraction
```python
>>> 3 - 3
0
```
##### Multiplication
```python
>>> 3 * 3
9
```

##### Division

Division ``/`` always returns a float. 
```python
>>> 2/2
1.0
```
To do *floor division* and get an integer result you can use the ``//`` operator.

```python
>>> 2//2
1
```

To calculate the remainder you can use ``%``:
```python
>>> 7 % 6
1
```

##### Exponentiation

Operator ``**`` is used to calculate powers.
--

## 3.2 Strings

Python can manipulate text (represented by type [`str`](https://docs.python.org/3/library/stdtypes.html#str "str"), so-called “strings”) as well as numbers. 

This includes characters “`!`”, words “`rabbit`”, names “`Paris`”, sentences “`Got your back.`”, etc. “`Yay! :)`”. 

They can be enclosed in single quotes (`'...'`) or double quotes (`"..."`).

**Note**: Strings are **immuatable**.

### Escaping Characters

To quote a quote, we need to “escape” it, by preceding it with `\`. Alternatively, we can use the other type of quotation marks:

### Raw Strings

If you don’t want characters prefaced by `\` to be interpreted as special characters, you can use _raw strings_ by adding an `r` before the first quote:

There is one subtle aspect to raw strings: a raw string may not end in an odd number of `\` characters; see [the FAQ entry](https://docs.python.org/3/faq/programming.html#faq-programming-raw-string-backslash) for more information and workarounds.

### Output 

String literals can span multiple lines.
One way is using triple-quotes: `"""..."""` or `'''...'''`. 

End of lines are automatically included in the string, but it’s possible to prevent this by adding a `\` at the end of the line. The following example:

### Operations

Strings and variables can be concatenated (glued together) with the `+` operator. Strings may also repeated with `*` operator:

Two or more _string literals_ (i.e. the ones enclosed between quotes) next to each other are automatically concatenated.

This feature is particularly useful when you want to break long strings:

### Indexing

Strings can be _indexed_ (subscripted), with the first character having index 0. There is no separate character type; a character is simply a string of size one:

Indices may also be negative numbers, to start counting from the right:

### Formatted String Literals

Formatted string literals or f-strings using prefixes ``'f'`` or ``'F'``. 

These strings may contain replacement fields, which are expressions delimited by curly braces `{}`. 

While other string literals always have a constant value, formatted strings are really expressions evaluated at run time.

```python
name = "John Doe"
print(F"Hello, I am {name}")
```
---



## 3.3 Lists

Python knows a number of **compound** data types, used to group together other values. 

The most versatile is the <span style="color:rgb(0, 176, 240)">list</span>, which can be written as a list of comma-separated values (items) between square brackets. 
Lists are **0-indexed** and **mutable**.
Lists might contain items of different types, but usually the items all have the same type.

```python
nums = [1,2,3,4,5]
print(nums)
```

Like ***strings*** (and all other built-in sequence types), lists can be indexed and sliced:

```python
print(nums[0:3])
```


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

### Slices 
A slice is a potion of a sequence.

Slices notation has the following syntax:
```python
'''
Regular Slice
'''
a[start:stop]  # items start through stop-1
a[start:]      # items start through the rest of the array
a[:stop]       # items from the beginning through stop-1
a[:]           # a copy of the whole array
```

**Extended Slices** support the third ``step`` argument.
At times, the ``step`` argument is used exclusively; therefore, it has the notation ``[::step]``.

```python
'''
Extended Slice
'''
a[start:stop:step]
a[::step]
```

Python allows negative indexing of lists and any other sequence type.
The **-1** refers to the last item in the sequence type.

```python
rev_st = 'string'[::-1]
print(rev_st)
```

#### Slice Operations
All slice operations return a new list containing the requested elements. This means that the following slice returns a [[References#Shallow Copy |shallow copy]] of the list:
```python
colors = ["Red", "Brown", "Yellow","Silver"]
less_colors = colors[0:2]
print(colors)
print(less_colors)
```

Assignment to slices is also possible, and this can even change the size of the list or clear it entirely:
```python
letters = ['C', 'D','E','F']
letters[0:2] = ['A','B']
print(letters)
```


## Example Scripts
[Chapter 3.1: Numbers](/assignments/bigdata/python/ch1-3/ch3-1.py)

[Chapter 3.2: Texts/Strings ](/assignments/bigdata/python/ch1-3/ch3-2.py)

[Chapter 3.3: Lists](/assignments/bigdata/python/ch1-3/ch3-3.py)
