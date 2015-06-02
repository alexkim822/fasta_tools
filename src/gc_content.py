#!/usr/bin/env python

import sys

fasta_filename = sys.argv[1]

# TODO declare some sort of variable to hold gc counts

with open(fasta_filename, 'r') as fasta_file:
    for line in fasta_file:
        # TODO do stuff to update gc counts
        pass

# TODO calculate gc content

# TODO print gc content; format should be "GC content: 0.X"
# for example, the single sequence GCAA would yield "GC content: 0.5"
