hrs = raw_input("Enter Hours:")
h = float(hrs)
rate = raw_input("Enter Rate:")
r = float(rate)

if (h <= 40):
	print "Gross pay: ", h * r
   
else:
    print  r * 40 + (h - 40) * 1.5 *r
