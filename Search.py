# Reference
# https://www.geeksforgeeks.org/linear-search/
# https://www.geeksforgeeks.org/binary-search/
# https://www.geeksforgeeks.org/jump-search/
# https://www.geeksforgeeks.org/interpolation-search/

import math
import matplotlib.pyplot as plt
import numpy as np
import Common
from timeit import default_timer as timer


# Template Method
class PeformanceSearch(Common.Performance):
    def __init__(self,title):
        self.timeStart = 0
        self.timeStop = 0
        self.title = title
        self.elapsedTime = 0
        self.numberofSteps = 0
        self.foundIndex = -1

    def startTime(self):
        #tempTime= datetime.time(datetime.now())
        #self.timeStart = (tempTime.second*1000) + (tempTime.microsecond/1000)
        self.timeStart = timer()
        #self.timeStart = float(datetime.time(datetime.now()).microsecond)
        print("Start Time: ",self.timeStart)

    def stopTime(self):
        #tempTime = datetime.time(datetime.now())
        #self.timeStop = (tempTime.second*1000) + (tempTime.microsecond/1000)
        self.timeStop = timer()
        #self.timeStop = float(datetime.time(datetime.now()).microsecond)
        print("Stop Time: ", self.timeStop)

    def calcTime(self):
        #print(type(self.timeStop - self.timeStart))
        self.elapsedTime = float(self.timeStop - self.timeStart)*1000
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


#searchTypes = ['Best', 'Worst', 'Average']
arrayLength = 100000
#usecases = Common.CaseFactory().buildCase('Best')
#usecases.setArray()
useArray =  list(range(arrayLength))

searchCases = ['Best','Worst','Average']
searchElement = {'Best':9999,'Worst':99999,'Average':50000}
searchTypes = ['Linear', 'Binary', 'Jump','Interpolation']
searchobjects = SearchObjects(searchTypes)

#timeStat=list()
#stepStat=list()

# Initialize statistical variables
#timeStat = [[0 for x in range(len(searchCases))] for y in range(len(searchTypes))]
#stepStat= [[0 for x in range(len(searchCases))] for y in range(len(searchTypes))]

# Number of running algorithm consecutively
epochs=10

def runSearch(searchtype, searchcase):
    search_factory = SearchFactory()
    alg = search_factory.buildSearch(searchtype)
    tStat = list()
    sStat = list()
    if searchcase == 'All':
        for newiter in range(0, len(searchCases)):
            totaltime = 0
            step = 0
            for epoch in range(0, epochs):
                index, time, step = alg.measurePerformance(useArray, arrayLength,
                                                           searchElement[searchCases[newiter]])
                totaltime = totaltime + time
            tStat.append(totaltime/epochs)
            sStat.append(step)
    else:
        totaltime=0
        for epoch in range(0, epochs):
            index, time, step = alg.measurePerformance(useArray, arrayLength,searchElement[searchcase])
            totaltime = totaltime + time
        tStat.append(totaltime / epochs)
        sStat.append(step)

    #return   tStat,sStat
    if searchcase == 'All':
        index = np.arange(len(searchCases))
        bar_width = 0.35
        opacity = 0.8
        colors = ['b', 'r', 'm']
        plt.bar(index + bar_width, tStat, bar_width / 2, alpha=opacity, color=colors)
        # plt.ylim(, 100000)
        # plt.yticks(np.arange(0, 100000, 500))
        plt.xlabel('Test Cases')
        plt.ylabel('Time in Miliseconds')
        plt.title('Time Performance for ' + searchtype + ' Search Algorithm')
        plt.xticks(index + bar_width, searchCases)
        plt.legend()

        plt.tight_layout()
        plt.show()

        plt.bar(index + bar_width, sStat, bar_width / 2, alpha=opacity, color=colors)
        # plt.ylim(, 100000)
        # plt.yticks(np.arange(0, 100000, 500))
        plt.xlabel('Test Cases')
        plt.ylabel('Number of Steps')
        plt.title('Complexity Performance for ' + searchtype + ' Search Algorithm')
        plt.xticks(index + bar_width, searchCases)
        plt.legend()

        plt.tight_layout()
        plt.show()
    else:

        plt.bar(searchcase, tStat, align='center', alpha=0.5)
        plt.title(searchtype)
        plt.xlabel('Time Performance for ' + searchtype)
        plt.ylabel('Time in Miliseconds')
        plt.tight_layout()
        plt.show()

        plt.bar(searchcase, sStat, align='center', alpha=0.5)
        plt.title(searchtype)
        plt.xlabel('Complexity Performance for ' + searchtype)
        plt.ylabel('Number of Steps')
        plt.tight_layout()
        plt.show()



