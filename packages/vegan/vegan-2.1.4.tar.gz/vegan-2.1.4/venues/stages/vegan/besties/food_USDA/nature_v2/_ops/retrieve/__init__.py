
'''
	from vegan.besties.food_USDA.nature_v2._ops.retrieve import retrieve_parsed_USDA_food
	out_packet = retrieve_parsed_USDA_food ({
		"USDA API Pass": 
		
		"FDC_ID": 1		
	})
'''

#----
#
import vegan.besties.food_USDA.deliveries.one as retrieve_1_food
import vegan.besties.food_USDA.nature_v2 as food_USDA_nature_v2
#
import law_dictionary
#
#----

def retrieve_parsed_USDA_food (packet):
	'''
		law_dictionary
	'''
	report = law_dictionary.check (	
		return_obstacle_if_not_legit = True,
		allow_extra_fields = False,
		laws = {
			"FDC_ID": {
				"required": True,
				"type": str
			},
			"USDA API Pass": {
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

	
	FDC_ID = packet ["FDC_ID"]
	USDA_API_Pass = packet ["USDA API Pass"]
	

	try:
		print ('food_USDA parse?')
	
		food_USDA = retrieve_1_food.presently (
			FDC_ID = FDC_ID,
			API_ellipse = USDA_API_Pass
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