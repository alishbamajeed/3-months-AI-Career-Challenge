# Operators In Python

# 1) Arithmetic Operators
# 2) Assignment Operators
# 3) Comparison Operators
# 4) Logical Operators
# 5) Identity Operators
# 6) Membership Operators
# 7) Bitwise Operators

a = 10
b = 25 

print ("Add" , a + b)
print ("Sub" , a - b)
print ("Mul" , a * b)
print ("Div" , a / b)
print ("Mod" , a % b)
print ("Pow" , a ** b)
print ("Floor" , a // b)


# Assignment Operators: yani jo bhi operator ha wo hum variable mein assign kar sakte ha
# = , += , -= , *= , /= , %= , **= , //=

x = 45
x += 5
print (x)

# Comparison Operators: hum ek value ko dosri value ka sath compare kar sakte ha
# == , != , > , < , >= , <=
c = 89
d = 20
print (c == d)
print (c != d)
print (c > d)
print (c < d)
print (c >= d)
print (c <= d)

#Logical Operators: 
# and , or , not

e = 6
f = 20
print (e > f and e < f)
print (e > f or e < f)
print (not(e > f and e < f))


# Identity Operators
# is : Agar dono same object hain  , is not : Agar dono different object hain

g = 10
h = 10
print (g is h)
print (g is not h)


# Membership Operators
# in :Check karta hai value present hai ya nahi , not in :Check karta hai value nahi hai
i = [1, 2, 3, 4, 5]
print (1 in i)
print (1 not in i)

# Bitwise Operators
# & , | , ^ , ~ , << , >>
j = 10
k = 20
print (j & k)
print (j | k)
print (j ^ k)
print (~j)
print (j << 2)
print (j >> 2)

