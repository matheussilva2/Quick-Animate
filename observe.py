from observer import Observer

def start():
	filename = str(input("Observed filename (without file type): "))
	filetype = str(input("Observed filetype (for example txt): "))

	ob = Observer(filename, filetype)
	ob.observe()

start()