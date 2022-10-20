import math             # Imports more complex Python math functions.
pi = math.pi

UnitType = str(input('Will you be using Diameter or Radius? D/R '))
if UnitType == 'D':     # Devides Diameter by two to get Radius instead.
  r = float(input('Please enter the Diameter. '))/2
elif UnitType == 'R': 
  r = float(input('Please enter the Radius. '))

else:                   # If the input was neither D or R, the program will close.
  exit('Terribly sorry, there was an error with defining the variables. Please restart the program!')
if r == 0:              # If the input was 0, the program will close.
  exit('You cant have a Radius of 0!')
  
A = pi*(r*r)
C = 2*pi*r

print('The area of your circle is', A, '!')
print('The circumference of your circle is', C, '!')