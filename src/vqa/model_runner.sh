#! /bin/bash

#$ -j yes
#$ -N model_runner
#$ -o /home//vagueness/src/jimena_work/model_run.out
#$ -l 'mem_free=1M,h_rt=01:00:00'
#$ -m ae -M jgualla1@jh.edu
#$ -cwd

/home/eliasse/lxmert/snap/pretrained/model_LXRT.pth 1 results_1 --test output_sunnycloudy.json #--load home/jgualla1/vagueness/src/jimena_work 
