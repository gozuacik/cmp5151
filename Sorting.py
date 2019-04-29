## Reference
#https://www.geeksforgeeks.org/selection-sort/
#https://www.geeksforgeeks.org/quick-sort/
#https://www.geeksforgeeks.org/merge-sort/
#https://www.geeksforgeeks.org/bubble-sort/

from datetime import datetime
import datetime
import time
import random
import math
import matplotlib.pyplot as plt
import numpy as np
from timeit import default_timer as timer


# 0 50000 99999
# ArrayLenght
arrayLength = 1000

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
        random.shuffle(self.array)
        print("Array[0]...Array[",arrayLength- 1, "]: ",self.array[0],self.array[arrayLength-1])

    def getArray(self):
        return self.array

# Template method
class PerformanceSearch:
    def __init__(self,title):
        self.timeStart = 0
        self.timeStop = 0
        self.title = title
        self.elapsedTime = 0
        self.numberofSteps = 0


    def startTime(self):
        #tempTime = datetime.time(datetime.now())
        self.timeStart =  timer()
        #self.timeStart = (tempTime.second*1000) + (tempTime.microsecond/1000)
        # self.timeStart = float(datetime.time(datetime.now()).microsecond)
        print("Start Time: ",datetime.datetime.now())


    def stopTime(self):
        #tempTime = datetime.time(datetime.now())
        self.timeStop = timer()
        #self.timeStop = (tempTime.second*1000) + (tempTime.microsecond/1000)
        #self.timeStop = float(datetime.time(datetime.now()).microsecond)
        print("Stop Time: ", datetime.datetime.now())

    def calcTime(self):
        #print(type(self.timeStop - self.timeStart))
        self.elapsedTime = self.timeStop - self.timeStart
        tempTimer = int(self.elapsedTime)
#        self.elapsedTime = datetime.datetime(self.timeStop - self.timeStart)
        print(self.title, " Elapsed Time = ",self.elapsedTime)
#        print('{:02d}:{:02d}:{:02d}'.format(tempTimer// 3600, (tempTimer % 3600 // 60), tempTimer % 60))


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
        self.sort(arr)
        self.stopTime()
        self.calcTime()
        return self.elapsedTime, self.numberofSteps

    def __iter__(self):
        return SortIterator(self)

class SortObjects():
    def __init__(self, sortTypes):
        self.sortTypes = sortTypes
        self.sortMax = len(sortTypes)

    def __iter__(self):
        return SortIterator(self)

# Iterator Pattern
class SortIterator(object):
    "An iterator."

    def __init__(self, container):
        self.container = container
        self.n = -1

    def __next__(self):
        self.n += 1
        if self.n >= self.container.sortMax:
            raise StopIteration
        return self.container.sortTypes[self.n],self.n

    def __iter__(self):
        return self

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
        if len(arr) > 1:
            mid = len(arr) // 2
            lefthalf = arr[:mid]
            righthalf = arr[mid:]

            self.sort(lefthalf)
            self.sort(righthalf)
            i = j = k = 0
            while i < len(lefthalf) and j < len(righthalf):
                self.numberofSteps = self.numberofSteps + 1
                if lefthalf[i] < righthalf[j]:
                    arr[k] = lefthalf[i]
                    i = i + 1
                else:
                    arr[k] = righthalf[j]
                    j = j + 1
                k = k + 1

            while i < len(lefthalf):
                self.numberofSteps = self.numberofSteps + 1
                arr[k] = lefthalf[i]
                i = i + 1
                k = k + 1

            while j < len(righthalf):
                self.numberofSteps = self.numberofSteps + 1
                arr[k] = righthalf[j]
                j = j + 1
                k = k + 1
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
'''
class QuickSort(PerformanceSearch):
    def sort(self, arr):
        n = len(arr)
        self.quickSort(arr, 0, n - 1)
        return arr

    def partition(self, arr, low, high):
            i = (low - 1)  # index of smaller element
            pivot = arr[high]  # pivot

            for j in range(low, high):
                self.numberofSteps = self.numberofSteps + 1
                # If current element is smaller than or
                # equal to pivot
                if arr[j] <= pivot:
                    # increment index of smaller element
                    i = i + 1
                    arr[i], arr[j] = arr[j], arr[i]

            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            return (i + 1)

    # Function to do Quick sort
    def quickSort(self,arr, low, high):
        if low < high:
            pi = self.partition(arr, low, high)

            self.quickSort(arr, low, pi - 1)
            self.quickSort(arr, pi + 1, high)
'''


