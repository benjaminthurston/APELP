#Standard Interface
import tkinter
import VoiceBox
from tkinter import *

respondingText = ''
speakingTo = ''
romCount = 5

def firstScript():
    VoiceBox.standardVocals("Hello, I am a pelp, I have limited intelligence at the moment so can I have your first name only, please?")

def nextResponse():
    global respondingText
    global rowCount
    respondingText = Answer.get()

    newSpeak = tkinter.LabelFrame(Interface,
                                   text=str(speakingTo))
    newSpeakBox=tkinter.Label(newSpeak,
       text=str(respondingText))
    newSpeak.grid(padx=2, pady=2)
    newSpeakBox.grid(row=rowCount)
    rowCount = rowCount + 1

    
    

def firstResponse():
    global respondingText
    global speakingTo
    Place
    respondingText = Answer.get()
    speakingTo = str(respondingText)
    AnswerButton.configure(command = nextResponse)
    newSpeak = tkinter.LabelFrame(Interface,
                                   text=str(speakingTo))
    newSpeakBox=tkinter.Label(newSpeak,
       text=str(speakingTo))
    newSpeak.grid(padx=2, pady=2)
    newSpeakBox.grid(row=3)
    
    speakingTo = str(respondingText)
    AnswerButton.configure(command = nextResponse)
    newAPELP = tkinter.LabelFrame(Interface,
                                   text="APELP")
    newAPELPBox=tkinter.Label(newAPELP,
       text=("Hello " + str(speakingTo) + ", it's nice to meet you, as you now know my name is APELP, it's an acronym for Assembled Pathos Ethos and Logos Program. Is there anything you want to ask me?"))
    newAPELP.grid(padx=2, pady=2)
    newAPELPBox.grid(row=4)
    
    VoiceBox.standardVocals("lowgoes")
>>> VoiceBox.standardVocals(("Hello " + str(speakingTo) + ", it's nice to meet you, as you now know my name is a pelp, it's an acronym for Assembled pathoes eathoes and lowgoes Program. Is there anything you want to ask me?"))


    

Interface = tkinter.Tk()
Interface.title = ("APELP Interface")
Answer = tkinter.Entry(Interface)
Answer.insert(0, "Type your Answer here")
Answer.grid(row=1, column=1)
AnswerButton = tkinter.Button(Interface,
    text="Respond", command=firstResponse)
AnswerButton.grid(row=1, column=2)

question = tkinter.LabelFrame(Interface,
                                   text="APELP")
questionBox=tkinter.Label(question,
       text="Hello, I am APELP, I have limited intelligence at the moment so can I have your first name only, please?")
question.grid(padx=10, pady=10)
questionBox.grid(row=2)

firstScript()


    
