
'''
	from vegan._essence import build_essence
	build_essence ()
'''


#----
#
import importlib
import pathlib
from os.path import dirname, join, normpath
import sys
import os
#
#
import rich
import pydash
#
#----

essence = {}
essence_built = "no"


def prepare_essence_from_py_file (essence_path):
	return prepare_essence (
		run_script_from_file (
			essence_path
		)
	)

def build_essence ():
	global essence_built;

	if (essence_built == "yes"):
		#print ('essence already built');
		return;
		

	CWD = os.getcwd ()
	print ("build essence:", CWD)
	
	found_essence_path = False
	possible_directory = CWD	
	while True:
		possible_location = str (normpath (join (possible_directory, "vegan_essence.py")));
		print ("checking for essence:", possible_location)
		
		if os.path.exists (possible_location):
			found_essence_path = possible_location
			print ("essence found @:", possible_location)
			break;
			
		possible_directory = os.path.dirname (possible_directory)
			
		if (possible_directory == "/"):
			break;
			
			
	if (type (found_essence_path) != str):
		raise Exception ("vegan_essence.py not found")
			

	the_merged_essence = prepare_essence_from_py_file (
		possible_location
	)
	
	for key in the_merged_essence:
		essence [ key ] = the_merged_essence [key]
		
	
	print ('essence built')
	essence_built = "yes"
	
	

def run_script_from_file (file_path):
	with open (file_path, 'r') as file:
		script_content = file.read ()
        
	proceeds = {}	
		
	exec (script_content, {
		#'__file__': os.getcwd () + "/" + os.path.basename (file_path)
		'__file__': file_path
	}, proceeds)
	
	essence = proceeds ['essence']
	
	return essence;



def prepare_essence (
	essence = {}
):
	this_directory = pathlib.Path (__file__).parent.resolve ()	
	the_mix_directory = str (normpath (join (this_directory, "../..")));

	'''
		"onsite": {
			"host": "0.0.0.0",
			"port": "39000",
			
			"path": crate ("monetary_1/data"),
			"logs_path": crate ("monetary_1/logs/the.logs"),
			"PID_path": crate ("monetary_1/the.process_identity_number"),
		}
	'''

	the_merged_essence = pydash.merge (
		{
			#
			#	4 detailed info
			#	3 info
			#	2 cautions
			#	1 alarms
			#
			"record_level": 2,
			
			"CWD": os.getcwd (),
			
			"monetary": {
				#
				#	optional: URL
				#
				"aliases": {
					"vegan_tract": "vegan_tract"
				}, 
				
				"collections": [
					"cautionary_ingredients",
					"essential_nutrients",
					"glossary",
					"goals"
				],
				
				#
				#	_saves
				#		
				#
				"saves": {
					"path":  str (normpath (join (
						the_mix_directory, 
						"adventures/monetary/__saves"
					))),
					
					"exports": {
						"path": str (normpath (join (
							the_mix_directory, 
							"adventures/monetary/__saves/exports"
						)))						
					},
					
					"dumps": {
						"path": str (normpath (join (
							the_mix_directory, 
							"adventures/monetary/__saves/dumps"
						)))
					}					
				}
			},
			
			
			
			"sanique": {
				"directory": str (normpath (join (
					the_mix_directory, 
					"adventures/sanique"
				))),
				
				"path": str (normpath (join (
					the_mix_directory, 
					"adventures/sanique/harbor/on.proc.py"
				))),
				
				"port": "8000",
				
				#
				#	don't modify these currently
				#
				#	These are used for retrieval, but no for launching the
				#	sanic inspector.
				#
				#	https://sanic.dev/en/guide/running/inspector.md#inspector
				#
				"inspector": {
					"port": "7457",
					"host": "0.0.0.0"
				}
			},
			"dictionary": {
				"path": str (normpath (join (the_mix_directory, "__dictionary"))),
				"vegan": str (normpath (join (the_mix_directory, "__dictionary/vegan"))),
			}
		},
		essence
	)
	
	return the_merged_essence