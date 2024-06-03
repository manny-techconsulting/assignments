# CHAPTER  3 . 2 STRINGS/TEXT

# ESCAPING CHARACTERS
print('\"This is a Quote\"')

#RAW STRINGS
print(r'"This is a raw string"')

#OUTPUT 
print('''
      String literals can span multiple lines.
      One way is using triple quotes: \'\'\' or \"\"\"
      ''')

print('''End of lines are automatically included in the string, 
      but it’s possible to prevent this by adding a \ at the end of the line. 
      The following example:\
    ''')

#CONCATENATION

# Operator +
print('Hello' + 'World')
# Operator *
print('Repeating\t' * 3)

#INDEXING 
greeting  = "Hello World"
print(greeting[0]) # Indexing from start 0
print(greeting[0:3]) # Indexing within 0 and 3 exclusive
print(greeting[3:]) # Indexing from starting position 3
print(greeting[:3]) # Indexing until 3 exclusive
print(greeting[:-1]) # Indexing backwards with negative numbers

# FORMATTED STRING LITERALS
name = "John Doe"
fmt_string = f'Hello {name}'
print(fmt_string)

