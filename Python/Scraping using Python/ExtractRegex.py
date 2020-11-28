import re

file = open('sum.txt')

total = 0
total = int(total)

for line in file:
    line = line.rstrip()
    lst = re.findall('\d+',line)

    for val in lst:
        d = int(val)
        total = total + d

print(total)    
