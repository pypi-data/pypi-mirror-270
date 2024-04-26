


def check_1 ():
	from vegan.clouds.food_USDA.nature_v2._ops.retrieve import retrieve_parsed_USDA_food
	out_packet = retrieve_parsed_USDA_food ({
		"FDC_ID": 1
	});
	
	assert ("anomaly" in out_packet)
	assert (out_packet ["anomaly"] == "The USDA API could not find that FDC_ID.")
	
checks = {
	"check 1": check_1
}