
# Reference
# https://www.geeksforgeeks.org/linear-search/
# https://www.geeksforgeeks.org/binary-search/
# https://www.geeksforgeeks.org/jump-search/
# https://www.geeksforgeeks.org/interpolation-search/
import math
from datetime import datetime

# 0 50000 99999
# ArrayLenght
arrayLength = 100000

class UseCases():
    def __init__(self):
        self.bestArray = list()
        self.averageArray = list()
        self.worstArray = list()

    def setBestArray(self):
        r = range(arrayLength)
        self.bestArray = list(r)

    def getBestArray(self):
        return self.bestArray


class BaseSearch:
    def __init__(self, title):
        self.title = title
        self.elapsedTime = 0
        self.numberofSteps = 0
        print(title)

    def search(self,arr,n,x):
        pass

    def getElsapedTime(self):
        print("Elapsed Time: ", self.elapsedTime)

    def getNumberofSteps(self):
        print("Number of Steps: ", self.numberofSteps)

class LinearSearch(BaseSearch):
    def search(self,arr, n, x):
        start_time=float(datetime.time(datetime.now()).microsecond)
        print(start_time)
        for i in range(0, n):
            self.numberofSteps = self.numberofSteps + 1
            if arr[i] == x:
                stop_time = float(datetime.time(datetime.now()).microsecond)
                print(stop_time)
                self.elapsedTime = float(stop_time - start_time)
                return i
        return -1


class BinarySearch(BaseSearch):
    def search(self,arr, n, x):
        l = 0
        r = n
        start_time=float(datetime.time(datetime.now()).microsecond)
        print(start_time)
        while l <= r:
            self.numberofSteps = self.numberofSteps + 1
            mid = int(l + (r - l) / 2)

            # Check if x is present at mid
            if arr[mid] == x:
                stop_time = float(datetime.time(datetime.now()).microsecond)
                print(stop_time)
                self.elapsedTime = float(stop_time - start_time)
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



class JumpSearch(BaseSearch):
    def search(self,arr, n, x):

        # Finding block size to be jumped
        step = math.sqrt(n)

        # Finding the block where element is
        # present (if it is present)
        prev = 0
        start_time=float(datetime.time(datetime.now()).microsecond)
        print(start_time)
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
            stop_time = float(datetime.time(datetime.now()).microsecond)
            print(stop_time)
            self.elapsedTime = float(stop_time - start_time)
            return prev

        return -1



class InterpolationSearch(BaseSearch):
    def search(self,arr, n, x):
        # Find indexs of two corners
        lo = 0
        hi = (n - 1)
        start_time=float(datetime.time(datetime.now()).microsecond)
        print(start_time)
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
                stop_time = float(datetime.time(datetime.now()).microsecond)
                print(stop_time)
                self.elapsedTime = float(stop_time - start_time)
                return pos

            # If x is larger, x is in upper part
            if arr[pos] < x:
                lo = pos + 1

            # If x is smaller, x is in lower part
            else:
                hi = pos - 1

        return -1


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



usecases = UseCases()
usecases.setBestArray()

#searchTypes = ['Linear', 'Binary', 'Jump','Interpolation']
search_factory = SearchFactory()
alg = search_factory.buildSearch('Linear')

searchElement = 25000

result = alg.search(usecases.getBestArray(), arrayLength, searchElement)
if result == -1:
    print("Element is not present in array")
else:
    print("Element is present at index", result)
    alg.getElsapedTime()
    alg.getNumberofSteps()


