s={1,2,3,4,5,6,7,8,9,10}
s.add(11)
print(s)

s.pop()
print(s)
s.discard(10)
print(s)

#union
a={1,2,3,4}
b={5,6,7,8,9}
c=a,b
#print(c)
print(a.union(b))

#intersection
a={1,2,3,4}
b={4,6,7,8,9}
c=a.intersection(b)
print(c)

#differance

a={1,2,3,4}
b={4,6,7,8,9}
c=a.difference(b)
c=a-b
print(c)

#Symmetric Differance

a={1,2,3,4}
b={4,6,7,8,9}
c=a.symmetric_difference(b)
c=a^b
print(c)
