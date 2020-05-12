#!/usr/bin/python                                                                                                                                            
#-----------------------------------------------                                                                                                             
import sys, os, pwd, commands, glob, fnmatch
import optparse, shlex, re
import time
from time import gmtime, strftime
import math
from array import array
from ROOT import *



#define function for parsing options
def parseOptions():

    usage = ('usage: %prog [options]\n'
             + '%prog -h for help')
    parser = optparse.OptionParser(usage)

    # input options
    parser.add_option('-t', '--taskname', dest='TASKNAME', type='string', help='task name')
    parser.add_option('-i', '--input', dest='INPUT', type='string', help='input file')

    # store options and arguments as global variables
    global opt, args
    (opt, args) = parser.parse_args()

# define function for processing the external os commands
def processCmd(cmd, quite = 0):
    if (status !=0 and not quite):
        print 'Error in processing command:\n   ['+cmd+']'
        print 'Output:\n   ['+output+'] \n'
    return output

def find_files(directory, pattern):
  for root, dirs, files in os.walk(directory):
    for basename in files:
      if fnmatch.fnmatch(basename, pattern):
        filename = os.path.join(root, basename)
        yield filename

def analyzeResults():

  global opt, args
  parseOptions()

  f = TFile(opt.INPUT,"READ")
  t = f.Get("Events")

  branches = t.GetListOfBranches()
  nbranches = branches.GetEntries()
  njob=-1

  #print "'drop *',"

  print "'keep *',"

  for i in xrange(nbranches):
    name = branches.At(i).GetName().replace(".","")
    if (not "_" in name): continue
    njob+=1

    status, output = commands.getstatusoutput("grep \"Begin Fatal\" "+opt.TASKNAME+"/*."+str(njob)+".err")

    #if (output==""): continue
    #print "'keep "+name+"',"
      
    if (output==""): 
      print "'drop "+name+"',"
      
if __name__ == "__main__":
  analyzeResults()
