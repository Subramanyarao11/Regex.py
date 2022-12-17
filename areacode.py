# To return only area code of the phone number
import re
message = 'call me 415-245-9089 tomorrow, or at 456-087-4646'
AreacodeRegex = re.compile(r'(\d\d\d)-\d\d\d-\d\d\d\d')
mo = AreacodeRegex.search(message)
print(mo.group(1))
# prints 415

# To print area code of both the numbers
# print(AreacodeRegex.findall(message))
# prints ['415', '456']
