# tabel kebenaran (logika bolean)
# an or not xor

# NOT
print("************logika not************")
x = False
y = not x
print("nilai dari x =",x)
print("nilai dari y =",y)

# and
print("************logika and************")
x = False
y = False
z = x and y
print( x, "and" , y, "=", z)

x = False
y = True
z = x and y
print( x, "and" , y, "=", z)

x = True
y = False
z = x and y
print( x, "and" , y, "=", z)
x = True
y = True
z = x and y
print( x, "and" , y, "=", z)


# or
print("************logika or************")
x = False
y = False
z = x or y
print( x, "or" , y, "=", z)

x = True
y = False
z = x or y
print( x, "or" , y, "=", z)

x = False
y = True
z = x or y
print( x, "or" , y, "=", z)

x = True
y = True
z = x or y
print( x, "or" , y, "=", z)

# xor
print("************logika xor************")
x = False
y = False
z = x ^ y
print( x, "xor" , y, "=", z)

x = True
y = False
z = x ^ y
print( x, "xor" , y, "=", z)

x = False
y = True
z = x ^ y
print( x, "xor" , y, "=", z)

x = True
y = True
z = x ^ y
print( x, "xor" , y, "=", z)

