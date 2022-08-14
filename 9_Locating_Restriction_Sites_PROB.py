# IMPORT
from Bio import SeqIO

# FUNCTION
def reverse_complementary(dna_string, dict_complementary):
    dna_list = list(dna_string)
    dna_list.reverse()
    dna_list_reverse = dna_list
    dna_list_reverse_complementary = []
    for elem in dna_list_reverse:
        dna_list_reverse_complementary.append(dict_complementary[elem])
    "".join(dna_list_reverse_complementary)
    return dna_list_reverse_complementary

def restriction_site_location(fasta_file, min_len, max_len, dict_complementary):
    dico_restriction_site = {}
    fasta_sequences = SeqIO.parse(open(fasta_file),'fasta')

    for fasta in fasta_sequences:
        _, sequence = fasta.id, str(fasta.seq)
        len_seq = len(sequence)
        # print(f"len seq: {len_seq}")
        if len_seq >= min_len:
            sequence_reverse_complementary = reverse_complementary(sequence, dict_complementary)
            sequence_reverse_complementary = list(sequence_reverse_complementary)
            sequence = list(sequence)

            for position in range(len_seq - min_len +1): # WARNING: position in output starts from 1

                len_restriction = min_len
                # print(position+1)
                while position+len_restriction -1 <=len_seq and  len_restriction <= max_len:
                    sequence_reverse_complementary_segment = reverse_complementary(sequence[position:position+len_restriction], dict_complementary)
                    # print(sequence[position:position+len_restriction])
                    # print(sequence_reverse_complementary_segment)
                    if sequence[position:position+len_restriction] == sequence_reverse_complementary_segment:
                        dico_restriction_site[position+1] = len_restriction
                    len_restriction += 1
    return dico_restriction_site

            

# PARAMETER
dict_complementary = {"A": "T",
                      "T": "A",
                      "C": "G",
                      "G": "C"}
fasta_file = "9_restriction_site.fasta"
min_len = 4
max_len = 12

# PROGRAM
dico = restriction_site_location(fasta_file, min_len, max_len, dict_complementary)
for key in dico:
    print(f"{key} {dico[key]}")
