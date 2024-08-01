strData='programming'
print("Original String is:",strData)

output =strData[0] #getfirst_character

l=len(strData) #get string size

mi=int(1/2)

output=output+strData[mi] #get middle character

output=output + strData[l-l] #get last output
print("new string:",output)
