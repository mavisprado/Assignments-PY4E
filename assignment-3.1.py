hrs = input("Enter Hours:")
h = float(hrs)
pph = input("Enter Payment per Hour:")
p = float(pph)
if h <= 40 :
    totalpay = p * h
if h > 40 :
    totalpay = (40 * p) + (h - 40) * (p * 1.5)
print(totalpay)
