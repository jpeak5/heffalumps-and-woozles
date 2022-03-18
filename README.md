## Heffalumps and Woozles
Solutions for math challenge problems brought home from Ms. G's 3rd grade class.

### Heffalump #3 - $1.00 Word Search

#### Prompt
Find as many words as possible that add up to $1.00, given that the letters in a word have value following the pattern 'a' = $0.01, 'b' = $0.02, ..., 'z' = $0.26.

With values assigned to the letters in this pattern, words like "excellent" and "discipline" total $1.00.

#### Solving with brute-force in python
one-dollar-words.py is a command line Python3 script that can be run with various options to explore this prompt.

##### Usage
```
$ ./one-dollar-words.py -h
usage: one-dollar-words.py [-h] [--dictionary-file DICTIONARY_FILE] [--letter-score]
                           [--score SCORE] [--skip-plurals] [--word WORD]

optional arguments:
  -h, --help            show this help message and exit
  --dictionary-file DICTIONARY_FILE, -f DICTIONARY_FILE
                        Path to a file
  --letter-score, -l    whether to print individual letter scores
  --score SCORE, -s SCORE
                        show only words matching this target score
  --skip-plurals, -p    whether to include plurals as valid
  --word WORD, -w WORD  Score a single word
```

Two modes exist and other options can be set to modify the behavior:

###### System dictionary
Without arguments, the script reads its input from /usr/share/dict/words, a dictionary provided under Linux. Running the script with no options is equivalent to running it with `--dictionary-file /usr/share/dict/words`. On other systems, provide this option, specifying the full path to a text file of words, one per line.

```
$ ./one-dollar-words.py
a: 1
aachen: 32
aaliyah: 57
aardvark: 76
aardvarks: 95
aaron: 49
...
zwingli: 100
zworykin: 141
zygote: 98
zygotes: 117
zyrtec: 97
zyuganov: 131
```

This output can be modified by providing any of the other options. For example, specifying `--score 101` will only emit words whose 'scores' equal 101.

The `--letter-score` option causes the script to print the value of each letter, in addition to the total score for a word:

It's possible to specify one or more words on the command line, causing the script to ignore the system (or user-specified) dictionary and evaluate only command line input. Combining this option with `--letter-score` is useful for checking your math.

Evaluate a word provided as an argument on the command line, for example:
```
$ ./one-dollar-words.py -w woozle
woozle: 96
```

Multiple words and `--letter-score`:
```
$ ./one-dollar-words.py --letter-score -w heffalump -w woozle

h:          8
e:          5
f:          6
f:          6
a:          1
l:         12
u:         21
m:         13
p:         16
heffalump: 88

w:      23
o:      15
o:      15
z:      26
l:      12
e:       5
woozle: 96
```
