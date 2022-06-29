from Tipe import *
import pylab as plt
from matplotlib.collections import LineCollection
from N_W_prog import *
from Gotoh_prog import *



def pltGraph_NW_LC (seqA, seqB, gap = 2, sim_mat = sim_mat_2,nameA = "Sequence 1",nameB = "Séquence 2",
                    deb_seqA = 0, deb_seqB = 0, check_error = True, mat = None) :
    if mat == None :
        mat = mat_ali_NW (seqA,seqB,gap,sim_mat)
    aliA, aliB, i, j = "", "", len(seqA), len(seqB)
    fig, ax = plt.subplots()
    plt.xlabel(nameA)
    plt.ylabel(nameB)
    seg_tab, col_tab = [], []
    while i > 0 and j > 0 :
        old_i, old_j = i, j
        if mat[i][j] == mat[i - 1][j] - gap :
            aliA, aliB = seqA[i - 1] + aliA, "_" + aliB
            i -= 1
            col = 'k'
        elif mat[i][j] == mat[i][j - 1] - gap :
            aliB, aliA = seqB[j - 1] + aliB, "_" + aliA     
            j -= 1
            col = 'k'
        elif mat[i][j] == mat[i - 1][j - 1] + sim_mat[dico (seqA[i - 1])][dico (seqB[j - 1])]:
            aliA, aliB = seqA[i - 1] + aliA, seqB[j - 1] + aliB
            
            if seqA[i - 1]== seqB[j - 1]:
                col = 'g'
            else:
                col = 'r'
                if check_error == True :
                    seg_tab.append([(i + deb_seqA,j + deb_seqB),(i + deb_seqA,deb_seqB)])
                    seg_tab.append([(i + deb_seqA,j + deb_seqB),(deb_seqA,j + deb_seqB)])
                    col_tab.append('r')
                    col_tab.append('r')
            i -= 1
            j -= 1
        seg_tab.append([(old_i + deb_seqA, old_j + deb_seqB),(i + deb_seqA,j + deb_seqB)])
        col_tab.append(col)
    while i > 0 :
        aliA, aliB = seqA[i - 1] + aliA, "_" + aliB
        seg_tab.append([(i + deb_seqA,j + deb_seqB),(i-1 + deb_seqA,j + deb_seqB)])
        col_tab.append('k')
        i -= 1
    while j > 0 :
        aliB, aliA = seqB[j - 1] + aliB, "_" + aliA
        seg_tab.append([(i + deb_seqA,j + deb_seqB),(i + deb_seqA,j-1 + deb_seqB)])
        col_tab.append('k')
        j -= 1

    ax.add_collection(LineCollection(seg_tab, colors = col_tab))
    ax.autoscale_view()
    plt.grid()
    plt.title("Alignement par algorithme de Needleman-Wunsch ({}//{},{})".format(gap,sim_mat[0][0],sim_mat[0][1]))
    plt.show()
    return aliA,aliB



def pltGraph_Gotoh_LC (seqQ, seqP, gap_start = 10, gap_extend = 0.5, sim_mat = sim_new,
                       nameA = "Sequence 1", nameB = "Séquence 2", deb_seqQ = 0, deb_seqP = 0, check_error = True) :
    D, Q, P = mat_ali_gotoh(seqQ, seqP, gap_start, gap_extend, sim_mat)
    aliA, aliB, i, j = "", "", len(seqQ), len(seqP)
    mat = D
    fig, ax = plt.subplots()
    plt.xlabel(nameA)
    plt.ylabel(nameB)
    seg_tab, col_tab = [], []
    while i > 0 and j > 0 :
        mark = True
        old_i, old_j = i + deb_seqQ, j + deb_seqP
        col = 'k'
        if mat == D :
            if D[i][j] == P[i][j] :
                mat = P
                mark = False
            elif D[i][j] == Q[i][j] :
                mat = Q
                mark = False
            elif D[i][j] == mat[i - 1][j - 1] + sim_mat[dico (seqQ[i - 1])][dico (seqP[j - 1])]:
                aliA, aliB = seqQ[i - 1] + aliA, seqP[j - 1] + aliB

                if seqQ[i - 1]== seqP[j - 1]:
                    col = 'g'
                else:
                    col = 'r'
                    if check_error == True :
                        seg_tab.append([(i + deb_seqQ,j + deb_seqP),(i + deb_seqQ, + deb_seqP)])
                        seg_tab.append([(i + deb_seqQ,j + deb_seqP),(deb_seqQ,j + deb_seqP)])
                        col_tab.append('r')
                        col_tab.append('r')
                i -= 1
                j -= 1
        elif mat == P :
            aliA, aliB = seqQ[i - 1] + aliA, "_" + aliB
            i -= 1
            if P[i][j] == D[i - 1][j] - gap_start :
                mat = D
        elif mat == Q :
            aliB, aliA = seqP[j - 1] + aliB, "_" + aliA     
            j -= 1
            if Q[i][j] == D[i][j - 1] - gap_start :
                mat = D
        if mark :
            seg_tab.append([(old_i, old_j),(i + deb_seqQ,j + deb_seqP)])
            col_tab.append(col)
                
    while i > 0 :
        aliA, aliB = seqQ[i - 1] + aliA, "_" + aliB
        seg_tab.append([(i + deb_seqQ,j + deb_seqP),(i-1 + deb_seqQ,j + deb_seqP)])
        col_tab.append('k')
        i -= 1
    while j > 0 :
        aliB, aliA = seqP[j - 1] + aliB, "_" + aliA   
        seg_tab.append([(i + deb_seqQ,j + deb_seqP),(i + deb_seqQ,j-1 + deb_seqP)])
        col_tab.append('k')
        j -= 1
        
    ax.add_collection(LineCollection(seg_tab, colors = col_tab))
    ax.autoscale_view()
    plt.title("Alignement par algorithme de Gotoh ({},{}//{},{})".format(gap_start,gap_extend,sim_mat[0][0],sim_mat[0][1]))
    plt.grid()
    plt.show()
    
    
    return aliA,aliB 





