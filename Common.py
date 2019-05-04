# Command types and data
import random

# 0 50000 99999
# ArrayLenght
arrayLength = 1000


class UseCases():
    def __init__(self):
        self.Array = list()

    def setArray(self):
        pass

    def getArray(self):
        pass

# List is ordered like 0...99999
class BestCase(UseCases):
    def setArray(self):
        r = range(arrayLength)
        self.Array = list(r)
        print("Array[0]...Array[",arrayLength-1,"]: ",self.Array[0],self.Array[arrayLength-1])

    def getArray(self):
        return self.Array

# List is ordered reverse like 999999...0
class WorstCase(UseCases):
    def setArray(self):
        r = sorted(range(arrayLength),reverse=True)
        self.Array = list(r)
        print("Array[0]...Array[",arrayLength-1,"]: ",self.Array[0],self.Array[arrayLength-1])

    def getArray(self):
        return self.Array

# List is shuffled.
class AverageCase(UseCases):
    def setArray(self):
        r = range(arrayLength)
        self.Array = list(r)
        random.shuffle(self.Array)
        print("Array[0]...Array[",arrayLength-1,"]: ",self.Array[0],self.Array[arrayLength-1])

    def getArray(self):
        return self.Array


class CaseFactory():
    def buildCase(self,type):
        if type == "Best":
            return BestCase()
        elif type =="Worst":
            return WorstCase()
        elif type == "Average":
            return AverageCase()


# Template method
class Performance:
    def __init__(self,title):
        self.timeStart = 0
        self.timeStop = 0
        self.title = title
        self.elapsedTime = 0
        self.numberofSteps = 0

    def startTime(self):
        pass

    def stopTime(self):
        pass

    def calcTime(self):
        pass

    def getElapsedTime(self):
        pass

    def getNumberOfSteps(self):
        pass

    def measurePerformance(self,arr):
        pass

    def __iter__(self):
        pass
