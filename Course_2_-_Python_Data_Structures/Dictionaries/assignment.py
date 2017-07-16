	fname = "mbox-short.txt"
handle = open(fname)
email={}

for line in handle:
	line=line.rstrip()
	if not line.startswith('From '): continue
	line=line.split()	
	email[ line[1] ] = email.get(line[1],0)+1
	

result=max(zip(email.values(),email.keys()))
print('%s %d' % (result[1], result[0]))
