# Deepurify_Project
**Paper --> Deepurify: a multi-modal deep language model to remove contamination from metagenome-assembled genomes**

Deepurify elevates metagenome-assembled genomes' (MAGs) quality by utilizing a multi-modal deep language model to filter contaminated contigs, and it can leverage GPU acceleration.


## Dependencies:
Create deepurify's conda environment by using this command:
```
conda env create -n deepurify -f deepurify-conda-env.yml
```

and Please download PyTorch v2.0.0 -cu118 from **[http://pytorch.org/](http://pytorch.org/)** if you want to use GPUs (We highly recommend to use GPUs).

### OR install the dependencies manually

Please independently install the following tools and ensure their proper functionality.

1. **[prodigal](https://github.com/hyattpd/Prodigal/wiki/installation)** v 2.6.3 (ORF/CDS-prediction)
2. **[hmmer](http://hmmer.org/download.html)** v.3.3.2 (Detecting conserved single-copy marker genes)
3. **[CheckM2](https://github.com/chklovski/CheckM2)** v 1.0.1 (Evaluate the quality of MAGs)
4. **[dRep](https://github.com/MrOlm/drep)** v3.5.0 (Filter replicated MAGs)
5. **[CONCOCT](https://github.com/BinPro/CONCOCT)** v1.1.0 (Binner)
6. **[MetaBAT2](https://bitbucket.org/berkeleylab/metabat/src/master/)** v2.15 (Binner)
7. **[Semibin2](https://github.com/BigDataBiology/SemiBin)** v2.1.0 (Binner)

**Note**: Ensure that all the listed dependencies above are installed and functioning without any errors.


## Installation:
**FIRST STEP**
Create deepurify's conda environment by using this command:
```
conda env create -n deepurify -f deepurify-conda-env.yml
```

**SECOND STEP**
Deepurify can be installed using pip. 
```
pip install Deepurify==2.3.0
```


## Download Files and Set Environment Variable for Running
- Download the database (required files) for running Deepurify from this **[LINK](https://drive.google.com/file/d/1FXpxoXFYHcX9QAFe7U6zfM8YjalxNLFk/view?usp=sharing)**.

- Unzip the downloaded file and set an **environment variable** called "DeepurifyInfoFiles" by adding the following line to the last line of .bashrc file (~/.bashrc):
```
export DeepurifyInfoFiles=/path/of/this/unzip/folder/
```
For example: 'export DeepurifyInfoFiles=/home/csbhzou/software/DeepurifyInfoFiles/'.

- Save the .bashrc file, and then execute:
```
source .bashrc
```


## Running Deepurify
1.  You can run the Deepurify through the **cleanMAGs** function.
```
from Deepurify.clean_func import cleanMAGs

if __name__ == "__main__":
    inputBinFolderPath = "./demo_input/"
    outputBinFolderPath = "./demo_output/"
    
    cleanMAGs(
        input_bin_folder_path=inputBinFolderPath, # Input directory containing MAGs
        output_bin_folder_path=outputBinFolderPath, # Output directory containing purification MAGs
        bin_suffix="fa", # The file suffix of MAGs.
        gpu_num=1, # Specify the number of GPUs to be used (use '0' for CPU, considerably slower than using GPU).
        batch_size_per_gpu=1, # The number of batch size for each GPU. Useless with gpu_num=0
        num_threads_per_device=1, # The number of threads for labeling taxonomic lineage for contigs.
        num_threads_call_genes=1, # The number of threads to call genes.
        checkM_process_num=1, # The number of processes to run CheckM simultaneously.
        num_threads_per_checkm=1, # The number of threads to run a single CheckM process.
        temp_output_folder=None, # The directory to store temporary files.
    )

```
Please refer to the documentation of this function for more details.

2.  You can run Deepurify through the following command:
```
deepurify clean  -i ./demo_input/ -o ./demo_output/ --bin_suffix fa --gpu_num 1 --num_threads_per_device 1
```
----------------------------------------------------------------------------------------------------------------------------------------
```
arguments:
    -i --input_path               Input directory containing MAGs
    -o --output_path              Output directory containing purification MAGs
       --bin_suffix               The file suffix of MAGs.

optional arguments:
       --gpu_num                  Specify the number of GPUs to be used (use '0' for CPU, considerably slower than using GPU).
       --num_threads_per_device   The number of threads for inference.
    -h --help                     show this help message and exit
```
Please run 'deepurify clean -h' for more details.


## Files in output directory
- #### The purified MAGs.
- #### time.txt 
The elapsed running time of Deepurify is shown in two columns. 

1. The first column represents the time (seconds) taken to infer the taxonomic lineage.
2. The second column represents the time (seconds) taken to evaluate the results.

- #### MetaInfo.txt 
This file contains the following columns: 

1. MAG name (first column), 
2. completeness of MAG (second column), 
3. contamination of MAG (third column), 
4. MAG quality (fourth column),
5. potential taxonomic lineage for MAG (fifth column).

## Minimum System Requirements for Running Deepurify
- System: Linux (>= Ubuntu 22.04.2 LTS)
- CPU: No restriction.
- RAM: > 45GB (Running CheckM with using the full reference genome tree required approximately 40 GB of memory.)
- GPU: The GPU memory must be equal to or greater than 3GB.

This system can run the configuration in the **"Running Deepurify"** section.


## Our System Config
- System: WSL (Ubuntu 22.04.2 LTS)
- CPU: AMD EPYC 7543 32 cores 64 threads.
- RAM: 256GB
- GPU: Double GTX-3090 24GB

This system can run the configuration in the main.py file.
