fname = "romeo.txt"

fh = open(fname)
lst = list()

for line in fh:
    line=line.rstrip()
    words=line.split()
    for x in range(len(words)):
        if(words[x] not in lst):
            lst.append(words[x])

lst.sort()            
print(lst)
