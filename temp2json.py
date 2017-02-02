#!/usr/bin/env python

import os
import time
import sys

class Convert:
    def __init__(self,argv):
        self.args = argv[1:]
        self.usageName  = os.path.basename(argv[0])
        self.setDefaults()

    def setDefaults(self):
        """ set default attributes"""
        self.format = "%Y/%m/%d %H:%M:%S"      # format of dat/time logging  from temp sensor
        if len(self.args) < 1:
            self.help()
        self.input = self.args[0]    
        self.output = self.input + ".json"

        # json file header, defines data format
        self.head = '{\n"cols": [\n'
        self.head += '  {"id": "timestamp", "label": "DateTime",  "type": "datetime"},\n'
        self.head += '  {"id": "tempF",     "label": "degrees F", "type": "number"},\n'
        self.head += '  {"id": "tempC",     "label": "degrees C", "type": "number"}\n'
        self.head += '],\n"rows": ['

        # json file tail
        self.tail = ']\n}'

    def help(self):
        """ prints usage"""
        print '\nNAME: \n' , \
              '\t%s - reads  a text file with tempearture records \n' % self.usageName, \
              '\tOutputs records in json format suitable for google DrawChart in the output file\n' ,\
              '\tOutput file name is an input file name with an extention .json\n' ,\
              '\nSYNOPSIS:\n' , \
              '\t%s  inputFile \n' % self.usageName, \
              '\nDESCRIPTION:\n' , \
              '\tinputFile - tempearute records file  (one per line) \n', \
        sys.exit(0)

    def readData(self):
        f = open(self.input,"r")
        lines = f.readlines()
        f.close()
        lsplit = map(lambda x: x.split(),lines)
        self.records = map(lambda x: [
                  time.strptime("%s %s" %(x[0],x[1]),self.format),
                  x[3].replace('F',''),\
                  x[4].replace('C','') 
                 ],lsplit)
        self.count = len(self.records)

    def writeJsonFile(self):
        text = self.head + self.data + self.tail
        f = open (self.output, 'w')
        f.write(text)
        f.close()

    def makeJsonData (self):
        self.data = ""
        lineno = 0
        for o in self.records:
             self.data += '{"c":[{"v": "Date(%d,%d,%d,%d,%d,%d)"}, {"v": %s}, {"v": %s}]}' % \
                    (o[0].tm_year,o[0].tm_mon-1,o[0].tm_mday,o[0].tm_hour,o[0].tm_min,o[0].tm_sec,o[1],o[2])
             lineno += 1
             if lineno < self.count:
                 self.data += ",\n"

    def run (self):
        self.readData()
        self.makeJsonData()
        self.writeJsonFile()
        sys.exit(0)


if __name__ == "__main__":
        app=Convert(sys.argv)
        app.run()

