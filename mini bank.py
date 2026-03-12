balance = 1000
correct_pin = 9089

print("Welcome in mini banking system\nChoose otion:")

while True:
	print("choose a option what you want:\n1.deposit\n2.Withdraw\n3.check Reamaing balance\n4.Exit")
	choice = input("Enter your option:")
	
	if choice == "1":
		depo = int(input("Enter your deposit amount:"))
		balance += depo
		print("your amount is deposit\nYour reamaning balance is", balance)
		
	elif choice == "2":
		pin = int(input("Enter your pin number:"))
		if pin == correct_pin:

			wit = int(input("Enter your withdraw amount:"))
			if wit > balance:
				print("insufficent balance")
				
			else:
				balance -= wit
				print("your amount is withdraw sucessfully")
				

	elif choice == "3":
		print("your reamaning balance is", balance)
		
	elif choice == "4":
		print("thank you for using mini bank system")
		break
		
	else:
		print("")

