import simplejson
from os import listdir
from os.path import isfile, join
import os

def main():

    mypath = "."
    allfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]

    lut = []

    for thefile in allfiles:
        if "towns.json" in thefile.lower():
            print "Reading: '{0}'".format(thefile)
            countyname = thefile.split('_county_towns.json')[0].replace('_',' ')
            f = open(thefile,"r")
            data = f.read()
            f.close()
            countydata = simplejson.loads(data)
            countycode = countydata['features'][0]['properties']['COUNTYFP']
            statecode = countydata['features'][0]['properties']['STATEFP']
            print "\tFound: {0} : {1} : {2}".format(countyname,countycode,statecode)
            lut.append({'countyname': countyname,'countycode': countycode,'statecode': statecode})
            #return
    json = simplejson.dumps(lut)
    with open("countylut.json","w") as f:
        f.write(json)

    print "Done."
main()
