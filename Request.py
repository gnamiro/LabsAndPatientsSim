class Request:
    """docstring for Request."""

    def __init__(self, patientId):
        self._insuranceId = None
        self._nationalId = None
        self._patientId = patientId
        self._listOfTests = None
        self._LabId = None
        self._SelectedSlot = None
        # print(self.patientId)


    def SetInfo(self, address, insuranceId, nationalId, phoneNumber):
        self._address = address
        self._insuranceId = insuranceId
        self._nationalId = nationalId
        self._phoneNumber = phoneNumber
        # print(address, insuranceId, nationalId, phoneNumber)

    def GetInsuranceId(self):
        return self._insuranceId

    def SetTestsList(self,listOfTests):
        self._listOfTests = listOfTests

    def GetListOfTests(self):
        return self._listOfTests

    def SetLabId(self,LabId):
        self._LabId = LabId

    def SetTimeSlot(self,selectedSlot):
        self._SelectedSlot = selectedSlot

    def changeStatus(self, status):
        self.status = status
