# Hey ho, here we go
import nltk
# Function which create list of words from text 
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
# Function which create list of parts of speech tags
def tokenizePOSList(wordList):
    pos = nltk.pos_tag(wordList)
    listPOS = []
    for tu in pos:
        listPOS.append(tu[1])
    return listPOS
# function breaks list of words into parts
# programm will beworking with each part 
def partlyTaken(wordList):
        desider = raw_input("\nNow please deside, if you want to have numerical parameter or relative\n if numerical: print 0\nif relative: print 1\n")
        if int(desider):
        #from now: variable is relative 
                part = raw_input("\nNow print the size of part you want to have (in format \"0.1\")  \n")
                ammountParts = 1/float(part)
                ammountParts = int(ammountParts)
                sizeParts = len(wordList) / ammountParts 
        else:
                sizeParts = raw_input("\n In this case enter tha size of each block.\n But take into concideration the size of text: %s \n" % (len(wordList))) 
                ammountParts =len(wordList)/int(sizeParts)
        counter = 0
        partsList = []        
        for times in range(ammountParts):
            partsList.append(wordList[counter:(int(counter)+int(sizeParts))])
            counter = int(sizeParts) + counter
        partsList.append(wordList[counter:])
        return partsList
# function which cut off phrasal verbs
# out of list of words 
def phrasalVerbsCut(wordList):
    listOfPhrVerbsUn = [["blow","up"],["break","down","in","out","out in","up"],["call","around","on"],["calm","down"],["care","for"],["catch","up"],["check","in","out"],["cheer","up"],["chip","in"],["come","across","apart","down with","forward","from"],["count","on"],["cut","back on","in"],["do","away with"],["dress","up"],["drop","up","back","by","in","out","over"],["eat","out"],["end","up"],["fall","apart","down","out"],["find","out"],["get","along","around","away","away with","back","back at","back into","on","over","round to","together","up"],["give","in","up"],["go","after","against","ahead","back","out","out with","over","without"],["grow","apart","back","into","out of","up"],["hang","in","on","out","up"],["hold","on","onto"],["keep","on"],["log","in","off","on","out"],["look","after","down on", "for","forward","into","out","out for","up to"],["make","up"],["pass","away","out"],["pay","for"],["put","up with"],["run","away","into","out","over","through"],["shop","around"],["show","off"],["sleep","over"],["take","after","off"],["think","back"],["turn","up"],["wake","up"],["warm","up"],["wear","off"],["work","out"]]
    listOfPhrVerbsDue = [["add","up to"],["ask","out"],["back","up"],["blow","up"],["break","down","in","into"],["bring","down","up"],["call","back","off","up"],["check","out"],["cheer","up"],["clean","up"],["cross","out"],["cut","down","off","out"],["do","over","up"],["drop","off"],["drop","off"],["fill","in","out","up"],["find","out"],["get","across","back","over"],["give","away","back","out","up"],["hand","down","in","out","over"],["hold","back","up"],["keep","from","out","up"],["let","down","in"],["look","over","up"],["make","up"],["mix","up"],["pass","out","up"],["pay","back"],["pick","out"],["point","out"],["put","down","off","on","out","together"],["send","back"],["set","up"],["sort","out"],["stick","to"],["switch","off","on"],["take","apart","back","off","out"],["tear","up"],["think","over"],["throw","away"],["try","on","out"],["turn","down","off","on","up"],["use","up"],["warm","up"],["work","out"]]
    c = 0
    co = 0
    for word in wordList[:-1]:
        for phrVerbList in listOfPhrVerbsUn: 
            if phrVerbList[0]== word.lower():
                for add in range(len(phrVerbList)-1):
                    if wordList[c+1] == phrVerbList[add+1]:
                        wordList.pop(c+1)
                        c = c - 1
                        co = co + 1
        c = c+1
    c = 0
    for word in wordList[:-2]:
        for phrVerbList in listOfPhrVerbsUn: 
            if phrVerbList[0]== word.lower(): 
                for add in range(len(phrVerbList)-1):
                    if wordList[c+1] == phrVerbList[add+1]:
                        wordList.pop(c+1)
                        c = c - 1
                        co = co + 1
                    elif wordList[c+2] == phrVerbList[add+1]:
                        wordList.pop(c+2)
                        c = c - 1
                        co = co + 1
                    
        c = c+1
    return [wordList,co]
