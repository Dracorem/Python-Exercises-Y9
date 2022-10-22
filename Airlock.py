# Airlock

#Input variables
from ast import While


Astronaut1 = "Commander Lorene"
Astronaut2 = "Corporal Alecks"
YesNo = "N"

#program

print(" ")
print('The inner airlock is closed and the outer airlock is open.')
print(f'Astronauts {Astronaut1} and {Astronaut2} are outside the moonbase and are walking to their moon rover')

while YesNo == 'N' or YesNo=="n":
  YesNo = input('Are they there yet" Y/N: ')
  if YesNo == "N" or YesNo == "n":
    print('They walk a little further')

YesNo = "N"

print(f'Astronauts {Astronaut1} and {Astronaut2} have climbed into their moon rover')
print('They are driving to the Helium Plant.')

while YesNo == 'N' or YesNo=="n":
  YesNo = input('Are they there yet" Y/N: ')
  if YesNo == "N" or YesNo == "n":
    print('They drive a little closer')

YesNo = "N"    

print(f'Astronauts {Astronaut1} and {Astronaut2} have arrived at the helium plant')    
print(f'{Astronaut1} falls and punctures their suit')    
print(f'{Astronaut2} looks for the spacesuit repair kit in the rover toolbox')    

while YesNo == 'N' or YesNo=="n":
  YesNo = input(f'Did {Astronaut2} find the spacesuit repair kit" Y/N: ')
  if YesNo == "N" or YesNo == "n":
    print(f'{Astronaut2} keeps looking for the repair kit.')

YesNo = "N"   

print(f'{Astronaut2} patches {Astronaut1}''s spacesuit' )    
print(f'{Astronaut2} loads {Astronaut1} and the helium canisters onto the rover and heads back to the moonbase')    

while YesNo == 'N' or YesNo=="n":
  YesNo = input(f'Have they arrived back at the Moonbase" Y/N: ')
  if YesNo == "N" or YesNo == "n":
    print('They keep driving toward the moonbase.')

YesNo = "N"   

print(f'{Astronaut2} helps {Astronaut1} into the moonbase airlock' )    
print(f'{Astronaut2} closes the airlock door and pressurises the airlock')  

while YesNo == 'N' or YesNo=="n":
  YesNo = input(f'Does the flow indicator show air movement into the airlock Y/N: ')
  if YesNo == "N" or YesNo == "n":
    print('The airlock continues to pressurise.')

YesNo = "N"   

print('The airlock is pressurised.' )    
print(f'{Astronaut2} opens the inner airlock door and enters the moonbase with {Astronaut1}')
print(f'{Astronaut2} takes {Astronaut1} to the med bay')
print('Mission complete')

