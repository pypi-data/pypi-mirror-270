

'''
	from vegan._essence import build_essence
	build_essence ()
'''

'''
	from vegan._essence import retrieve_essence
	essence = retrieve_essence ()
'''

'''
	from vegan._essence import receive_monetary_URL
	monetary_URL = receive_monetary_URL (
		vegan_essence = vegan_essence
	)
'''


'''
	from vegan._essence import prepare_essence
	vegan_essence = prepare_essence ({
		"monetary": {
			"name": "vegan ingredients",
			"port": "39001"
		}
	})
'''

'''
	itinerary:
		[ ] harbor pid for starting and stopping:
				"PID_path": crate ("harbor/the.process_identity_number")
'''




import pathlib
from os.path import dirname, join, normpath
import sys
import os

import rich
import pydash

from .build import essence
from .build import build_essence


#
#	Use this; that way can easily
# 	start using redis or something.
#
def retrieve_essence ():
	build_essence ()
	return essence


def receive_monetary_URL (database = ""):
	if ("URL" in essence ["monetary"]):
		return essence ["monetary"] ["URL"] + database;

	return "mongodb://" + essence ["monetary"] ["host"] + ":" + essence ["monetary"] ["port"] + "/" + database;