# Python code to implement Stable QuickSort.
# The code uses middle element as pivot.
class QuickSort(PerformanceSearch):
    def sort(self, arr):

        if len(arr) <= 1:
            return arr
            # Let us choose middle element a pivot
        else:
            mid = len(arr) // 2
            pivot = arr[mid]

        # key element is used to break the array
        # into 2 halves according to their values
        smaller, greater = [], []

        # Put greater elements in greater list,
        # smaller elements in smaller list. Also,
        # compare positions to decide where to put.
        for indx, val in enumerate(arr):
            self.numberofSteps = self.numberofSteps + 1
            if indx != mid:
                if val < pivot:
                    smaller.append(val)
                elif val > pivot:
                    greater.append(val)

                # If value is same, then considering
                # position to decide the list.
                else:
                    if indx < mid:
                        smaller.append(val)
                    else:
                        greater.append(val)
        return self.sort(smaller) + [pivot] + self.sort(greater)

# Simple Factory Method
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


#sortTypes = ['Best', 'Worst', 'Average']
#usecases = CaseFactory().buildCase('Average')
#usecases.setArray()

sortCases = ['Best', 'Worst', 'Average']
sortTypes = ['Bubble','Merge','Selection', 'Quick']
sortobjects = SortObjects(sortTypes)

epochs = 10

def runSort(sorttype, sortcase):
    sort_factory = SortFactory()
    alg = sort_factory.buildSort(sorttype)
    tStat = list()
    sStat = list()
    if sortcase == 'All':
        for newiter in range(0, len(sortCases)):
            totaltime = 0
            step = 0
            usecases = CaseFactory().buildCase(sortCases[newiter])
            usecases.setArray()

            for epoch in range(0, epochs):
                time, step = alg.measurePerformance(usecases.getArray())
                totaltime = totaltime + time
            tStat.append(totaltime/epochs)
            sStat.append(step)
    else:
        usecases = CaseFactory().buildCase(sortcase)
        usecases.setArray()
        totaltime=0
        for epoch in range(0, epochs):
            time, step = alg.measurePerformance(usecases.getArray())
            totaltime = totaltime + time
        tStat.append(totaltime / epochs)
        sStat.append(step)

    #return   tStat,sStat
    if sortcase == 'All':
        index = np.arange(len(sortCases))
        bar_width = 0.35
        opacity = 0.8
        colors = ['b', 'r', 'm']
        plt.bar(index + bar_width, tStat, bar_width / 2, alpha=opacity, color=colors)
        # plt.ylim(, 100000)
        # plt.yticks(np.arange(0, 100000, 500))
        plt.xlabel('Test Cases')
        plt.ylabel('Time in Miliseconds')
        plt.title('Time Performance for ' + sorttype + ' Sorting Algorithm')
        plt.xticks(index + bar_width, sortCases)
        plt.legend()

        plt.tight_layout()
        plt.show()

        plt.bar(index + bar_width, sStat, bar_width / 2, alpha=opacity, color=colors)
        # plt.ylim(, 100000)
        # plt.yticks(np.arange(0, 100000, 500))
        plt.xlabel('Test Cases')
        plt.ylabel('Number of Steps')
        plt.title('Complexity Performance for ' + sorttype + ' Sorting Algorithm')
        plt.xticks(index + bar_width, sortCases)
        plt.legend()

        plt.tight_layout()
        plt.show()
    else:

        plt.bar(sortcase, tStat, align='center', alpha=0.5)
        plt.title(sorttype)
        plt.xlabel('Time Performance for ' + sorttype)
        plt.ylabel('Time in Milisecons')
        plt.tight_layout()
        plt.show()

        plt.bar(sortcase, sStat, align='center', alpha=0.5)
        plt.title(sorttype)
        plt.xlabel('Complexity Performance for ' + sorttype)
        plt.ylabel('Number of Steps')
        plt.tight_layout()
        plt.show()



