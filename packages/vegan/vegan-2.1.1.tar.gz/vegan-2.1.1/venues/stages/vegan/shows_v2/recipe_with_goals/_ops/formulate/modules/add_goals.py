



#----
#
import vegan.measures.number.decimal.reduce as reduce_decimal
#
from .find_goal import find_goal
#
#
import ships.modules.exceptions.parse as parse_exception
from ships.flow.simultaneous_v2 import simultaneously_v2
#
#
import rich
#
#
import time
from fractions import Fraction
import copy
#
#----

'''
	returns:
		skipped_composition
		goal not found for
'''
def add_goals (packet):
	recipe = packet ["recipe"]
	essential_nutrients_grove = packet ["essential_nutrients_grove"]
	goal_region = packet ["goal_region"]
	records = packet ["records"]
	
	return_packet = {
		"goal not found for": [],
		"skipped_composition": []
	}
	
	def move (ingredient):
		print ("move")
	
		assert ("info" in ingredient), ingredient
		assert ("names" in ingredient ["info"]), ingredient
	
		ingredient_names = ingredient ["info"] ["names"]
		ingredient ["goal"] = {}
		
		goal = None;
		try:
			goal = find_goal ({
				"ingredient_names": ingredient_names,
				"goal_region": goal_region
			})
		except Exception as E:	
			if (records >= 1): print (parse_exception.now (E))
			return_packet ["goal not found for"].append (ingredient_names)
			return;
		
		
		#
		#	grams:
		#
		#	
		try:
			if ("mass + mass equivalents" in ingredient ["measures"]):			
				grams_per_recipe = (
					ingredient ["measures"] ["mass + mass equivalents"] ["per recipe"] ["grams"] ["fraction string"]
				)
				grams_per_goal = (
					goal ["goal"] ["mass + mass equivalents"] ["per Earth day"] ["grams"] ["fraction string"]
				)
				goal_per_day = (
					Fraction (grams_per_recipe) / 
					Fraction (grams_per_goal)
				)
				
				decimal_string = "?"
				try:
					decimal_string = str (reduce_decimal.start (goal_per_day, partial_size = 3));
				except Exception:
					pass;
				
				ingredient ["goal"] = {
					"days of ingredient": {
						"mass + mass equivalents": {
							"per recipe": {
								"fraction string": str (goal_per_day),
								"decimal string": decimal_string
							}
						}
					}
				}
	
			
		except Exception as E:
			if (records >= 1): print (parse_exception.now (E))
			return_packet ["skipped_composition"].append (ingredient_names)
			pass;
			
		
		if ("unites" in ingredient):				
			add_goals_to_recipe (ingredient ["unites"])

	def add_goals_to_recipe (the_grove):
		print ("add_goals_to_recipe")
	
		simultaneously_v2 (
			items = the_grove,
			capacity = 10,
			move = move
		)
	
	
	'''
	def add_goals_to_recipe (the_grove):		
		for ingredient in the_grove:
			assert ("info" in ingredient), ingredient
			assert ("names" in ingredient ["info"]), ingredient
		
			ingredient_names = ingredient ["info"] ["names"]
			ingredient ["goal"] = {}
			
			goal = None;
			try:
				goal = find_goal ({
					"ingredient_names": ingredient_names,
					"goal_region": goal_region
				})
			except Exception as E:	
				if (records >= 1): print (parse_exception.now (E))
				return_packet ["goal not found for"].append (ingredient_names)
				continue;
			
			
			#
			#	grams:
			#
			#	
			try:
				if ("mass + mass equivalents" in ingredient ["measures"]):			
					grams_per_recipe = (
						ingredient ["measures"] ["mass + mass equivalents"] ["per recipe"] ["grams"] ["fraction string"]
					)
					grams_per_goal = (
						goal ["goal"] ["mass + mass equivalents"] ["per Earth day"] ["grams"] ["fraction string"]
					)
					goal_per_day = (
						Fraction (grams_per_recipe) / 
						Fraction (grams_per_goal)
					)
					
					decimal_string = "?"
					try:
						decimal_string = str (reduce_decimal.start (goal_per_day, partial_size = 3));
					except Exception:
						pass;
					
					ingredient ["goal"] = {
						"days of ingredient": {
							"mass + mass equivalents": {
								"per recipe": {
									"fraction string": str (goal_per_day),
									"decimal string": decimal_string
								}
							}
						}
					}
		
				
			except Exception as E:
				if (records >= 1): print (parse_exception.now (E))
				return_packet ["skipped_composition"].append (ingredient_names)
				pass;
				
			
			if ("unites" in ingredient):				
				add_goals_to_recipe (ingredient ["unites"])
	'''
	
	add_goals_to_recipe (essential_nutrients_grove)

	recipe ["goal notes"] = return_packet
