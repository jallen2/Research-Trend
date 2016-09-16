
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
    
def addtolist():
	for i in award_list:
		addIDandAbs(i.find("AwardID").text,i.find("AbstractNarration").text)    
#print(glob.glob("sample/0*.xml"))
for items in glob.glob("sample/*.xml"):
	item = open(items)
	str_data =  item.read()
	data = et.fromstring(str_data)
#    global award_list 
#    award_list = data.findall("Award")
#    for i in award_list:
#    addIDandAbs(i.find("AwardID").text,i.find("AbstractNarration").text)
	addIDandAbs(data.find("Award").find("AwardID").text,data.find("Award").find("Institution").find("Name").text)
	
for k, v in awards.items(): 
	sorted(awards.keys())
	print(k+":", v)



