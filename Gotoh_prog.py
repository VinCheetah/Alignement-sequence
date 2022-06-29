from Tipe import *



def mat_ali_gotoh (seqA, seqB, gap_start = 10, gap_extend = 0.5, sim_mat = sim_new, print_seq = False) :
    """
    Utilise l'algorithme de Gotoh pour déterminer la matrice des meilleurs alignements entre
    chaque position des deux séquences
    
    Complexité temporelle : O(n^2)
    Complexité spatiale : O(n^2)

    Parameters
    ----------
    seqA : Liste de caractères de la première séquence de la forme : ['A', 'C', 'G', 'T', ...]
    seqB : Liste de caractères de la première séquence de la forme : ['A', 'C', 'G', 'T', ...]
    gap_start : Valeur de la pénalité de la création d'un nouveau trou ('_')
                2 par défaut
    gap_extend : Valeur de la pénalité de l'agrandissement d'un trou ('_')
                 0.5 par défaut
    sim_mat : Matrice des valeurs des associations entre nucléotides
              Identité de taille 4 par défaut

    Returns
    -------
    mat : matrice avec m[i][j] le meilleur score pour l'alignement de seqA[:i] et seqB[:j]
    matA : matrice avec m[i][j] le meilleur score pour l'alignement de seqA[:i] et seqB[:j] dont l'alignement
           se termine sur l'association (a_i / '_')
    matB : matrice avec m[i][j] le meilleur score pour l'alignement de seqA[:i] et seqB[:j] dont l'alignement
           se termine sur l'association ('_' / b_j)

    """
    mat = [[0] + [- gap_start - (i - 1) * gap_extend for i in range(1,len(seqA) + 1)]]
    matA = [[]]
    matB = [[- math.inf] * (len(seqA) + 1)]
    for i in range (1,len(seqA) + 1):
        mat2 = [-gap_start - (i - 1) * gap_extend]
        mat2B = [None]
        mat2A = [- math.inf]
        for j in range (1,len(seqB) + 1):
            caseB = max(mat[i - 1][j] - gap_start,
                        matB[i - 1][j] - gap_extend)
            caseA = max(mat2[j - 1] - gap_start,
                        mat2A[j - 1] - gap_extend)
            case = max (mat[i - 1][j - 1] + sim_mat[dico(seqA[i - 1])][dico(seqB[j - 1])],                            
                        caseB,
                        caseA)
            mat2.append(case)
            mat2B.append(caseB)
            mat2A.append(caseA)
        mat.append(mat2)
        matB.append(mat2B)
        matA.append(mat2A)
    return mat, matA, matB


def ali_gotoh (seqA, seqB, gap_start = 10, gap_extend = 0.5, sim_mat = sim_new) :
    """
    Utilise l'algorithme de Gotoh pour déterminer le meilleur alignement global de deux séquences
    
    Complexité temporelle : O(n^2)
    Complexité spatiale : O(n^2)


    Parameters
    ----------
    seqA : Liste de caractères de la première séquence de la forme : ['A', 'C', 'G', 'T', ...]
    seqB : Liste de caractères de la première séquence de la forme : ['A', 'C', 'G', 'T', ...]
    gap_start : Valeur de la pénalité de la création d'un nouveau trou ('_')
                2 par défaut
    gap_extend : Valeur de la pénalité de l'agrandissement d'un trou ('_')
                 0.5 par défaut
    sim_mat : Matrice des valeurs des associations entre nucléotides
              Identité de taille 4 par défaut

    Returns
    -------
    aliA : Alignement optimal de la première chaine
    aliB : Alignement optimal de la seconde chaine
    score : Score maximal obtenu pour l'alignement global des chaines

    """
def ali_gotoh (seqA, seqB, gap_start = 10, gap_extend = 0.5, sim_mat = sim_new) :
    mat, matA, matB = mat_ali_gotoh(seqA, seqB, gap_start, gap_extend, sim_mat)
    aliA, aliB, i, j = "", "", len(seqA), len(seqB)
    last_mat = 'mat'
    while i > 0 and j > 0 :
        if last_mat == 'mat' :
            if mat[i][j] == matB[i][j] :
                last_mat = 'B'
            elif mat[i][j] == matA[i][j] :
                last_mat = 'A'
            elif mat[i][j] == mat[i - 1][j - 1] + sim_mat[dico (seqA[i - 1])][dico (seqB[j - 1])]:
                aliA, aliB = seqA[i - 1] + aliA, seqB[j - 1] + aliB
                i -= 1
                j -= 1
        elif last_mat == 'B' :
            aliA, aliB = seqA[i - 1] + aliA, "_" + aliB
            i -= 1
            if matB[i][j] == mat[i - 1][j] - gap_start :
                last_mat = 'mat'
        elif last_mat == 'A' :
            aliB, aliA = seqB[j - 1] + aliB, "_" + aliA     
            j -= 1
            if matA[i][j] == mat[i][j - 1] - gap_start :
                last_mat = 'mat'
                
    while i > 0 :
        aliA, aliB = seqA[i - 1] + aliA, "_" + aliB
        i -= 1
    while j > 0 :
        aliB, aliA = seqB[j - 1] + aliB, "_" + aliA     
        j -= 1
    return aliA, aliB, mat[len(seqA)][len(seqB)]


