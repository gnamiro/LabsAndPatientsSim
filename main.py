"""
this program is just made for simulating so inputs are given from testcase.txt and
labid or timeSlot that are chosen by the patient already given from the result.
classes like validation and methods like PayFinalCost don't really work I mean it's just name and simulation
"""

import RequestController
import User
import sys
import Lib

requestController = RequestController.RequestController.GetInstance()





if __name__ == "__main__":
    try:
        id, phone, address, firstName, lastName, nationalId, insuranceId = input('pls enter user Info: Phone, Address, firstName, lastName , nationalId, insuranceId\n').split()
        print('hello ',firstName , 'welcome :))))))))')
        patient = User.Patient(id, phone, address, firstName, lastName, nationalId, insuranceId)

        user_request = input('do you want to create new Request(y/n):\n')
        # print(user_request)
        if(user_request == 'y'):
            requestController.MakeNewRequest(patient)
            user_input = input('do you want to do tests for ohter guy(y/n)?\n')
            print(user_input)

            if(user_input == 'n'):
                requestController.EnterRequiredInfo(patient, patient.GetCurrentRequest())

            else:
                while True:
                    user_inputs = input('Enter New address, insuranceId, nationalId, phoneNumber\n').split()
                    print(user_inputs)
                    status = requestController.EnterRequiredInfo(patient, patient.GetCurrentRequest(), True, user_inputs[0], user_inputs[1], user_inputs[2], user_inputs[3])
                    if status:
                        break
            jsonData = Lib.ReadJsonFile('LabsData.txt')
            print('select One of These Test that are in same labs')
            for item in jsonData:
                print('[', end = '')
                for test in jsonData[item]['tests']:
                    print(test[0],',',end=' ')
                print(']')

            numOfTests = int(input("enter number of tests : "))
            listOfTests = []
            while numOfTests != 0:
                test = input('Write your Tests\n')
                listOfTests.append(test)
                numOfTests -= 1

            labIds = requestController.RequestListOfAvailableLabs(listOfTests, patient.GetCurrentRequest())
            print(labIds)
            if(labIds == []):
                raise Exception('sry there is no avialable lab for these tests we truely HOPE you become Well,GoodLock!')
            LabId = input('pls select one of these Labs : ')
            listOfSlots = requestController.SetSelectedLabAndGetTimeSlot(LabId,  patient.GetCurrentRequest())
            if(listOfSlots = []):
                raise Exception('pls enter correct Lab Name!')
            print(listOfSlots)
            selectedSlot = input("please select from one of these time slots ")
            # print("please select from one of these time slots!")
            # selectedSlot = listOfSlots[0][0]
            Total_cost = requestController.SelectTimeSlotAndCalcTotalCost(LabId, selectedSlot, patient.GetCurrentRequest())
            print(Total_cost)
            requestController.PayFinalCost(Total_cost, patient.GetCurrentRequest())

        else:
            print('bye bye')
    except Exception as e:
        print('Error: ',e)
