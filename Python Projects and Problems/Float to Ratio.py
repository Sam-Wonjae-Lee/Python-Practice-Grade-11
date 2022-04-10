from fractions import Fraction
value = float(input("Enter Number: "))
print(Fraction(value).limit_denominator())