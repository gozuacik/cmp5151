
import Search
import Sorting


class Visitor():
    def visitSearch(self):pass
    def visitSort(self):pass

class SearchVisit(object):
    def accept(self, visitor):
        visitor.visitSearch()


class SortVisit(object):
    def accept(self, visitor):
        visitor.visitSort()


class AlgVisitor(Visitor):
    def __init__(self,type,case):
        self.type = type
        self.case = case

    def visitSearch(self):
        print("1")
        if self.type == 'All':
            Search.runAll(self.type, self.case)
        else:
            Search.runSearch(self.type, self.case)

    def visitSort(self):
        print("2")
        if self.type == 'All':
            Sorting.runAll(self.type, self.case)
        else:
            Sorting.runSort(self.type, self.case)
