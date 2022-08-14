# IMPORT

# FUNCTION
def convert_mRNA_protein(mRNA, dico_genetic_code):
    mRNA = list(mRNA)
    print(mRNA)
    len_mRNA = len(mRNA)
    print(len_mRNA)
    protein = []
    num_codon = 0
    triplet = mRNA[num_codon*3: (num_codon+1)*3]
    triplet = "".join(triplet)
    print(triplet)
    print(dico_genetic_code[triplet])
    while dico_genetic_code[triplet] != "Stop": # and (num_codon+1)*3 <= len_mRNA:
        protein.append(dico_genetic_code[triplet])
        num_codon += 1
        print((num_codon+1)*3)
        if (num_codon+1)*3 <= len_mRNA:
            triplet = mRNA[num_codon*3: (num_codon+1)*3]
            triplet = "".join(triplet)
            
    print("".join(protein))




# PARAMETER
mRNA = "AUGCUUCUUAUAGGGGGCAUAGUCUGCGGAUCAGGACAAAAUAGAGCGAGAUCGUUGGAGCCCAGCGAGGGACGCUCAGCUUUAUCUAAAUAUUCGUCCAAGUGUUUUGAUCAGCGGAAAGCAAACCGAGCACACGCUGUUGUGCUCCGACUGACGAAUCAAGGCUAUCACACUGUAGCAUCGCGGGAGCACAGAUACAGUAACGAGGAUACCCAACUGCUCGGCUCGGACUGCGGCAUACGGGUAGAUUUCGGUUUAAAUCCAACUUUCCCAGGCAUCCGCAGAGGGAGUAUAUUUUGUAGCGGUAUUCAGCUAGUUCUACCCCUUAGGCUUAAGAGUCCCAGGACUCAGGUAUUUGAUGAGGAUGAUCUUUUCUAUGAACAAUGGCGGGGCCUCGAGGCUAAACAUUUCACAAUGAACAAGGCGGCAAUCGUGUUGUUAUGGACUUUACUCCAGCGGAAGAAACGUCCCACCCAGUAUCCUAGUUUGCACGCCGAUGUGGCCGCAAUAGUCCUUCAGAGGCGUCCUACUCGCCCGAAAAAACCUCAUUGGCCCGGGGGUACAGACAUUUGUCGCGAGGUUAGGUGUUUGGUUGCCUUCGACCUGACUCAUACCAUAGAGCGGAUCACAUCGAGCCGAGUGUGUGCAAUCUUCCUGCGUGCUGGCUUCUGUUCGCCAGGGGCGCCAUUCAUCUCGUUCACCAGGAGAUGCUCCCCAGCGGUUCCGCCGUCUCGAAUACUCCUUACGACACAUGUAGCAAUAUACACACCUUGCAAGUUCAUGGCCCCGUCCUCCUUGGAAUGGCCCGGCGCAACUUGUUCUGCAACGCAAGUCUUUAGGUUUCAUGGAAGAUUGUCCAAACACUCGAGGGCCAUUUCUGCGGCUUCCAAUGUUAGAUACAGCCGCAGCACUUAUCGUGACGAACUGGCCAUGUCCUACGCAGGUGCCGCCGCUCGGGGGCUGGCGACUGGUACCUUCAAUUGGUUGGGAAUGGGCCCCAAUGCGAAACGGGUGUACGGUUGUGUCAUUAACCGUGGCGCACGCUUAGGUAGACCAAGAAUACCGCGCAGAACCAGUUUACCGUGUAAUCCAGGCGUACUCGUCUUCGUUCAUAUGAAUCAGGACGAACAGUCUUCAUUGUGGUAUAGAGUGGCGGUUAAGUUUCAGGUAAAUCGAUUCAUCCCACACCGGCACUGGUACGUAUGCUUCCUGCCUCGCACGUGGAUACGUGGACGGCUGCCUGACAAGGUAAGCUCCGAGACAAUGCUAACCCGUUCAAAGCGCACUCGUCACGUCCGCCGCAGAUCACCAAAGCUGGGGAGUCUACCCCAGAAAACUCCCCCUCACCGUGGUGGUAGGCCCACUCUCCUAUGGAGAGAAUACGCCUCCAAUGACGGCUGCUCCUGUGCUGAAAAAGCUCUUCAUAUUCCGCCCUUUGCUACACCGGCGGGAGGUCUUCACGCGUCAUCCGAGCUCAGCGCCGUACAAGGAGUCUCAGGUGUUCCAGUGCACUAUGCACCGUUAGUGUGUAGCCAUCGUAUUUGUCUCCAGUGCACAGAGAAAAAUGGAACAGUCCAGUCUAAUCAGGCAGAGAUGCGACGCGCCGAGAGAAGGGCAGUACUCCCGUUCAUGACUACUACUUCUGGAGAUAGCUGUGGACUGCUUCUAUACAAUGCGAGACGACUCCAUAAUACGCAUGCCUAUGUACCGAUUCCAAUCAAGGAUUGUGAGAGACCAUAUCCCUACGCACCAUUCCUGCCAGGGAGACGAUGCUCGGCAAACACACACCGGCAGAGCCUGCACAGUACCAUCCUGCCUGAGCCCGUAUCUACGACUGAUCCAAUACUAGCACUAGGAAAGUCUAAUCUCCAAAGGCUCUUGACUCAAGCCGAGUUCAACGAAUAUGAGUUUUCUCUAUGUGUGGUAUCACCGCCUGAAUCGUGCUCAGAGAAAUGGGUCACUGGCUAUGACCACAGACGCCGGAUAGUUGUGCACGAAUAUGCUCAAAAGCUCCAUGGGUGUCAAGUUGUCAUAACAGCGUUAGAGGCAAAUUGCAUGUACAGGUCCUAUAAUGCUAUUGAGCGCGGCAUCACCGUGCGUUAUACUCGAAGCCCCCAAAUUAGACUGUCUAGGACUAUUUCUGAAACGUGGUCAAAGUAUACCGCCGACUAUACUGGUGAGAAAGGUUUCGGACUUUACCUGUUUGACUGUUUUGCCAAAGUAGUGGGCUCCCGAAUCAAUCCCUGUAGGACAAAAAAGCGUCGUCAAUGUGGACCGAGCAGGGCUCAGACAAUCUGUACUUCAUUACAGAAUUGUGUACUAUUAUCUGGCUACCGAUGCAUAUCCCUAUUAUCACAUUUUAGGCCAUUACUAGGGCAUUGCUUAGGGUUCUCCGAGAUUUCUCGUGUGGGUGGUACAUUUCAGCUACUAGGAUAUACGCUCAGGAGACGCCGCCCAUGCGGAACUCGUAAAGUUCGGGCCACCCAAAGAGCCAUGUUAUUGCUAUGUGCACACGAUACACCAUUUCGCUCGAUGGAGUCGUCGGCGCAACUUGUCCGGGUCCACGGUAGAAGUAAUACUAGUUACGGACCUCUCGUACAUGAUAAGCACACGAAUGGAUGCGAUGAUCACGUGUCUAUCACUAACGUUUCUGGCCAUGUCAUUGAGACAUGCAGAGAGACGACCUAUAAGAAUAUGACUACGGGUAGCCAUUACGUUAGGGUCGACUCCGGGCUUGGGGCUACUAGCGGGGACAGCACACUCCUCAGCAACGCCACCGCCCGUGAGCUGCAGGAGACUUUUCCUCUUACGCGGUUAACGAGUUAUCUCCACAGUGCUUGGCGCCUCGGGCUACUAAGUUCCCUAUCUAAUUUGCGGCCCAGCUCAUGGAUGAGAGGACCAAUUGGGAUUAACGAUUAUGUCUUUGGCUCAGCCUUCCCCGUACCAGGGGACUACAUUAGUCCCACCUCACACACCCCAACGGCAUUACACCAUCGACGCGAGUACAUGUCUUAUUACCGAAAAAGCGCCCAAAAAUGUAUCAUAACCUAUAGGCACGUUCUGACACUGAUGCGGGCUGGUGCCAGUUCGUUUCUCACGCUUGGCGUAGGAGCUCUGAGCUUUAGCGGUGCUUCGCGAUGUAAUCUCCCCAAGAUAAGUCUUUGCCCUACGGAUCGCAACGCGGCUCAGGCUGUCGUGUCCCUCGAGGCACAGGCCCACAACAGUGAUGACCUCAAUUCGUGUACUGGUGCCUAUACUCGAACUGUAUGUUAUUUGGUGGAGCCUAUUAGGUUUGUAAACUCGAUCUCGCGCCAAACUAUGAAACACGUGUCUCAGGCUAGCGUUGGUCCCGCGUUGGUUCUUCCCGCUUCAACAAUAAGAACUCACCACGGGGGAUUUUGUGAUCCAGGAUCCAACGAGCCUCCUAUGCUAGGCUGGGAACACACGCCUAGAUCACGAGAUGGUUCCGUUCUGCGUUUAAUUUGCCAUAGAUCAUUUCCGUAUUUGGGACGCGGUCACGCCUCGUCACACACGUCUAGAUCGUGCUCUGAUUUUUACAUCACAGGAGUAGUUUUGCGCUGUCCCUUCUCACGAAACGACCCUAAUCAUACCAGCAAGUACUCGUCCAUUUGCCAAAGCUUGCAUAGUGCGGGCCCUUCUUUCCCGGCUUAUUCUUGCGUUGGACAUUAUCGCCGGAGAAGUUUUGCCACCGGAUUCACGUAUCCAAACCAUUCUGAGUCAUGCAAGGUGGUUAGAAAGGACCCCCGGAGGACACUCUCGAUGGUUGAUGUUUCCAACUCACAGUACAGUUACCCUCACCUCAAGAAGAUGGUUAGGCGCGGUUAUCCGGCGGGCCAGUGGCGGAUUCAUCACUUUAUCUUGAAGAAUUAUAGGGUGUCCGGUUGUUCCCAUCAUCCAACUUGCACCAUAUGUCAGAUUUCUCACGUGAGUUGCAGCCGUAUCAUCCGGGGGCUGGACAUGUGGUGCGCACUGAAAACCUUGAGAAAGCUUCUCCCCGUUCGUAGCGCCUAUAUUGCAUCACCCGCAGUCCAAGUGCCUUUAGAUUGGAAGCCACUAAUAGCAUCCCAGUGCACACCGGCAAAUUACGUGCGGGCGAGUAACAGGGUAACAGGCCCAACCGCUUCAGUAGCGUGCAACACGAUCCACUUUUAUAAUAACCGCCAAGUGCCUUUGCCAUGCGAUCGGAGGAGGGGUUUUGUACGAUCACUUGAAGGCGCAGCCCACCCAUUUAUGUCCUUAGUAGUAGACUCAGAAUUUUUUUUGAAAUGCCUACCCUGGAGUAUUUACGUCUGGUUAUUAUGGACCGUGCUGGAUCGCAAGGGUCCGCUAGCAACAGCUCCUCAGCUUCGGCAGGAACUACCCAAGAUUAAUUGUUUGGCAAUGCGCCUCCGCCUCGCGGUUUACGUGGAUCUGCUCGAAGAAAGGACAUUCCGCUCAGAUCGCACUAGUAACGCGAAGACAAAACCGGAGGUAGACCUUGUCUGGUGCUCAUGGAGUGCGACUCUUGUCUCCAGGGCGAAUUCAACCUAUCUUGGGGCAGCUGCGGCUGCAAGGAAGGAGUGGUUCAUCGAAAAUAGGAGAACCCGAUCUGGUCCAGACUUUGGGCCCAGGCCACACUCAUAUGGCCUUUCAGCUCGCAGUACGCGAAUUGGAUUGACGGGACACUGGCAACUUAACGACGCCACAUUCUUCCUCUUCUUCUUGAGUUCCAAUACGAGACGUUGCUGUCCAGCGCAGCUCCGGCUCUUGCGAGUUAGACGCCACUUCCAUGCGAAGGCGUGUCUCUUUCCGCACCAGUUUCUGGCUCCGACCUAUAGGGGUAAAAAGCUUUCGUCAUUUUGUAGAGCGAGCGACGCCUCGGUCCGGGACUCCGAUCCUCAGUGUUUCCUGCGUCCUAAUCUCCCAUCAAAGCUGAAUAUUAACCGUGGUGGAAAAGGAAUAAGAGGGAAGUAUGAGGUAAAUGGCAGAUCACAUUCAGGUACGGCGAGAAUCGGUCAGUAUCGAGUGCGCAAACCUUAUUUUUAUAACGAAGAACGAGUAAGCUGUUUCGCCUGUGAUCCAAACCAGAUUCACCAACUGCUAAAGUGUGAUGAAGAACUACCAAGCUCUCAAUGUGACAGCAACCGGGCCCGCUCCGUCGGACGAAUGUCAACCGUGUCCGUUGAGGAUUACGGCUCAUCGAAUGUCUACACAACUCUCCGUGAAAGUCUAGCUUGCUCCAUUUUGACAGGCCGUUCGACGGGAUCAAGUCAAAAAAGUGGCUCCGUGUAUUUGGAAUCUUCCGCGGGACAACAGAAGUCACUGGUGCCAAACCCAGAGGGCAGGUCUGUUCAGGAAGGGUCGGGCACUAGGCCAGCCGAAGGAUUGCCCAACAUUUAUCAGAGUCGCACUUAUGACGUGUUCUCUCAUCGCGAUACGCGACAUAAAAAGGUGCUGGGUCUAAAGCAAGUUUCCACCAGACUAGGGUAUAGUGUCAGUUUUGUGCGUGUUAUCAAGACAAAUGGCAGUGAUAAACUCGGCAUGUCUUACAGUCAGAGGCAAAGAGAUUUCAGACACCCUCCGUACGCCGUGCAGUGCCCGGUGGACCUAGGAAAGGAGAGAGAUGUGAGUAUUCGUUACACUCGCCUCCCAUUAUCAUCCAGACAACCUGCCGAAGCAAUACAGAGACCGGUAGUGAAGAGACAGGCAUAUGAUCUUCACUUGGAGGCCCGGUCUCGUCCCAGCCGUCGGUCAACAUUACCACUUAGUAAAGCGUUCUCCCUUGGCUCGACACUUGGAGGCCAGCUGGGGCCUCGAAUUCGUACGGAACGUGGGACGCCUGGCCUUCAGGGUCAAACUGAUAUCACUGGUAUAAGACCGCCCAGCUGCCUUAUAAGGUGUCACGCGGUAAGACUAUCACUCAUUUCGACGUCCUUGAGGAGGCCACAAAGGCGAAAAUUGUGCUAUCAGCUCGCUAUCGAGCGAGGGGUUUGCCCCCUUAAGAGACGCGCUAAGGUGGUAAAGGAGGGGGCUGCGCUGAAGGAAUAUGUCCAGGGGAAAAACUUAGAAAUAAAUUUCCAUCAUUGGGCCAUCGUCGGGGUUAUACCGCCCGGGUCUUGCCCUUUUAACAUUACUAGGCCUUCUAAAUUCUCUGAGCAGAUCGGUUUGGUCCUACCCCUCGUUCUCUGCAUACGCAGAGCGUGCGUGUGCAGCACAAUUGUACUUCGCGCCGGUCCUGGUAAAGACCGGGCUAUUGUUUGGCCUACGAAAGACACGAGCAGUGUUGCUCAGAUAGCGAGCUACCUUUCUAUGACUUCCGACAGAUCGUCACAGGUAGCGAUAAUGUGUCGGUCGACGUCGAUUAUCCGCUUGGCGGUAAUCGCGGCACGUUUCCAAACAACAGAAAUGGUCCGAGCCCAUAGCUCACUGAUCCUCUUUCUUAGGGGUACGAGGGUCUUGGGCCUUGCAGAGCCACCGGUGAGUCCUACUAGAAGAGAUAAGUGGAAGGGAUUUGCGAGUACGUCCAAGGUAUCUUGUCGCCCAAUAAAACCAUCUGCAUGGGCGACACAAAAUCUACAUACCUCUAGUGGGCCAGGCAAAUCAGUUCGCCAAGAUCGCCGUGAUUUCGCUACUGGCUUCCCGUACAUAAUGCUCGGUGUAACAAAACUCUUGCUCAUAAGGAUUCCCCCAUCAUCCAUCAAUUUUACUCGGUUUUCCGACGGAACCUCUGUCACCGUUCCGGCUACUGCGAUUAAAGUCCCUUUUUGGCGUCUCGACAGAGACUGCCGUCUCGGCUGGAGCAGACGAAUGAUACGUAGGCCGGUCGUACCUAUCGUAGCCGCCCAAACUGAAGUGACCUUACAUCAGCCGAAUGCAGCGUCUAGAGGGCACUCCCGAUUUGAUGGGUGUGGAAACCACCAUCUGAUUUUGGACGCCGUACACACGAGGCCUUUGGGUAGCCUUCGCAGCAGCGACGGUGAGAACAGUUACUACGCGGUCGUGCUUCAGGGUCGCUCUGGCAGUGUCUUAGAGGGCUUACACGUAGGAACCGACAUUCCGUAUGAUCAAUUCCCGCUUGUCUCCCAUUUUGUCAAGAGGUCCUCGUCCUGGUAUCCAGUUAAUGGCCGCACGCAUUUACCGGACUUCAGUCUCAUAAUGCAGCACCGCUCGACAUUUAUCCAAUCCAGACGAGAGCUAACUUGUUUUGACAUGGCAGCCACGAGAUUGGCGGUAAAGCGUUUGCUCCUUGAAUCCCCGCGCGAUCUUUACAAGGAGGAUGGGUUUUUUAAUCUAUCUAGUAUUGUAUUAUACCAGCCUGCUAGGAUUUUUGUGAAAUAUGACAACUACUGUUUUCAUAAUACACCUGCGUUUCUAGGCAGAUCUGCCAAUAACUUGGUCAAGUCCAUACCGCGUGGAAAAACGUUACAGCAGCUAGACGGCGUUAGACUUCACUCGAACCUUACGAUUUCCCCAACAGCUGCUCACCGGGGGAUUAAAUGCUACCGUUCGGUUCAGUUGUUUCUGAGAAAAGGCUGGGGGUGCACCAAGCGGUGCUUGUAUUCUAGAACGAACGAACCCCAGAGCCUCCUCUAUCUACUCUGCCUUAGCUCGGUGCGCGCCGUUUUGGAGGGAUCCUUCGCCCUCCCCACGUCAGUGUUAGGACAUACUUUCCAGAGUGCCACUCGCAGACCUAACUCGGUAACCAAGUGGGACGAUAUGCUCUCGGAAUAUGGGGAGGAGCCCGUCCAAAUACGAACUACCAUGCUGCCGUCGGUCUACACGAUGGGUGACCGCAGAAACCCCGUUACGCAGACUGUUCGCGCCAUUCGUAUUUACAAUGCACUUAACCAGCUCCCUCGAACGCGCGAAUACCAAGCUAUGUCCUCCAAGUUCGCUAUGUUCAGCCAGAUCAAACCAAGAUGUUUCGGAUCCCGCAUGGAUAUAGUUCGGUUAUUAAAGGCAUGCCCCACAGAACACGUAGUUAUAGGUGGAGUAAUUGCGGUUGCUGGGCUGAUGUCGAGGGACUUUCGUAAAAGUUGUGCUGCGAAAUCGCCAACAAUCCAACUUCGCCAGGACAAGGUCGGCGAUCGGGGAAAGUCCGCCUCUCUACGCUCCCAUUUGAGUAGGGGUCCAGCAACCCGGGACCGGCCAGCACCAUAUCUUGCGCUAGCGAGGGGCAUCAACAUCACUCAACUGAGCCAUCCACACGAAACAGAGGGACCGGAUAGGCCCGGUUGCCUUCAGUUAAAGGUUCAUGGUCAUUCGGGAUUCAUGGUGGCGGUCUCGGGGUCCUAUAAAGUUAGUGGCUGGCUUGAGAAGAAUGCAGUCAAACUUAUUGGCCAAGGGUUAUUUACGACCCGAGGAGAGUAUGAGAGUCGGUUCUGGUUCACUCACGGUACCGUGUUAAGAACUAAAUCGCGCGAGAGGUAUGACCGGCAAGUCGGCAAUACCCGAUCGCCUGCGGCCCUCCGGAGCUCCGCUGGCGGUCCGAAUCUGCUAUACUUAGAGGUUGAUAGGUCUUACGCCCGUUCAUUUCGGAGCUUUCACACCCCGUUUGCAGGUCGGAAGGGGCAGGACUUCCGGUGGAUCAAUGAAGUGACUAUUACGAUGGACUUAGUGCGCGCAUCCGUUGGCUGGGAACCUUCGCUCUCGGUGUGUGGUAUACCAAUACUGGCUAUCCGUUAG"

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
# PROGRAM
convert_mRNA_protein(mRNA, dico_genetic_code)