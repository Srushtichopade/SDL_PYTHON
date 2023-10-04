#if statement
a = 20 ; 
b = 20 ;
if (a == b):
	print("a and b are equal")
	print("If block ended")


#if-else statement
number = 10

if number > 0:
    print('Positive number')

else:
    print('Negative number')

print('This statement is always executed')



#if-elif ladder
number = 0

if number > 0:
    print("Positive number")

elif number == 0:
    print('Zero')
else:
    print('Negative number')

print('This statement is always executed')


#while loop

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")