
import xml.etree.ElementTree as et
import glob 

awards=dict()

def addIDandAbs(ID,abstract):
	for i in awards:
		if i == ID:
			print("Error")
		return
	awards[ID] = abstract

for items in glob.glob("sample/0*.xml"):
	item = open(items)                 		
	str_data =  item.read()
	data = et.fromstring(str_data)
	award_list = data.findall("Award")
for i in award_list
	addIDandAbs(i.find("AwardID").text,i.find("AbstractNarration").text)
	 
print(awards)
