
'''
	from vegan.adventures.monetary.DB.ingredients._land.retrieve_every import retrieve_every_ingredient
	ingredients = retrieve_every_ingredient ({
		"collection": "essential_nutrients"
	})
'''

from vegan.adventures.monetary.DB.ingredients.connect import connect_to_ingredients
	
def retrieve_every_ingredient (packet):
	[ driver, ingredients_DB ] = connect_to_ingredients ()
	
	collection = ingredients_DB [ packet ["collection"] ]

	ingredients = []
	documents = collection.find ({}, {'_id': 0})
	for document in documents:
		ingredients.append (document)

	driver.close ()
	
	return ingredients;