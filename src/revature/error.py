
import pickle
import os
import subprocess
def userexists(newname):

	pickle_in = open('dict.pickle','rb')
	userId = pickle.load(pickle_in)
	for key in userId:
		if key == newname:
			raise ValueError('User Name Not Available!!')
			
	


#------------------------------------------------------------------------





