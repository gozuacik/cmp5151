## Reference
#https://www.geeksforgeeks.org/selection-sort/
#https://www.geeksforgeeks.org/quick-sort/
#https://www.geeksforgeeks.org/merge-sort/
#https://www.geeksforgeeks.org/bubble-sort/

from datetime import datetime
import random
import math
import sys

# 0 50000 99999
# ArrayLenght
arrayLength = 10

class UseCase:
    def __init__(self):
        self.array = list()

    def setArray(self): pass

    def getArray(self): pass

# list is ordered like 0 ....99999
class BestCase(UseCase):
    def setArray(self):
        r = range(arrayLength)
        self.array = list(r)
        print("Array[0]...Array[",arrayLength- 1, "]: ",self.array[0],self.array[arrayLength-1])

    def getArray(self):
        return self.array


# list is ordered reverse like 99999....0000
class WorstCase(UseCase):
    def setArray(self):
        r = sorted(range(arrayLength),reverse = True)
        self.array = list(r)
        print("Array[0]...Array[",arrayLength- 1, "]: ",self.array[0],self.array[arrayLength-1])

    def getArray(self):
        return self.array

# list is shuffled.
class AverageCase(UseCase):
    def setArray(self):
        r = range(arrayLength)
        self.array = list(r)
        random.shuffle(self.array)  # shuffle ????
        print("Array[0]...Array[",arrayLength- 1, "]: ",self.array[0],self.array[arrayLength-1])

    def getArray(self):
        return self.array

# template method
class PerformanceSearch:
    def __init__(self,title):
        self.timeStart = 0
        self.timeStop = 0
        self.title = title
        self.elapsedTime = 0
        self.numberofSteps = 0
        self.foundIndex = -1

    def startTime(self):
        self.timeStart = float (datetime.time(datetime.now()).microsecond)
        print("Start Time : ", self.timeStart)

    def stopTime(self):
        self.timeStop = float (datetime.time(datetime.now()).microsecond)
        print("Stop Time : ",self.timeStop)

    def calcTime(self):
        self.elapsedTime = float(self.timeStop - self.timeStart)
        print("Elapsed Time : ", self.elapsedTime)

    def sort(self,arr):
        return list

    def getElapsedTime(self):
        print("Elapsed Time : ", self.elapsedTime)
        return self.elapsedTime

    def getNumberOfSteps(self):
        print("Number of Steps: ", self.numberofSteps)
        return self.numberofSteps

    def measurePerformance(self,arr):
        self.startTime()
        self.stopTime()
        self.calcTime()
        return self.elapsedTime,self.numberofSteps

class BubbleSort(PerformanceSearch):
    def sort(self,arr):
        #start_time=float(datetime.time(datetime.now()).microsecond)
        #print(start_time)
        n = len(arr)
        for i in range(n):
            self.numberofSteps = self.numberofSteps + 1
            swapped = False
            for j in range(0, n - i - 1):
                self.numberofSteps = self.numberofSteps + 1
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            if swapped == False:
                break
        # stop_time = float(datetime.time(datetime.now()).microsecond)
        # print(stop_time)
        # self.elapsedTime = float(stop_time - start_time)
        return arr

class MergeSort(PerformanceSearch):
    def sort(self,arr):
        #start_time=float(datetime.time(datetime.now()).microsecond)
        #print(start_time)
        if len(arr)>1:
            mid = len(arr)//2
            L = arr[:mid]
            R = arr[mid:]

           # sortfactory(L)
           # MergeSort(R)
            i = j = k = 0

            # copy data to temp arrays L[] and R[]
            while i< len(L) and j < len(R):
                self.numberofSteps = self.numberofSteps + 1
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i+=1
                else:
                    arr[k] = R[j]
                    j+=1
                k+=1

            #Checking if any element was left
            while i<len(L):
                 self.numberofSteps = self.numberofSteps + 1
                 arr[k] = L[i]
                 i+=1
                 k+=1

            while j<len(R):
                self.numberofSteps = self.numberofSteps + 1
                arr[k] = R[j]
                j+=1
                k+=1
        # stop_time = float(datetime.time(datetime.now()).microsecond)
        # print(stop_time)
        # self.elapsedTime = float(stop_time - start_time)
        return arr

class SelectionSort(PerformanceSearch):
    def sort(self,arr):
        for i in range(len(arr)):
            self.numberofSteps = self.numberofSteps + 1
            # Find the minimum element in remaining
            # unsorted array
            min_idx = i
            for j in range(i + 1, len(arr)):
                self.numberofSteps = self.numberofSteps + 1
                if arr[min_idx] > arr[j]:
                    min_idx = j

            # Swap the found minimum element with
            # the first element
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        # stop_time = float(datetime.time(datetime.now()).microsecond)
        # print(stop_time)
        # self.elapsedTime = float(stop_time - start_time)
        return arr


class QuickSort(PerformanceSearch):
    def partition(arr, low, high):
        i = (low - 1)
        pivot = arr[high]

        for j in range(low, high):
            if arr[j] <= pivot:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return (i + 1)

    def sort(self, arr):
        n = len(arr)
        low = 0
        high = n - 1

        #if low < high:

            #pi = partition(arr, low, high)

            # method QuickSort (arr, low,pi -1)
            # method QuickSort (arr, pi+ 1,high)


# Simple factory method
class SortFactory:
    def buildSort(self,type):
        if type == "Bubble":
            return BubbleSort("Bubble Sort")
        elif type == "Merge":
            return MergeSort("Merge Sort")
        elif type == "Quick":
            return QuickSort("Quick Sort")
        elif type == "Selection":
            return SelectionSort("Selection Sort")

class CaseFactory():
    def buildCase(self,type):
        if type == "Best":
            return BestCase()
        elif type =="Worst":
            return WorstCase()
        elif type == "Average":
            return AverageCase()


#Case = ["Best","Worst", "Average"]
usecases = CaseFactory().buildCase("Average")
usecases.setArray()

#sortTypes = ["Bubble,"Merge","Selection, "Quick"]
sortfactory = SortFactory()
alg = sortfactory.buildSort("Merge")

sortedarry = alg.sort(usecases.getArray())

time,steps = alg.measurePerformance(usecases.getArray())

print("The sorted list is :")
for i in range (len(sortedarry)):
    print(sortedarry[i])

print("Time: ",time)
print("Step: ",steps)