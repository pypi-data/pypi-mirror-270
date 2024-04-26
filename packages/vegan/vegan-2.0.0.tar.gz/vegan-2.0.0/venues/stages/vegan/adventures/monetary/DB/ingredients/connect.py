
'''	
	from vegan.adventures.monetary.DB.ingredients.connect import connect_to_ingredients
	[ driver, ingredients_DB ] = connect_to_ingredients ()
	driver.close ()
'''

'''
	from vegan.adventures.monetary.DB.ingredients.connect import connect_to_ingredients
	essential_nutrients_collection = connect_to_ingredients () ["essential_nutrients"]	
	essential_nutrients_collection.disconnect ()
'''


'''
	from vegan.adventures.monetary.DB.ingredients.connect import connect_to_ingredients
	cautionary_ingredients_collection = connect_to_ingredients () ["cautionary_ingredients"]	
	cautionary_ingredients_collection.disconnect ()
'''

from vegan._essence import receive_monetary_URL
from vegan._essence import retrieve_essence
	
import pymongo

def connect_to_ingredients ():
	essence = retrieve_essence ()
	
	ingredients_DB_name = essence ["monetary"] ["aliases"] ["ingredients"]
	
	monetary_URL = receive_monetary_URL ()

	driver = pymongo.MongoClient (monetary_URL)

	return [
		driver,
		driver [ ingredients_DB_name ]
	]