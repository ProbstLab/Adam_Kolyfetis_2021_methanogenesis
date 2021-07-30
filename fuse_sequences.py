##Copyright 2021 GEORGE E KOLYFETIS
##Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
##The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
##THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## This script fuses (interactively) sequences from an alignment. It is used for sequences that are split (e.g. due to sequencing or ORF prediction errors), using their accession numbers as a guide.

#usage : python fuse_sequences.py alignment_file.aln logfile.txt outfile.txt 

import sys
import os
from Bio.SeqIO.FastaIO import SimpleFastaParser
from Bio import SeqIO

#Create an outfile (g) based on the input file name. Logfile is the second argument.
#Create an empty list for the unique assemblies, and an empty dictionary for the header-sequence pairs.
assemblies = list()
g = open(sys.argv[3], 'a')
o = open(sys.argv[2], 'a')
same_assemblies_records = dict()

#Define the function n_c_terminal. Input is the numbers of the sequences you want to be fused (as asked by the output of the yes_or_no function)
#For all possible sequence combinations (n*(n-1) total), split the header of the first sequence.
#Then split the header of the second sequence. The first element of the new headers (new accession) becomes a fusion of the two accessions, 
#then a space, then the remaining elements of the first header joined by spaces (the ones that were removed when splitting).
#The sequences become fused in the given order. Write them in the outfile. Remove them from the dictionary
#Write the remaining sequences (remaining in the dictionary) in the outfile.
#If you need multiple fusions per assembly, you have to rerun the script.
#In the logfile, write the name of the file, FUSED, header1, AND, header2.
#At the end of the function clear the dictionary for this assembly to proceed to the next one.
def n_c_terminal(question2):
    a, b = input(question2).split() 
    print('\n' + "Fused sequences, N-terminal sequence is {} and C-terminal sequence is {}".format(a, b)) 
    if a == '1':
        x = first_key.split(' ')
        if b == '2':
            y = second_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + first_val + second_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + first_key + ' ' + 'AND' + ' ' + second_key + '\n')
            del same_assemblies_records[first_key]
            del same_assemblies_records[second_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '3':
            y = third_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + first_val + third_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + first_key + ' ' + 'AND' + ' ' + third_key + '\n')
            del same_assemblies_records[first_key]
            del same_assemblies_records[third_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '4':
            y = fourth_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + first_val + fourth_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + first_key + ' ' + 'AND' + ' ' + fourth_key + '\n')
            del same_assemblies_records[first_key]
            del same_assemblies_records[fourth_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '5':
            y = fifth_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + first_val + fifth_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + first_key + ' ' + 'AND' + ' ' + fifth_key + '\n')
            del same_assemblies_records[first_key]
            del same_assemblies_records[fifth_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '6':
            y = sixth_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + first_val + sixth_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + first_key + ' ' + 'AND' + ' ' + sixth_key + '\n')
            del same_assemblies_records[first_key]
            del same_assemblies_records[sixth_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '7':
            y = seventh_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + first_val + seventh_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + first_key + ' ' + 'AND' + ' ' + seventh_key + '\n')
            del same_assemblies_records[first_key]
            del same_assemblies_records[seventh_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '8':
            y = eighth_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + first_val + eighth_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + first_key + ' ' + 'AND' + ' ' + eighth_key + '\n')
            del same_assemblies_records[first_key]
            del same_assemblies_records[eighth_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '9':
            y = nineth_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + first_val + nineth_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + first_key + ' ' + 'AND' + ' ' + nineth_key + '\n')
            del same_assemblies_records[first_key]
            del same_assemblies_records[nineth_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '10':
            y = tenth_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + first_val + tenth_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + first_key + ' ' + 'AND' + ' ' + tenth_key + '\n')
            del same_assemblies_records[first_key]
            del same_assemblies_records[tenth_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
    if a == '2':
        x = second_key.split(' ')
        if b == '1':
            y = first_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + second_val + first_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + second_key + ' ' + 'AND' + ' ' + first_key + '\n')
            del same_assemblies_records[second_key]
            del same_assemblies_records[first_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '3':
            y = third_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + second_val + third_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + second_key + ' ' + 'AND' + ' ' + third_key + '\n')
            del same_assemblies_records[second_key]
            del same_assemblies_records[third_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '4':
            y = fourth_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + second_val + fourth_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + second_key + ' ' + 'AND' + ' ' + fourth_key + '\n')
            del same_assemblies_records[second_key]
            del same_assemblies_records[fourth_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '5':
            y = fifth_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + second_val + fifth_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + second_key + ' ' + 'AND' + ' ' + fifth_key + '\n')
            del same_assemblies_records[second_key]
            del same_assemblies_records[fifth_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '6':
            y = sixth_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + second_val + sixth_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + second_key + ' ' + 'AND' + ' ' + sixth_key + '\n')
            del same_assemblies_records[second_key]
            del same_assemblies_records[sixth_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '7':
            y = seventh_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + second_val + seventh_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + second_key + ' ' + 'AND' + ' ' + seventh_key + '\n')
            del same_assemblies_records[second_key]
            del same_assemblies_records[seventh_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '8':
            y = eighth_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + second_val + eighth_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + second_key + ' ' + 'AND' + ' ' + eighth_key + '\n')
            del same_assemblies_records[second_key]
            del same_assemblies_records[eighth_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '9':
            y = nineth_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + second_val + nineth_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + second_key + ' ' + 'AND' + ' ' + nineth_key + '\n')
            del same_assemblies_records[second_key]
            del same_assemblies_records[nineth_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '10':
            y = tenth_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + second_val + tenth_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + second_key + ' ' + 'AND' + ' ' + tenth_key + '\n')
            del same_assemblies_records[second_key]
            del same_assemblies_records[tenth_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
    if a == '3':
        x = third_key.split(' ')
        if b == '1':
            y = first_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + third_val + first_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + third_key + ' ' + 'AND' + ' ' + first_key + '\n')
            del same_assemblies_records[third_key]
            del same_assemblies_records[first_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '2':
            y = second_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + third_val + second_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + third_key + ' ' + 'AND' + ' ' + second_key + '\n')
            del same_assemblies_records[third_key]
            del same_assemblies_records[second_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '4':
            y = fourth_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + third_val + fourth_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + third_key + ' ' + 'AND' + ' ' + fourth_key + '\n')
            del same_assemblies_records[third_key]
            del same_assemblies_records[fourth_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '5':
            y = fifth_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + third_val + fifth_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + third_key + ' ' + 'AND' + ' ' + fifth_key + '\n')
            del same_assemblies_records[third_key]
            del same_assemblies_records[fifth_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '6':
            y = sixth_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + third_val + sixth_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + third_key + ' ' + 'AND' + ' ' + sixth_key + '\n')
            del same_assemblies_records[third_key]
            del same_assemblies_records[sixth_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '7':
            y = seventh_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + third_val + seventh_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + third_key + ' ' + 'AND' + ' ' + seventh_key + '\n')
            del same_assemblies_records[third_key]
            del same_assemblies_records[seventh_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '8':
            y = eighth_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + third_val + eighth_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + third_key + ' ' + 'AND' + ' ' + eighth_key + '\n')
            del same_assemblies_records[third_key]
            del same_assemblies_records[eighth_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '9':
            y = nineth_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + third_val + nineth_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + third_key + ' ' + 'AND' + ' ' + nineth_key + '\n')
            del same_assemblies_records[third_key]
            del same_assemblies_records[nineth_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '10':
            y = tenth_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + third_val + tenth_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + third_key + ' ' + 'AND' + ' ' + tenth_key + '\n')
            del same_assemblies_records[third_key]
            del same_assemblies_records[tenth_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
    if a == '4':
        x = fourth_key.split(' ')
        if b == '1':
            y = first_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + fourth_val + first_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + fourth_key + ' ' + 'AND' + ' ' + first_key + '\n')
            del same_assemblies_records[fourth_key]
            del same_assemblies_records[first_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '2':
            y = second_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + fourth_val + second_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + fourth_key + ' ' + 'AND' + ' ' + second_key + '\n')
            del same_assemblies_records[fourth_key]
            del same_assemblies_records[second_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '3':
            y = third_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + fourth_val + third_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + fourth_key + ' ' + 'AND' + ' ' + third_key + '\n')
            del same_assemblies_records[fourth_key]
            del same_assemblies_records[third_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '5':
            y = fifth_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + fourth_val + fifth_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + fourth_key + ' ' + 'AND' + ' ' + fifth_key + '\n')
            del same_assemblies_records[fourth_key]
            del same_assemblies_records[fifth_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '6':
            y = sixth_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + fourth_val + sixth_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + fourth_key + ' ' + 'AND' + ' ' + sixth_key + '\n')
            del same_assemblies_records[fourth_key]
            del same_assemblies_records[sixth_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '7':
            y = seventh_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + fourth_val + seventh_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + fourth_key + ' ' + 'AND' + ' ' + seventh_key + '\n')
            del same_assemblies_records[fourth_key]
            del same_assemblies_records[seventh_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '8':
            y = eighth_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + fourth_val + eighth_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + fourth_key + ' ' + 'AND' + ' ' + eighth_key + '\n')
            del same_assemblies_records[fourth_key]
            del same_assemblies_records[eighth_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '9':
            y = nineth_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + fourth_val + nineth_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + fourth_key + ' ' + 'AND' + ' ' + nineth_key + '\n')
            del same_assemblies_records[fourth_key]
            del same_assemblies_records[nineth_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '10':
            y = tenth_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + fourth_val + tenth_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + fourth_key + ' ' + 'AND' + ' ' + tenth_key + '\n')
            del same_assemblies_records[fourth_key]
            del same_assemblies_records[tenth_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
    if a == '5':
        x = fifth_key.split(' ')
        if b == '1':
            y = first_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + fifth_val + first_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + fifth_key + ' ' + 'AND' + ' ' + first_key + '\n')
            del same_assemblies_records[fifth_key]
            del same_assemblies_records[first_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '2':
            y = second_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + fifth_val + second_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + fifth_key + ' ' + 'AND' + ' ' + second_key + '\n')
            del same_assemblies_records[fifth_key]
            del same_assemblies_records[second_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '3':
            y = third_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + fifth_val + third_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + fifth_key + ' ' + 'AND' + ' ' + third_key + '\n')
            del same_assemblies_records[fifth_key]
            del same_assemblies_records[third_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '4':
            y = fourth_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + fifth_val + fourth_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + fifth_key + ' ' + 'AND' + ' ' + fourth_key + '\n')
            del same_assemblies_records[fifth_key]
            del same_assemblies_records[fourth_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '6':
            y = sixth_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + fifth_val + sixth_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + fifth_key + ' ' + 'AND' + ' ' + sixth_key + '\n')
            del same_assemblies_records[fifth_key]
            del same_assemblies_records[sixth_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '7':
            y = seventh_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + fifth_val + seventh_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + fifth_key + ' ' + 'AND' + ' ' + seventh_key + '\n')
            del same_assemblies_records[fifth_key]
            del same_assemblies_records[seventh_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '8':
            y = eighth_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + fifth_val + eighth_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + fifth_key + ' ' + 'AND' + ' ' + eighth_key + '\n')
            del same_assemblies_records[fifth_key]
            del same_assemblies_records[eighth_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '9':
            y = nineth_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + fifth_val + nineth_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + fifth_key + ' ' + 'AND' + ' ' + nineth_key + '\n')
            del same_assemblies_records[fifth_key]
            del same_assemblies_records[nineth_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '10':
            y = tenth_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + fifth_val + tenth_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + fifth_key + ' ' + 'AND' + ' ' + tenth_key + '\n')
            del same_assemblies_records[fifth_key]
            del same_assemblies_records[tenth_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
    if a == '6':
        x = sixth_key.split(' ')
        if b == '1':
            y = first_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + sixth_val + first_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + sixth_key + ' ' + 'AND' + ' ' + first_key + '\n')
            del same_assemblies_records[sixth_key]
            del same_assemblies_records[first_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '2':
            y = second_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + sixth_val + second_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + sixth_key + ' ' + 'AND' + ' ' + second_key + '\n')
            del same_assemblies_records[sixth_key]
            del same_assemblies_records[second_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '3':
            y = third_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + sixth_val + third_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + sixth_key + ' ' + 'AND' + ' ' + third_key + '\n')
            del same_assemblies_records[sixth_key]
            del same_assemblies_records[third_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '4':
            y = fourth_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + sixth_val + fourth_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + sixth_key + ' ' + 'AND' + ' ' + fourth_key + '\n')
            del same_assemblies_records[sixth_key]
            del same_assemblies_records[fourth_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '5':
            y = fifth_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + sixth_val + fifth_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + sixth_key + ' ' + 'AND' + ' ' + fifth_key + '\n')
            del same_assemblies_records[sixth_key]
            del same_assemblies_records[fifth_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '7':
            y = seventh_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + sixth_val + seventh_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + sixth_key + ' ' + 'AND' + ' ' + seventh_key + '\n')
            del same_assemblies_records[sixth_key]
            del same_assemblies_records[seventh_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '8':
            y = eighth_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + sixth_val + eighth_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + sixth_key + ' ' + 'AND' + ' ' + eighth_key + '\n')
            del same_assemblies_records[sixth_key]
            del same_assemblies_records[eighth_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '9':
            y = nineth_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + sixth_val + nineth_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + sixth_key + ' ' + 'AND' + ' ' + nineth_key + '\n')
            del same_assemblies_records[sixth_key]
            del same_assemblies_records[nineth_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '10':
            y = tenth_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + sixth_val + tenth_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + sixth_key + ' ' + 'AND' + ' ' + tenth_key + '\n')
            del same_assemblies_records[sixth_key]
            del same_assemblies_records[tenth_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
    if a == '7':
        x = seventh_key.split(' ')
        if b == '1':
            y = first_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + seventh_val + first_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + seventh_key + ' ' + 'AND' + ' ' + first_key + '\n')
            del same_assemblies_records[seventh_key]
            del same_assemblies_records[first_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '2':
            y = second_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + seventh_val + second_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + seventh_key + ' ' + 'AND' + ' ' + second_key + '\n')
            del same_assemblies_records[seventh_key]
            del same_assemblies_records[second_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '3':
            y = third_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + seventh_val + third_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + seventh_key + ' ' + 'AND' + ' ' + third_key + '\n')
            del same_assemblies_records[seventh_key]
            del same_assemblies_records[third_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '4':
            y = fourth_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + seventh_val + fourth_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + seventh_key + ' ' + 'AND' + ' ' + fourth_key + '\n')
            del same_assemblies_records[seventh_key]
            del same_assemblies_records[fourth_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '5':
            y = fifth_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + seventh_val + fifth_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + seventh_key + ' ' + 'AND' + ' ' + fifth_key + '\n')
            del same_assemblies_records[seventh_key]
            del same_assemblies_records[fifth_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '6':
            y = sixth_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + seventh_val + sixth_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + seventh_key + ' ' + 'AND' + ' ' + sixth_key + '\n')
            del same_assemblies_records[seventh_key]
            del same_assemblies_records[sixth_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '8':
            y = eighth_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + seventh_val + eighth_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + seventh_key + ' ' + 'AND' + ' ' + eighth_key + '\n')
            del same_assemblies_records[seventh_key]
            del same_assemblies_records[eighth_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '9':
            y = nineth_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + seventh_val + nineth_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + seventh_key + ' ' + 'AND' + ' ' + nineth_key + '\n')
            del same_assemblies_records[seventh_key]
            del same_assemblies_records[nineth_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '10':
            y = tenth_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + seventh_val + tenth_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + seventh_key + ' ' + 'AND' + ' ' + tenth_key + '\n')
            del same_assemblies_records[seventh_key]
            del same_assemblies_records[tenth_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
    if a == '8':
        x = eighth_key.split(' ')
        if b == '1':
            y = first_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + eighth_val + first_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + eighth_key + ' ' + 'AND' + ' ' + first_key + '\n')
            del same_assemblies_records[eighth_key]
            del same_assemblies_records[first_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '2':
            y = second_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + eighth_val + second_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + eighth_key + ' ' + 'AND' + ' ' + second_key + '\n')
            del same_assemblies_records[eighth_key]
            del same_assemblies_records[second_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '3':
            y = third_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + eighth_val + third_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + eighth_key + ' ' + 'AND' + ' ' + third_key + '\n')
            del same_assemblies_records[eighth_key]
            del same_assemblies_records[third_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '4':
            y = fourth_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + eighth_val + fourth_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + eighth_key + ' ' + 'AND' + ' ' + fourth_key + '\n')
            del same_assemblies_records[eighth_key]
            del same_assemblies_records[fourth_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '5':
            y = fifth_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + eighth_val + fifth_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + eighth_key + ' ' + 'AND' + ' ' + fifth_key + '\n')
            del same_assemblies_records[eighth_key]
            del same_assemblies_records[fifth_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '6':
            y = sixth_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + eighth_val + sixth_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + eighth_key + ' ' + 'AND' + ' ' + sixth_key + '\n')
            del same_assemblies_records[eighth_key]
            del same_assemblies_records[sixth_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '7':
            y = seventh_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + eighth_val + seventh_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + eighth_key + ' ' + 'AND' + ' ' + seventh_key + '\n')
            del same_assemblies_records[eighth_key]
            del same_assemblies_records[seventh_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '9':
            y = nineth_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + eighth_val + nineth_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + eighth_key + ' ' + 'AND' + ' ' + nineth_key + '\n')
            del same_assemblies_records[eighth_key]
            del same_assemblies_records[nineth_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '10':
            y = tenth_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + eighth_val + tenth_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + eighth_key + ' ' + 'AND' + ' ' + tenth_key + '\n')
            del same_assemblies_records[eighth_key]
            del same_assemblies_records[tenth_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
    if a == '9':
        x = nineth_key.split(' ')
        if b == '1':
            y = first_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + nineth_val + first_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + nineth_key + ' ' + 'AND' + ' ' + first_key + '\n')
            del same_assemblies_records[nineth_key]
            del same_assemblies_records[first_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '2':
            y = second_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + nineth_val + second_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + nineth_key + ' ' + 'AND' + ' ' + second_key + '\n')
            del same_assemblies_records[nineth_key]
            del same_assemblies_records[second_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '3':
            y = third_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + nineth_val + third_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + nineth_key + ' ' + 'AND' + ' ' + third_key + '\n')
            del same_assemblies_records[nineth_key]
            del same_assemblies_records[third_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '4':
            y = fourth_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + nineth_val + fourth_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + nineth_key + ' ' + 'AND' + ' ' + fourth_key + '\n')
            del same_assemblies_records[nineth_key]
            del same_assemblies_records[fourth_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '5':
            y = fifth_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + nineth_val + fifth_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + nineth_key + ' ' + 'AND' + ' ' + fifth_key + '\n')
            del same_assemblies_records[nineth_key]
            del same_assemblies_records[fifth_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '6':
            y = sixth_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + nineth_val + sixth_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + nineth_key + ' ' + 'AND' + ' ' + sixth_key + '\n')
            del same_assemblies_records[nineth_key]
            del same_assemblies_records[sixth_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '7':
            y = seventh_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + nineth_val + seventh_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + nineth_key + ' ' + 'AND' + ' ' + seventh_key + '\n')
            del same_assemblies_records[nineth_key]
            del same_assemblies_records[seventh_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '8':
            y = eighth_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + nineth_val + eighth_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + nineth_key + ' ' + 'AND' + ' ' + eighth_key + '\n')
            del same_assemblies_records[nineth_key]
            del same_assemblies_records[eighth_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '10':
            y = tenth_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + nineth_val + tenth_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + nineth_key + ' ' + 'AND' + ' ' + tenth_key + '\n')
            del same_assemblies_records[nineth_key]
            del same_assemblies_records[tenth_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
    if a == '10':
        x = tenth_key.split(' ')
        if b == '1':
            y = first_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + tenth_val + first_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + tenth_key + ' ' + 'AND' + ' ' + first_key + '\n')
            del same_assemblies_records[tenth_key]
            del same_assemblies_records[first_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '2':
            y = second_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + tenth_val + second_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + tenth_key + ' ' + 'AND' + ' ' + second_key + '\n')
            del same_assemblies_records[tenth_key]
            del same_assemblies_records[second_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '3':
            y = third_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + tenth_val + third_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + tenth_key + ' ' + 'AND' + ' ' + third_key + '\n')
            del same_assemblies_records[tenth_key]
            del same_assemblies_records[third_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '4':
            y = fourth_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + tenth_val + fourth_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + tenth_key + ' ' + 'AND' + ' ' + fourth_key + '\n')
            del same_assemblies_records[tenth_key]
            del same_assemblies_records[fourth_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '5':
            y = fifth_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + tenth_val + fifth_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + tenth_key + ' ' + 'AND' + ' ' + fifth_key + '\n')
            del same_assemblies_records[tenth_key]
            del same_assemblies_records[fifth_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '6':
            y = sixth_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + tenth_val + sixth_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + tenth_key + ' ' + 'AND' + ' ' + sixth_key + '\n')
            del same_assemblies_records[tenth_key]
            del same_assemblies_records[sixth_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '7':
            y = seventh_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + tenth_val + seventh_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + tenth_key + ' ' + 'AND' + ' ' + seventh_key + '\n')
            del same_assemblies_records[tenth_key]
            del same_assemblies_records[seventh_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '8':
            y = eighth_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + tenth_val + eighth_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + tenth_key + ' ' + 'AND' + ' ' + eighth_key + '\n')
            del same_assemblies_records[tenth_key]
            del same_assemblies_records[eighth_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
        elif b == '9':
            y = nineth_key.split(' ')
            g.write('>' + x[0] + y[0] + ' ' + " ".join(x[1:]) + '\n' + tenth_val + nineth_val + '\n')
            o.write((os.path.splitext(sys.argv[1])[0]) + '\n' + 'FUSED: ' + tenth_key + ' ' + 'AND' + ' ' + nineth_key + '\n')
            del same_assemblies_records[tenth_key]
            del same_assemblies_records[nineth_key]
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
    same_assemblies_records.clear()   




#Create boolean function. The reply converts the answer to lower case and strips. It takes y or n as input.
#If yes, call the n_c_terminal function from above.
#If no, write the sequences in the outfile as they are.
#If you give it sth else, it will skip and the sequences will be lost. 
def yes_or_no(question):
    reply = str(input(question+' (y/n): ')).lower().strip()
    if reply[0] == 'y':
        print('Neat' +'\n')
        n_c_terminal("Type in N-terminal sequence first and C-terminal sequence second (for example, type: 1 2, if the first sequence is the N-terminal sequence and the second sequence is the C-terminal sequence, please separate with space): ")
    if reply[0] == 'n':
        print('Oh, cmon' + '\n')
        for key, value in same_assemblies_records.items():
            g.write('>' + key + '\n' + value + '\n')
        same_assemblies_records.clear()
        

#Open fasta input with sequences. Split header elements at spaces.
with open(sys.argv[1]) as in_fasta:
    for title, seq in SimpleFastaParser(in_fasta):
        x = title.split(' ')
#Create a list of unique assemblies (second element) of the MSA sequences.
        if x[1] not in assemblies:
            assemblies.append(x[1])


#For each unique assembly, set a variable n at 0. Open the alignment and split thr headers; if the assembly matches the one getting checked, put it in a dictionary (header is key, sequence is value).
for item in assemblies:
    n=0
    with open(sys.argv[1]) as in_fasta:
        for title, seq in SimpleFastaParser(in_fasta):
            y = title.split(' ')
            if y[1] == item:
                same_assemblies_records.update( {title : seq} )
                n +=1    
#If you've found two sequences with the same assembly, print them and define variables for the key and value of each. Ask if user wants to fuse calling the yes_or_no function from above.
#Repeat for different numbers of sequences up to ten. If there are more than ten sequences no question is asked and they just get written in the outfile.
        if n == 2:
            for key, value in same_assemblies_records.items():
                print(key + '\n' + value)
            first_key = list(same_assemblies_records)[0]
            first_val = list(same_assemblies_records.values())[0]
            second_key = list(same_assemblies_records)[1]
            second_val = list(same_assemblies_records.values())[1]
            yes_or_no('Hi, would you like to fuse some of these sequences?')
        elif n == 3:
            for key, value in same_assemblies_records.items():
                print(key + '\n' + value)
            first_key = list(same_assemblies_records)[0]
            first_val = list(same_assemblies_records.values())[0]
            second_key = list(same_assemblies_records)[1]
            second_val = list(same_assemblies_records.values())[1]
            third_key = list(same_assemblies_records)[2]
            third_val = list(same_assemblies_records.values())[2]
            yes_or_no('Hi, would you like to fuse some of these sequences?')
        elif n == 4:
            for key, value in same_assemblies_records.items():
                print(key + '\n' + value)
            first_key = list(same_assemblies_records)[0]
            first_val = list(same_assemblies_records.values())[0]
            second_key = list(same_assemblies_records)[1]
            second_val = list(same_assemblies_records.values())[1]
            third_key = list(same_assemblies_records)[2]
            third_val = list(same_assemblies_records.values())[2]
            fourth_key = list(same_assemblies_records)[3]
            fourth_val = list(same_assemblies_records.values())[3]
            yes_or_no('Hi, would you like to fuse some of these sequences?')
        elif n == 5:
            for key, value in same_assemblies_records.items():
                print(key + '\n' + value)
            first_key = list(same_assemblies_records)[0]
            first_val = list(same_assemblies_records.values())[0]
            second_key = list(same_assemblies_records)[1]
            second_val = list(same_assemblies_records.values())[1]
            third_key = list(same_assemblies_records)[2]
            third_val = list(same_assemblies_records.values())[2]
            fourth_key = list(same_assemblies_records)[3]
            fourth_val = list(same_assemblies_records.values())[3]
            fifth_key = list(same_assemblies_records)[4]
            fifth_val = list(same_assemblies_records.values())[4]
            yes_or_no('Hi, would you like to fuse some of these sequences?')
        elif n == 6:
            for key, value in same_assemblies_records.items():
                print(key + '\n' + value)
            first_key = list(same_assemblies_records)[0]
            first_val = list(same_assemblies_records.values())[0]
            second_key = list(same_assemblies_records)[1]
            second_val = list(same_assemblies_records.values())[1]
            third_key = list(same_assemblies_records)[2]
            third_val = list(same_assemblies_records.values())[2]
            fourth_key = list(same_assemblies_records)[3]
            fourth_val = list(same_assemblies_records.values())[3]
            fifth_key = list(same_assemblies_records)[4]
            fifth_val = list(same_assemblies_records.values())[4]
            sixth_key = list(same_assemblies_records)[5]
            sixth_val = list(same_assemblies_records.values())[5]
            yes_or_no('Hi, would you like to fuse some of these sequences?')
        elif n == 7:
            for key, value in same_assemblies_records.items():
                print(key + '\n' + value)
            first_key = list(same_assemblies_records)[0]
            first_val = list(same_assemblies_records.values())[0]
            second_key = list(same_assemblies_records)[1]
            second_val = list(same_assemblies_records.values())[1]
            third_key = list(same_assemblies_records)[2]
            third_val = list(same_assemblies_records.values())[2]
            fourth_key = list(same_assemblies_records)[3]
            fourth_val = list(same_assemblies_records.values())[3]
            fifth_key = list(same_assemblies_records)[4]
            fifth_val = list(same_assemblies_records.values())[4]
            sixth_key = list(same_assemblies_records)[5]
            sixth_val = list(same_assemblies_records.values())[5]
            seventh_key = list(same_assemblies_records)[6]
            seventh_val = list(same_assemblies_records.values())[6]
            yes_or_no('Hi, would you like to fuse some of these sequences?')
        elif n == 8:
            for key, value in same_assemblies_records.items():
                print(key + '\n' + value)
            first_key = list(same_assemblies_records)[0]
            first_val = list(same_assemblies_records.values())[0]
            second_key = list(same_assemblies_records)[1]
            second_val = list(same_assemblies_records.values())[1]
            third_key = list(same_assemblies_records)[2]
            third_val = list(same_assemblies_records.values())[2]
            fourth_key = list(same_assemblies_records)[3]
            fourth_val = list(same_assemblies_records.values())[3]
            fifth_key = list(same_assemblies_records)[4]
            fifth_val = list(same_assemblies_records.values())[4]
            sixth_key = list(same_assemblies_records)[5]
            sixth_val = list(same_assemblies_records.values())[5]
            seventh_key = list(same_assemblies_records)[6]
            seventh_val = list(same_assemblies_records.values())[6]
            eighth_key = list(same_assemblies_records)[7]
            eighth_val = list(same_assemblies_records.values())[7]
            yes_or_no('Hi, would you like to fuse some of these sequences?')
        elif n == 9:
            for key, value in same_assemblies_records.items():
                print(key + '\n' + value)
            first_key = list(same_assemblies_records)[0]
            first_val = list(same_assemblies_records.values())[0]
            second_key = list(same_assemblies_records)[1]
            second_val = list(same_assemblies_records.values())[1]
            third_key = list(same_assemblies_records)[2]
            third_val = list(same_assemblies_records.values())[2]
            fourth_key = list(same_assemblies_records)[3]
            fourth_val = list(same_assemblies_records.values())[3]
            fifth_key = list(same_assemblies_records)[4]
            fifth_val = list(same_assemblies_records.values())[4]
            sixth_key = list(same_assemblies_records)[5]
            sixth_val = list(same_assemblies_records.values())[5]
            seventh_key = list(same_assemblies_records)[6]
            seventh_val = list(same_assemblies_records.values())[6]
            eighth_key = list(same_assemblies_records)[7]
            eighth_val = list(same_assemblies_records.values())[7]
            nineth_key = list(same_assemblies_records)[8]
            nineth_val = list(same_assemblies_records.values())[8]
            yes_or_no('Hi, would you like to fuse some of these sequences?')
        elif n == 10:
            for key, value in same_assemblies_records.items():
                print(key + '\n' + value)
            first_key = list(same_assemblies_records)[0]
            first_val = list(same_assemblies_records.values())[0]
            second_key = list(same_assemblies_records)[1]
            second_val = list(same_assemblies_records.values())[1]
            third_key = list(same_assemblies_records)[2]
            third_val = list(same_assemblies_records.values())[2]
            fourth_key = list(same_assemblies_records)[3]
            fourth_val = list(same_assemblies_records.values())[3]
            fifth_key = list(same_assemblies_records)[4]
            fifth_val = list(same_assemblies_records.values())[4]
            sixth_key = list(same_assemblies_records)[5]
            sixth_val = list(same_assemblies_records.values())[5]
            seventh_key = list(same_assemblies_records)[6]
            seventh_val = list(same_assemblies_records.values())[6]
            eighth_key = list(same_assemblies_records)[7]
            eighth_val = list(same_assemblies_records.values())[7]
            nineth_key = list(same_assemblies_records)[8]
            nineth_val = list(same_assemblies_records.values())[8]
            tenth_key = list(same_assemblies_records)[9]
            tenth_val = list(same_assemblies_records.values())[9]
            yes_or_no('Hi, would you like to fuse some of these sequences?')
        else:
            for key, value in same_assemblies_records.items():
                g.write('>' + key + '\n' + value + '\n')
            same_assemblies_records.clear()
g.close()
o.close()
