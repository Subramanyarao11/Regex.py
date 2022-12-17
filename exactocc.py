import re
adjectives = "Subramanya is good, Subramanya is great, Subramanya is awesome"

regex = re.compile(r'(Subramanya){3}')
mo = regex.search(adjectives)
print(mo.group())
