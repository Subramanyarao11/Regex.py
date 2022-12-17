import re

# batRegex = re.compile(r'Bat(wo)?man')
# mo = batRegex.search('The Adventures of Batwoman')
# print(mo.group())
# Prints Batwoman

# However if the search string was "Batwowowowoman" then it would not print anything i.e. mo == None
# mo.group() would throw an AttributeError

# To match more than one character, use the * character
# The * character means "zero or more" of the preceding character
# The * character is greedy, meaning it will match as many characters as possible
# To match as few characters as possible, use the *? non-greedy form

batRegex = re.compile(r'Bat(wo)*man')
mo = batRegex.search('The Adventures of Batwowowowman')
print(mo.group())
