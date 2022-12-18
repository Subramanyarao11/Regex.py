import re
lyrics = ''''12 drummers drumming
Eleven pipers piping
Ten lords a-leaping
Nine ladies dancing
Eight maids a-milking
Seven swans a-swimming
Six geese a-laying
Five golden rings (five golden rings)
Four calling birds
Three French hens
Two turtle-doves
And a partridge in a pear tree
And a partridge in a pear tree'''


xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall(lyrics))
