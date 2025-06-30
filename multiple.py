from modules import findMultiple
from fileHandler import *


def getMultiple(list):
    answer = []
    if list != None:
        for each in list:
            answer.append(findMultiple(each[0], each[1], each[2]))
        writeToFile(answer)
        print("!! Success !!")


getMultiple(readFile())
