# Find the greatest common denominator of two numbers
# using Euclid's Algorithm

def gcd(a,b):
    while(b!=0):
        t = a
        a = b
        b = t % b
    return a
        
a = int(input("Enter a number:"))

b = int(input("Enter a number:"))

GCD = gcd(a,b)

print("GCD is:",GCD)
        
    
