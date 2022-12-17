import re

message = 'call me 415-245-9089 tomorrow, or at 456-087-4646'
USphoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# mo = USphoneNumRegex.search(message)
# print(mo.group())
# Prints 415-245-9089

# To print both the numbers replace search by findall
print(USphoneNumRegex.findall(message))
# prints ['415-245-9089', '456-087-4646']
