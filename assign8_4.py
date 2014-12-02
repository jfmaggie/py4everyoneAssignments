fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:
    #print line.rstrip()
    a = line.split()
    for word in a:
        #print word
        if word not in lst: lst.append(word)
        else: continue
lst.sort()
print lst
