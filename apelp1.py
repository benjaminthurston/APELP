#apelp mark 1
#this is the start of something crazy.

import datetime
import os
import random
import datetime
import webbrowser
import time
import calendar

#I am trying to import the file 8ball to the file so that we can call the 8ball function
#from folder.apelp import file 8ball


# apelp greets you first with one of these greeetings 
greet = random.choice(("hi","hey","sup","whats up","hey it's jarvis","hello","hey there","good to see you"))
print (greet)
os.system("say '"+greet+"'") 
resp1 = input("")