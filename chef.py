from Chef import Chef



with open("test/hello_world.chef", "r+") as recipe:
	inscript = "".join(recipe.readlines())
	# print(inscript)
	Process = Chef(script=inscript, recipename=u"Chai Latte with A Pop.\n\n")
	print(Process.parse())