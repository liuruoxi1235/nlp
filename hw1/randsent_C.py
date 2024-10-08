#!/usr/bin/env python3
"""
601.465/665 — Natural Language Processing
Assignment 1: Designing Context-Free Grammars

Assignment written by Jason Eisner
Modified by Kevin Duh
Re-modified by Alexandra DeLucia

Code template written by Alexandra DeLucia,
based on the submitted assignment with Keith Harrigian
and Carlos Aguirre Fall 2019
"""
import os
import sys
import random
import argparse

# Want to know what command-line arguments a program allows?
# Commonly you can ask by passing it the --help option, like this:
#     python randsent.py --help
# This is possible for any program that processes its command-line
# arguments using the argparse module, as we do below.
#
# NOTE: When you use the Python argparse module, parse_args() is the
# traditional name for the function that you create to analyze the
# command line.  Parsing the command line is different from parsing a
# natural-language sentence.  It's easier.  But in both cases,
# "parsing" a string means identifying the elements of the string and
# the roles they play.

def parse_args():
    """
    Parse command-line arguments.

    Returns:
        args (an argparse.Namespace): Stores command-line attributes
    """
    # Initialize parser
    parser = argparse.ArgumentParser(description="Generate random sentences from a PCFG")
    # Grammar file (required argument)
    parser.add_argument(
        "-g",
        "--grammar",
        type=str, required=True,
        help="Path to grammar file",
    )
    # Start symbol of the grammar
    parser.add_argument(
        "-s",
        "--start_symbol",
        type=str,
        help="Start symbol of the grammar (default is ROOT)",
        default="ROOT",
    )
    # Number of sentences
    parser.add_argument(
        "-n",
        "--num_sentences",
        type=int,
        help="Number of sentences to generate (default is 1)",
        default=1,
    )
    # Max number of nonterminals to expand when generating a sentence
    parser.add_argument(
        "-M",
        "--max_expansions",
        type=int,
        help="Max number of nonterminals to expand when generating a sentence",
        default=450,
    )
    # Print the derivation tree for each generated sentence
    parser.add_argument(
        "-t",
        "--tree",
        action="store_true",
        help="Print the derivation tree for each generated sentence",
        default=False,
    )
    return parser.parse_args()


class Grammar:
    def __init__(self, grammar_file):
        """
        Context-Free Grammar (CFG) Sentence Generator

        Args:
            grammar_file (str): Path to a .gr grammar file
        
        Returns:
            self
        """
        # Parse the input grammar file
        self.rules = {}
        self._load_rules_from_file(grammar_file)

    def _load_rules_from_file(self, grammar_file):
        """
        Read grammar file and store its rules in self.rules

        Args:
            grammar_file (str): Path to the raw grammar file 
        """

        with open(grammar_file, 'r') as file:
            for line in file:

                #Eliminate excessive whitespace
                line = line.strip()

                #Exclude comment lines or blank lines
                if line and not line.startswith('#'):

                    #Read the relative odds(int), LHS(str), RHS(list of str)
                    content = line.split('\t')
                    rel_odd = int(content[0])
                    lhs = content[1]
                    rhs = content[2].split() if len(content) > 2 else [] #allow empty rhs

                    #Check for illegal characters before inserting into rules
                    if any(char in '#()' for char in lhs):
                        continue

                    valid_rhs = []
                    for element in rhs:
                        if any(char in '#()' for char in element):
                            break
                        valid_rhs.append(element)
                
                    #Create a new entry in rules if lhs is not yet presented in rules
                    if lhs not in self.rules:
                        self.rules[lhs] = []
                
                    #Add the rhs & relative odds to the corresponding lhs entry
                    self.rules[lhs].append((rel_odd, valid_rhs)) 


    def sample(self, derivation_tree, max_expansions, start_symbol):
        """
        Sample a random sentence from this grammar

        Args:
            derivation_tree (bool): if true, the returned string will represent 
                the tree (using bracket notation) that records how the sentence 
                was derived
                               
            max_expansions (int): max number of nonterminal expansions we allow

            start_symbol (str): start symbol to generate from

        Returns:
            str: the random sentence or its derivation tree
        """

        #initialize a sentence with ROOT
        start_sent = [start_symbol]
        expansions_left = max_expansions - 1 #since 'ROOT' is also a non-terminal
        def expand(sent, expansions_left):

            #recursion endpoints
            if not any(symbol in self.rules for symbol in sent):
                return sent

            #locate the first symbol to expand. this will yield depth-first expansion
            expand_idx = 0
            while sent[expand_idx] not in self.rules:
                expand_idx += 1

            #randomly select an expansion rule based on odds
            expand_rule = random.choices(self.rules[sent[expand_idx]], weights=[odd for (odd, rhs) in self.rules[sent[expand_idx]]])
            [(_, rhs)] = expand_rule

            #if running out of expansions, prevent future non-terminals
            if expansions_left <= 0:
                rhs = ['...' if symbol in self.rules else symbol for symbol in rhs]

            #replace non-terminal with new symbols
            sent = sent[:expand_idx] + rhs + sent[expand_idx+1:]
            print(sent)
            
            #update expansion counts
            non_terminal_count = sum(1 for symbol in rhs if symbol in self.rules)
            expansions_left -= non_terminal_count

            return expand(sent, expansions_left)

        return " ".join(expand(start_sent, expansions_left))


        raise NotImplementedError


####################
### Main Program
####################
def main():
    # Parse command-line options
    args = parse_args()

    # Initialize Grammar object
    grammar = Grammar(args.grammar)

    # Generate sentences
    for i in range(args.num_sentences):
        # Use Grammar object to generate sentence
        sentence = grammar.sample(
            derivation_tree=args.tree,
            max_expansions=args.max_expansions,
            start_symbol=args.start_symbol
        )

        # Print the sentence with the specified format.
        # If it's a tree, we'll pipe the output through the prettyprint script.
        if args.tree:
            prettyprint_path = os.path.join(os.getcwd(), 'prettyprint')
            t = os.system(f"echo '{sentence}' | perl {prettyprint_path}")
        else:
            print(sentence)


if __name__ == "__main__":
    main()
