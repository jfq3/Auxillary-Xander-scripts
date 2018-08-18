#!/usr/bin/env python
# usage: python filter_unclutured_seqs.py infile.fasta outfile.fasta
import sys

InFileName = sys.argv[1]
OutFileName = sys.argv[2]

InFile = open( InFileName, 'rU' )
OutFile = open( OutFileName, 'w')
seq = False
for Line in InFile:
    if seq == True:
        OutFile.write( Line )
        seq = False
    if Line.strip()[0]==">":
        if Line.find( "uncul" ) < 0:       
            OutFile.write( Line )
            seq = True
InFile.close()
OutFile.close()