def start():
	print("What should i do?")
	print("1 - Observe a file\n2 - Render an animation\n3 - Quit")
	try:
		choose = int(input("> "))
		if(choose == 1):
			import observe
		elif(choose == 2):
			import render
		elif(choose == 3):
			pass
		else:
			print("Oops! I don't know what should i do.")
			start()
	except Exception as e:
		print("Something gone wrong :(")
		print(e)
		input("")

print("Welcome to Quick Animate")
start()