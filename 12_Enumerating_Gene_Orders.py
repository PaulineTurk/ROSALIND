# IMPORT
from itertools import permutations
# FUNCTION
def rearrangements(integer):
    list_int = [str(i) for i in range(1, integer+1)]
    list_int = "".join(list_int)
    # print(list_int)
    list_permutation = list(permutations(list_int))
    # print(list_permutation)
    n_permutation = len(list_permutation)
    print(n_permutation)
    for elem in list_permutation:
        for char in elem:
            print( int(char),end=' ')
        print("")

# PARAMETER
integer = 6

# PROGRAM
rearrangements(integer)