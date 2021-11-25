


def main():
    numberOfFlightSchedules = int(input(f"Please enter the number of flight schedules: "))
    masterList = flightScheduleInputs(numberOfFlightSchedules)
    newMasterList = listToString(masterList)
    inputToFiles(newMasterList)

def flightScheduleInputs(numberOfFS):
    masterFlightSchedules = []
    for n in range(numberOfFS):
        flightSchedule = []
        flightNumber = input(f"Please enter the flight number: ")
        flightSchedule.append(flightNumber)
        origin = input(f"Please enter the origin: ")
        flightSchedule.append(origin)
        departureDate = input(f"Please enter the depature date: ")
        flightSchedule.append(departureDate)
        departureTime = input(f"Please enter the departure time: ")
        flightSchedule.append(departureTime)
        destination = input(f"Please enter the destination: ")
        flightSchedule.append(destination)
        arrivalDate = input(f"Please enter the arrival date: ")
        flightSchedule.append(arrivalDate)
        arrivalTime = input(f"Please enter the arrival time: ")
        flightSchedule.append(arrivalTime)
        masterFlightSchedules.append(flightSchedule)
    return masterFlightSchedules

def listToString(list):
    listOfStrings = []
    for item in list:
        itemString = "#".join(item)
        listOfStrings.append(itemString)
    return listOfStrings

def stringToList(stringList):
    listOfList = []
    for item in stringList:
        itemList = item.split("#")
        listOfList.append(itemList)
    return listOfList

def inputToFiles(sch):
    while True:
        choice = input("Would you like to save this file? 1. for yes and 2. for no")
        if choice == "1":
                flights = open("Flight Schedules", "w")
                schedules = "\n".join(sch)
                flights.write(schedules)
                flights.close()
                break
        elif choice == "2":
            print("The data is not saved.")
            return None
        else:
            print("Enter a valid option!")
            continue

main()