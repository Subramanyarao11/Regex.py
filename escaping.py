import re
# regex = re.compile(r'\+\*\?')
# mo = regex.search('I learned about +*? regex syntax')
# print(mo.group())
# Here we are literally searching for the characters +*? in the string and we are escaping the special characters by using a backslash\


# Escaping and printing one or more occurrences of the same character
regex = re.compile(r'(\+\*\?)+')
mo = regex.search("I learned about +*?+*?+*? regex syntax")
# print(mo.group())
# prints +*?+*?+*?
print(mo.group(1))
# prints +*?
