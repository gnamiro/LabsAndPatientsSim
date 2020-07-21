import RequestController
import Lib

class User:

    def __init__(self, userId, Phone, Address, firstName, lastName, nationalId):
        self._userId = userId
        self._Phone = Phone
        self._Address = Address
        self._firstName = firstName
        self._lastName = lastName
        self._nationalId = nationalId


    def GetUserId(self):
        return self._userId

class Patient(User):
    """docstring for ."""

    def __init__(self, userId, Phone, Address, firstName, lastName, nationalId, insuranceId):
        super().__init__(userId, Phone, Address, firstName, lastName, nationalId)
        # threading.Thread.__init__(self)
        self._insuranceId = insuranceId
        self._Requests = []
        self._currRequest = None

    def GetInfo(self):
        return [self._Address, self._insuranceId, self._nationalId, self._Phone]

    def GetCurrentRequest(self):
        return self._currRequest

    def AddNewRequest(self, new_request):
        self._Requests.append(new_request)
        self._currRequest = new_request


class Sampler(User):
    """docstring for Sampler."""

    def __init__(self, userId, Phone, Address, firstName, lastName, nationalId, labId ,FreeTimes):
        super().__init__(userId, Phone, Address, firstName, lastName, nationalId)
        self._slotTimes = []
        self._freeTimes = FreeTimes
        self._labId = labId

    def SlotTime(self, Time, listOfTests):
        if(int(Time) in self._freeTimes):
            self._freeTimes.remove(int(Time))
            self._slotTimes.append((Time, listOfTests))
            Lib.ReWriteJSON('LabsData.txt', int(Time), self._userId, self._labId)
            print("user id = ", self._userId)
            return 1

        return 0



    def GetFreeTimes(self):
        data = Lib.ReadJsonFile('LabsData.txt')
        for i in range(len(data[self._labId]['samplers'])):
            samplerDict = data[self._labId]['samplers'][i]
            if samplerDict['id'] == self._userId:
                self._freeTimes = data[self._labId]['samplers'][i]['FreeTimes']
                break
        return self._freeTimes
