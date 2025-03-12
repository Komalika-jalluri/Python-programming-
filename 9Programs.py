#reverse of a string 
a="engineering college"[ ::-1]
print(a)

#password
password=input()
l=len(password)
if(l<8):
    print("Invalid password")
digit=False
upper=False
lower=False
special=False
special_character="@#&!$%^'?()-+_/*;<>{}[]\"
for i in password:
    if i.isdigit():
        digit=True
    elif i.isupper():
        upper=True
    elif i.islower():
        lower=True
    elif i in special_character:
        special=True
if digit and upper and lower:
    print("Valid password")
else:
    print("Invalid password")

#smallest number
a=int(input("First number: ")
b=int(input("Second number: ")
c=int(input("Third number: ")
if(a<b and a<c):
    print("a is smallest")
elif(b<a and b<c):
    print("b is smallest")
elif(c<b and c<a):
    print("c is smallest")
elif(a==b==c):
    print("all are equal")
elif(a==b and b>c)
    print(" c is smallest")

#months and seasons
month=int(input())
if month== 12 or 1 or 2:
   print("WINTER")
elif month== 3 or 4 or 5:
   print("SUMMER")
elif month== 6 or 7 or 8:
   print("RAINY")
elif month== 9 or 10:
   print("SPRING")
elif month==11:
   print("AUTUMN")
else:
   print("None")

#keywords and ascii values
help("keywords")

for i in range(56,98):
     print(chr(i))

#calculator
a=int(input("first integer: ")
operator=input()
b=int(input("second integer: ")
if operator=='+':
    print(a+b)
elif operator=='-':
    print(a-b)
elif operator=='*':
    print(a*b)
elif operator=='/':
    print(a/b)
elif operator=='%':
    print(a%b)
elif operator=='//':
    print(a//b)
elif operator=='**':
    print(a**b)

#hypenated
s=input()
print('-'.join())

bitwise operators
# Define the input bitstring
bitstring = "1A0B0C1"

# Start with the first bit
result = int(bitstring[0])

# Loop through the string to apply operations
for i in range(1, len(bitstring) - 1, 2):
    operator = bitstring[i]
    next_bit = int(bitstring[i + 1])

    if operator == 'A':   # AND operation
        result &= next_bit
    elif operator == 'B': # OR operation
        result |= next_bit
    elif operator == 'C': # XOR operation
        result ^= next_bit
print("Result:", result)

#denomination
amount = int(input("Enter amount: "))

five_hundred_notes = amount // 500
amount %= 500
print("Five Hundred (500):", five_hundred_notes)

hundred_notes = amount // 100
amount %= 100
print("Hundred (100):", hundred_notes)

fifty_notes = amount // 50
amount %= 50
print("Fifty (50):", fifty_notes)

ten_notes = amount // 10
amount %= 10
print("Ten (10):", ten_notes)
