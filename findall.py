import re

phoneregex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneregex.findall('Cell: 415-555-9999 Work: 212-555-0000'))
# If the search pattern has 0 or 1 group phoneregex.findall returns a list of matches


# However if the search pattern has more than 2 groups then phoneregex.findall returns a tuple of list of Strings
