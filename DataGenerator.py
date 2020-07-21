from bs4 import BeautifulSoup
import urllib.request
import random
import json

def GetListOfTests():
    html_page = urllib.request.urlopen('http://www.zibashahrlab.ir/Tests-List.aspx').read()
    soup = BeautifulSoup(html_page, "lxml")
    listOfAs = soup.findAll('a')
    listOfAs =  listOfAs[26:]
    list = listOfAs[2::3]
    return [element.text for element in list][:-3]


def GetListOfLabsIds():
    html_page = urllib.request.urlopen("https://www.urmc.rochester.edu/labs/all.aspx").read()
    soup = BeautifulSoup(html_page, "lxml")
    listOfAs = soup.select('div.department-wrapper a')

    return [element.text for element in listOfAs]

def ChooseLabs(listOfLabs, N):
    selectedLabs = []
    for i in range(N):
        item = random.choice(listOfLabs)
        selectedLabs.append(item)
        listOfLabs.remove(item)

    return selectedLabs

def ChooseTest(listOfTests, N):
    selectedTests = []
    for i in range(N):
        item = random.choice(listOfTests)
        selectedTests.append((item, random.randint(1, 200)))
        listOfTests.remove(item)

    return selectedTests

if __name__ == "__main__":
    listOfLabs = ChooseLabs(GetListOfLabsIds(), 3)
    ListOfTests = GetListOfTests() # :|
    listOfTests = ChooseTest(ListOfTests, 30)



    file = open('LabsData.txt','w')
    Dict = {}
    # Dict['samplers'] = [{'name': 'Kazem', FreeTimes = [0,1,2,3,4,5,6]}]
    for i in range(3):
        Dict[listOfLabs[i]] = {'tests': listOfTests[10*i:10*i+10], 'insurance': random.randint(1, 256), 'samplers': [{'firstName': 'Kazem', 'lastName': 'Ghorbani', 'id': random.randint(1, 256), "FreeTimes": list(range(random.randint(0, 6)))}, {'firstName': 'Alireza', 'lastName': 'ghavi nejad', 'id': random.randint(1, 256), 'FreeTimes':list(range(random.randint(0, 6))) }]}

    file.write(json.dumps(Dict, indent=4))
    file.close()

    # file = open('Tests.txt','w')
    # Dict = {}
    # Dict['tests'] = []
    # for test in ListOfTests:
    #     Dict['tests'].append((test, random.rand(1,100))
    #
    # file.write(json.dumps(Dict, indent=4))
    # file.close()
#(╯°□°）╯︵ ┻━┻
