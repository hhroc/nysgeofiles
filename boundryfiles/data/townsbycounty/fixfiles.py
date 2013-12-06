import simplejson
from os import listdir
from os.path import isfile, join
import os

def main():

    mypath = "."
    allfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]

    for thefile in allfiles:
        if ".json" in thefile.lower():
            print "Working on '{0}'".format(thefile.lower())
            lines = []
            newline = ""
            f = open(thefile,"r")
            lines = f.readlines()
            #print "char: '{0}'".format(lines[len(lines)-3].strip()[:-1])
            lines[len(lines)-3] = lines[len(lines)-3].strip()[:-1]
            f.close()
            os.remove(thefile)
            newfile = "{0}".format(thefile)
            f = open(newfile,"w")
            f.writelines(lines)
            f.close()
            #print lines
            with open(newfile) as f:
                stuff = simplejson.loads(f.read())
            #return

main()
