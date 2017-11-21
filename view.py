class View:

	def printOut(self, output):
		print(output)

	def takeInput(self, prompt):
		return input(prompt)

	def printUserMenu(self):
		print("1. Create a new account")
		print("2. Login to existing account")
		print("3. Exit")
		return input("Enter a menu option: ")

	def printAccountMenu(self):
		print("1. Withdraw money")
		print("2. Deposit money")
		print("3. Get account information")
		print("4. Transfer money to another account")
		print("5. Exit")
		return input("Enter a menu option: ")

	def printAccountChoices(self):
		print("1. Checking")
		print("2. Savings")
		return input("Select an account: ")