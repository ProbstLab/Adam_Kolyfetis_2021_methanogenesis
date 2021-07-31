## Supplementary scripts used in "Genomic remnants of ancestral hydrogen and methane metabolism in Archaea drive anaerobic carbon cycling." by Adam Kolyfetis et al 2021

## License

The scripts within this repository are supplied under the MIT license (see associated LICENSE file).

## Contact Information

For any questions, please consult Panagiotis Adam (panagiotis.adam@uni-due.de).

## Table of Contents

- LICENSE
- ASR_parser.py
- distributions_uniprot.py
- fuse_sequences.py

## Dependencies

- All scripts are written in python3
- required non-standard python3 modules: 
	- Biopython (fuse_sequences.py and distributions_uniprot.py)

## Usage instructions

- ASR_parser.py
	- This script parses the output .state file produced by IQ-TREE ancestral sequence reconstruction. For each node in the tree, it outputs the most probable reconstructed sequence containing the most probable state/amino acid for each position, and the probability of the reconstructed sequence as the mean probability of the individual positions.
	- Usage: python ASR_parser.py input.state X Y Z output.faa
		- input.state: output .state file from IQ-TREE
		- X: start position of wanted gene (see from sequence supermatrix)  
		- Y: stop position of wanted gene (see from sequence supermatrix)
		- Z: gene length (do the substraction) Z=(Y-X)+1
		- output.faa: Output fasta file with every node sequence

- distributions_uniprot.py
	- This script starts by searching each accession from a list of Pfam accessions (given by the user as a text file) in a Uniprot records file (given again by the user). For each Pfam accession it outputs the number for each Domain of life (plus Viruses and Unclassified organisms) this accession can be found in plus the percentage of all those records that corresponds to Archaea only.
	- Usage: python distributions_uniprot.py pfam_accessions.txt uniprot_records.txt
		- pfam_accessions.txt: user-supplied list of Pfam accessions
		- uniprot_records.txt: uniprot records file 
	- Prints to STDOUT

- fuse_sequences.py
	- This script fuses (interactively) sequences from an alignment. It is used for sequences that are split (e.g. due to sequencing or ORF prediction errors), using their accession numbers as a guide.
	- Usage: python fuse_sequences.py fasta_file.faa logfile.txt outfile.txt
		- fasta_file.faa: Alignment file with possible split sequences 
		- logfile.txt: log file detailing cases of fusing of split genes
		- outfile.txt: edited alignment output file with fused and not fused genes