#Time to count, how many of each tag there is in our text
def finalCount(terminal,temp):
#counting ammounts of each tag in final list of pos tags
    listTags = [["cc"] , ["cd"] , ["dt"] , ["ex"] , ["fw"] , ["in"] , ["jj"] , ["jjr"], ["jjs"], ["ls"], ["md"], ["nn"], ["nns"] , ["nnp"] , ["nnps"] , ["pdt"] , ["pos"] , ["prp"] , ["prp$"] , ["rb"] , ["rbr"] , ["bs"] , ["rp"] , ["sym"] , ["to"] , ["uh"] , ["vb"] , ["vbd"] , ["vbg"] , ["vbn"] , ["vbp"] , ["vbz"] , ["wdt"] , ["wp"] , ["wp$"] , ["wrb"]]
    for tag in listTags:
        tag.append(terminal.count(tag[0].upper()))
#Part of speech tags, which counted as function words
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
#                                           Add  for articles  
    finalCount = listTags[0][1]+ listTags[2][1] +listTags[3][1] + listTags[5][1] + listTags[15][1] + listTags[17][1] + listTags[18][1] + listTags[22][1] + listTags[24][1] + listTags[25][1] + listTags[32][1] +listTags[33][1] + listTags[34][1]
    finalCount = float(finalCount)
    z = 0
    if finalCount>0:
        q = len(terminal)+int(temp)
        z = (q/finalCount)
    return z
    

# Opening original text file in .xml fromat
# Creating additional files without tags 
# That will significantly simplify work
name = raw_input("Write the name of your file with postfix.\n")
name = str(name)
fileOutputWith = open(name[:4] + "NewWith.txt", 'w+')
fileOutputWithout = open((name[:4]+ 'NewWithout.txt'), 'w+')
fileOrig = open(name,"r")
# Read file, add important parts in temp files,
# depends on which tags we consider important and which - not
pointWithout = True
writerWithPlus = "<SPEAKER>"
writerWithMinus = "</SPEAKER>"
tempGuy = ["<LINE>","</LINE>","</TITLE>","<TITLE>","</SPEECH>","<SPEECH>","</SPEAKER>","<SPEAKER>","Epilogue","CHAPTER"]
for string in fileOrig:
    stringWith = ""
    stringWithout = ""
    stringReal = string.split()
    for wordy in stringReal:
        word = str(wordy)
        if word==writerWithPlus:
            pointWithout = False
        if word==writerWithMinus:
            pointWithout = True
        if tempGuy.count(word)==0:
            stringWith =  stringWith+ " " + word
            if pointWithout:
                stringWithout = stringWithout + " " + word 
    fileOutputWith.write(stringWith)
    fileOutputWithout.write(stringWithout)
fileOutputWith.close()
fileOutputWithout.close()
# Now we can choose between working with remarques and without
# and create lists of parts of words
# and break it into parts
desider = raw_input("\nWith which modedo you want to work?\n 0 - for with remarques \n 1 - for without remarques \n")
fileWith = open(name[:4] + "NewWith.txt", 'r')
fileWithout = open((name[:4]+ 'NewWithout.txt'), 'r')
listOfNumbers = []
f = raw_input("\n And what a about phrasal verbs? \n 0 - to count without them \n 1 - to count with them \n")
if int(f)==0:
    if (int(desider) == 1):
        wordList = fromTextToList(fileWithout)
        listsOfParts = partlyTaken(wordList)
        for part in listsOfParts:
            temp = phrasalVerbsCut(part)[1]
            part = phrasalVerbsCut(part)[0]
            print temp
            listOfNumbers.append(finalCount(tokenizePOSList(part),temp))
    if (int(desider) == 0):
        wordList = fromTextToList(fileWith)
        listsOfParts = partlyTaken(wordList)
        for part in listsOfParts:
            temp = phrasalVerbsCut(part)[1]
            part = phrasalVerbsCut(part)[0]
            print temp
            listOfNumbers.append(finalCount(tokenizePOSList(part),temp))
else:
    if (int(desider)== 1):
        wordList = fromTextToList(fileWithout)
        listsOfParts = partlyTaken(wordList)
        for part in listsOfParts:
            listOfNumbers.append(finalCount(tokenizePOSList(part),0))
    if (int(desider) == 0):
        wordList = fromTextToList(fileWith)
        listsOfParts = partlyTaken(wordList)
        for part in listsOfParts:
            listOfNumbers.append(finalCount(tokenizePOSList(part),0))
print listOfNumbers

