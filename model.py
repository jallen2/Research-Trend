import xml.etree.ElementTree as et
import glob 

global awards
awards=dict()

def addIDandAbs(ID,abstract):
    for i in awards:
        if i == ID:
            print("Error")
            return
    awards[ID] = abstract   
def totalabs():
    x = 0
    y = 0
    for items in glob.glob("20*/*.xml"): #Iterate through all xml files in the 2001 directory
        item = open(items)
        str_data =  item.read()
        data = et.fromstring(str_data)
# check brackets <Institution> doesnt hold <AbstractNarraction> in 2002 xml files for certant years 
        an = data.find("Award").find("AbstractNarration").text
        if an is not None:
            y = y + 1
            addIDandAbs(data.find("Award").find("AwardID").text,data.find("Award").find("AbstractNarration").text)
		#for k, v in awards.items(): 
		#sorted(awards.keys())
		#print(k+":", v) 
        else:
            x = x + 1
    print("Abstracts not found:", x)
    print("Abstracts found:", y)
    print("Total files:", x+y)
def fileandabs():
    for items in glob.glob("2015/*.xml"):
        item = open(items)
        str_data = item.read()
        data = et.fromstring(str_data)
        an = data.find("Award").find("AbstractNarration").text
        if an is not None:
            addIDandAbs(data.find("Award").find("AwardID").text,data.find("Award").find("AbstractNarration").text)
    key = raw_input("Dictionary Key: ")
    print("Key:",key,"\nAbstract:", awards[key])                                        

print("\nHow would you like to proceed?")
print("A: Abstract Totals(found, not found, total files)")
print("B: Key and Abstract") 
print("NOTE: Type the letter associated with the program you wish to run.")
answer = raw_input("Selection:")
if answer == "A":
    totalabs()
elif answer == "B":
    fileandabs()
else:
    print("Exit Program.")
