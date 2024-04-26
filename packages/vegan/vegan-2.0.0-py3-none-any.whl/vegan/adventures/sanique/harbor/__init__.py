

'''
	itinerary:
		[ ] pass the current python path to this procedure
'''


'''
	https://sanic.dev/en/guide/running/manager.html#dynamic-applications
'''

'''
	worker manager:
		https://sanic.dev/en/guide/running/manager.html
'''

'''
	Asynchronous Server Gateway Interface, ASGI:
		https://sanic.dev/en/guide/running/running.html#asgi
		
		uvicorn harbor:create
'''

'''
	Robyn, rust
		https://robyn.tech/
'''

'''
	--factory
'''

#----
#
from vegan._essence import retrieve_essence	
from vegan._essence import build_essence
#
from vegan.clouds.food_USDA.nature_v2._ops.retrieve import retrieve_parsed_USDA_food
#
#
from biotech.topics.show.variable import show_variable
#
#
import sanic
from sanic import Sanic
from sanic_ext import openapi
#from sanic_openapi import swagger_blueprint, doc
import sanic.response as sanic_response
#
#
import json
import os
import traceback
#
#----

'''
	https://sanic.dev/en/guide/running/running.html#using-a-factory
'''
def create ():
	USDA_food_ellipse = os.environ.get ('USDA_food')
	NIH_supp_ellipse = os.environ.get ('NIH_supp')
	inspector_port = os.environ.get ('inspector_port')
	essence = os.environ.get ('essence')
	
	env_vars = os.environ.copy ()
	#print ("env_vars:", env_vars)
	#show_variable () 
	
	'''
		#
		#	https://sanic.dev/en/guide/running/configuration.html#inspector
		#
		INSPECTOR_PORT
	'''
	app = Sanic (__name__)
	#app.blueprint(swagger_blueprint)
	app.config.INSPECTOR = True
	app.config.INSPECTOR_HOST = "0.0.0.0"
	app.config.INSPECTOR_PORT = int (inspector_port)
	
	
	#app.blueprint(swagger_blueprint)

	@app.route ("/")
	async def home (request):
		essence = retrieve_essence ()
	
		#print ("essence:", essence)
	
		return sanic.json (
			json.loads (env_vars ["essence"])
		)
	
		#return sanic_response.text ("home")
	
	
	@app.route ("/off")
	async def off (request):
		return sanic_response.text ("not possible")
		
	
	@app.route ("/PID")
	async def PID (request):
		return sanic_response.text ("not possible")
	
	@app.websocket ('/ws')
	async def ws_handler(request, ws):
		while True:
			data = await ws.recv ()  # Receive data from the client
			await ws.send (f"Echo: {data}")  # Send the received data back to the client
	
	#
	#	#@app.route ("/USDA/food")
	#
	'''
		
	'''
	@app.patch('/USDA/food_v2')
	async def USDA_food (request, name):
		data = request.json
		return json.dumps (data, indent = 4)
		
	
	'''
		 https://sanic.dev/en/plugins/sanic-ext/openapi/decorators.html#ui
	'''
	@app.route ('/food_USDA/nature_v2/<FDC_ID>')
	@openapi.summary("Food")
	@openapi.description("Food parsing route, examples: 2369390")
	#@doc.produces ({'message': str})
	#@doc.response (200, {"message": "Hello, {name}!"})
	async def USDA_food_FDC_ID (request, FDC_ID):
		try:
			out_packet = retrieve_parsed_USDA_food ({
				"FDC_ID": FDC_ID,
				"USDA API Pass": USDA_food_ellipse
			})
			
			if ("anomaly" in out_packet):
				if (out_packet ["anomaly"] == "The USDA API could not find that FDC_ID."):
					return sanic_response.json (out_packet, status = 604)
			
				return sanic_response.json (out_packet, status = 600)
			
			return sanic_response.json (out_packet)
			
		except Exception as E:
			print (str (E))
			
		return sanic_response.json ({
			"anomaly": "An unaccounted for anomaly occurred."
		}, status = 600)
	
		
		
	@app.patch ("/supp_NIH/nature_v2/<DLSD_ID>")
	async def NIH_supp (request, DLSD_ID):
		data = request.json
	
		return sanic_response.json (json.dumps (data, indent = 4))
		
	return app

