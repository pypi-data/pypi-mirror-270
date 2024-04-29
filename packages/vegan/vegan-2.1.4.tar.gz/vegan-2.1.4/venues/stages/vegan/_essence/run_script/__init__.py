

'''
	from vegan._essence.run_script import run_script_move
	run_script_move ()
'''
def run_script_move (script_name, function_name):
    try:
        # Import the script as a module
        script_module = importlib.import_module(script_name)
        
        # Access the function from the module
        func = getattr(script_module, function_name)
        
        # Execute the function
        func()
    except Exception as e:
        print(f"An error occurred: {e}")