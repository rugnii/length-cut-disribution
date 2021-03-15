import csv
import numpy as numpy
class supply:
    def __init__(self, length):
        self.setLength(length)
        self.setRest(length)
    def setLength(self, length):
        self.length = length
    def getLength(self):
        return self.length
    def setRest(self, value):
        self.rest = value
    def getRest(self):        
        return self.rest
    def cut(self, length):
        self.rest = self.rest - length

class main:
    def __init__(self, cut1):
        print("initializing length cutting with first length: ")
        print(cut1)
        s1 = supply(700)
        s1.cut(cut1)
        print(s1.getRest())

m = main(500)
