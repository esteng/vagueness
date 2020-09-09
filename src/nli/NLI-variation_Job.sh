#!/bin/bash

#$ -j yes
#$ -N NLI-variation_Job.
#$ -o /home/jgualla1/vagueness/src/NLI-variation_Data/output_normed.json
#$ -l 'mem_free=1M,h_rt=01:00:00'
#$ -m ae -M jgualla1@jh.edu
#$ -cwd

python NLI-variation_Sort.py
