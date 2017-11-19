#Hopefully will contain the voice box of the program.
#from subprocess import call -possibly obsolete
import os

def standardVocals(phrase):
    methodPhrase = 'StandardVoice.vbs ("' + str(phrase) +'")'
    os.system(methodPhrase)

