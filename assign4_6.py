def computepay(h,r):
    if h <= 40:
        pay = h * r
    else: 
        pay = (h-40)*1.5*r + 40*r
    return pay

hrs = raw_input("Enter Hours:")
h = float(hrs)
rate = raw_input("Enter Rate:")
r = float(rate)

p = computepay(h,r)
print p
