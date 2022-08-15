# IMPORT

# FUNCTION
def redundancy_genetic_code(dico_genetic_code):
    dico_redundancy_genetic_code = {}

    for _, value in dico_genetic_code.items():
        if value in dico_redundancy_genetic_code:
            dico_redundancy_genetic_code[value] += 1
        else:
            dico_redundancy_genetic_code[value] = 1
    return dico_redundancy_genetic_code


def get_Alphabet(dico_genetic_code):
    Alphabet = []
    for _, value in dico_genetic_code.items():
        if value != "Stop" and value not in Alphabet:
            Alphabet.append(value)
    return Alphabet


def elem_counter(sequence: str, Alphabet):
    sequence = list(sequence)
    dict_count = {}
    for char in Alphabet:
        dict_count[char] = 0
    for elem in sequence:
        dict_count[elem] += 1
    return dict_count

def number_mRNA_from_Protein(dict_count, dico_redundancy_genetic_code, modulo_number):
    n_mRNA = 1
    for elem, value in dict_count.items():
        if value != 0:
            n_mRNA *= dico_redundancy_genetic_code[elem]**value
    print(f" number of m_RNA [1M]: {n_mRNA*3 % modulo_number}")   #*3 for the last stop triplet available in 3 options


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

seq_protein = "MIRHDQYFHVNLTSHSSIFDTDVTFNTHWGIKCTHPILWDITYCVMPMISTTMHDFCLNMAMVWIPIDGRIENVECYKKWDMIDHCSYCTCVMDNNFFYYCTIYGLESLVLKAIRVDAPSTYIRVFLYQCESRWCMLFIINTTRIEMIKARWWPNHANLSQLVWHPFTDRKIPPTKRWQNWQNPEECHEMYALPISEQVEWEWVWMMCLTMDFCREQHFGERFHGPAYMDVFNLDRSQCEQDMKNLPLTCEIKWLYQQKHMFIYCWCRYWYEVVKHGMFQGWVYFEYEVFMNISMKYGVTRPTFGVANCMSQGHRKALIMQDRKHSDLYCTWENEMHWILIMHRFDSKGSWMLLLEPTEFWKAPHQRYTIWMFHTPHKGHVCTLCWSREIEQDLEAHQCVFVCMYDFIQHYPVMLKEIMWYETMGFVHQLFRQCQVDRTDDICSSQAPKEIWPQKQLWCTGSIKIEGHKGFTDWPPDNSPVIAWYIPQPDPICWGWSIDWVFKESRAHTMKDPFIDISSIHLLFNKGIWYEGAKHYHTFYYHYMMSFCIWQQYPFWCEFYIHSPTHVPESYIRDNSKDARQAVCSVSHMCYGMPAYGQFLDDTWCCPIHIPCQSVHMYSFAAKPVEFMAVGQKLIKLFACAYHDCYLWYEKICVVLQDRAVVEWHLHYQYCLRLLKCYHSIKAVISNSGQKCQRSYDNLYSWESIKCEYGVTHQSWCKKLGEPMTFAMHIVLFWENWQDTHIMLILWGMWGKEAYTKLRHNKLNDWENSQTKRNYTAIKWHWYLDFCHNPGELNNRRVRPNYQKSYHWVDHVCNQLACKSIKNVDRGKWHQGCYCCYAVDQFCLMILQLMSYNNWEEWETDYCRKKVGNVIHMYSPNYFIHMKPCKTTDPGIQGIVTDDTFLMLCTTERCGDLRDMPPYFSAWLPPMLQTINAWTCINSDMRAIYPVLDRSQSCHQKKGTHDMGPHYCDFECQWKSGFPYENSGSANNEFMWQASDDGA"
modulo_number = 1_000_000

# PROGRAM
dico_redundancy_genetic_code = redundancy_genetic_code(dico_genetic_code)
# print(dico_redundancy_genetic_code)
Alphabet = get_Alphabet(dico_genetic_code)
# print(Alphabet)
dict_count = elem_counter(seq_protein, Alphabet)
# print(dict_count)
number_mRNA_from_Protein(dict_count, dico_redundancy_genetic_code, modulo_number)