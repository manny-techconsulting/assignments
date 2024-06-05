The most useful form is to specify a default value for one or more arguments. This creates a function that can be called with fewer arguments than it is defined to allow

```python
def ask_ok(prompt,retries=4,reminder="Please try again!"):
	while True:
		reply = input(prompt)
		if reply in {'y', 'ye', 'yes'}:
			return True
		if reply in {'n', 'ne', 'no'}:
			return False
		retries -= 1
		if retries < 0:
			raise ValueError('invalid user response')
		print(reminder)

#ask_ok("Do you want to quit?")
#ask_ok('OK to overwrite the file?', 2)
ask_ok('Ok to overwrite?',2,"Only yes or no")
```

### Defining Scope

The default values are evaluated at the point of function definition in the _defining_ scope.

The default value is evaluated only once.
This makes a difference when the default is a mutable object such as a ``list``, ``dictionary``, or instances of most classes. 

For example, the following function accumulates the arguments passed to it on subsequent calls.

```python
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))
```

If you don’t want the default to be shared between subsequent calls, you can write the function like this instead:

```python
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
print( f(1))
print( f(2))
```