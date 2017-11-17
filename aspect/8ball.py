#this is for an 8ball function

def magic_8ball():
	x=raw_input("What is your question? enter to quit. ")
	Eightball_list = ["It is certain", "Outlook good","You may rely on it","Ask again later","Concentrate and ask again","Reply hazy, try again","My reply is no","My sources say no"]
	if x=="":
		print "exiting..."
	else:
		print random.choice(Eightball_list)
magic_8ball()