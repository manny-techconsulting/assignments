Functions can also be called using *keyword arguments* for the form ``kwarg=value``

```python
def describe_employee(id,fname="John", lname="Doe"):
	s = F"Employee:\nID:{id}\nFirst Name:{fname}\nLast Name:{lname}\n"
	return s
print(describe_employee(12))
print(describe_employee(12, "Manny"))
```

In this function, there is 1 required positional argument and 2 optional arguments with default values.

In a function call, keyword arguments **must** follow positional arguments. 
All the keyword arguments passed must match one of the arguments accepted by the function and their order is not important.
No argument may receive a value more than once.

When a final formal parameter of the form `**name` is present, it receives a dictionary containing all keyword arguments except for those corresponding to a formal parameter. 
This may be combined with a formal parameter of the form `*name` (described in the next subsection) which receives a  containing the positional arguments beyond the formal parameter list. 
(`*name` must occur before `**name`.) 

```python
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])
        
cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
```