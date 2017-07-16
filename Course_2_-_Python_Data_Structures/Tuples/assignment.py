fname = "mbox-short.txt"

handle = open(fname)

count={}
for line in handle:
    line=line.rstrip()
    if( not line.startswith('From ') ) : continue
    line.split()
    count[ line[-13:-11] ]= count.get( line[-13:-11], 0 ) + 1

result=count.items()
result=sorted(result)

for k, v in result:
    print('%s %d' % (k, v))
