# A ideia é fazer um programa que calcule a conta que cada um deve pagar em uma conta de restaurante

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

# Então vamos fazer o valor total, ou seja, conta + gorjeta e depois dividir pelo numéro de pessoas..
print(f'Each person should pay: {round((bill+bill*(tip/100))/people, 2)}')