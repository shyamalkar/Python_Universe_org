a = float(input("Enter a valid number: "))
b = float(input("Enter a 2nd valid number: "))
c = float(input("Enter a 3rd valid number: "))

s = ( a + b + c) / 2

area = (s * ( s - a) *(s - b) * (s - c))
print(area)

print(s)