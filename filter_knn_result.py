#!/usr/bin/env python
# usage: python filter_knn_result.py knn_infile outfile.fasta
import sys

InFileName = sys.argv[1]
OutFileName = sys.argv[2]

InFile = open( InFileName, 'rU' )
OutFile = open( OutFileName, 'w')
seq = False
for Line in InFile:
    if seq == True:
        Line = Line.replace('>', '')
	Line = Line.replace('-' ,'')
	OutFile.write( Line )
        seq = False
    if Line.strip()[0]=="@":
        MyLine = Line.split()
        if float(MyLine[4]) >= 0.5:
            OutFile.write( MyLine[0].replace("@", ">") + " " + MyLine[4] + '\n')
            seq = True
InFile.close()
OutFile.close()
