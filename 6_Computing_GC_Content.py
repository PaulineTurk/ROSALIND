# IMPORT
from Bio import SeqIO

# FUNCTION
# "AGCTATAG" is 37.5%

def seq_GC(seq):
    list_seq = list(seq)
    len_seq = len(seq)
    counter_GC = 0
    for elem in list_seq:
        if elem in ["G" ,"C"]:
            counter_GC += 1
    return 100*counter_GC/len_seq


def seq_GC_max(input_file):
    list_name = []
    list_GC_percentage = []
    fasta_sequences = SeqIO.parse(open(input_file),'fasta')
    for fasta in fasta_sequences:
        name, sequence = fasta.id, str(fasta.seq)
        list_name.append(name)
        list_GC_percentage.append(seq_GC(sequence))
    GC_max = 0
    index_max = 0
    for index ,GC_percentage in enumerate(list_GC_percentage):
        if GC_percentage > GC_max:
            GC_max = GC_percentage
            index_max =index
    print(list_name[index_max])
    print(list_GC_percentage[index_max])




# PARAMETER
input_file = "6.fasta"

# PROGRAM
# seq_GC("AGCTATAG")
seq_GC_max(input_file)