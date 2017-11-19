Dim message, sapi
Set Arg = WScript.Arguments

message = Arg(0)

Set sapi=CreateObject("sapi.spvoice")
sapi.Speak message