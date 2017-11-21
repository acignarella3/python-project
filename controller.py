from view import View
from model import Bank

display = View()

bank = Bank()

bank.create_tables()

access = True

user_id = ""

while access:

	login = False
	user_menu = True

	while user_menu:

		user_choice = display.printUserMenu()

		if user_choice == "1":
			username = display.takeInput("Enter a username: ")
			password = display.takeInput("Enter a password: ")

			result = bank.createUser(username, password)

			if result:
				user_id = username
				login = True
				user_menu = False

		elif user_choice == "2":
			username = display.takeInput("Enter a username: ")
			password = display.takeInput("Enter a password: ")

			result = bank.checkUser(username, password)

			if result:
				user_id = username
				login = True
				user_menu = False

		elif user_choice == "3":
			user_menu = False
			access = False

		else:
			display.printOut("Please try again")

	if login:

		bank_menu = True

		while bank_menu:
		
			bank_choice = display.printAccountMenu()

			if bank_choice == "1":
				money = display.takeInput("Enter the amount of money to deposit: ")

				account = display.printAccountChoices()

				if account == "1":
					bank.depositMoneyIntoChecking(user_id, int(money))
				elif account == "2":
					bank.depositMoneyIntoSavings(user_id, int(money))
				else:
					display.printOut("Sorry, could not complete")

			elif bank_choice == "2":
				money = display.takeInput("Enter the amount of money to withdraw: ")

				account = display.printAccountChoices()

				if account == "1":
					bank.withdrawMoneyFromChecking(user_id, int(money))
				elif account == "2":
					bank.withdrawMoneyFromSavings(user_id, int(money))
				else:
					display.printOut("Sorry, could not complete")

			elif bank_choice == "3":
				bank.printAccountInformation(user_id)

			elif bank_choice == "4":
				pass

			elif bank_choice == "5":
				user_id = ""
				login = False
				user_menu = True
				bank_menu = False

			else:
				display.printOut("Please try again")

