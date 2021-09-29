#!/usr/bin/env python3
import cgi

form = cgi.FieldStorage()

encryptbtn = form.getfirst("encrypt", "не задано")
decryptbtn = form.getfirst("decrypt", "не задано")
startMessage = form.getfirst("message", "не задано")
oneKey = form.getfirst("key", "не задано")
finalMessage = form.getfirst("final", "не задано")

'''
def Encripter(encryptbtn, startMessage, oneKey):
    oneKey *= len(startMessage) // len(oneKey) + 1
    finalMessage = ""
    for i, j in enumerate(startMessage):
        if encryptbtn:
            temp = ord(j) + ord(oneKey[i])
        if decryptbtn:
            temp = ord(j) - ord(oneKey[i])
        finalMessage += chr(temp % 26 + ord('A'))
    return finalMessage
'''

print("Content-type: text/html")
print()
print(finalMessage)
print(oneKey)
print(startMessage)
