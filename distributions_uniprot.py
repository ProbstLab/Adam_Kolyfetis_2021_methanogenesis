##The MIT License (MIT) Copyright (c) 2021 GEORGE E KOLYFETIS 
##Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
##The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
##THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## This script starts by searching each accession from a list of Pfam accessions (given by the user as a text file) in a Uniprot records file (given again by the user). For each Pfam accession it outputs the number for each Domain
## of life (plus Viruses and Unclassified organisms) this accession can be found in, plus the percentage of Archaea in each of those records.

#usage : python distributions_uniprot.py {pfam_accessions.txt} {uniprot_records.txt}


import Bio.SwissProt as sp
import sys
g = open(sys.argv[1], 'r')
d = dict()

entries = g.read().split("\n") #read the text file with the pfam accessions (one accession per line)
#open the uniprot records file, parse
with open(sys.argv[2]) as handle:   
    records = sp.parse(handle)
    for record in records:
        res = list(map("".join, record.cross_references))#create list with the cross references of all records
        ser = ("; ".join(record.organism_classification))#create list with the organism classifications of all records
        d.update( {str(res) : str(ser)} )#create a dictionary : key is cross reference, value is organism classification 

for item in entries:
    item1 = 'Pfam%s'%(item)#modify the accession putting Pfam instead of PF infront
#set values to 0 for all organism classifications
    B_C = 0
    E_C = 0
    A_C = 0
    UC = 0
    V_C = 0
#iterate over the dictionary and search for the organism classification of each record, matching the given Pfam accession
    for key, value in d.items() :
        if item1 in key:
            if "Bacteria" in value:
                B_C += 1
            elif "Eukaryota" in value:
                E_C += 1
            elif "Archaea" in value:
                A_C += 1
            elif "unclassified" in value:
                UC += 1
            elif "Viruses" in value:            
                V_C += 1
    PA = (A_C + 0.)/(A_C + B_C + E_C + UC + V_C +0.) * 100    #percentage of Arhaea for the given accession                                       
    PAR = round(PA, 2)
    print((item),(":"),("B_C:"),(B_C),("E_C:"),(E_C),("A_C:"),(A_C),("Unclassified:"),(UC),("V_C:"),(V_C),("%Archaea: "),(PAR),("%"))   #print number of records found in each Domain of Life plus Archaea percentage   
