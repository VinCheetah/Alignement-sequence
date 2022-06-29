from Tipe import *
from math import log

sim_mat_bas = [[{True:1, False:0}.get(i == j) for j in range (4)] for i in range (4)]

def identity (k) :
    return int(k)

def affine (coef_dir,abs_ori) :
    def F (x) :
        return coef_dir * x + abs_ori
    return F

def log_fun (coef, const, base_log) :
    def F (x) :
        return coef * log(k,base) + const

def mat_ali_SWB (seqA, seqB, gap_fun = identity, sim_mat = sim_mat_bas) :
    """
    Utilise l'algorithme de Smith-Waterman-Beyer pour déterminer le meilleur alignement global de deux séquences
    
    Complexité temporelle : O(n^3)
    Complexité spatiale : O(n^2)

    Parameters
    ----------
    seqA : Tableau de string d'une nucléotide
        
    seqB : Tableau de string d'une nucléotide
    
    gap_fun : Fonction qui prend un entier en argument
    
    sim_mat : TYPE, optional
        DESCRIPTION. The default is sim_mat_bas.

    Returns
    -------
    mat : matrice avec m[i][j] le meilleur score pour l'alignement de seqA[:i] et seqB[:j]

    """
    mat = []
    for i in range (len(seqA) + 1) :
        mat2 = []
        for j in range (len(seqB) + 1):
            if i == 0 :
                case = - gap_fun (j)
            elif j == 0 :
                case = - gap_fun (i)
            else :
                case = mat[- 1][j - 1] + sim_mat[dico (seqA[i - 1])][dico (seqB[j - 1])]
                for k in range (1, i + 1) :
                    case = max (case, mat[i - k][j] - gap_fun (k))
                for k in range (1, j + 1) :
                    case = max (case, mat2[j - k] - gap_fun (k))
            mat2.append(case)
        mat.append(mat2)
    return mat



                    
                