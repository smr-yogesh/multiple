def inputHandler(data):
    result = ""
    for each in data:
        if len(each) == 3:
            result = "ok"
        else:
            result = "ko"
            break
    return result


def checkIfBigTarget(data):
    result = ""
    for x in data:
        if x[0] < x[2] and x[1] < x[2]:
            result = "ok"
        else:
            result = "ko"
            break
    return result


def checkIfZero(data):
    result = ""
    for x in data:
        if x[0] == 0 or x[1] == 0 or x[2] == 0:
            result = "ko"
            break
        else:
            result = "ok"
    return result


def readFile():
    newList = []
    with open("files/input.txt", "r") as file:
        for line in file:
            numbers = list(map(int, line.strip().split()))
            newList.append(numbers)
    if inputHandler(newList) == "ok":
        if checkIfBigTarget(newList) == "ok":
            if checkIfZero(newList) == "ok":
                return newList
            else:
                print("no values can be zero")
        else:
            print(" All target should be bigger than divisibles")
    else:
        print("Input format incorrect ")
        return None


def writeToFile(data):
    with open("files/output.txt", "w") as file:
        for item in data:
            first_number = item[0]
            number_list = item[2]
            file.write(f"{first_number} {number_list}\n")
