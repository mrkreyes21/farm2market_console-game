# CMSC 12 PROJECT - Farm2Market Game
# Author: Mark Andrei M. Reyes
# Section: T22L
# Date: 12/15/2022
# Description: This program is a farm game wherein you can buy items, plant seeds and place livestocks on farm lot, and sell your harvests.

import pickle

# Global Variables

# Set the initial amount of money
# 5000 for farmlot; 5000 for farming items
money = 10000

# Flag to keep track of whether a farmlot has been bought or not
farmLotBought = False

# Create a dictionary to store the items and their quantities
# The items are represented as a list with the following elements:
# - The first element is the quantity of the item
# - The second element is a list with the following elements:
#   - The first element is the Unicode emoji representing the item
#   - The second element is the number of produces
#   - The third element is the name of the produce

items = {
	"Maize": [0, ["[🌽 ]", 30, "Corn"]], 
	"Pumpkin Seeds": [0, ["[🎃 ]", 4, "Pumpkin"]], 
	"Cow": [0, ["[🐮 ]", 10, "Baby Cow"]], 
	"Chicken": [0, ["[🐔 ]", 6, "Eggs"]]
}

# Create a variable to store the farm lot ID
FARM_LOT_ID = 0

# Create a dictionary to store the farm lot data
# Each farm lot will be represented as a dictionary with space block IDs as keys and crop names as values
# Add the new farm lot to the farmlot dictionary
farmlot = {
	0: [],
	1: [],
	2: [],
	3: [],
	4: [],
	5: [],
	6: [],
	7: [],
	8: [],
	9: []
}

# Imports datetime module
import datetime


# Create a dictionary to keep track of the player's harvests
# Create a dictionary to keep track of the player's harvests
# Each harvest is represented as a list with the following elements:
# - The first element is the quantity of the harvest
# - The second element is the selling value of the harvest
harvests = {
	"Corn": [0, 64],
	"Pumpkin": [0, 9.6],
	"Baby Cow": [0, 18,000],
	"Eggs": [0, 10]
}


# Import the timedelta class from the datetime module
from datetime import timedelta

# Calculate the harvest time by adding 1 minute to the current time
def harvest_time():
	return datetime.datetime.now() + timedelta(minutes=1)

print('''	

░█▀▀▀ █▀▀█ █▀▀█ █▀▄▀█ █▀█ ░█▀▄▀█ █▀▀█ █▀▀█ █─█ █▀▀ ▀▀█▀▀ 
░█▀▀▀ █▄▄█ █▄▄▀ █─▀─█ ─▄▀ ░█░█░█ █▄▄█ █▄▄▀ █▀▄ █▀▀ ──█── 
░█─── ▀──▀ ▀─▀▀ ▀───▀ █▄▄ ░█──░█ ▀──▀ ▀─▀▀ ▀─▀ ▀▀▀ ──▀──

---------------- Welcome to Farm2Market -----------------
This is a farm simulation game. You'll play the role of
a farmer in this game. You are given an initial amount
of PHP. 5,000 pesos as a budget for your farm.
''')

# Menu
# Displays the main menu and prompts the user to enter a choice
# Returns the user's choice as an integer
def menu():
	choice = int(input('''
✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶
================[Main Menu]================
✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶

 [1] Visit my farm lot
 [2] Visit item shop
 [3] Plant my seeds/Place your livestocks
 [4] Sell my farm produce
 [0] Exit game

Enter a choice: '''))
	return choice


# Item Shop; choice = 1
# Function to buy a farmlot
# Tries to buy a farmlot for the user if they don't already have one and if they have enough money
# Updates the global variables `money` and `farmLotBought`
# Returns the updated values of `money` and `farmLotBought`
def buyFarmLot():
	global money, farmLotBought
	# Check if a farmlot has already been bought
	if farmLotBought:
		print("You have already bought a farmlot. You can only buy one farmlot.")
	else:
		# Check if the user has enough money to buy a farmlot
		if money >= 5000:
			# Proceed with the purchase and update the flag
			print("You have bought a farmlot.")
			money -= 5000.00
			farmLotBought = True
		else:
			print("You don't have enough money to buy a farmlot.")

	return money, farmLotBought

