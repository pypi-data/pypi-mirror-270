
'''
	from vegan.shows_v2.recipe._ops.formulate import formulate_recipe
	recipes = formulate_recipe ({
		"natures_with_amounts": [
			{
				"FDC_ID": "",
				"packets": 10
			},
			{
				"FDC_ID": "",
				"packets": 5
			},
			{
				"DSLD_ID": "",
				"packets": 5
			}
		]	
	})
'''


from vegan.shows_v2.recipe._ops.formulate import formulate_recipe
from vegan.clouds.food_USDA.nature_v2._ops.retrieve import retrieve_parsed_USDA_food

def retrieve_recipe (packet):
	natures_with_amounts = packet ["natures_with_amounts"]
	
	formula_data = []
	for natures_with_amount in natures_with_amounts:
		amount_of_packets = natures_with_amounts ["packets"]
		if ("FDC_ID" in natures_with_amount):
			out_packet = retrieve_parsed_USDA_food ({
				"FDC_ID": 1
			})
			
			formula_data.append ([
				out_packet, amount_of_packets
			])
		
		elif ("DSLD_ID" in natures_with_amount):
		
		
		else:
			raise Exception (f"""
			
				neither FDC_ID or DSLD_ID was found in natures_with_amount: 
				
				{ natures_with_amount }
				
				""")

		
		

	recipes = formulate_recipe ({
		"natures_with_amounts": [
			[ food_1, 1 ],
			[ ]
		]	
	})