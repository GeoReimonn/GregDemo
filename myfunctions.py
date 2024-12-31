import os

def sqrt(n):
    return(n**0.5)

def exp(n):
    return(n**1.21)

def REIMONNaddValue(d):
    x = d['REIMONN OUTPUT']['x']
    y = d['REIMONN OUTPUT']['y']
    i = -1
    z = []
    for a in x:
        i = i + 1
        p = i * y[i]
        z.append(p)
    d['REIMONN Added Value'] = z
    return(d)

def listOfFiles(mypath='C:/Users/GeoRe/git/GregDemo'):
    onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
    oarray = []
    for f in onlyfiles:
        if '.dat.json' in f:
            oarray.append(os.path.join(mypath, f))
    return(oarray)
