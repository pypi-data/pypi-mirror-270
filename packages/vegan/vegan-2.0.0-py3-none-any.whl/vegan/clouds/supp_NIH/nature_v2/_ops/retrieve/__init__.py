
'''
	from vegan.clouds.food_USDA.nature_v2._ops.retrieve import retrieve_parsed_USDA_food
	out_packet = retrieve_parsed_USDA_food ({
		"DSLD_ID": 1,
		"NIH API Pass": ""
	})
'''

#----
#
import vegan.clouds.supp_NIH.deliveries.one as NIH_API_one
import vegan.clouds.supp_NIH.nature_v2 as supp_NIH_nature_v2
#
import law_dictionary
#
#----

'''
	supplement = NIH_API_one.find (
		dsld_id,
		api_key
	)
	
	NIH_supplement_data = supplement ["data"]
	NIH_supplement_source = supplement ["source"]
'''

def retrieve_parsed_USDA_food (packet):
	'''
		law_dictionary
	'''
	report = law_dictionary.check (	
		return_obstacle_if_not_legit = True,
		allow_extra_fields = False,
		laws = {
			"DSLD_ID": {
				"required": True,
				"type": str
			},
			"NIH API Pass": {
				"required": True,
				"type": str
			}
		},
		dictionary = packet
	)
	if (report ["advance"] != True):
		return {
			"anomaly": report ["obstacle"]
		}

	
	DSLD_ID = packet ["DSLD_ID"]
	NIH_API_Pass = packet ["NIH API Pass"]
	
	
	
	'''
		API Ask
	'''
	try:
		print ('supp_NIH parse?')
	
		supp_NIH = NIH_API_one.find (
			DSLD_ID = DSLD_ID,
			api_key = NIH_API_Pass
		)
	except Exception as E:
		try:
			exc_msg = str (E)
			print ("exception message:", exc_msg)
			
			if (exc_msg == "The USDA API returned status code 404."):
				return {
					"anomaly": "The USDA API could not find that FDC_ID."
				}
			
			exc_type = type (E).__name__
			print ("exception type:", exc_type)
			
			exc_traceback = sys.exc_info () [2]
	
		except Exception as E2:
			pass;
		
		return {
			"anomaly": "The food could not be retrieved from the USDA API."
		}
		
		
	try:
		nature = food_USDA_nature_v2.create (food_USDA ["data"])
		return nature
		
	except Exception as E:
		print ("exception:", E)
	
		return {
			"anomaly": "The food could not be parsed."
		}
	
	return {
		"anomaly": "An unaccouted for anomaly occurred while parsing and retrieving the food data."
	}