#Exercice 1
import numpy as np

A = np.array([ [3,1,3], [4,3,-1], [2,1,2] ])
B = np.array([ [1,-1,3], [2,1,3], [1,2,3] ])

C = A+B 
print("A : ", A)
print("A : ", B)
print("A + B : ", C)

#Exercice 2
import numpy as np
 
A = np.array([ [3, 1, 4], [2, 2, -1], [1, 2, 2] ])
B = np.array([ [2, -1, 3], [2, 1, 3], [1, 2, 3] ])
 
C = A.dot(B)
 
print("A : ", A)
print("B : ", B)
print("A * B : ", C)

#Exercice 3
def eststochastique(P):
    nl = len(P)  # nombre de lignes
    nc = len(P[0])  # nombre de colonnes
 
    etat = True  # on suppose que la matrice est stochastique
    for i in range(nl):
        s = 0
        for j in range(nc):
            s += P[i][j]
        if s > 1:
            etat = False
            break
    return etat
 
 
def estbistochastique(P):
    nl = len(P)  # nombre de lignes
    nc = len(P[0])  # nombre de colonnes
 
    etat = True  # on suppose que la matrice est bistochastique
    if(eststochastique(P)):
        for j in range(nc):
            s = 0
            for i in range(nl):
                s += P[i][j]
            if s > 1:
                etat = False
                break
    return etat
 
 
def vecteurstable(G, h):
    nl = len(G)  # nombre de lignes
    nc = len(G[0])  # nombre de colonnes
    etat = True
    if(eststochastique(G)):
        for j in range(nc):
            s = 0
            for i in range(nl):
                s += h[i]*G[i][j]
            if s != h[j]:
                etat = False
                break
    else:
        etat = False
    return etat
	
#Exercice 4
import numpy as np
 
A = np.array([ [3, 1, 5], [9, 8, -1], [18, 12, 2] ])
 
C = A.transpose()
 
print("A : ", A)
print("Transposée de A : ", C)

#Exercice 5
def apply_permutation(A,perm,N):
    B=np.empty_like(A) # A est une matrice NxN d'entiers dans range(N)
    for i in range(N):
            B[A[:]==i]=perm[i] # perm est une permutation de range(N)
    return B