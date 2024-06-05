There is no type checking  since Python supports dynamic typing.

However, annotations can be used to collect information about the type of the parameters and the return type of the function to keep track of the type change occurring in the function.

```python
def add(a: int, b: int) -> int:
	return a + b
print(add(1,2))
```