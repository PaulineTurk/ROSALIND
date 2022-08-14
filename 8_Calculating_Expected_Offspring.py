# IMPORT

# FUNCTION
def expectancy_pheno_dominant(dico_number,
                              dico_proba_pheno_dominant,
                              offspring_number_per_couple):
    expectancy = 0
    for key in dico_number:
        expectancy += offspring_number_per_couple*dico_number[key]*dico_proba_pheno_dominant[key]
    print(expectancy)
    


# PARAMETER
dico_number = {"AA-AA": 16510,
               "AA-Aa": 16486,
               "AA-aa": 19786,
               "Aa-Aa": 17322,
               "Aa-aa": 19858,
               "aa-aa": 16339}

dico_proba_pheno_dominant = {   "AA-AA": 1,
                                "AA-Aa": 1,
                                "AA-aa": 1,
                                "Aa-Aa": 0.75,
                                "Aa-aa": 0.5,
                                "aa-aa": 0}

offspring_number_per_couple = 2

# PROGRAM
expectancy_pheno_dominant(dico_number,
                              dico_proba_pheno_dominant,
                              offspring_number_per_couple)
                              