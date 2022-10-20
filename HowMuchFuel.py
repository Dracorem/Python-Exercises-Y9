# How Much Petrol and What Cost

#Input variables
model = ""
KmPL = 0
AverageSpeed = 0
HoursDriving = 0
CostOfPetrol = 0

# Output variables
KilometersTravelled = 0
LitresPetrolUsed = 0
TotalCostPetrol = 0

#program
print('Inputs:')
model = input('Model of car: ')
KmPL = float(input('How many kilometres does the car go on a litre: '))
AverageSpeed = float(input('Average speed in kmph for journey: '))
HoursDriving = float(input('How many hours driving: '))
CostOfPetrol = float(input('Cost of petrol per litre (in cents): '))

#Calculations
KilometersTravelled = AverageSpeed*HoursDriving
LitresPetrolUsed = KilometersTravelled/ KmPL
TotalCostPetrol = LitresPetrolUsed *CostOfPetrol/100
TotalCostPetrol = round(TotalCostPetrol, 2)

print(" ")
print('Outputs:')
print(f'Driving your {model} car for {HoursDriving} hours at {AverageSpeed} kmph: ')
print(" ")
print(f'Kilometers travelled: {KilometersTravelled} km')
print(f'Petrol used: {LitresPetrolUsed} L')
print(f'Cost of petrol: ${TotalCostPetrol}')