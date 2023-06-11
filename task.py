import csv
from time import process_time
import tracemalloc

def createDictionary(dictionaryFileName):
    dictionary={}
    with open(dictionaryFileName, mode ='r') as file:
        csvFile = csv.reader(file)

        for line in csvFile:
            dictionary[line[0]]=[line[1],0]
    return dictionary

def translate(InputFileName,dictionaryFileName):
    dictionary=createDictionary(dictionaryFileName)  

    with open(InputFileName,'r') as file:
        resultFile = open("t8.shakespeare.translated.txt", "w")#output file

        for line in file: #processing input line by line
            tempLine=""
            line=line[:-1]

            for word in line.split(" "): #processing input word by word
                ending=""

                if word[-1:] in [':',';',',','.']: #if word ends with these charector then remove and add after translation
                    ending=word[-1:]
                    word=word[:-1]

                try :
                    tempLine+=dictionary[word][0]+ending+" " #mapping words in dictionary
                    dictionary[word][1]+=1
                except KeyError:
                    tempLine+=word+ending+" "

            tempLine=tempLine[:-1]
            resultFile.write(tempLine+"\n") #adding translated line to output file

    #adding frequency of translated word
    with open("frequency.csv",'w',encoding='UTF8', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(["English Word","French Word","Frequency"])

        for x in dictionary:
            if dictionary[x][1]!=0:
                writer.writerow([x]+dictionary[x])


t1_start = process_time()
tracemalloc.start()

InputFileName="t8.shakespeare.txt"
dictionaryName="french_dictionary.csv"

translate(InputFileName,dictionaryName)

t1_stop = process_time()

memory=tracemalloc.get_traced_memory()
print("Time to process:",t1_stop-t1_start,"seconds")
print("Memory used:",(memory[1]-memory[0])/100000,"MB")
tracemalloc.stop()
