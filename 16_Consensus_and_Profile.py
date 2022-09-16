# IMPORT
from Bio import SeqIO


# FUNCTION

def profile_ADN(input_file):

    fasta_sequences = list(SeqIO.parse(open(input_file),'fasta'))
    len_seq = len(fasta_sequences[0].seq)   # hyp. all seq have same len in the fasta file
    # print(f"len seq : {len_seq}")
    dict_profile = {"A": [0]*len_seq ,
                    "C": [0]*len_seq,
                    "G": [0]*len_seq,
                    "T": [0]*len_seq}
    # print(dict_profile)

    for fasta in fasta_sequences:
        sequence = list(fasta.seq)
        for index, nucleotide in enumerate(sequence):
            for key in dict_profile:
                dict_profile[key][index] += int(key == nucleotide)

    return dict_profile, len_seq


def consensus(dict_profile, len_seq):
    consensus_list = []
    list_keys = list(dict_profile.keys())
    for index in range(len_seq):
        max_value = 0
        for key in list_keys:
            str = key
            value = dict_profile[str][index]
            if value >= max_value:    # '=' not necessary, it's a choice
                str_max = key
                max_value = value

        consensus_list.append(str_max)

    print( ''.join(consensus_list))




# PARAMETERS
input_file = "16_equal_len.fasta"

# PROGRAM
dict_profile, len_seq = profile_ADN(input_file)

consensus(dict_profile, len_seq)
for key, value in dict_profile.items():
    print(f"{key}: ", end = "") 
    for num  in value:
        print(f"{num} ", end = "")
    print("")
    