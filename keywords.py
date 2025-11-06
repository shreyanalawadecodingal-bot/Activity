import keyword

# List all Python keywords
print(keyword.kwlist)

# Check if a word is a keyword
print(keyword.iskeyword("for"))   # Output: True
print(keyword.iskeyword("hello")) # Output: False
