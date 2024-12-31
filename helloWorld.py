import os
import myfunctions
import json

#print('Hello world!')
#y = myfunctions.sqrt(10)
#z = myfunctions.exp(4)
#print(y,z)

experiment1 = {
    'Experiment Name': 'My first experiment',
    'Experiment Date': '2024-01-31',
    'Experimentor': 'Greg Reimonn',
    'Type': 'REIMONN Spectroscopy',
    'REIMONN OUTPUT': {'x': [1,2,3,4],
                       'y': [5,4,3,2]}
    }

updatedD = myfunctions.REIMONNaddValue(experiment1)

filenames = myfunctions.listOfFiles()
goodfiles = []
for fname in filesnames:
    with open(fname, 'r') as infile:
        d = json.load(infile)
        if d['Experimentor'] == 'Greg Reimonn':
            goodfiles.append(fname)

experiments = []
for fname in goodfiles:
    with open(fname, 'r') as infile:
        d = json.load(infile)
        experiments.append(d)
bigAnalysis = myfunctions.aggregator(experiments)
with open('my big analysis', 'w') as outfile:
    json.dump(bigAnalysis, outfile)