def runAll(searchtype, searchcase):

    search_factory = SearchFactory()
    if searchcase == 'All':
        tStat = [[0 for x in range(len(searchCases))] for y in range(len(searchTypes))]
        sStat = [[0 for x in range(len(searchCases))] for y in range(len(searchTypes))]
        for iter, order in searchobjects:
            print(iter)
            alg = search_factory.buildSearch(iter)
            for newiter in range(0, len(searchCases)):
                totaltime = 0
                step = 0
                for epoch in range(0, epochs):
                    index, time, step = alg.measurePerformance(useArray, arrayLength,
                                                               searchElement[searchCases[newiter]])
                    totaltime = totaltime + time
                tStat[order][newiter] = totaltime / epochs
                sStat[order][newiter] = step

        print(tStat)
        index = np.arange(len(searchCases))
        bar_width = 0.35
        opacity = 0.8
        colors = ['b', 'r', 'm', 'g']
        # All graphics for Time Performance
        for iter in range(0, len(searchTypes)):
            plt.bar(index + (iter * bar_width), tStat[iter], bar_width / 2, alpha=opacity, color=colors[iter],
                    label=searchTypes[iter])
            # index=index+bar_width

        # plt.ylim(, 100000)
        # plt.yticks(np.arange(0, 100000, 500))
        plt.xlabel('Test Cases')
        plt.ylabel('Time in Miliseconds')
        plt.title('Time Performance for Search Algorithms')
        plt.xticks(index + bar_width, searchCases)
        plt.legend()

        plt.tight_layout()
        plt.show()

        for iter in range(0, len(searchTypes)):
            plt.bar(index + (iter * bar_width), sStat[iter], bar_width / 2, alpha=opacity, color=colors[iter],
                    label=searchTypes[iter])
            # index=index+bar_width

        # plt.ylim(, 100000)
        # plt.yticks(np.arange(0, 100000, 500))
        plt.xlabel('Test Cases')
        plt.ylabel('Number of Steps')
        plt.title('Complexity Performance for Search Algorithms')
        plt.xticks(index + bar_width, searchCases)
        plt.legend()

        plt.tight_layout()
        plt.show()

    else:
        #tStat = [[0 for x in range(0,1)] for y in range(len(searchTypes))]
        #sStat = [[0 for x in range(0,1)] for y in range(len(searchTypes))]
        tStat = list()
        sStat = list()
        for iter, order in searchobjects:
            print(iter)
            alg = search_factory.buildSearch(iter)
            totaltime = 0
            step = 0
            for epoch in range(0, epochs):
                index, time, step = alg.measurePerformance(useArray, arrayLength,
                                                           searchElement[searchcase])
                totaltime = totaltime + time
            tStat.append(totaltime / epochs)
            sStat.append(step)

        index = np.arange(len(searchTypes))
        bar_width = 0.35
        opacity = 0.8
        colors = ['b', 'r', 'm', 'g']
        plt.bar(index + bar_width, tStat, bar_width / 2, alpha=opacity, color=colors)
        # plt.ylim(, 100000)
        # plt.yticks(np.arange(0, 100000, 500))
        plt.xlabel('Test Cases')
        plt.ylabel('Time in Miliseconds')
        plt.title('Time Performance for ' + searchtype + ' Search Algorithm')
        plt.xticks(index + bar_width, searchTypes)
        plt.legend()

        plt.tight_layout()
        plt.show()

        plt.bar(index + bar_width, sStat, bar_width / 2, alpha=opacity, color=colors)
        # plt.ylim(, 100000)
        # plt.yticks(np.arange(0, 100000, 500))
        plt.xlabel('Test Cases')
        plt.ylabel('Number of Steps')
        plt.title('Complexity Performance for ' + searchtype + ' Search Algorithm')
        plt.xticks(index + bar_width, searchCases)
        plt.legend()

        plt.tight_layout()
        plt.show()


