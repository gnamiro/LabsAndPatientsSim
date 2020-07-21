import Request
import Lib
import User
import Lab

class Validator:
    """docstring for Validator."""

    def __init__(self, nationalId, insuranceId, phoneNumber):
        self._nationalId = nationalId
        self._insuranceId = insuranceId
        self._phoneNumber = phoneNumber

    def SendQueryToNIMC(self):
        print('sending nationalId to NIMC site and checking its validation(by default it is true)')
        return True

    def SendQueryToInsurance(self):
        print('sending nationalId to insurance sites and checking its validation(by default it is true)')
        return True

    def SendSmS(self):
        print('send SmS to client pls enter number 123(simulation:))')
        return True

class RequestController:
    __instance = None
    @staticmethod
    def GetInstance():
        """ Static access method. """
        if RequestController.__instance == None:
            RequestController()
        return RequestController.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if RequestController.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            RequestController.__instance = self
        # self.Requests = []


    def MakeNewRequest(self, patient):
        new_request = Request.Request(patient.GetUserId())
        # self.Requests.append(new_request)
        new_request.changeStatus('Initialized')
        patient.AddNewRequest(new_request)




    def EnterRequiredInfo(self, patient, request, isForAnotherPatient=False, address=None, insuranceId=None, nationalId=None, phoneNumber=None):
        if isForAnotherPatient:
            validator = Validator(nationalId, insuranceId, phoneNumber)
            resultNIMC = validator.SendQueryToNIMC()
            resultInsurance = validator.SendQueryToInsurance()
            resultPhone = validator.SendSmS()
            if resultNIMC and resultInsurance and resultPhone:
                print('Validation Successful')
                request.SetInfo(address, insuranceId, nationalId, phoneNumber)
            else:
                print('Validation returned False!!')
                return False
        else:
            info = patient.GetInfo()
            request.SetInfo(info[0], info[1], info[2], info[3])
            # patient.getCurrentRequest().setInfo()
        return True


    def RequestListOfAvailableLabs(self, listOfTests, currentRequest):
        currentRequest.changeStatus('listOfTests Confirmed')
        currentRequest.SetTestsList(listOfTests)
        insuranceId = currentRequest.GetInsuranceId()

        listOfAvailableLabs = Lab.LabContainer.GetInstance().GetAvailableLabs(listOfTests, insuranceId)

        return listOfAvailableLabs

    def SetSelectedLabAndGetTimeSlot(self, labId, currentRequest):
        currentRequest.SetLabId(labId)

        for lab in Lab.LabContainer.GetInstance().GetListOfLabs():
            if lab.GetLabId() == labId:
                return lab.RequestTimeSlot()

    def SelectTimeSlotAndCalcTotalCost(self, labId, selectedSlot, currentRequest):
        currentRequest.SetTimeSlot(selectedSlot)
        insuranceId = currentRequest.GetInsuranceId()
        listOfTests = currentRequest.GetListOfTests()
        totalCost = 0
        for lab in Lab.LabContainer.GetInstance().GetListOfLabs():

            if lab.GetLabId() == labId:
                # print(labId)/
                totalCost =  lab.GetTotalCost(listOfTests, insuranceId)
                lab.AssignListOfTestsToSampler(listOfTests, selectedSlot)
        return totalCost

    def PayFinalCost(self,Total_cost, currentRequest):
        currentRequest.changeStatus('isGoingtoPaid')
        print('Redirect to Shaaparak site with cost ',Total_cost)
        currentRequest.changeStatus('SendToSampler')
