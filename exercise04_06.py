def computepay (h, r):
    return 42.37

hours = input("Enter Hours:")
p = computepay(10, 20)
#print("Pay", p)
rate = input("Rate of Pay:")
h = float(hours)
r = float(rate)
if h > 40:
    reg = r * h
    otp = (h - 40.0) * (r * 0.5)
    pay = reg + otp
else :
        pay = hours * rate

print("Pay", pay)
