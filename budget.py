import time
income_total = 0
outgoings_total = 0

def finalcalculation():
	time.sleep(0.5)
	global income_total
	global outgoings_total
	calcFinal = (income_total - outgoings_total)
	print("Based on what you've told us, your surplus each month is: " + str(calcFinal) + ".")
	time.sleep(0.5)
	print("Start new calculation?")
	finalCalcChoice = input("Y/N: ")

	if finalCalcChoice == "Y":
		income_total = 0
		outgoings_total = 0
		incomecalculator()

	elif finalCalcChoice == "N":
		exit()

	else:
		print("Invalid input.")


def outgoingcalculator():
	time.sleep(0.5)
	global outgoings_total
	outgoings_rent = input("Enter your monthly rent (not mortgage) here: ")
	outgoings_mortgage = input("Enter your mortgage payment(s) here: ")
	outgoings_car = input("Enter monthly car payments here: ")
	outgoings_leisure = input("Enter monthly leisure spend here: ")
	outgoings_debts = input("Enter monthly debt repayments here: ")
	outgoings_total = float(outgoings_rent) + float(outgoings_mortgage) + float(outgoings_car) + float(outgoings_leisure) + float(outgoings_debts)
	print("Your outgoings are: " + str(outgoings_total) + ". Correct?")

	outgoChoice = input("Y/N: ")
	if outgoChoice == "Y":
		finalcalculation()
	elif incomeChoice == "N":
		outgoingcalculator()
	else:
		print("Invalid input")

def incomecalculator():
	time.sleep(0.5)
	global income_total
	income_salary = input("Enter monthly income from work: ")
	income_benefits = input("Enter monthly income from benefits: ")
	income_other = input("Enter any other income here: ")
	income_total = (float(income_salary)) + (float(income_benefits)) + (float(income_other))
	print("Your income is: " + str(income_total) + ". Correct?")

	incomeChoice = input("Y/N: ")
	if incomeChoice == "Y":
		outgoingcalculator()
	elif incomeChoice == "N":
		incomecalculator()
	else:
		print("Invalid input")

#First stage of script - basic input.
print("""Welcome to OLDBUDGET. This is an old-school budget calculator.

	Enter Y to continue.""")

ob_menu_choice = input("Input: ")
if ob_menu_choice == "Y" or "y":
	incomecalculator()
else:
	print("Invalid input.")