# Option 1: Visit my farm lot
# Function to view the farm lot
# Prints the layout of the farm lot and allows the user to view their crops and livestock or harvest their crops
# Calls the `viewLivestock()` and `harvest()` functions as needed
# Returns nothing
def viewFarm():
	global farmlot, datetime
	if farmLotBought:
		# Print the farm lot information
		print("===Farm layout===")

		# Iterate over each element in the farmlot list
		for i in range(0, len(farmlot)):
			# If the element at index i is not an empty list,
			if farmlot[i] != []:
				# print the unique ID, farm graphic, and time remaining until harvest
				print("[ " + str(i) + " ]" + farmlot[i][2][0]+ "[" + str(farmlot[i][1]) + "]")
			else:
				# If the element at index i is an empty list, 
				# print a placeholder for the farm graphic
				print("[ " + str(i) + " ]" + "[ _ ][ _ ]")

		choice = int(input('''
		
[1] View my crops and livestocks
[2] Harvest crops and livestocks
[0] Go back to main menu
What do you want to do? '''))
			
		# Check the user's choice and take appropriate action
		if choice == 1:
			# View the user's crops and livestocks
			viewLivestock()
		elif choice == 2:
			# Harvest the user's crops and livestocks
			harvest()
		elif choice == 0: 
			# Return to the main menu
			return
		else:
			# If the user enters an invalid choice, print an error message
			print("Invalid choice!")
	else:
		# If the user hasn't bought a farm layout, print an error message
		print("No farm layout here!")

		# Prompt the user to enter their choice
		choice = int(input('''

[0] Go back to main menu
What do you want to do? '''))

		# Check the user's choice and take appropriate action
		if choice == 0: 
			# Return to the main menu
			return
		else:
			# If the user enters an invalid choice, print an error message
			print("Invalid choice!")

# Option 3: Plant Seeds
# Allow the user to plant crops and place livestocks in a space block in their farm.
def plantCrops(farmlot):
	
	# Check if the farm lot has been bought
	if farmLotBought:
		# Ask the user for the space block ID
		block_id = int(input("Enter the space block ID: "))

		#  Check if the space block exists in the farm lot
		if block_id in farmlot:
			# Check if the space block is empty
			if farmlot[block_id] == []:
				# Print the player's inventory
				print("Available Items:")
				for crop, quantity in items.items():
					print(f"{crop}: {quantity[0]}")

				# Ask the user which crop they want to plant/ livestock to place
				name = input("Enter the name of the crop you want to plant: ")

				# Check if the crop exists in the items dictionary
				if name in items:
					# Check if the quantity of the selected crop/livestock is greater than 0
					if items[name][0] > 0:
						# Update the items dictionary to keep track of the crops/livestock that have been planted/ placed
						items[name][0] -= 1

						# Update the farm lot with the new crop/livetstock
						farmlot[block_id] = [name, harvest_time(), items[name][1]]

						# Print a success message
						print(f"{name} was successfully planted in space block {block_id}!")
					else:
						# If the player does not have any crops/livestocks
						print("You haven't bought anything yet!")
				else:
						# If the crop does not exist in the items dictionary, print an error message
						print(f"{name} is not a valid crop!")
			else:
				# If the space block is not empty, print an error message
				print(f"Space block {block_id} is not empty!")
		else:
			# If the space block does not exist, print an error message
			print(f"Space block {block_id} does not exist in farm lot!")

	else:
		# If the farm lot does not exist, print an error message
		print(f"Farm lot does not exist!")

