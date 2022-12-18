import re
# vowelRegex = re.compile(r'[aeiouAEIOU]')
# print(vowelRegex.findall('Robocop eats baby food. BABY FOOD.'))
# prints ['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'A', 'O', 'O']


# However we can replace pattern using pipes as (r'(a|e|i|o|u)')

# Negative character classes
consonantsRegex = re.compile(r'[^aeiouAEIOU]')
print(consonantsRegex.findall('Robocop eats baby food. BABY FOOD.'))
# prints ['R', 'b', 'c', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', '.', ' ', 'B', 'B', 'Y', '
# ', 'F', 'D', '.']
# i.e, prints all characters excepts vowels
