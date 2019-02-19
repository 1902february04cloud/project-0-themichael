#!/usr/bin/env python3

import os
import sys
import service as serv
import io1
import pickle
import error 
#--------------------------------------------------------------
#shows user homescreen
def homescreen():
	print('Welcome to Mike Banking!')
	sign = input("Type 'log in': type 'sign up': or type 'exit': ")

	if sign == 'sign up':
		#sign up returns a string for .txt placement
		x = signup()
		io1.read_write(x)
		homescreen()
	elif sign == 'log in':
		signin()
	elif sign == 'exit':
		exit()
	else:
		print('No such option')
		homescreen()
	
#----------------------------------------------------------------
#allows users to sign in

		
def signin():
	userName = input('Type User Name: ')
	userPassword = input('Type Password: ')
	#import pickle containing udername dictionary
	pickle_in = open('dict.pickle','rb')
	userId = pickle.load(pickle_in)
	#checking if user name matches password

	try:
		print(userName)
		x=userId[userName]
	except KeyError:
		print('No such username, try again.')
		signin()
	finally:
		print('')



	if userId[userName] == userPassword:
		withordeposite = input('Welcome back, would you like to view balance, withdraw or deposit?: ')
	else:
		print('WRONG USERNAME OR PASSWORD, TRY AGAIN')
		signin()
	#redirects to account balance
	if withordeposite == 'withdraw':
		serv.withdraw(userName)
	elif withordeposite == 'deposit':
		serv.deposite(userName)
	elif withordeposite == 'view balance':
		serv.viewbalance(userName)
	else:
		print('No such phrase')
		signin()
	

#---------------------------------------------------------------

#---------------------------------------------------------------


def signup():

	name = input('Enter your full name: ')
	username = input('Create a user name: ')
	try:
		error.userexists(username)
	except ValueError:
		print('Username exists, try again.')
		signup()
	password = input('Create Password: ')
	#pickle for username/password
	pickle_in = open('dict.pickle','rb')
	userId = pickle.load(pickle_in)
	userId[username] = password
	pickle_out = open('dict.pickle', 'wb')
	pickle.dump(userId, pickle_out)
	pickle_out.close()	

	#pickle for username/balance
	pickler_in = open('balance.pickle','rb')
	balance = pickle.load(pickler_in)
	balance[username] = 0.0
	pickler_out = open('balance.pickle','wb')
	pickle.dump(balance,pickler_out)
	pickle_out.close()
	info = '{}:{}:{}'.format(name,username,password)

	with open('{}.txt'.format(username),'a') as txtfile:

		view = txtfile.write('You have $0.00 in your account.\n')


	
	return info
	