# View Farm: [1] View my crops and livestocks
# Define the viewLivestock() function
def viewLivestock():
	# Print the livestock/crops information
	print("===Livestock & Crops===")
	print(f"Maize: {str(items['Maize'][0])}")
	print(f"Pumpkin: {str(items['Pumpkin Seeds'][0])}")
	print(f"Cows: {str(items['Cow'][0])}")
	print(f"Chickens: {str(items['Chicken'][0])}")

# View Farm: [2] Harvest crops and livestocks
# Define the harvest() function
def harvest():
	global farmlot
	# Ask the player which space block they want to harvest
	block_id = int(input("Enter the space block you want to harvest: "))
	# Check if the player has entered a valid space block number
	if block_id in farmlot:
		# If the player has entered a valid space block number
		if farmlot[block_id] == []: 
			# If the space block is empty, print an error message
			print("The space block is empty")
			return
		if not (farmlot[block_id][1] <= datetime.datetime.now()):
			# If the space block is not ready for harvesting, print an error message
			print("It is not ready for harvesting.")
			return
		# If the space block is ready for harvesting, print a success message
		print(f"Space block {block_id} was successfully harvested!")
		# Update the harvests dictionary with the harvested item
		# Increment the value of the harvested crop in the harvests dictionary
		harvests[farmlot[block_id][2][2]][0] += farmlot[block_id][2][1]
		farmlot[block_id] = []
		# Calls the function that prints the inventory of harvested items
		harvested()
	else:
		# If the player has entered an invalid space block number, print an error message
		print(f"Space block {block_id} does not exist!")

def harvested():
# Print the inventory of harvested items
	for item, quantity in harvests.items():
		# Check if the quantity of the harvested item is greater than 0
		if quantity[0] > 0:
			# Print the heading and the name and quantity of the harvested item
			print("Available produces:")
			print(f"{item}: {str(quantity[0])}")


# Option 2: Item Shop
# simulates a store where a player can buy different items such as farm lot, maize, pumpkin seeds, cow, and chicken.
def itemShop():
	# Add the global keyword to allow the function to access the global variable
	global money

	# Print the welcome message and the player's current money
	print('''    
✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶
----------Welcome to the Item Shop---------
✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶
''')
	print("Your wallet is: ", money)

	num = int(input('''
1. Buy 10 Farm Lot @5000.00
2. Buy 6 Maize @80.00
3. Buy Pumpkin Seeds @12.00
4. Buy Cow @20000.00
5. Buy Chicken @1000.00
0. Go back to Main Menu

What do you want to buy?: ''')) 
	# Check the user's input
	if num == 1:
		# If the user wants to buy Farm Lot
		buyFarmLot()
	elif num == 2:
		maize_cost = 80
		if money >= maize_cost:       
			# If they have enough money, subtract the cost of the 6 maize from their money
			money -= maize_cost
			# Increment the quantity of the maize in the items dictionary
			items["Maize"][0] += 6
			# Print a message to the player
			print("You bought 6 Maize")
		else:
			print("Your money is not enough!")
	elif num == 3:
		pumpkin_cost = 12
		if money >= pumpkin_cost:       
			# If they have enough money, subtract the cost of the 6 pumpkin from their money
			money -= pumpkin_cost
			# Increment the quantity of the pumpkin in the items dictionary
			items["Pumpkin Seeds"][0]  += 6
			# Print a message to the player
			print("You bought 6 Pumpkin Seeds")
		else:
			print("Your money is not enough!")
	elif num == 4:
		cow_cost = 20000
		if money >= cow_cost:       
			# If they have enough money, subtract the cost of the cow from their money
			money -= cow_cost
			# Increment the quantity of the cow in the items dictionary
			items["Cow"][0]  += 1
			# Print a message to the player
			print("You bought a Cow")
		else:
			print("Your money is not enough!")
	elif num == 5:
		chicken_cost = 1000
		if money >= chicken_cost:       
			# If they have enough money, subtract the cost of the chicken from their money
			money -= chicken_cost
			# Increment the quantity of the chicken in the items dictionary
			items["Chicken"][0]  += 1
			# Print a message to the player
			print("You bought a Chicken")
		else:
			print("Your money is not enough!")
	elif num == 0:
		# Use the imported function
		return
	else:
		# If the user enters an invalid item number, the code prints a "no item" message and bring back the user to the itemShop
		print("No item")
		return

