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
	* IDBA (iterative De Bruijn Graph De Novo Assembler) [conda install -c bioconda idba]
	* Prodigal [conda install -c bioconda prodigal]
	* BDGP: Neural Network Promoter Prediction 2.2
	* antiSMASH: antibiotics & Secondary Metabolite Analysis Shell (Optional: required for downstream analysis only.)
	* BOWTIE (Optional: only required for downstream analysis)

If you already have Anaconda environment setup, you can quickly install the prerequisites using any one command from each section:
1. IDBA
	
	conda install -c bioconda idba
	
	
	conda install -c bioconda/label/cf201901 idba
	
2. Prodigal
	
	conda install -c bioconda prodigal
	
	
	conda install -c bioconda/label/cf201901 prodigal
	
3. antiSMASH

	conda install -c bioconda antismash
	
	
	conda install -c bioconda/label/cf201901 antismash
	
4. BOWTIE2

	conda install -c bioconda bowtie

	conda install -c bioconda/label/cf201901 bowtie


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
  
  -n,	--sample            
	Sample name without any dot/underscore/dash
  
  -p,	--process            
	1. ago: assembly gene prediction and operon prediciton
        2. op: operon prediction only. 


If 'ago', please provide the following parameters:

--sample,--process, --read_type, --read_length, --paired_1, --paired_2, --output


If 'op', please provide the following parameters:

--sample, --process, --igp, --isc, --tool, --output 



  -rt,	--read_type            
	Enter read type. 'merge' if the reads are paired-end in two files. 'paired' if the reads are paired-end in one file.
  
  -rl,	--read_length            
	Enter 'l' if read length is longer than 128 bases and 'r' if read length is shorter than 128 bases
  
  -pe1,	--paired_1            
	Enter paired read file 1
  
  -pe2,	--paired_2            
	Enter paired read file 2
  
  -pm,	--paired_merged            
	Enter the paired end read file if both paired-end reads are in one file
  
  -i,	--igp            
	Select the gene prediction .tab file generated via MetageneMark or Prodigal
  
  -j,	--isc            
	Select the file containing all scaftigs
  
  -t,	--tool            
	Enter 1 for MetaGeneMark, 2 for Prodigal
  
  -o,	--output            
	Enter output destination folder
  
  
=======================================================*NOTE*=======================================================

1- If the selected --process is  'op', then please refer to the provided scaftig and gene prediction file format

2- Add NNPP2.2 path to the config.txt file
 
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


Proposed downstream anslysis
----------------------------

1. Secondary Metabolites

	a. Secondary Metabolites identified from operonic sequences using antiSMASH
	
	b. Differntial abundance of Secondary Metabolites (condition-1 / Disease vs Condition-2 / Control)
	
2. Operonnic pathways

	a. Mapping raw metagenomic reads to operonic sequences using BOWTIE
	
	b. Submitting the mapped reads to Functional Mapping and Analysis Pipeline (FMAP)
	
	c. Identifying differential abundance of pathways between disease and control or environment-1 and environment-2


	

Support
========
If you have questions, or found any bug in the program, please write to us at 

``syedshujaat[at]comsats.edu.pk``
``syedzaidi[at]arizona.edu``
