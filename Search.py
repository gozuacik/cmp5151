
# Reference
# https://www.geeksforgeeks.org/linear-search/
# https://www.geeksforgeeks.org/binary-search/
# https://www.geeksforgeeks.org/jump-search/
# https://www.geeksforgeeks.org/interpolation-search/

from datetime import datetime
import time
import random
import math
import matplotlib.pyplot as plt
import numpy as np


# 0 50000 99999
# ArrayLenght
arrayLength = 100000

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


# Template Method
class PeformanceSearch:
    def __init__(self,title):
        self.timeStart = 0
        self.timeStop = 0
        self.title = title
        self.elapsedTime = 0
        self.numberofSteps = 0
        self.foundIndex = -1

    def startTime(self):
        tempTime= datetime.time(datetime.now())
        self.timeStart = (tempTime.second*1000) + (tempTime.microsecond/1000)
        #self.timeStart = float(datetime.time(datetime.now()).microsecond)
        print("Start Time: ",self.timeStart)

    def stopTime(self):
        tempTime = datetime.time(datetime.now())
        self.timeStop = (tempTime.second*1000) + (tempTime.microsecond/1000)
        #self.timeStop = float(datetime.time(datetime.now()).microsecond)
        print("Stop Time: ", self.timeStop)

    def calcTime(self):
        #print(type(self.timeStop - self.timeStart))
        self.elapsedTime = float(self.timeStop - self.timeStart)
        #self.elapsedTime = float(self.timeStop - self.timeStart)
        print(self.title, " Elapsed Time: ", self.elapsedTime)

    def search(self,arr,n,x):
        return -1

    def getElsapedTime(self):
        print("Elapsed Time: ", self.elapsedTime)
        return self.elapsedTime

    def getNumberofSteps(self):
        print("Number of Steps: ", self.numberofSteps)
        return self.numberofSteps

    def measurePerformance(self,arr,n,x):
        self.startTime()
        self.foundIndex = self.search(arr,n,x)
        self.stopTime()
        self.calcTime()
        return self.foundIndex,self.elapsedTime,self.numberofSteps

    def __iter__(self):
        return SearchIterator(self)


class SearchObjects():
    def __init__(self, searchTypes):
        self.searchTypes = searchTypes
        self.searchMax = len(searchTypes)

    def __iter__(self):
        return SearchIterator(self)

# Iterator Pattern
class SearchIterator(object):
    "An iterator."

    def __init__(self, container):
        self.container = container
        self.n = -1

    def __next__(self):
        self.n += 1
        if self.n >= self.container.searchMax:
            raise StopIteration
        return self.container.searchTypes[self.n],self.n

    def __iter__(self):
        return self


class LinearSearch(PeformanceSearch):
    def search(self,arr, n, x):
        #start_time=float(datetime.time(datetime.now()).microsecond)
        #print(start_time)
        self.numberofSteps=0
        for i in range(0, n):
            self.numberofSteps = self.numberofSteps + 1
            if arr[i] == x:
                #stop_time = float(datetime.time(datetime.now()).microsecond)
                #print(stop_time)
                #self.elapsedTime = float(stop_time - start_time)
                return i
        return -1


class BinarySearch(PeformanceSearch):
    def search(self,arr, n, x):
        l = 0
        r = n
        #start_time=float(datetime.time(datetime.now()).microsecond)
        #print(start_time)
        self.numberofSteps = 0
        while l <= r:
            self.numberofSteps = self.numberofSteps + 1
            mid = int(l + (r - l) / 2)
            #print("L R Mid:", l,r,mid)

            # Check if x is present at mid
            if arr[mid] == x:
                #stop_time = float(datetime.time(datetime.now()).microsecond)
                #print(stop_time)
                #self.elapsedTime = float(stop_time - start_time)
                return mid

            # If x is greater, ignore left half
            elif arr[mid] < x:
                l = mid + 1

            # If x is smaller, ignore right half
            else:
                r = mid - 1

        # If we reach here, then the element
        # was not present
        return -1



class JumpSearch(PeformanceSearch):
    def search(self,arr, n, x):

        # Finding block size to be jumped
        step = math.sqrt(n)

        # Finding the block where element is
        # present (if it is present)
        prev = 0
        #start_time=float(datetime.time(datetime.now()).microsecond)
        #print(start_time)
        self.numberofSteps = 0
        while arr[int(min(step, n) - 1)] < x:
            self.numberofSteps = self.numberofSteps + 1
            prev = step
            step += math.sqrt(n)
            if prev >= n:
                return -1

        # Doing a linear search for x in
        # block beginning with prev.
        while arr[int(prev)] < x:
            prev += 1

            # If we reached next block or end
            # of array, element is not present.
            if prev == min(step, n):
                return -1

        # If element is found
        if arr[int(prev)] == x:
            #stop_time = float(datetime.time(datetime.now()).microsecond)
            #print(stop_time)
            #self.elapsedTime = float(stop_time - start_time)
            return prev

        return -1



