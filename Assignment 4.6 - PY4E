#Here we define the formula for extra hours payment

def computepay(h, r):
    if h <= 40:
        return h * r
    if h > 40:
        extra = (h - 40)
        payment = extra * (r * 1.5) + (h - extra) * r
        return payment

hrs = input("Enter Hours:")

#Here we can check bad input from the user
try: 
    h = float(hrs)
except:
    print("Please give a numeric statement. E.g: 40")
    quit()

pph = input("Enter Payment per Hour:")

#Again checking bad input to return an error message
try: 
    r = float(pph)
except: 
    print("Please give a numeric statement. E.g: 10")
    quit()
    
tp = computepay(h, r)
print("Pay", tp)
