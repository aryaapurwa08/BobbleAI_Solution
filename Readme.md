# Word Suggestion

## Goal

Given a list of words (say dictionary) in a csv file along with its frequency. Take a word as input
and suggest five closest words from the dictionary sorted in order of relevance.
Assume that the user is trying to type a dictionary word which they misspelled, and you have to
suggest the correct word.


## Language

python 3.6

## Usage

1. Download the code.py from repositry
2. Create your own csv file or use the one provided in dump folder.
3. Running the code
	Format - ``` code.py <data csv file> <search word>```
	3.1 Windows
	```sh
	> python code.py data.csv hellp
	```
	3.2 Linux and mac
	```sh
	$ chmod +x code.py
	$ ./code.py data.csv hellp
	```

