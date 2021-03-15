import csv
import numpy as np
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


with open('values.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    cuts = np.empty(1)
    cuts = []
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            #cuts = np.append(cuts, row[1])
            cuts.append(int(row[1]))
            #print(f'\t{row[0]} works in the {row[1]} department, and was born in.')
            #line_count += 1
    print(f'Processed {line_count} lines.')
    npCuts = np.array(cuts)
    npCuts = np.flip(np.sort(npCuts))
    cutsUsed = np.array([npCuts, np.zeros(len(npCuts))])
    cutsUsed = cutsUsed.reshape(len(npCuts),2, order='F')
    print(cutsUsed)
