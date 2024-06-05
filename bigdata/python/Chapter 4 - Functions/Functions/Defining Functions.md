The keyword ``def`` introduces a function _definition_. 

It must be followed by the function name and the parenthesized list of formal parameters. 
The statements that form the body of the function start at the next line, and must be indented.

The first statement of the function body can optionally be a string literal; this string literal is the function’s documentation string, or _docstring_.

```python
def do_something():
	'''
	Demonstrates document string literals
	'''
	return None
print(do_something())
```

The _execution_ of a function introduces a new symbol table used for the local variables of the function. 

More precisely, all variable assignments in a function store the value in the local symbol table; whereas variable references first look in the local symbol table, then in the local symbol tables of enclosing functions, then in the global symbol table, and finally in the table of built-in names. 

Thus, global variables and variables of enclosing functions cannot be directly assigned a value within a function (unless, for global variables, named in a `global` statement, or, for variables of enclosing functions, named in a `nonlocal` statement), although they may be referenced.

The actual parameters (arguments) to a function call are introduced in the local symbol table of the called function when it is called; thus, arguments are passed using _call by value_ (where the _value_ is always an object _reference_, not the value of the object).

When a function calls another function, or calls itself recursively, a new local symbol table is created for that call.

A function definition associates the function name with the function object in the current symbol table. 
The interpreter recognizes the object pointed to by that name as a user-defined function. 
Other names can also point to that same function object and can also be used to access the function:

```python
action = do_something
print(action())
```

Functions without a ``return``statement still return a value: ``None``. It is normally suppressed by the interpreter. 

```python
def none():
	pass
print(none()) # Prints None
```