def runAll(sorttype, sortcase):
    sort_factory = SortFactory()

    if sortcase == 'All':
        tStat = [[0 for x in range(len(sortCases))] for y in range(len(sortTypes))]
        sStat = [[0 for x in range(len(sortCases))] for y in range(len(sortTypes))]
        for iter, order in sortobjects:
            print(iter)
            alg = sort_factory.buildSort(iter)
            for newiter in range(0, len(sortCases)):
                totaltime = 0
                step = 0
                usecases = CaseFactory().buildCase(sortCases[newiter])
                usecases.setArray()
                for epoch in range(0, epochs):
                    time, step = alg.measurePerformance(usecases.getArray())
                    totaltime = totaltime + time
                tStat[order][newiter] = totaltime / epochs
                sStat[order][newiter] = step

        print(tStat)
        index = np.arange(len(sortCases))
        bar_width = 0.35
        opacity = 0.8
        colors = ['b', 'r', 'm', 'g']
        # All graphics for Time Performance
        for iter in range(0, len(sortTypes)):
            plt.bar(index + (iter * bar_width), tStat[iter], bar_width / 2, alpha=opacity, color=colors[iter],
                    label=sortTypes[iter])
            # index=index+bar_width

        # plt.ylim(, 100000)
        # plt.yticks(np.arange(0, 100000, 500))
        plt.xlabel('Test Cases')
        plt.ylabel('Time in Miliseconds')
        plt.title('Time Performance for Sorting Algorithms')
        plt.xticks(index + bar_width, sortCases)
        plt.legend()

        plt.tight_layout()
        plt.show()

        for iter in range(0, len(sortTypes)):
            plt.bar(index + (iter * bar_width), sStat[iter], bar_width / 2, alpha=opacity, color=colors[iter],
                    label=sortTypes[iter])
            # index=index+bar_width

        # plt.ylim(, 100000)
        # plt.yticks(np.arange(0, 100000, 500))
        plt.xlabel('Test Cases')
        plt.ylabel('Number of Steps')
        plt.title('Complexity Performance for Sorting Algorithms')
        plt.xticks(index + bar_width, sortCases)
        plt.legend()

        plt.tight_layout()
        plt.show()

    else:
        #tStat = [[0 for x in range(0,1)] for y in range(len(searchTypes))]
        #sStat = [[0 for x in range(0,1)] for y in range(len(searchTypes))]
        tStat = list()
        sStat = list()
        for iter, order in sortobjects:
            print(iter)
            alg = sort_factory.buildSort(iter)
            totaltime = 0
            step = 0
            usecases = CaseFactory().buildCase(sortcase)
            usecases.setArray()
            for epoch in range(0, epochs):
                time, step = alg.measurePerformance(usecases.getArray())
                totaltime = totaltime + time
            tStat.append(totaltime / epochs)
            sStat.append(step)

        index = np.arange(len(sortTypes))
        bar_width = 0.35
        opacity = 0.8
        colors = ['b', 'r', 'm', 'g']
        plt.bar(index + bar_width, tStat, bar_width / 2, alpha=opacity, color=colors)
        # plt.ylim(, 100000)
        # plt.yticks(np.arange(0, 100000, 500))
        plt.xlabel('Test Cases')
        plt.ylabel('Time in Miliseconds')
        plt.title('Time Performance for ' + sorttype + ' Sorting Algorithm')
        plt.xticks(index + bar_width, sortTypes)
        plt.legend()

        plt.tight_layout()
        plt.show()

        plt.bar(index + bar_width, sStat, bar_width / 2, alpha=opacity, color=colors)
        # plt.ylim(, 100000)
        # plt.yticks(np.arange(0, 100000, 500))
        plt.xlabel('Test Cases')
        plt.ylabel('Number of Steps')
        plt.title('Complexity Performance for ' + sorttype + ' Sorting Algorithm')
        plt.xticks(index + bar_width, sortCases)
        plt.legend()

        plt.tight_layout()
        plt.show()


#runSort('Selection','Worst')
#runSort('Selection','All')
#runAll('All','Worst')

'''
sortfactory = SortFactory()
alg = sortfactory.buildSort("Selection")

sortedarry = alg.sort(usecases.getArray())

time,steps = alg.measurePerformance(usecases.getArray())

print("The sorted list is :")
for i in range (len(sortedarry)):
    print(sortedarry[i])

print("Time: ",time)
print("Step: ",steps)
'''