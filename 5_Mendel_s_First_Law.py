# IMPORT

# FUNCTION
def dominant_phenotype(k: int, m:int, n:int, dict_dominance):
    
    total = k + m + n

    dict_init_number = {"dominant": k,
                      "heterozygote": m,
                      "recessif": n}

    dict_init_proba = {"dominant": k/total,
                      "heterozygote": m/total,
                      "recessif": n/total}

    dict_proba = {}
    for phenotype_1 in dict_init_proba:
        dict_proba[phenotype_1] = {}
        for phenotype_2 in dict_init_proba:
            if phenotype_1 == phenotype_2:
                dict_proba[phenotype_1][phenotype_2] = dict_init_proba[phenotype_1] * ((dict_init_number[phenotype_1]-1)/(total-1))
            else:
                dict_proba[phenotype_1][phenotype_2] = dict_init_proba[phenotype_1] * ((dict_init_number[phenotype_2])/(total-1))
    # print(dict_proba)

    proba_dominance = 0
    for phenotype_1 in dict_init_proba:
        for phenotype_2 in dict_init_proba:
            proba_dominance += dict_proba[phenotype_1][phenotype_2] * dict_dominance[(phenotype_1, phenotype_2)]
    print(proba_dominance)



# PARAMETER
k, m, n = 15, 23, 25

dict_dominance = {("dominant","dominant"):1,
                  ("dominant","heterozygote"):1,
                  ("dominant","recessif"):1,
                  ("heterozygote","dominant"):1,
                  ("heterozygote","heterozygote"):0.75,
                  ("heterozygote","recessif"):0.5,
                  ("recessif","dominant"):1,
                  ("recessif","heterozygote"):0.5,
                  ("recessif","recessif"):0}
                    

# PROGRAM
dominant_phenotype(k, m, n, dict_dominance)
