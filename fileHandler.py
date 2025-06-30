def inputHandler(data):
    result = ""
    for each in data:
        if len(each) == 3:
            result = "ok"
        else:
            result = "no"
            break
    return result


def readFile():
    newList = []
    with open("files/input.txt", "r") as file:
        for line in file:
            numbers = list(map(int, line.strip().split()))
            newList.append(numbers)
    if inputHandler(newList) == "ok":
        return newList
    else:
        print("Input format incorrect ")
        return None


def writeToFile(data):
    with open("files/output.txt", "w") as file:
        for item in data:
            first_number = item[0]
            number_list = item[2]
            file.write(f"{first_number} {number_list}\n")
