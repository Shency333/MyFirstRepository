
#Arithmetic Operators

print("Arithmetic Operations")

A=20
B=3
print(A+B)
print(A-B)
print(A*B)
print(A/B)
print(A%B)
print(A**B)# Exponent
print(A//B)# Floor division

#Assignment operators

print("Assignment operators")

X=5
print(X)
X+=5
print(X)
X-=5
print(X)
X*=5
print(X)
X/=5
print(X)
X%=5
print(X)
X**=5
print(X)
X//=5
print(X)


#Comparison Operators

print("Comparison operators")

Y,Z=10,20
print(Y==Z)
print(Y!=Z)
print(Y>Z)
print(Y<Z)
print(Y>=Z)
print(Y<=Z)


#Logical Operators


print("Logical Operators")

E=60
print(E>10 and E>30)
print(E>10 or E>100)
print(not(E>10 and E>30))

#Identity Operators

print("Identity operators")

mylist1=["a","b"]
print(id(mylist1))
mylist2=["a","b"]
print(id(mylist2))
mylist=mylist1
print(id(mylist))
print(mylist1 is mylist)
print(mylist1 is mylist2)
print(mylist1 is not mylist2)

#membership operators

print("membership operators")

fruits=["apple","banana","cherry"]
print("banana" in fruits)
print("lemon" in fruits)
print("lemon" not in fruits)

#Bitwise operators

print("Bitwise operators")

# 0001 - 1

# 0011 - 3
#out:0001 - 1

print(1 & 3)
print(1 | 3)
print(1 ^ 3) # EXOR
print(~-4)

#zero fill leftshift

print(1<<2)
print(5<<2)

#signed rightshift

print(4>>2)
print(3>>2)








































