import random
import json
userNames = ["No", "Sep", "HR", "FG", "AZ" , "Battry", "AA1999", "Narm1", "ClassDiagram"]
phoneNumbers = ["09148902145", "09121288431", "09201920674"]
address = ['Bonab', 'Tehran' , 'Karaj', 'Rasht', 'New York', 'Nagoya' , 'Kabol']
labsDataFilePath = 'LabsData.txt'



def RandomUserName(List):
    return random.choice(List)

def GetDataForLab(Lab):
    pass

def ReadJsonFile(filePath):
    with open(filePath) as f:
        data = json.load(f)
        return data

def PrintListOfTests(filePath):
    data = ReadJsonFile(filePath)
    print([lab['tests'] for lab in data])

def ReWriteJSON(filePath, elementToRemove, samplerId, labId):
    data = ReadJsonFile(filePath)
    for i in range(len(data[labId]['samplers'])):
        samplerDict = data[labId]['samplers'][i]
        if samplerDict['id'] == samplerId:
            data[labId]['samplers'][i]['FreeTimes'].remove(elementToRemove)
            break
    file = open(filePath, 'w')
    file.write(json.dumps(data, indent=4))
    file.close()
