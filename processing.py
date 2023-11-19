import json
import math
import numpy as np
import pandas as pd

import os
dir_name = os.path.dirname(os.path.realpath(__file__))

SA1data = pd.read_csv(dir_name+"\\enrolment.csv")
SA1data.columns=["Current", "SA2 code", "SA2 name", "SA1", "SA1 code", "Actual", "Projected", "Growth"]
SA1data.drop(["SA2 code", "SA2 name", "SA1 code","Growth"],axis=1,inplace=True)
SA1data.dropna(inplace=True)
SA1data["Current"]=SA1data["Current"].str.strip()
SA1data.Actual=SA1data.Actual.astype("int32")
SA1data.Projected=SA1data.Projected.astype("int32")
SA1data.SA1=SA1data.SA1.astype("int64")

electorateData = SA1data[["Current","SA1"]]
outjs="var elecToSA1 = "+electorateData.groupby('Current').agg(list).to_json()
with open(dir_name+"\\electorateSA1s.js","w") as file:
    file.write(outjs)

populationData = SA1data[["SA1","Actual","Projected"]]
populationData = populationData.groupby("SA1").sum()
populationData["Change"]=populationData["Projected"]/populationData["Actual"]-1
populationData["Change"]=populationData["Change"].fillna(0)
populationData["Division"]=-1
populationData.Division = populationData.Division.astype("int32")

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
populationData["Names"]=seatNames

outjs="var allocations = "+json.dumps(populationData)
with open(dir_name+"\\allocations.js","w") as file:
    file.write(outjs)