##The MIT License (MIT) Copyright (c) 2021 GEORGE E KOLYFETIS 
##Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
##The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
##THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## This script parses the output .state file produced by IQ-TREE ancestral sequence reconstruction. For each node in the tree, it outputs the most probable reconstructed sequence containing the most probable 
## state/amino acid for each position, and the probability of the reconstructed sequence as the mean probability of the individual positions. It can function on part of an alignment/supermatrix.




# !! Remove all lines from asr output file (.state), that do not start with a Node number (even the headers line).
# the order of aminoacids is p_A	p_R	p_N	p_D	p_C	p_Q	p_E	p_G	p_H	p_I	p_L	p_K	p_M	p_F	p_P	p_S	p_T	p_W	p_Y	p_V

# usage : python ASR_parser.py {input.state} X Y Z {output.faa}

#argument 1 = input file from ASR (.state)
#argument 2 = start position of wanted gene (find it from the input alignment) (X)
#argument 3 = stop position of wanted gene (find it from the input alignment) (Y)
#argument 4 = gene length (do the substraction) (Z = (Y-X)+1)
#argument 5 = output fasta file with every node sequence

import sys

g=open(sys.argv[5] , 'a')
nodes = list()



with open(sys.argv[1], 'r') as ASR:
#open ASR output file (.state), read
#create a list with the unique node numbers
    for line in ASR:
        x = line.split('\t')
        if x[0] not in nodes:
            nodes.append(x[0])          

for i in nodes:
    probfinal=0 #final probability of ancestral sequence
    prob=0 #probability of each sequence position
#set the node sequence to empty, in order to start filling it
    node_sequence=''                
    with open(sys.argv[1], 'r') as ASR:
        for line in ASR:
            x = line.split('\t')
            highest=0 #highest probability of each sequence position
            if i == x[0]:
#pick the highest probability for the position
                highest=max([float(x[3]),float(x[4]),float(x[5]),float(x[6]),float(x[7]),float(x[8]),float(x[9]),float(x[10]),float(x[11]),float(x[12]),float(x[13]),float(x[14]),float(x[15]),float(x[16]),float(x[17]),float(x[18]),float(x[19]),float(x[20]),float(x[21]),float(x[22])])
                if int(x[1]) >= int(sys.argv[2]) and int(x[1]) <= int(sys.argv[3]):
                    prob=prob+highest
#creation of ancestral sequence of the gene
                    node_sequence=node_sequence + x[2] 
#calculation of final probability
            probfinal=prob/int(sys.argv[4])
    g.write('>' + i + ' ' + str(probfinal) + '\n' + node_sequence + '\n')

g.close()
