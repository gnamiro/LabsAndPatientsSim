import Lib
import User

class Lab:
    """docstring for Lab."""

    def __init__(self, labId, address, phone, listOfTests, supportedInsuranceList, samplers):
        self._labId = labId
        self._address = address
        self._phone = phone
        self._DictOfTests = dict(listOfTests)
        self._supportedInsuranceList = supportedInsuranceList
        self._samplers = [User.Sampler(samplers[i]['id'], phone, address, samplers[i]['firstName'], samplers[i]['lastName'], 0, self._labId, samplers[i]['FreeTimes']) for i in range(len(samplers))]

    def GetLabId(self):
        return self._labId

    def AbleToDoTests(self, listOfTests, insuranceId):
        isInsuranceSupported =  int(insuranceId) in range(int(self._supportedInsuranceList))
        isTestSupported = True
        for test in listOfTests:
            if test not in self._DictOfTests:
                isTestSupported = False
                break

        return (isInsuranceSupported, isTestSupported)

    def RequestTimeSlot(self):
        FreeTimes = []
        for sampler in self._samplers:
            FreeTimes.append(sampler.GetFreeTimes())

        return FreeTimes

    def GetCostOfTest(self, testName):
        if not testName in self._DictOfTests:
            return 0
        return self._DictOfTests[testName]

    def GetTotalCost(self, listOfTests, insuranceId):
        isInsuranceSupported =  int(insuranceId) in range(int(self._supportedInsuranceList))
        totalCost = 0
        for test in listOfTests:
            if test not in self._DictOfTests:
                raise Exception('test is not availabe in this lab!')

            totalCost += int(self._DictOfTests[test])
        if isInsuranceSupported:
            return totalCost * 0.8
        else:
            return totalCost
    def AssignListOfTestsToSampler(self, listOfTests, timeSlot):
        for sampler in self._samplers:
            if sampler.SlotTime(timeSlot,listOfTests):
                return 1

        raise Exception('Time not found!')

class LabContainer:
    """docstring for LabContainer."""

    __instance = None
    @staticmethod
    def GetInstance():
        """ Static access method. """
        if LabContainer.__instance == None:
            LabContainer()
        return LabContainer.__instance

    def __init__(self, labsDataFilePath):
        """ Virtually private constructor. """
        if LabContainer.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            LabContainer.__instance = self
            labsJson = Lib.ReadJsonFile(labsDataFilePath)
            labsIds = list(labsJson.keys())

            LabContainer.__instance._listOfLabs = [Lab(labsIds[i], Lib.address[: len(labsIds)][i], Lib.phoneNumbers[i], labsJson[labsIds[i]]['tests'], labsJson[labsIds[i]]['insurance'], labsJson[labsIds[i]]['samplers']) for i in range(len(labsIds))]


        # self.Requests = []



    def GetAvailableLabs(self, listOfTests, insuranceId):
        listOfCapableLabs = []
        for lab in self._listOfLabs:
            labAnswer = lab.AbleToDoTests(listOfTests, insuranceId)
            if labAnswer[1]:
                listOfCapableLabs.append((lab.GetLabId(), labAnswer[0]))

        return listOfCapableLabs

    def GetListOfLabs(self):
        return self._listOfLabs


labContainer = LabContainer(Lib.labsDataFilePath)

# (╯°□°）╯︵ ┻━┻
