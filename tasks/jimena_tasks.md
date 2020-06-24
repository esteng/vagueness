# TODO

## Housekeeping and setup
- filling out paperwork X 
    - I-9 form X
- get set up on CLSP grid [here](intro.html) X
	- understand difference between a login node and worker node X
	- understand what kind of hardware is available X
- learn [how to submit jobs](qsub.html) X
	- understand role of a submission script X
	- understand general do's/don'ts of submitting jobs X
	- understand how to submit an interactive job
- set up a virtualenv using conda or virtualenv  X
	- python version 3.7 or 3.6 X
- submit a practice job X 
	- make a python file called "example.py" that prints out the system information (system name, node name, machine, processor) (see [here](https://www.thepythoncode.com/article/get-hardware-system-information-python)) X
	- run the script once on the login node  X
	- run the script in an interactive job 
	- run the script from inside a submitted bash script X

## Vagueness project 
- download VQA dataset [here](https://visualqa.org) X
	- don't download the images just yet, just the questions/captions 
- construct regular expressions for the predicates listed in list_of_canonical_preds.txt file  	X
	- these regexs should capture most forms of the predicate 
	- for example, it should capture "an old man", "the woman is old", "Old people" but not "oldsmobile" or "I told you so" 
	- the <color> predicate should be expanded to match all common colors (e.g. red, blue, etc., periwinkle and chartreuse type colors can be excluded) 
	- try to construct a general regex template that you can then automatically fill with the predicate, rather than hardcoding the template for each predicate
- Use the regexs to search over the image captions and questions in order to find examples like what's already in the VQA folder 
	- the output of this search should have the predicate, the image id, the caption/question string, and the dataset label

	
