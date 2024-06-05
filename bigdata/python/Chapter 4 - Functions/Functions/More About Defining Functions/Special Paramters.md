By default, arguments may be passed to a Python function either by position or explicitly by keyword. 

For readability and performance, it makes sense to restrict the way arguments can be passed so that a developer need only look at the function definition to determine if items are passed by position, by position or keyword, or by keyword.

A function definition may look like the following where ``/`` and ``*`` are optional.

```python
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
        |             |                  |
        |        Positional or keyword   |
        |                                - Keyword only
         -- Positional only
```

If used, these symbols indicate the kind of parameter by how the arguments may be passed to the function: *positional-only*, *positional-or-keyword*, and *keyword-only*. 
Keyword parameters are also referred to as named parameters.

##### Positional-or-Keyword Arguments
If `/` and `*` are not present in the function definition, arguments may be passed to a function by position or by keyword.

```python
def standard_arg(arg):
    print(arg)

standard_arg(2)
standard_arg(arg=2)
```

##### Positional-Only Arguments
Looking at this in a bit more detail, it is possible to mark certain parameters as _positional-only_. 
If _positional-only_, the parameters’ order matters, and the parameters cannot be passed by keyword.
Positional-only parameters are placed before a `/` (forward-slash). 
The `/` is used to logically separate the positional-only parameters from the rest of the parameters.
If there is no `/` in the function definition, there are no positional-only parameters.

Parameters following the `/` may be _positional-or-keyword_ or _keyword-only_.

```python
def pos_only_arg(arg, /):
    print(arg)

pos_only_arg(1)
pos_only_arg(arg=1) # causes an error
```

##### Keyword-Only Arguments
To mark parameters as _keyword-only_, indicating the parameters must be passed by keyword argument, place an `*` in the arguments list just before the first _keyword-only_ parameter.

```python
def kwd_only_arg(*, arg):
    print(arg)

kwd_only_arg(arg=1)
kwd_only_arg(1) # causes an error
```

##### Collision
Finally, consider this function definition which has a potential collision between the positional argument `name`and `**kwds` which has `name` as a key:

```python
def foo(name, **kwds):
    return 'name' in kwds
```

There is no possible call that will make it return `True` as the keyword `'name'` will always bind to the first parameter.

```python
foo(1, **{'name': 2}) # causes an error
```

But using `/` (positional only arguments), it is possible since it allows `name` as a positional argument and `'name'` as a key in the keyword arguments:

```python
def foo(name, /, **kwds):
    return 'name' in kwds
```

```python
foo(1, **{'name': 2})
```




