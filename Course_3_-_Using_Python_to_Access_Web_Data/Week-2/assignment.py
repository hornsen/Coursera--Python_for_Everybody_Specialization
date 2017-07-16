
import re
hand = open('actualData.txt')
numlist = []

for line in hand:
	line = line.rstrip()
	stuff = re.findall('[0-9]+',line)
	if len(stuff) > 0 : 
		for x in range(len(stuff)):					
			numlist.append( int( stuff[x] ) )
	
print(sum(numlist))