#runSearch('Linear','Best')
#runSearch('Linear','Worst')
#runSearch('Linear','Average')
#runSearch('Linear','All')
#
#runSearch('Binary','Best')
#runSearch('Binary','Worst')
#runSearch('Binary','Average')
#runSearch('Binary','All')
#
#runSearch('Jump','Best')
#runSearch('Jump','Worst')
#runSearch('Jump','Average')
#runSearch('Jump','All')
#
#runSearch('Interpolation','Best')
#runSearch('Interpolation','Worst')
#runSearch('Interpolation','Average')
#runSearch('Interpolation','All')
#
#runAll('All','Best')
#runAll('All','Worst')
#runAll('All','Average')
#runAll('All','All')



'''
# Individual graphics for Time Performance
def plotIndividualTime(case,alg):
    plt.bar(case, timeStat[alg], align='center', alpha=0.5)
    plt.title(searchTypes[alg])
    plt.xlabel('Time Performance for ' + searchTypes[alg])
    plt.ylabel('Time in Milisecons')
    plt.tight_layout()
    plt.show()
# Individual graphics for Complexity Performance
def plotIndividualComplexity(case,alg):
    plt.bar(case, stepStat[alg], align='center', alpha=0.5)
    plt.title(searchTypes[alg])
    plt.xlabel('Time Performance for ' + searchTypes[alg])
    plt.ylabel('Time in Milisecons')
    plt.tight_layout()
    plt.show()
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
def plotIndividualTime(case,alg):
    plt.bar(case, timeStat[alg], align='center', alpha=0.5)
    plt.title(searchTypes[alg])
    plt.xlabel('Time Performance for ' + searchTypes[alg])
    plt.ylabel('Time in Milisecons')
    plt.tight_layout()
    plt.show()
# Individual graphics for Complexity Performance
def plotIndividualComplexity(case,alg):
    plt.bar(case, stepStat[alg], align='center', alpha=0.5)
    plt.title(searchTypes[alg])
    plt.xlabel('Time Performance for ' + searchTypes[alg])
    plt.ylabel('Time in Milisecons')
    plt.tight_layout()
    plt.show()
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
# All graphics for Time Performance
def plotAllTime():
    fig, ax = plt.subplots()
    index = np.arange(len(searchCases))
    bar_width = 0.35
    opacity = 0.8
    colors = ['b', 'r', 'm', 'g']
    # All graphics for Time Performance
    for iter in range(0, len(searchTypes)):
        plt.bar(index + (iter * bar_width), timeStat[iter], bar_width / 2, alpha=opacity, color=colors[iter],
                label=searchTypes[iter])
        # index=index+bar_width
    # plt.ylim(, 100000)
    # plt.yticks(np.arange(0, 100000, 500))
    plt.xlabel('Test Cases')
    plt.ylabel('Timer in Miliseconds')
    plt.title('Time Performance for Search Algorithms')
    plt.xticks(index + bar_width, searchCases)
    plt.legend()
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
def plotAllComplexity():
    fig, ax = plt.subplots()
    index = np.arange(len(searchCases))
    bar_width = 0.35
    opacity = 0.8
    colors = ['b', 'r', 'm', 'g']
    # All graphics for Complexity Performance
    for iter in range(0, len(searchTypes)):
        plt.bar(index + (iter * bar_width), stepStat[iter], bar_width / 2, alpha=opacity, color=colors[iter],
                label=searchTypes[iter])
        # index=index+bar_width
    # plt.ylim(, 100000)
    # plt.yticks(np.arange(0, 100000, 500))
    plt.xlabel('Test Cases')
    plt.ylabel('Number of Steps')
    plt.title('Complexity Performance for Search Algorithms')
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
'''