The reverse situation occurs when the arguments are already in a list or tuple but need to be unpacked for a function call requiring separate positional arguments. 

For instance, the built-in `range()` function expects separate _start_ and _stop_ arguments. 
If they are not available separately, write the function call with the  `*`-operator to unpack the arguments out of a list or tuple:

```python
args=[3,6]
l = list(range(*args)) # args is unpacked from list
print(l)
```

In the same fashion, dictionaries can deliver keyword arguments with the `**`-operator:
```python
def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

p = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}

parrot(**p)
```
