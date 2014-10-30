score = raw_input("Enter a score: ")
s = float(score)

if s in [0.0,1.0]:
    print "Type Error"
elif s >= 0.9:
    print "A"
elif s >= 0.8:
    print "B"
elif s >= 0.7:
    print "C"
elif s >= 0.6:
    print "D"
else :
    print "F"



    
    
