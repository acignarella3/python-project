import sqlite3

class Bank:

	def __init__(self):
		self.connection = sqlite3.connect("bank.db")
		self.cursor = self.connection.cursor()

	def create_tables(self):

		self.cursor.execute("""CREATE TABLE user(
			username VARCHAR(256) PRIMARY KEY,
			password VARCHAR(256))""")

		self.cursor.execute("""CREATE TABLE checking_account(
			id INTEGER PRIMARY KEY,
			user_id VARCHAR(256),
			account_number VARCHAR(256),
			balance INTEGER DEFAULT 0,
			FOREIGN KEY (user_id) REFERENCES user(username))""")

		self.cursor.execute("""CREATE TABLE savings_account(
			id INTEGER PRIMARY KEY,
			user_id VARCHAR(256),
			account_number VARCHAR(256),
			balance INTEGER DEFAULT 0,
			FOREIGN KEY (user_id) REFERENCES user(username))""")

		self.connection.commit()

	def createUser(self, username, password):

		self.cursor.execute("""SELECT * FROM user WHERE username = ?""", (username,))

		user = self.cursor.fetchone()

		#print(user)

		if user != None and user[0] == username:

			print("Sorry, this username is already in use")
			return False

		else:

			checking = input("Enter a checking account number: ")
			savings = input("Enter a savings account number: ")

			self.cursor.execute("""INSERT INTO user(username, password) VALUES (?, ?)""", (username, password))
			self.cursor.execute("""INSERT INTO checking_account(user_id, account_number, balance) VALUES (?, ?, ?)""", (username, checking, 0))
			self.cursor.execute("""INSERT INTO savings_account(user_id, account_number, balance) VALUES (?, ?, ?)""", (username, savings, 0))
			self.connection.commit()
			return True


	def checkUser(self, username, password):
		self.cursor.execute("""SELECT * FROM user WHERE username = ?""", (username,))

		user = self.cursor.fetchone()

		self.connection.commit()

		if user == None:
			print("Sorry, this user is not registered")
			return False

		else:

			print(user)
			print(user[0])
			print(user[1])

			if user[0] == username and user[1] == password:
				return True
			else:
				print("Sorry, this username and password combination is incorrect")
				return False

	def depositMoneyIntoChecking(self, username, amount):
		self.cursor.execute("""UPDATE checking_account SET balance = balance + ? WHERE user_id = ?""", (amount, username))
		self.connection.commit()

	def depositMoneyIntoSavings(self, username, amount):
		self.cursor.execute("""UPDATE savings_account SET balance = balance + ? WHERE user_id = ?""", (amount, username))
		self.connection.commit()

	def withdrawMoneyFromChecking(self, username, amount):
		self.cursor.execute("""SELECT * FROM checking_account WHERE user_id = ?""", (username,))

		account = self.cursor.fetchone()

		if (amount > account[3]):
			print("Sorry, we can't withdraw as much as you want, but we will empty your account")
			amount = account[3]

		self.cursor.execute("""UPDATE checking_account SET balance = balance - ? WHERE user_id = ?""", (amount, username))

		self.connection.commit()

	def withdrawMoneyFromSavings(self, username, amount):
		self.cursor.execute("""SELECT * FROM savings_account WHERE user_id = ?""", (username,))

		account = self.cursor.fetchone()

		if (amount > account[3]):
			print("Sorry, we can't withdraw as much as you want, but we will empty your account")
			amount = account[3]

		self.cursor.execute("""UPDATE savings_account SET balance = balance - ? WHERE user_id = ?""", (amount, username))

		self.connection.commit()

	def printAccountInformation(self, username):

		self.cursor.execute("""SELECT * FROM checking_account WHERE user_id = ?""", (username,))

		checking = self.cursor.fetchone()

		print("Checking Account #: " + checking[2])
		print("Checking Account Balance: " + str(checking[3]))

		self.cursor.execute("""SELECT * FROM savings_account WHERE user_id = ?""", (username,))

		savings = self.cursor.fetchone()

		print("Savings Account #: " + savings[2])
		print("Savings Account Balance: " + str(savings[3]))

	def close_connection(self):
		self.connection.close()