# Function to sell items
def sellItem():
	# Add the global keyword to allow the function to access the global variable
	global money
	# Print the items available by calling the harvested function
	harvested()
	# Ask the player which item they want to sell
	item = str(input("What do you want to sell? "))
	# Ask the player how many items they want to sell
	quantity = int(input("How many do you want to sell? "))
	
	# If the player doesn't have the item, print an error message
	if item in harvests: #if the input name exists in harvest continue if not, skip function 
		if harvests[item][0] < quantity: #skip function iff quantity is greater than what you have
			print("You do not have that much to sell!")
			return
	else: 
		print("Invalid Item!")
		return
	# If they have the item...
	# # Calculate the selling price by multiplying the quantity and selling price of the item
	sold = harvests[item][1] * quantity
	# Add the selling price to the player's money
	money += sold
	# Decrement the quantity of the item in the harvest inventory
	harvests[item][0] -= quantity
	# Print a message to the player
	# Print the quantity, item and selling price of the item sold
	print("You sold", str(quantity) + " " + item + " " + " for ", sold)

# Define a function to save the game data to a file
def saveGame(money, farmLotBought, items, FARM_LOT_ID, farmlot, harvests):
	# Open the file in binary mode
	fh = open("data.dat", "wb")

	# Use the pickle.dump() method to serialize and save the variables
	pickle.dump(money, fh)
	pickle.dump(farmLotBought, fh)
	pickle.dump(items, fh)
	pickle.dump(FARM_LOT_ID, fh)
	pickle.dump(farmlot, fh)
	pickle.dump(harvests, fh)

	# Close the file
	fh.close()

# Define a function to load the game data from a file
def loadGame():
	global money, farmLotBought, items, FARM_LOT_ID, farmlot, harvests
	# Open the file in binary mode
	fh = open("data.dat", "rb")

	# Use the pickle.load() method to deserialize and load the variables
	money = pickle.load(fh)
	farmLotBought = pickle.load(fh)
	items = pickle.log(fh)
	FARM_LOT_ID = pickle.load(fh)
	farmlot = pickle.load (fh)
	harvests = pickle.load

# Menu
# This is the main menu of the game. 
# The while loop continues to run until the player enters 0 (to exit the game).
# The code asks the player to enter a number (1, 2, 3, 4, or 0) to choose an option from the menu.
# Depending on the number the player enters, the code runs the corresponding function: viewFarm(), itemShop(), plantCrops(farmlot), or sellItem().
# Depending on the number the player enters, the code runs the corresponding function: viewFarm(), itemShop(), plantCrops(farmlot), or sellItem().
while True:
	print()
	choice = menu()
	if (choice == 1):
		viewFarm()
	elif (choice == 2):
		itemShop()
	elif (choice == 3):
		plantCrops(farmlot)
	elif (choice == 6):
		saveGame(money, farmLotBought, items, FARM_LOT_ID, farmlot, harvests)
	elif (choice == 0):
		print('''
				█████▀█████████████████████████████████████
				█─▄▄▄▄█─▄▄─█─▄▄─█▄─▄▄▀█▄─▄─▀█▄─█─▄█▄─▄▄─█░█
				█─██▄─█─██─█─██─██─██─██─▄─▀██▄─▄███─▄█▀█▄█
				▀▄▄▄▄▄▀▄▄▄▄▀▄▄▄▄▀▄▄▄▄▀▀▄▄▄▄▀▀▀▄▄▄▀▀▄▄▄▄▄▀▄▀''') #Exit Game
		break
	else:
		print("Invalid") #if the number entered is not 0, 1, 2, 3, and 4
	print()
