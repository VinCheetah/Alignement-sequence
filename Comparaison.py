from Tipe import *


def simi_ali_NW (aliA, aliB, gap, sim_mat) :
    min_nucl = min(sim_mat[0]), min(sim_mat[1]), min(sim_mat[2]), min(sim_mat[3])
    score = 0
    scoreMax = 0
    scoreMin = 0
    for i in range(len(aliA)) :
        if aliA[i] == '_' or aliB[i] == '_' :
            score -= gap
            scoreMin -= gap
            if aliA[i] != '_' :
                scoreMax += sim_mat[dico(aliA[i])][dico(aliA[i])]
            else :
                scoreMax += sim_mat[dico(aliB[i])][dico(aliB[i])]
        else :
            score += sim_mat[dico(aliA[i])][dico(aliB[i])]
            scoreMax += max (sim_mat[dico(aliA[i])][dico(aliA[i])], sim_mat[dico(aliB[i])][dico(aliB[i])])
            scoreMin += min (min_nucl[dico(aliA[i])], min_nucl[dico(aliB[i])])
            
    return int((score - scoreMin) / (scoreMax - scoreMin) * 10000) / 100

def simi_seq_NW (seqA, seqB, gap, sim_mat) :
    aliA, aliB = pltGraph_NW_LC(seqA, seqB, gap, sim_mat)
    return simi_ali_NW(aliA, aliB, gap, sim_mat)
    

def comp_simi (seqA, seqB, gap = 1, sim_mat = sim_mat_bas) :
    if isinstance(seqA,int) :
        seqA = rand_seq(seqA)
    if isinstance(seqB,int) :
        seqB = rand_seq(seqB)
    s1 = simi_ali_NW(seqA + ["_"] * max(0, len(seqB) - len(seqA)),
                     seqB + ["_"] * max(0, len(seqA) - len(seqB)), gap, sim_mat)
    print('Similarité sans alignement : ', s1)
    aliA , aliB, _ = ali_NW(seqA,seqB,gap,sim_mat)
    s2 = simi_ali_NW (aliA, aliB, gap, sim_mat)
    print('Similarité alignement Needleman-Wunsch : ', s2)
    pltGraph_NW_LC (seqA, seqB, gap, sim_mat)


def identite_ali_NW (alia,alib) :
    sc = 0
    for i in range(len(alia)) :
        if alia[i] == alib[i] :
            sc += 1
    return sc / len(alia) * 100
