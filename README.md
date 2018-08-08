Introduction
============
MetaRon (Metagenomic opeRon prediction pipeline) is a computational workflow for the prediction of operons from metagenomic data. The pipeline predicts metagenomic operons without any any functional or experimental data. It comes with options to process the metagenomic data starting from filtered raw reads, which includes: assembly into scaffolds via IDBA, data manipulation, gene prediction via prodigal and lastly operon prediction based on gene's co-directionality, intergenic distance (IGD) and promoters.

Metagenomic operon prediction redefines the operonic clusters by identifying promoters in co-directional genes with an intergenic distance threshold of <= 600 bp. 


Installation
============

Prerequisites
-------------
MetaRon requires:

	* Python (2.7 )

Install MetaRon
---------------
You can install MetaRon either from PyPi using pip and install it from the source. Please make sure you have already installed the above mentioned python libraries required to run MetaRon.

Install from PyPi::

	pip install metaron

Install from the source::
	
	tar -zxvf metaron-1.0.tar.gz
	cd metaron-1.0
	python setup.py install

	
How to use MetaRon
==================
Once you have installed MetaRon, you can type:

	metaron --help

to find the available commands and required parameters to run MetaRon. 


  -h,	--help            
	Show this help message and exit					
  -n	--sample
  	Sample name without any dot, underscore or dash
						
  -p 	PROCESS, 		        --process
			1. ago: assembly gene prediction and operon prediciton
                        2. op: operon prediction only. 

If 'ago', please provide the following parameters:

--sample,--process, --read_type, --read_length, --paired_1, --paired_2, --output

If 'op', please provide the following parameters:

--sample, --process, --igp, --isc, --tool, --output 

  -rt 	READ_TYPE,        --read_type
                          Enter read type. 'merge' if the reads are paired-end in two file. 'paired' if the reads are paired-end in one file.
                        						
  -rl 	READ_LENGTH,	    --read_length
                          Enter 'l'if read length is longer than 128 bases and 'r' if read length is shorter than 128 bases
                         
  -pe1 	PAIRED_1, 		    --paired_1
                          Enter enter paired read file 1
  
  -pe2 	PAIRED_2, 		    --paired_2
                          Enter enter paired read file 2
  
  -pm 	PAIRED_MERGED, 	   --paired_merged
                          Enter the paired end read file if both pairedend reads are in one file
                        
  -i 	IGP, 			          --igp      
						              Select the gene prediction .tab file generated via MetageneMark or Prodigal
                         
  -j 	ISC, 			          --isc
						              Select the file containing all scaftigs
  
  -t 	TOOL, 			        --tool
						              Enter 1 for MetaGeneMark, 2 for Prodigal
  
  -o 	OUTPUT, 		        --output
                          Enter output destination folder


=======================================================*NOTE*=======================================================

If the selected --process is  'op', then please refer to the provided scaftig and gene prediction file format
 
====================================================================================================================

Make predictions
------------------
Metagenomic operon prediction could be performed by providing filtered raw reads under the process "ago" i.e. assembly, gene prediction and operon identification

## test_sample: ERR022075.1.fastq & ERR022075.2.fastq

	metaron --sample ERR022075 --process ago --read_type merge OR paired --read_length r OR l --paired_1 ~/path/to/ERR022075.1.fastq --paired_2 ~/path/to/ERR022075.2.fastq --output ~/path/to/output/directory/

If metagenomic scaffolds and gene predictions are already available, the user can predict operon under the process "op"

## test_assembly: ERR022075_scaf.fa 
## test_gene_prediction: ERR022075_MC

	metaron --sample ERR022075 --process op --igp ERR022075_MC --isc ERR022075_scaf.fa --tool 1 OR 2 --output ~/path/to/output/directory/

This will save metagenomic operon predictions ``Operon_File.tab``.  The prediction file will report the operonic information based on the above mentioned parameters. 


Support
========
If you have questions, or found any bug in the program, please write to us at ``syedshujaat[at]comsats.edu.pk``
