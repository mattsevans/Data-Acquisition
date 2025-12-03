from math import sqrt

#define functions
def dimensionGet(dimName): #get the dimension from datasheet
    while(True):
        dim = input("Input " + dimName + " in mm: ")
        check = input("Is " + dim + " mm correct? (Y/N): ").upper()
        if check == "Y":
            return float(dim)

#define constants
Jt = 0.55
Jh = 0.45
Js = 0.05
F = .01
dimName_list = ["Minimum Lead Width", "Maximum Package Width", "Minimum Total Width", "Ideal Pitch"]
tolName_list = ["Lead Width Tolerance", "Package Width Tolerance", "Total Width Tolerance"]

#define variables
inputList = []
toleranceList = []
measurementList = []

#get the dimensions and tolerances from data sheet
for i in dimName_list: #dimensions
    inputList.append(dimensionGet(i))
#get the tolerances from the data sheet
for i in tolName_list: #tolerances
    toleranceList.append(dimensionGet(i))

#calculate the measurements needed to place the pads
Xmax = inputList[0] + 2*Js + sqrt(toleranceList[0] + F**2 + inputList[3]) #pad width
print("Xmax is:",Xmax," mm")
Gmin = inputList[1] - 2*Jh - sqrt(toleranceList[1] + F**2 + inputList[3]) #horizontal spacing
print("Gmin is:",Gmin,"mm")
Zmin = inputList[2] + 2*Jt + sqrt(toleranceList[2] + F**2 + inputList[3]) #total width
print("Zmin is:",Zmin,"mm")