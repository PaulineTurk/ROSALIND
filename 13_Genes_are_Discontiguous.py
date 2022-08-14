# IMPORT
from Bio import SeqIO

# FUNCTION
def intron_removal(fasta_file):
    fasta_sequences = SeqIO.parse(open(fasta_file),'fasta')
    list_sequence = []
    for fasta in fasta_sequences:
        _, sequence = fasta.id, str(fasta.seq)
        list_sequence.append(sequence)
    sequence_intron_exon = list(list_sequence[0])
    list_intron = list_sequence[1: len(list_sequence)]
    for intron in list_intron:
        len_sequence_intron_exon = len(sequence_intron_exon)
        len_intron = len(intron)
        for position in range(len_sequence_intron_exon-len_intron):
            if "".join(sequence_intron_exon[position: position+len_intron]) == intron: #-1
                del sequence_intron_exon[position: position+len_intron]
    len_sequence_intron_exon = len(sequence_intron_exon)
    sequence_intron_exon_ARN = conversion_T_U(sequence_intron_exon)
    sequence_intron_exon_ARN = "".join(sequence_intron_exon_ARN)
    return sequence_intron_exon_ARN

def conversion_T_U(seq_ADN):
    for index, elem in enumerate(seq_ADN):
        if elem == "T":
            seq_ADN[index] = "U"
    return seq_ADN





def convert_mRNA_protein(mRNA, dico_genetic_code):
    mRNA = list(mRNA)
    print(mRNA)
    len_mRNA = len(mRNA)
    # print(len_mRNA)
    protein = []
    num_codon = 0
    triplet = mRNA[num_codon*3: (num_codon+1)*3]
    triplet = "".join(triplet)
    # print(triplet)
    # print(dico_genetic_code[triplet])
    while dico_genetic_code[triplet] != "Stop": # and (num_codon+1)*3 <= len_mRNA:
        protein.append(dico_genetic_code[triplet])
        num_codon += 1
        # print((num_codon+1)*3)
        if (num_codon+1)*3 <= len_mRNA:
            triplet = mRNA[num_codon*3: (num_codon+1)*3]
            triplet = "".join(triplet)
            
    print("".join(protein))

# PARAMETER
dico_genetic_code = {"UUU": "F",  "CUU": "L", "AUU": "I", "GUU": "V",
                     "UUC": "F",  "CUC": "L", "AUC": "I", "GUC": "V",
                     "UUA": "L",  "CUA": "L", "AUA": "I", "GUA": "V",
                     "UUG": "L",  "CUG": "L", "AUG": "M", "GUG": "V",
                     "UCU": "S",  "CCU": "P", "ACU": "T", "GCU": "A",
                     "UCC": "S",  "CCC": "P", "ACC": "T", "GCC": "A",
                     "UCA": "S",  "CCA": "P", "ACA": "T", "GCA": "A",
                     "UCG": "S",  "CCG": "P", "ACG": "T", "GCG": "A",
                     "UAU": "Y",  "CAU": "H", "AAU": "N", "GAU": "D",
                     "UAC": "Y",  "CAC": "H", "AAC": "N", "GAC": "D",
                     "UAA": "Stop", "CAA": "Q", "AAA": "K", "GAA": "E",
                     "UAG": "Stop", "CAG": "Q", "AAG": "K", "GAG": "E",
                     "UGU": "C",  "CGU": "R", "AGU": "S", "GGU": "G",
                     "UGC": "C",  "CGC": "R", "AGC": "S", "GGC": "G",
                     "UGA": "Stop", "CGA": "R", "AGA": "R", "GGA": "G",
                     "UGG": "W",  "CGG": "R", "AGG": "R", "GGG": "G"}

fasta_file = "13.fasta"

# PROGRAM
mRNA = intron_removal(fasta_file)
print(mRNA)
convert_mRNA_protein(mRNA, dico_genetic_code)
