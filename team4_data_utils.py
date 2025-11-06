def lcm(a, b): 
    from math import gcd; 
    return abs(a*b) // gcd(a, b)
print('FIND LCM')
a=int(input("enter Element 1:"))
b=int(input("Enter Element 2:"))
print(lcm(a,b))


