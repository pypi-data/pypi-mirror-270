import sys
import os
import urllib.request

sys.path.append('pathmodules/')
# from blastvariables import *

def run_blastp(seq1, seq2):
    os.system("blastp -query " + input_seq + seq1 +
        ".fasta -subject " + input_seq + seq2 +
        ".fasta -out " + seq1 + "-" + seq2 + ".aln")

def get_seq(seq1, seq2):
    for seq in (seq1, seq2):
        url = 'http://www.uniprot.org/uniprot/' + seq + '.fasta'
        handler = urllib.request.urlopen(url)
        fasta = handler.read().decode('utf-8')
        out = open(input_seq + seq + '.fasta', 'w')
        out.write(fasta)

if __name__ == '__main__':
    try:
        seq1 = sys.argv[1]
        seq2 = sys.argv[2]
    except:
        print('usage: BlastpWrapper.py seq1-UniprotAC seq2-UniprotAC')
        raise SystemExit
    else:
        if os.path.exists(input_seq + seq1 + '.fasta') \
        and os.path.exists(input_seq + seq2 + '.fasta'):
            run_blastp(seq1, seq2)
        else:
            get_seq(seq1, seq2)
            run_blastp(seq1, seq2)