class InterpolationSearch(PeformanceSearch):
    def search(self,arr, n, x):
        # Find indexs of two corners
        lo = 0
        hi = (n - 1)
        #start_time=float(datetime.time(datetime.now()).microsecond)
        #print(start_time)
        self.numberofSteps = 0
        # Since array is sorted, an element present
        # in array must be in range defined by corner
        while lo <= hi and x >= arr[lo] and x <= arr[hi]:
            self.numberofSteps = self.numberofSteps + 1
            # Probing the position with keeping
            # uniform distribution in mind.
            pos = lo + int(((float(hi - lo) /
                             (arr[hi] - arr[lo])) * (x - arr[lo])))

            # Condition of target found
            if arr[pos] == x:
                #stop_time = float(datetime.time(datetime.now()).microsecond)
                #print(stop_time)
                #self.elapsedTime = float(stop_time - start_time)
                return pos

            # If x is larger, x is in upper part
            if arr[pos] < x:
                lo = pos + 1

            # If x is smaller, x is in lower part
            else:
                hi = pos - 1

        return -1

# Simple Factory Method
class SearchFactory():
   def buildSearch(self, typ):
       if typ == 'Linear':
          return LinearSearch('Linear Search')
       elif typ == 'Binary':
           return BinarySearch('Binary Search')
       elif typ == 'Jump':
           return JumpSearch('Jump Search')
       elif typ == 'Interpolation':
           return InterpolationSearch('Interpolation Search')


class CaseFactory():
   def buildCase(self, typ):
       if typ == 'Best':
          return BestCase()
       elif typ == 'Worst':
           return WorstCase()
       elif typ == 'Average':
           return AverageCase()

#searchTypes = ['Best', 'Worst', 'Average']
usecases = CaseFactory().buildCase('Best')
usecases.setArray()

searchCases = ['Best','Worst','Average']
searchElement = {'Best':9999,'Worst':99999,'Average':50000}
searchTypes = ['Linear', 'Binary', 'Jump','Interpolation']
searchobjects = SearchObjects(searchTypes)

#timeStat=list()
#stepStat=list()

# Initialize statistical variables
timeStat = [[0 for x in range(len(searchCases))] for y in range(len(searchTypes))]
stepStat= [[0 for x in range(len(searchCases))] for y in range(len(searchTypes))]

#for iter in range(0,len(searchTypes)):
for iter,order in searchobjects:
    for newiter in range(0,len(searchCases)):
        search_factory = SearchFactory()
        #alg = search_factory.buildSearch(searchTypes[iter])
        #alg = search_factory.buildSearch(iter)
        totaltime=0
        step=0
        # Running the algorithm for 10 times to compute the average result
        for epoch in range(0,10):
            alg = search_factory.buildSearch(iter)
            index, time, step = alg.measurePerformance(usecases.getArray(), arrayLength, searchElement[searchCases[newiter]])
            #print("mmmm",step)
            totaltime = totaltime + time
        timeStat[order][newiter]=totaltime/10
        stepStat[order][newiter]=step


print("Time Stat",timeStat)
print("Step",stepStat)

#plt.plot(searchTypes, timeStat, 'g', label='Train Loss')
#plt.plot(searchTypes, stepStat,'b', label='Validation Loss')
#plt.xticks(np.arange(rStart, rStop, 1))

# Individual graphics for Time Performance
for iter in range(0,len(searchTypes)):
    plt.bar(searchCases, timeStat[iter], align='center', alpha=0.5)
    plt.title(searchTypes[iter])
    plt.xlabel('Time Performance for '+searchTypes[iter])
    plt.ylabel('Time in Milisecons')
    plt.tight_layout()
    plt.show()

# Individual graphics for Complexity Performance
for iter in range(0,len(searchTypes)):
    plt.bar(searchCases, stepStat[iter], align='center', alpha=0.5)
    plt.title(searchTypes[iter])
    plt.xlabel('Number of Steps Performance for '+searchTypes[iter])
    plt.ylabel('Number of Steps')
    plt.tight_layout()
    plt.show()


fig, ax = plt.subplots()
index = np.arange(len(searchCases))
bar_width = 0.35
opacity = 0.8
colors=['b','r','m','g']

# All graphics for Time Performance
for iter in range(0,len(searchTypes)):
    plt.bar(index+(iter*bar_width), timeStat[iter],bar_width/2,alpha=opacity,color=colors[iter],label=searchTypes[iter])
    #index=index+bar_width

#plt.ylim(, 100000)
#plt.yticks(np.arange(0, 100000, 500))
plt.xlabel('Test Cases')
plt.ylabel('Timer in Miliseconds')
plt.title('Time Performance for Search Algorithms')
plt.xticks(index + bar_width, searchCases)
plt.legend()

plt.tight_layout()
plt.show()

# All graphics for Complexity Performance
for iter in range(0,len(searchTypes)):
    plt.bar(index+(iter*bar_width), stepStat[iter],bar_width/2,alpha=opacity,color=colors[iter],label=searchTypes[iter])
    #index=index+bar_width

#plt.ylim(, 100000)
#plt.yticks(np.arange(0, 100000, 500))
plt.xlabel('Test Cases')
plt.ylabel('Number of Steps')
plt.title('Complexity Performance for Search Algorithms')
plt.xticks(index + bar_width, searchCases)
plt.legend()

plt.tight_layout()
plt.show()









#plt.xticks(searchTypes, objects)
#plt.ylabel('Usage')
#plt.title('Programming language usage')


#plt.legend()


#result = alg.search(usecases.getArray(), arrayLength, searchElement)


'''
if index == -1:
    print("Element is not present in array")
else:
    print("Element is present at index", index)
    print("Time: ",time)
    print("Step: ",step)
'''

