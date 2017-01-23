


doc1 = ['f','e','r']
doc2 = ['1','2','3']
doc3 = ['d','3','1']



def arrayadd(*args):
	doc4 = []
	for i in range(len(args)):
		doc4 = doc4[args]
	return doc4

print(arrayadd(*doc1))

 
