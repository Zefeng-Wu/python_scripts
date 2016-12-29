#!/usr/bin/env python

from __future__ import print_function
import argparse
import sys
import gzip
from collections import defaultdict
from Bio import SeqIO

parser = argparse.ArgumentParser(description="extract_cds_by_gff")
parser.add_argument('-t', '--type', type=str, default='CDS', help='gene type [CDS]')
parser.add_argument('-us', '--up-stream', type=int, default=0, help='up stream length [0]')
parser.add_argument('-ds', '--down-stream', type=int, default=0, help='down stream length [0]')
parser.add_argument('gff_file', type=str, help='gff file')
parser.add_argument('fasta_file', type=str, help='fasta file')
args = parser.parse_args()
if not (args.up_stream >= 0 and args.down_stream >= 0):
    print('value of --up-stream and --down-stream should be >= 0', file=sys.stderr)
    sys.exit(1)


def read_gff_file(file):
    genes = defaultdict(list)
    with open(file, 'rt') as fh:
        for row in fh:
            data = row.strip().split('\t')
            if len(data) < 9:
                continue
            name = data[0]
            
            genes[name].append(gene)
    return genes


genes = read_gff_file(args.gff_file)

fh = gzip.open(args.fasta_file, 'rt') if args.fasta_file.endswith('.gz') else open(args.fasta_file, 'r')
for record in SeqIO.parse(fh, 'fasta'):
    name, genome = record.id, record.seq
    if record.id not in genes:
        continue

    for gene in genes[name]:
        if gene['type'].lower() != args.type.lower():
            continue
        seq = ''
        if gene['strand'] == '+':
            s = gene['start'] - args.up_stream - 1
            s = 0 if s < 0 else s
            seq = genome[s:gene['end'] + args.down_stream]
        else:
            s = gene['start'] - args.down_stream - 1
            s = 0 if s < 0 else s
            seq = genome[s:gene['end'] + args.up_stream].reverse_complement()
        print('>{}_{}..{}..{}\n{}'.format(name, gene['start'], gene['end'], gene['strand'], seq))
fh.close()
