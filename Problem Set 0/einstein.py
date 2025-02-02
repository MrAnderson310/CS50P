#Take in user input and using Einsteins equation to convert into Jules
#Takes in the users input and casts it as an in
mass = int(input("enter mass in kilograms: "))
#Using the input mass we calculate the energy using Einstein's eq
energy = (mass * (300000000 ** 2))
#Print the result
print("Energy (jules):", energy)
