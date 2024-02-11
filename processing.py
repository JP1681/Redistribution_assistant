import json
import math
import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
dir_name = os.path.dirname(os.path.realpath(__file__))
root = tk.Tk()
root.withdraw()

tk.messagebox.showinfo(title="Please select a file",message="Please use the next screen to select the .csv/xlsx file containing the enrolment data.")
while True:
    file_path = filedialog.askopenfilename()
    if file_path[-4:]==".csv":
        SA1data = pd.read_csv(file_path)
        break
    elif file_path[-5:]==".xlsx":
        SA1data = pd.read_excel(file_path)
        break
    else:
        tk.messagebox.showinfo(title="Wrong file type",message="Please select either a .csv or .xlsx file.")


for i in range(len(SA1data.columns)):
    print("Column "+str(i)+": "+SA1data.columns[i]+str(list(SA1data[SA1data.columns[i]].head())))
    print()
print("Each column of the .csv file is shown above, along with the first few entries.")
questionSuffixes = ["SA1 codes (10-digit numbers, possibly with .0)","current enrolment numbers","projected enrolment numbers"]
newColumnNames = ["SA1","Actual","Projected"]
columnNumbers = []
for i in range(len(questionSuffixes)):
    valid = False
    while not valid:
        newNum = input("What number is the column containing " + questionSuffixes[i] + "? ")
        try:
            newNum = int(newNum)
            if (newNum < 0) or (newNum >= len(SA1data.columns)):
                print("Please enter a valid column number.")
            else:
                if newNum in columnNumbers:
                    print("You have already entered that number.")
                else:
                    columnNumbers.append(newNum)
                    valid = True
        except:
            print("Please enter an integer.")
SA1data=SA1data.iloc[:,columnNumbers]
SA1data.columns=newColumnNames
SA1data.dropna(inplace=True)
#SA1data["Current"]=SA1data["Current"].str.strip()
SA1data.Actual=SA1data.Actual.astype("int32")
SA1data.Projected=SA1data.Projected.astype("int32")
SA1data.SA1=SA1data.SA1.astype("int64")

#electorateData = SA1data[["Current","SA1"]]
#outjs="var elecToSA1 = "+electorateData.groupby('Current').agg(list).to_json()
#with open(dir_name+"\\electorateSA1s.js","w") as file:
#    file.write(outjs)

populationData = SA1data[["SA1","Actual","Projected"]]
populationData = populationData.groupby("SA1").sum()
populationData["Change"]=populationData["Projected"]/populationData["Actual"]-1
populationData["Change"]=populationData["Change"].fillna(0)
populationData["Change"].replace(np.inf,0,inplace=True)
allocationData = pd.DataFrame(index=populationData.index)
allocationData["Division"]=-1
allocationData.Division = allocationData.Division.astype("int32")
allocationData = json.loads(allocationData.to_json())

actualExt = [math.log10(populationData["Actual"].min()+1),math.log10(populationData["Actual"].max()+1)]
projectedExt = [math.log10(populationData["Projected"].min()+1),math.log10(populationData["Projected"].max()+1)]
changeExt = [populationData["Change"].min(),populationData["Change"].max()]
totals = [str(populationData["Actual"].sum()),str(populationData["Projected"].sum())]

populationData=json.loads(populationData.to_json())
populationData["CurrentExtreme"]=actualExt
populationData["ProjectedExtreme"]=projectedExt
populationData["ChangeExtreme"]=changeExt
populationData["Totals"]=totals

inputValid = False
while inputValid==False:
    num_seats = input("How many divisions will there be? ")
    try:
        num_seats = int(num_seats)
        if num_seats >= 2:
            inputValid = True
        else:
            raise Exception()
    except:
        print("Try again. Enter an integer greater than 1.")
seatNames = dict(zip(range(num_seats),['']*num_seats))
colours = dict(zip(range(num_seats),['#000000']*num_seats))
numbers = dict(zip(range(num_seats),[1]*num_seats))
allocationData["Names"]=seatNames
allocationData["Colours"]=colours
allocationData["Numbers"]=numbers

outjs="var populations = "+json.dumps(populationData)
with open(dir_name+"\\populations.js","w") as file:
    file.write(outjs)

outjs="var allocations = "+json.dumps(allocationData)
with open(dir_name+"\\allocations.js","w") as file:
    file.write(outjs)

input("You can now open redist.html. Press enter to close this window.")