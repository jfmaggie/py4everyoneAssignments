# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)

li = list()
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    #print line.rstrip()
    li.append(line.rstrip())
    
    
    
#print "Done"
count = 0
ave = 0
for item in li:
    index = item.find('0')
    val = float(item[index:])
    #print val,'====='
    count += 1
    ave = val + ave

print 'Average spam confidence:', ave / count

