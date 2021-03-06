import os
import xml.etree.ElementTree as etree 
import nltk
	


# This script uses nltk linrary to count ammount of
# functional words in text and it's relation to 
# full text size.
#
#	Part of speech tags, which counted as function words
#
#1.     CC	Coordinating conjunction
#3.	DT	Determiner
#4.	EX	Existential there
#6.	IN	Preposition or subordinating conjunction
#16.	PDT	Predeterminer
#18.	PRP	Personal pronoun
#19.	PRP$	Possessive pronoun
#23.	RP	Particle
#25.	TO	to
#26.	UH	Interjection
#33.	WDT	Wh-determiner
#34.	WP	Wh-pronoun
#35.	WP$	Possessive wh-pronoun
# 


# (f) Create list of words from text: 

def fromTextToList(textFile):
    finalList = []
    goodString = ""
    banned = [",","/",".",";",":","\\", "<", ">","-", "]", "[", "{", "}", "&", "*", "^","%","#" ,"!", "?","\'"]
    for string in textFile:
        goodString = ""
        for sign in string:
            if sign not in banned:
                goodString = goodString + sign
        tempList = goodString.split()
        for singleWord in tempList:
            finalList.append(singleWord)
    return finalList

# (f) Create list of parts of speech tags:

def tokenizePOSList(wordList):
    pos = nltk.pos_tag(wordList)
    listPOS = []
    for tu in pos:
        listPOS.append(tu[1])
    return listPOS

# (f) Counting ammounts of each tag in final list of pos tags

def finalCount(terminal):
    listTags = [["cc"] , ["cd"] , ["dt"] , ["ex"] , ["fw"] , ["in"] , ["jj"] , ["jjr"], ["jjs"], ["ls"], ["md"], ["nn"], ["nns"] , ["nnp"] , ["nnps"] , ["pdt"] , ["pos"] , ["prp"] , ["prp$"] , ["rb"] , ["rbr"] , ["bs"] , ["rp"] , ["sym"] , ["to"] , ["uh"] , ["vb"] , ["vbd"] , ["vbg"] , ["vbn"] , ["vbp"] , ["vbz"] , ["wdt"] , ["wp"] , ["wp$"] , ["wrb"]]
    for tag in listTags:
        tag.append(terminal.count(tag[0].upper())) 
    finalCount = listTags[0][1]+ listTags[2][1] +listTags[3][1] + listTags[5][1] + listTags[15][1] + listTags[17][1] + listTags[18][1] + listTags[22][1] + listTags[24][1] + listTags[25][1] + listTags[32][1] +listTags[33][1] + listTags[34][1]
    finalCount = float(finalCount)
    z = 0
    if finalCount>0:
        q = len(terminal)
        z = (finalCount/q)
    return z
    
	

# (1) Find all xml files in current directory

listOfXML = []

dir = os.getcwd()
names = os.listdir(dir)
for a in names:
	if a[-3:] == "xml":
		listOfXML.append(a)

print(listOfXML)

# (1.5) Create list of files, make copies and make some replacements.
# And collect names of temp files

listOfFiles = []
trashlist = []
listOfFilesWorking = []

for a in listOfXML:
	d = open(a,"r")
	listOfFiles.append(d)

for a in range(len(listOfFiles)):
	f = open(listOfXML[a][:-4] + "New" + listOfXML[a][-4:],"w")
	trashlist.append(listOfXML[a][:-4] + "New" + listOfXML[a][-4:])
	for string in listOfFiles[a]:
		s = string
		s = s.replace("<TEXT>","<TEXT> <TX>")
		s = s.replace("<REMARQUE>","</TX> <REMARQUE>")
		s = s.replace("</REMARQUE>","</REMARQUE> <TX>")
		s = s.replace("</TEXT>","</TX> </TEXT>")
		f.write(s)
	f.close()
	

for a in listOfFiles:
	a.close()

# (2) Parse XML file

for f in trashlist:
	tree = etree.parse(f)
	root = tree.getroot()
	z = open(f[:-7]+"temp.txt","w")
	for n in root[1]:
		if n.tag=="TX":
			z.write(n.text)
	z.close()
	z = open(f[:-7]+"temp.txt","r")
	ind = finalCount(tokenizePOSList(fromTextToList(z)))	
	print(f[:-7])
	print("\n")
	print(ind)
	print("\n")
	z.close()
	os.remove(f[:-7]+"temp.txt")

# (3) Delete Temp Files
 
for a in range(len(listOfFiles)):
	os.remove(listOfXML[a][:-4] + "New" + listOfXML[a][-4:])
