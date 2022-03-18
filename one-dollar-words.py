#!/usr/bin/python3

import argparse
import re
import string
import sys


def get_letter_map():
    """Flip the list of ascii chars so that the index becomes the value"""
    letter_map = {}
    idx = 1
    for letter in string.ascii_lowercase:
        letter_map[letter] = idx
        idx += 1
    return letter_map

def score_word(word, letter_map=None):
    """Sum the values for each character according to letter_map"""
    score = 0
    word = word.lower()
    if re.match(r'^[a-z]+$', word) is None:
        raise Exception(f"'{word}' is not in [a-z]")

    if letter_map is None:
        letter_map = get_letter_map()

    for character in word:
        score += letter_map[character]

    return score

def get_default_word_list_from_file(dictionary_file):
    """Param dictionary file should have one word per line

       Words will be lowercased in the resulting list.
       'Words' containing non-letter characters will be dropped.
    """
    with open(dictionary_file, 'r') as f:
        lines = sorted([line.strip().lower() for line in f.readlines()])
        list_of_words = []
        for word in lines:
            if re.match(r'^[a-z]+$', word) is None:
                continue
            list_of_words.append(word)
        return list_of_words

def get_args_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dictionary-file", "-f", help="Path to a file", default="/usr/share/dict/words")
    parser.add_argument("--letter-score", "-l", help="whether to print individual letter scores", action='store_true')
    parser.add_argument("--score", "-s", help="show only words matching this target score", type=int)
    parser.add_argument("--skip-plurals", "-p", help="whether to include plurals as valid", action='store_true', default=False)
    parser.add_argument("--word", "-w", help="Score a single word", action='append')
    return parser

def word_score(word, score):
    return f'{word}: {score}'
    
def per_letter_score(word, letter_map=None):
    if letter_map is None:
        letter_map = get_letter_map()
    word_length = len(word)
    total_score_width = len(str(score_word(word)))
    padding = word_length + total_score_width
    lines_to_print = []
    for idx,char in enumerate(word):
        line = f"{char}:{letter_map[char]: > {padding}}"
        lines_to_print.append(line)
    return lines_to_print
        

def remove_plurals(word_list):
    singulars = []
    for word in word_list:
        if word.lower().endswith('s'):
            continue
        singulars.append(word)
    return singulars

if __name__ == '__main__':
    parser = get_args_parser()
    args = parser.parse_args()

    if args.word:
        word_list = args.word
    else:
        word_list = get_default_word_list_from_file(args.dictionary_file)

    if args.skip_plurals is True:
        word_list = remove_plurals(word_list)

    for word in word_list:
        score = score_word(word)
        if args.score and score != args.score:
            continue
        if args.letter_score:
            print()
            print("\n".join(per_letter_score(word)))
        print(word_score(word, score))
