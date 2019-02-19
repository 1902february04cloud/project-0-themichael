import os
import sys
import pickle
import error
import controller as cont

'''
This is where all the service functions go.

--withdraw
--deposite
-balance
-pickle
'''
#--------------------------------------------------------------------
# lets user withdraw money. wont let him go into the negatives
def withdraw(userName):
	
	amount = input('How much money would you like to withdraw? $')
	pickle_in = open('balance.pickle','rb')
	balance = pickle.load(pickle_in)
	
	try:
		amount = float(amount)
	except ValueError:
		print('not a cash value')
		withdraw(userName)
	if balance[userName] - amount < 0:
		print('Not enough money in account')
		withdraw(userName)
	else:
		balance[userName] = balance[userName] - amount


	

	with open('{}.txt'.format(userName),'a+') as txtfile:
		txtfile.write('{} withdrawn from account. Total amount left: {}\n'.format(amount,balance[userName]))


	pickle_out = open('balance.pickle','wb')
	pickle.dump(balance,pickle_out)
	pickle_out.close()

	whattodo = input('Would you like to view balance or log out?: ')
	if whattodo == 'view balance':
		viewbalance(userName)
	elif whattodo == 'log out':
		cont.homescreen()
	else:
		print('No such option, ')
		viewbalance(userName)
	 	
#--------------------------------------------------------------------
# lets user deposite money. 
def deposite(userName):
	amount = input('How much would you like to deposit?: $')
	
	try:
		amount = float(amount)
	except ValueError:
		print('not a cash value')
		deposite(userName)
	pickle_in = open('balance.pickle','rb')
	balance = pickle.load(pickle_in)
	balance[userName] = amount +  balance[userName]
	print(balance[userName])
	

	with open('{}.txt'.format(userName),'a+') as txtfile:
		txtfile.write('{} deposited into your acount. Total amount: {}\n'.format(amount,balance[userName]))
		
	with open('{}.txt'.format(userName),'r') as textfile:
		view = textfile.read()
		print('Transaction History:', view)

	pickle_out = open('balance.pickle','wb')
	pickle.dump(balance,pickle_out)
	pickle_out.close()

	whattodo = input('Would you like to withdraw, deposit, or log out?: ')
	if whattodo == 'withdraw':
		withdraw(userName)
	elif whattodo == 'deposit':
		deposite(userName)
	elif whattodo == 'log out':
		cont.homescreen()
	else:
		print('Not an option, try again....')
		deposit(userName)
		
#-------------------------------------------------------------------
#lets users view there balance and acount history
def viewbalance(userName):
	#gets users balance file
	with open('{}.txt'.format(userName)) as txtfile:
		view = txtfile.read()
		print('Transaction History:', view)
	
	whattodo = input('Would you like to withdraw, deposit, or log out?: ')
	#checks input
	if whattodo == 'withdraw':
		withdraw(userName)
	elif whattodo == 'deposit':
		deposite(userName)
	elif whattodo == 'log out':
		cont.homescreen()
	else:
		print('No such option, try again')
		viewbalance(userName)
		





#--------------------------------------------------------------------



	 

#pickle creation
#resets username and password pickle
def create_pickle():
	userId = {}
	pickle_out = open('dict.pickle','wb')
	pickle.dump(userId,pickle_out)
	pickle_out.close()
#resets username and amount pickle
def user_pickle_creation():
	balance = {}
	pickle_out = open('balance.pickle','wb')
	pickle.dump(balance,pickle_out)
	pickle_out.close()





