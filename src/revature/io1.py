import os
import sys

#---------------------------------------------------------------------
# this writes the user info into user_storage.txt
def read_write(func):

	with open('user_storage.txt', 'a+') as fff:
		fff.write('\n{}'.format(func))
		#fff.seek(0)
#---------------------------------------------------------------------	
		












