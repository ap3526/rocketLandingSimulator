#Program made by Akash Patel CS-171-A Lab Section 060 
import sys
#initial Values
gravity = -1.622
altitude = 50
velocity = 0
unitsFuel = 150
thrusterAccel = 0.1
counter = 0
go = True
#Dictionary that contains all levels and corresponding values
allLevels = [('Moon', -1.622, 150), ('Earth', -9.81, 5000), ('Pluto', -0.42, 1000), ('Neptune', -14.07, 1000), ('Uranus', -10.67, 1000), ('Saturn', -11.08, 1000), ('Jupiter', -25.95, 1000), ('Mars', -3.77, 1000), ('Venus', -8.87, 1000), ('Mercury', -3.59, 1000), ('Sun', -274.13, 50000)]
f = 0
def ask_fuel(current_fuel):
  #ask for fuel and make sure it follows the requirements stated in homework
  accept = False
  #Run a loop until a valid input is reached
  while(accept is False):
    #First step make sure input is an integer
    f = input('Enter Units of Fuel to Use: ')
    try:
      f = int(f)
    except ValueError:
      continue
    #If it is an integer, make sure it is less than the current fuel and not negative
    if(f > current_fuel):
      print('Not enough fuel. Max fuel:', current_fuel)
      accept = False
    elif(f < 0):
      print('Cannot use negative fuel')
      accept = False
    else:
      accept = True
  return f
def play_level(name, G, unitsFuel):
  #print introduction with user inputted values
  altitude = 50
  f = 0
  go = True
  global counter
  fuelLeft = unitsFuel
  print('Landing on the', name)
  print('Gravity is', G, 'm/s^2')
  print('Initial Altitude: 50 meters')
  print('Intial Velocity: 0.00 m/s')
  print('Burning a unit of fuel causes a 0.10 m/s slowdown')
  print('Initial Fuel Level:', unitsFuel, 'units\n')
  print('GO\n')
  x = 0
  velocity = 0
  #while user wants to keep playing, run the main loop
  while (go is True):
    x += 1 #update seconds
    f = ask_fuel(fuelLeft)
    fuelLeft = fuelLeft - f #update fuel level
    velocity = velocity + G + thrusterAccel * f #update velocity
    altitude += velocity #update altitude
    #if altitude dips below 0, set it to 0 and break the while loop so user can know if they landed or crashed
    if(altitude <= 0):
      altitude = 0
      break
    #display updated values
    print('\nAfter', x, 'second(s):')
    print('Altitude:', round(altitude,2),'m')
    print('Velocity:', round(velocity,2), 'm/s')
    print('Remaining Fuel:', fuelLeft, 'units')

  if(altitude == 0 and (velocity > -2 and velocity < 2)): #if altitude reaches 0 and velocity is between -2 and 2, landed successfully
    print('Landed Successfully.')
    #counter represents the level, add one to give them access to the next level
    counter += 1
    #only 11 levels so if counter is greater than 11, user has completed the game
    if(counter == 11):
        print('You have reached the end of the Lunar Lander Simulation')
        sys.exit()
    print('Do you want to play level', counter + 1,'? (yes/no)')
    keep = input()
    #change go depending if user wants to play or not
    if(keep.lower() == 'yes'):
      go = True
    else:
      go = False
      print('You passed', counter, 'level(s)')
      sys.exit()
  #if altitude is 0 and velocity isn't between -2 and 2, user crashed
  else:
    print('Crashed')
    #Ask if they want to replay level
    print('Do you want to replay level', counter + 1,'? (yes/no)')
    keep = input()
    if(keep.lower() == 'yes'):
      go = True
    elif(keep.lower() == 'no'):
      print('You passed', counter, 'level(s)')
      go = False
      sys.exit()
    
    
#start game by asking if user wants to play level 1    
answer = input('Do you want to play level1? (yes/no)\n')
while answer.lower() == 'yes':
  #access data from the allLevels dictionary depending on counter value
  play_level(allLevels[counter][0], allLevels[counter][1], allLevels[counter][2])
if(answer.lower() == 'no'):
  sys.exit()

    
    
    
    
    
    
  