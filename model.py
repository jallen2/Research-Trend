import xml.etree.ElementTree as et
import glob 

global awards
awards=dict()
x = 0
y = 0 

def addIDandAbs(ID,abstract):
    for i in awards:
        if i == ID:
            print("Error")
            return
    awards[ID] = abstract   
for items in glob.glob("2002/*.xml"): #Iterate through all xml files in the 2001 directory
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
                                       
                                      
# for k, v in awards.items(): 
# def addIstr_data ef addIstr_data sorted(awards.keys())
# print(k+":", v)
