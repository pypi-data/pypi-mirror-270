

'''
	from vegan._ops.status import check_status
	check_status ()
'''


from vegan._essence import retrieve_essence

from vegan.adventures.sanique._ops.status import check_sanique_status
from vegan.adventures.monetary._ops.status import check_monetary_status
	

import rich

def check_status ():	
	essence = retrieve_essence ()

	the_monetary_status = ""
	if ("onsite" in essence ["monetary"]):
		the_monetary_status = check_monetary_status ()
		
	the_sanic_status = check_sanique_status ()
	
	the_status = {
		"monetary": {
			"local": the_monetary_status
		},
		"sanique": {
			"local": the_sanic_status
		}
	}
	
	rich.print_json (data = {
		"statuses": the_status
	})
	
	return the_status