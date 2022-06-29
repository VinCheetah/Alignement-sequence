from Tipe import *
import time



def max_mat (matrice) :
    m, pos = matrice[0][0], [(0,0)]
    for i in range(len(matrice)) :
        for j in range(len(matrice[i])) :
            if m == matrice[i][j] :
                pos.append((i,j))
            elif m < matrice[i][j] :
                m, pos = matrice[i][j], [(i, j)]
    return m, pos

def mat_ali_SW (seqA, seqB, gap = 0, sim_mat = sim_mat_bas) :
    mat = []
    for i in range (len(seqA) + 1):
        mat2 = []
        for j in range (len(seqB) + 1):
            if i == 0 or j == 0 :
                case = 0
            else :
                case = max (mat[- 1][j - 1] + sim_mat[dico (seqA[i - 1])][dico (seqB[j - 1])],
                            max (mat[- 1][j], mat2[-1]) - gap,
                            0)
            mat2.append(case)
        mat.append(mat2)
    return mat

def alignement_SW (seqA, seqB, gap = 0, sim_mat = sim_mat_bas, fichier = None) :
    mat = mat_ali_SW (seqA, seqB,gap,sim_mat)
    tab_ali, (maxi, tab) = [], max_mat (mat)
    for (i,j) in tab :
        aliA, aliB = "", ""
        while i > 0 and j > 0 and mat[i][j] > 0 :
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
        tab_ali.append((aliA,aliB))
    if fichier == None :
        fichier = open("Alignement",'a')
    fichier.write("\n\n" + time.asctime() + "\n" + "".join(seqA) + "\n" + "".join(seqB) + "\n \n")
    for ali1,ali2 in tab_ali :
        fichier.write(ali1 + "\n" + ali2 + "\n\n")        
    return tab_ali





