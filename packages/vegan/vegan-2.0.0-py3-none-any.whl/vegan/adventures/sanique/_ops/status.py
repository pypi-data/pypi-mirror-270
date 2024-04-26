
'''
	sanic inspect shutdown
'''

'''	
	from vegan.adventures.sanique._ops.status import check_sanique_status
	the_sanic_status = check_sanique_status ()
'''


	

#----
#
from vegan._essence import retrieve_essence
from ..utilities.has_sanic_check import has_sanic_check
#
#
from biotech.topics.show.variable import show_variable
#
#
import requests
import rich
#
#
import multiprocessing
import subprocess
import time
import os
import atexit
#
#----

def background (procedure, CWD):
	print ("procedure:", procedure)
	process = subprocess.Popen (procedure, cwd = CWD)


def check_sanique_status (packet = {}):
	essence = retrieve_essence ()
	record_level = essence ["record_level"]

	has_sanic_check ()

	host = essence ["sanique"] ["inspector"] ["host"]
	port = essence ["sanique"] ["inspector"] ["port"]
	URL = f"http://{ host }:{ port }"
	
	try:
		response = requests.get (URL)
		if response.status_code == 200:
			data = response.json ()
			
			#if (record_level >= 4):
			show_variable ({
				"sanique seems to be on": {
					"inspector URL": URL,
					"status": data
				}
				
			})
			
			return "on"
		
		else:
			print ("Error:", response.status_code)
	
	except Exception as E:
		print ("exception:", E)

	return "off"