# Old Versions






def pltgraph_NW (seqA, seqB, gap = 0, sim_mat = sim_mat_bas,nameA = "Sequence 1", nameB = "Séquence 2", check_error = True) :
    mat = mat_ali_NW (seqA,seqB,gap,sim_mat)
    aliA, aliB, i, j = "", "", len(seqA), len(seqB)
    plt.figure(figsize = (i,j))
    plt.axis([-0.1,i+0.1,-0.1,j+0.1])
    plt.xlabel(nameA)
    plt.ylabel(nameB)
    while i > 0 and j > 0 :
        old_x, old_y = i, j
        if mat[i][j] == mat[i - 1][j] - gap :
            aliA, aliB = seqA[i - 1] + aliA, "_" + aliB
            i -= 1
            col = 'k'
        elif mat[i][j] == mat[i][j - 1] - gap :
            aliB, aliA = seqB[j - 1] + aliB, "_" + aliA     
            j -= 1
            col = 'k'
        elif mat[i][j] == mat[i - 1][j - 1] + sim_mat[dico (seqA[i - 1])][dico (seqB[j - 1])]:
            aliA, aliB = seqA[i - 1] + aliA, seqB[j - 1] + aliB
            
            if seqA[i - 1]== seqB[j - 1]:
                col = 'g'
            else:
                col = 'r'
                if check_error == True :
                    plt.plot([i,i], [j,0],linewidth = 0.5,color = 'r',ls = "--")
                    plt.plot([i,0], [j,j],linewidth = 0.5,color = 'r',ls = "--")
            i -= 1
            j -= 1
        plt.plot ([old_x, i], [old_y, j], color = col)
    while i > 0 :
        aliA, aliB = seqA[i - 1] + aliA, "_" + aliB
        plt.plot ([i, i-1], [j, j], color ='k')
        i -= 1
    while j > 0 :
        aliB, aliA = seqB[j - 1] + aliB, "_" + aliA     
        plt.plot ([i, i], [j, j-1], color ='k')
        j -= 1
    plt.grid()
    plt.show()
    return aliA,aliB



def pltgraph_nocol_NW (seqA, seqB, gap = 0, sim_mat = sim_mat_bas,nameA = "Sequence 1", nameB = "Séquence 2", check_error = True) :
    mat = mat_ali_NW (seqA,seqB,gap,sim_mat)
    aliA, aliB, i, j = "", "", len(seqA), len(seqB)
    plt.figure(figsize = (i,j))
    plt.axis([-0.1,i+0.1,-0.1,j+0.1])
    plt.xlabel(nameA)
    plt.ylabel(nameB)
    X,Y = [i],[j]
    while i > 0 and j > 0 :
        if mat[i][j] == mat[i - 1][j] - gap :
            aliA, aliB = seqA[i - 1] + aliA, "_" + aliB
            i -= 1
        elif mat[i][j] == mat[i][j - 1] - gap :
            aliB, aliA = seqB[j - 1] + aliB, "_" + aliA     
            j -= 1
        elif mat[i][j] == mat[i - 1][j - 1] + sim_mat[dico (seqA[i - 1])][dico (seqB[j - 1])]:
            aliA, aliB = seqA[i - 1] + aliA, seqB[j - 1] + aliB
            if seqA[i - 1] != seqB[j - 1] :
                plt.plot([i-0.5], [j-0.5],marker = '+', mew = 5, color = 'r')
            i -= 1
            j -= 1
        X.append(i)
        Y.append(j)
    while i > 0 :
        aliA, aliB = seqA[i - 1] + aliA, "_" + aliB
        i -= 1
        X.append(i)
        Y.append(j)
    while j > 0 :
        aliB, aliA = seqB[j - 1] + aliB, "_" + aliA
        j -= 1
        X.append(i)
        Y.append(j)
    plt.plot(X,Y,color = 'g')
    plt.grid()
    plt.show()
    return aliA,aliB


