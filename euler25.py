## Python program to solve Euler Problem 25
a = 0
b = 1
c = 1 #a,b = fib variables, c = index counter

while len(str(a)) < 1000: # using len to check if the amount of digits in a is
  b = b + a
  a = b #fibonacci sequence
  c += 1

print (a)
print (c) #prints a the current number, and c the index.
