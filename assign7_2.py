'''
7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below.
You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

Output: 
Average spam confidence: 0.750718518519

'''
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

