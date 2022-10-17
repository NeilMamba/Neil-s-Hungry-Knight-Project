#Name: Neil Cleare Jr
# Class Name: CS 230
# Due Date: Tue, January 24th, 2022
## @description In this assignment I will be developing a program to carry out the registration..
## process for the King's hungry knights. Because I know i will get my coin returned, my humble...
## quest is to politely take the knight's orders and to avoid letting what happened to the...
## Prancing Pony happen to the Hungry Knight Inn and Tavern.

print("Welcome fellow lads and lasses to the Hungry Knight Inn!")

name = input("What is your name? ")
characteristic = input("What is your characteristic? ")

print("Hello Sir " + name + " The " + characteristic)   #spaces are important in between quotations for readability
print("Welcome to The Hungry Knight Inn ")

#Prompt the user to enter the number of Roast Pheasant plates, bowls of Beef Stew, loafs of fine
#bread, and pieces of fine fruit that the Hungry Knight consumes and store the values for each of
#these quantities in appropriately named variables.

roast_pheasant_plates = int()
beef_stew_plates = int()
bread_plates = int()
fruit_plates = int()

roast_pheasant = float()
beef_stew = float()
bread = float()
fruit = float()

roast_pheasant = float(15.10)
beef_stew = float(3.49)
bread = float(5.17)
fruit = float(1.19)
#total for 1 of each is 24.95 tax is 1.2475

roast_pheasant_plates = int(input('Enter how many plates of roast pheasant:'))
beef_stew_plates = int(input('Enter how many plates of beef stew:'))
fruit_plates = int(input('Enter how many plates of fruit:'))
bread_plates = int(input('Enter how many plates of bread:'))



print('you said you want these many plates of beef stew:', beef_stew_plates)
print('you said you want these many plates of bread:', bread_plates)
print('you said you want these many plates of fruit:', fruit_plates)
print('you said you want these many pheasant plates:', roast_pheasant_plates)

total = ((roast_pheasant_plates * 15.10) + (beef_stew_plates * 3.49) + (fruit_plates * 1.19) + (bread_plates * 5.17)) #formula for total

print('Your subtotal is: ', total ) # must include total after statement
round(total) #rounds total

print('Your final cost is')

tax = (total * 0.05) #multiplying total for tax

value = float(input(total + tax))

final_cost = value - (value + tax)
print(float(final_cost, 2)) #print(round(final_cost,2)) did same thing

print(f'total: {total: .2f} total')











