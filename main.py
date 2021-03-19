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
    supplyLength = 0
    sawBladeWidth = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            quantity = 1
            if row[3]:
                quantity = int(row[3])
            for i in range(quantity):
                cuts.append(int(row[2]))
                #print(f'added cut with length {int(row[2])}')
            if row[0]:
                sawBladeWidth = float(row[0])
                print(f'saw blade width = {sawBladeWidth}mm')
            if row[1]:
                supplyLength = int(row[1])
                print(f'supply length = {supplyLength}mm')
            #print(f'\t{row[0]} works in the {row[1]} department, and was born in.')
            line_count += 1
    print(f'Processed {line_count} lines.')
    npCuts = np.array(cuts)
    npCuts = np.array([np.flip(np.sort(npCuts)), np.arange(len(npCuts))]).swapaxes(0,1)
    cutsNotSet = np.copy(npCuts)
    #cutsUsed = np.array([npCuts, np.zeros(len(npCuts))])
    #cutsUsed = cutsUsed.swapaxes(0,1)
    #cutsUsed = np.delete(cutsUsed, [len(npCuts)-1], )
    print(cutsNotSet)

def findFit(currentCutIdx, avblLen, allCuts):
    for idx in range(currentCutIdx+1, len(allCuts)):
        if(avblLen -(allCuts[currentCutIdx]+allCuts[idx]) > 0):
            return idx
        else:
            return -1

setups = []

class CutSetup:
    def __init__(self, length, firstIndex, firstCutL, bladeWidth):
        print(f'init {bladeWidth}')
        self.length = length
        self.indexes = []
        self.rest = length
        self.bladeWidth = bladeWidth
        self.cut(firstIndex, firstCutL)
        print(f'blade width {bladeWidth}')
    def fitsIn(self, cutL):
        return self.rest >= cutL
    def cut(self, index, cutL):
        self.indexes.append(index)
        self.rest = self.rest - (cutL + self.bladeWidth)
        #print(f'Cut sucessful, setup now contains indexes {self.indexes} and has rest {self.rest}mm')

def getSetup(cuts, supply, sawBladeWidth):
    cut = CutSetup(supply, cuts[0][1], cuts[0][0], sawBladeWidth)
    full = False
    while not full:
        
        found1 = False
        for idx in range(1, len(cuts)):
            if not cuts[idx][1] in cut.indexes:
                if cut.fitsIn(cuts[idx][0]):
                    cut.cut(cuts[idx][1], cuts[idx][0])
                    found1 = True
                    break
        if not found1:
            full = True
            print(f'setup complete!')
    return cut

while len(cutsNotSet) > 0:
    s = getSetup(cutsNotSet, supplyLength, sawBladeWidth)
    #print(setups)
    toDel = []
    for idx in range(len(cutsNotSet)):
        if cutsNotSet[idx][1] in s.indexes:
            toDel.append(idx)
    setups.append(s)
    #indexes = findBestSetup(cutsNotSet)
    cutsNotSet = np.delete(cutsNotSet, toDel, 0)
print(f'successful cut all pieces. Total beams needed: {len(setups)}, all setups: ')
for idx in range(len(setups)):
    print(f'setup{idx+1} with rest {setups[idx].rest:.1f} and lengths: ')
    for i in setups[idx].indexes:
        print(f'{npCuts[i][0]}mm of index {i}')

with open('result.csv', mode='w', newline='') as result_file:
    result_writer = csv.writer(result_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    for idx in range(len(setups)):
        result_writer.writerow([f'setup_{idx+1} with rest {setups[idx].rest:.1f} and lengths: ','length in mm','index'])
        for i in setups[idx].indexes:
            result_writer.writerow(['',f'{npCuts[i][0]}',f'{i}'])

def findBestSetup(cuts):
    rest = supplyLength
    index = 0
    for cut in cutsNotSet:


        full = False
        while not full:
            c2 = findFit(index, rest-cut[0], cutsNotSet)
            if c2 == -1:
                full = True 
            #else:


        index = index + 1



        for secondCut in cutsNotSet:
            if secondCut == firstCut:
                break
            #if supplyLength - (firstCut + secondCut) > 0