# IMPORTS



# FUNCTIONS
def fibo_k(n,k):
    if n <= 2:
        fibo = 1
    else:
        fibo = k*fibo_k(n-2,k) + fibo_k(n-1,k) 
    return fibo


# PROGRAM
n,k = 34, 5
nbre_rabbits = fibo_k(n,k)
print(nbre_rabbits) 