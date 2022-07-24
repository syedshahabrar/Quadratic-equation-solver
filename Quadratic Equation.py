import math

print ('Welcome to Comp 208 quadratic equation solver.')

a = int(input('Please enter the value of “a”: \n'))
b = int(input('Please enter the value of “b”: \n'))
c = int(input('Please enter the value of “c”: \n'))

x1 = (-b+math.sqrt(b**2-4*a*c))/2*a
x2 = (-b-math.sqrt(b**2-4*a*c))/2*a
#I wanted to use a function for this but it only would return one value

print('The first solution is:', x1)
print('The second solution is:', x2)