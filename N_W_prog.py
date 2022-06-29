from Tipe import *



def mat_ali_NW (seqA, seqB, gap = 2, sim_mat = sim_mat_2) :
    """
    Utilise l'algorithme de Needleman-Wunsch pour déterminer la matrice des meilleurs alignements entre
    chaque position des deux séquences
    
    Complexité temporelle : O(n^2)
    Complexité spatiale : O(n^2)
    
    Parameters
    ----------
    seqA : Liste de caractères de la première séquence de la forme : ['A', 'C', 'G', 'T', ...]
    seqB : Liste de caractères de la première séquence de la forme : ['A', 'C', 'G', 'T', ...]
    gap : Valeur de la pénalité d'une association d'une nucléotide avec un trou ('_')
          0 par défaut
    sim_mat : Matrice des valeurs des associations entre nucléotides
              Identité de taille 4 par défaut

    Returns
    -------
    mat : matrice avec m[i][j] le meilleur score pour l'alignement de seqA[:i] et seqB[:j]

    """
    mat = [[- i * gap for i in range(len(seqA) + 1)]]
    for i in range (1,len(seqA) + 1):
        mat2 = [- i * gap]
        for j in range (1,len(seqB) + 1):
            mat2.append(max (mat[- 1][j - 1] + sim_mat[dico (seqA[i - 1])][dico (seqB[j - 1])],
                        max (mat[- 1][j], mat2[-1]) - gap))
        mat.append(mat2)
    return mat
  

def ali_NW (seqA, seqB, gap = 2, sim_mat = sim_mat_2) :
    """
    Utilise l'algorithme de Needleman-Wunsch pour déterminer le meilleur alignement global 
    de deux séquences
    
    Complexité temporelle : O(n^2)
    Complexité spatiale : O(n^2)

    Parameters
    ----------
    seqA : Liste de caractères de la première séquence de la forme : ['A', 'C', 'G', 'T', ...]
    seqB : Liste de caractères de la première séquence de la forme : ['A', 'C', 'G', 'T', ...]
    gap : Valeur de la pénalité d'une association d'une nucléotide avec un trou ('_')
          2 par défaut
    sim_mat : Matrice des valeurs des associations entre nucléotides
              1 si match -1 sinon de taille 4 par défaut

    Returns
    -------
    aliA : Alignement optimal de la première chaine
    aliB : Alignement optimal de la seconde chaine
    score : Score maximal obtenu pour l'alignement global des chaines
    """
    mat = mat_ali_NW(seqA, seqB,gap,sim_mat)
    aliA, aliB, i, j = "", "", len(seqA), len(seqB)
    while i > 0 and j > 0 :
        if mat[i][j] == mat[i - 1][j] - gap :
            aliA, aliB = seqA[i - 1] + aliA, "_" + aliB
            i -= 1
        elif mat[i][j] == mat[i][j - 1] - gap :
            aliB, aliA = seqB[j - 1] + aliB, "_" + aliA     
            j -= 1
        elif mat[i][j] == mat[i - 1][j - 1] + sim_mat[dico (seqA[i - 1])][dico (seqB[j - 1])]:
            aliA, aliB = seqA[i - 1] + aliA, seqB[j - 1] + aliB
            i -= 1
            j -= 1
    while i > 0 :
        aliA, aliB = seqA[i - 1] + aliA, "_" + aliB
        i -= 1
    while j > 0 : 
        aliB, aliA = seqB[j - 1] + aliB, "_" + aliA     
        j -= 1
    return aliA, aliB, mat[len(seqA)][len(seqB)]

