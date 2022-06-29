
import pylab as plt
import time
import copy
import math
from Sequence import *
from TurtleGraphe import *
from PltGraphe import *
from S_W_B_prog import *
from N_W_prog import *
from S_W_prog import *
from Gotoh_prog import *
from ali_cov import *



def verif_ali_fun (n,f1 = mat_ali_NW, f2 = mat_ali_SWB) :
    s1, s2 = rand_seq (n), rand_seq(n)
    ali1 , ali2 = f1(s1,s2), f2(s1,s2)
    if ali1 == ali2 :
        return True
    else :
        return s1,s2



def duree_test (seqA,seqB) :
    t1 = time.time()
    a,b,score = ali_NW(seqA, seqB, gap = 2, sim_mat = sim_mat_2)
    t2 = time.time()
    return t2 - t1

def duree_test2 (seqA,seqB) :
    t1 = time.time()
    a,b,score = ali_gotoh(seqA, seqB)
    t2 = time.time()
    return t2 - t1

def chrono_rand (n):
    s1,s2 = rand_seq(n),rand_seq(n)
    t1 = time.time()
    a,b,score = alignement(s1,s2)
    t2 = time.time()
    return t2 - t1, score


def graphe (nombre_tests,rep = 1,t_seq = 0,deb = 1,pas = 1):
    X =  [k for k in range(deb,nombre_tests,pas)]
    Y_tps = []
    for i in range(deb,nombre_tests,pas):
        tps = 0
        for k in range(rep) :
            tps += duree_test(rand_seq(max (t_seq, i)),rand_seq(max(t_seq,i)))
        Y_tps.append(tps / rep)
    plt.figure()
    plt.xlabel("Taille des séquences à aligner")
    plt.ylabel("Durée de l'alignement (s)")
    plt.plot(X,Y_tps)
    plt.show()
    
def graphe2 (nombre_tests,rep = 1,t_seq = 0,deb = 1,pas = 1):
    X =  [k for k in range(deb,nombre_tests,pas)]
    Y_tps1 = []
    Y_tps2 = []
    for i in range(deb,nombre_tests,pas):
        tps1 = 0
        tps2 = 0
        for k in range(rep) :
            tps1 += duree_test(rand_seq(max (t_seq, i)),rand_seq(max(t_seq,i)))
            tps2 += duree_test2(rand_seq(max (t_seq, i)),rand_seq(max(t_seq,i)))
        Y_tps1.append(tps1 / rep)
        Y_tps2.append(tps2 / rep)
    plt.figure()
    plt.xlabel("Taille des séquences à aligner")
    plt.ylabel("Durée de l'alignement (s)")
    plt.plot(X,Y_tps1, label = "Needleman - Wunsch", c = 'b')
    plt.plot(X,Y_tps2, label = "Gotoh", c = 'r')
    plt.legend(loc = 'best')
    plt.show()
    
def taux_proximite (precision,seqA, seqB, gap = 0, sim_mat = sim_mat_bas) :
    a,b,score = alignement(seqA, seqB, gap, sim_mat)
    tab_score = [score]
    for k in range(precision) :
        rd.shuffle(seqA)
        rd.shuffle(seqB)
        a,b, new_s = alignement(seqA,seqB,gap,sim_mat)
        tab_score.append(new_s)
    tab_score.sort()
    return (tab_score.index(score) / precision) * 100,score

def taux_proximite_ref (precision,seqA, seqRef, gap = 0, sim_mat = sim_mat_bas, severite = 1) :
    '''Plutot decevant, score trop eleve, le hasard n'est pas suffisant'''
    a,b,score = alignement(seqA, seqRef, gap, sim_mat)
    tab_score = [score]
    newA = copy.copy(seqA)
    for k in range(precision) :
        rd.shuffle(newA)
        a,b, new_s = alignement(newA,seqRef,gap,sim_mat)
        tab_score.append(new_s)
    tab_score.sort()
    return ((tab_score.index(score) / precision) ** severite) * 100,score


def taux_proxi (seqA, seqB, gap = 0, sim_mat = sim_mat_bas, severite = 1) :
    '''Plutot bien, à développer avec un pourcentage selon le score max des appariemments possibles''' 
    aliA,aliB, s = alignement(seqA, seqB,gap,sim_mat)
    score = 0
    for i in range(len(aliA)) :
        if aliA[i] == aliB[i] :
            score += 1
    return (score / len(aliA))** severite *100,s

def comp_sim_mat (s1,s2,seqA,seqB,gap) :
    screen1 = tl.Screen()
    turt_ali_colo(seqA, seqB,gap,s1)
    screen1.onclick(nothing())
    screen1.clear()
    turt_ali_colo(seqA, seqB,gap,s2)
    
n = 120
    
def tot (seqA = rand_seq(n), seqB = rand_seq(n)) :
    alignement_SW(seqA,seqB,2,sim_mat_2, open("Alignement","w"))
    turt_ali_co(seqA, seqB, 2, sim_mat_2,quadrillage = True,pointille = False, nom_seq_A = "Séquence 1", nom_seq_B = "Séquence 2", sim_ma = "classique", pen_trou = "2")
    
def t():
    sA = rand_seq(200)
    sB = rand_seq(200)

    pltGraph_NW_LC(sA,sB,2,sim_mat_2)
    pltGraph_Gotoh_LC(sA,sB,2,0.5,sim_mat_2)
    
    
def recup_mut (ali1,ali2) :
    openGap = 0
    mut_tab = []
    next_mut = []
    gap1, gap2 = 0, 0
    
    for i in range(min(len(ali1),len(ali2))) :
        
        if ali1[i] == '_' :
            if openGap == 1 :
                next_mut[1] += ali1[i]
                next_mut[2] += ali2[i]
            else :
                if openGap == 2 :
                    mut_tab.append(next_mut)
                next_mut = [(i - gap1, i - gap2),ali1[i],ali2[i]]
                openGap = 1
            gap1 += 1
            
        elif ali2[i] == '_' :
            if openGap == 2 :
                next_mut[1] += ali1[i]
                next_mut[2] += ali2[i]
            else :
                if openGap == 1 :
                    mut_tab.append(next_mut)
                next_mut = [(i - gap1, i - gap2),ali1[i],ali2[i]]
                openGap = 2
            gap2 += 1
        
        elif ali1[i] != ali2[i] :
            
            if openGap != 0 :
                openGap = 0
                mut_tab.append(next_mut)
            mut_tab.append([(i - gap1, i - gap2),ali1[i],ali2[i]])
                 
    if openGap != 0 :
        mut_tab.append(next_mut)
        
    return mut_tab


def co_mut(ali1,ali2,ali3,ali4) :
    mut1 = recup_mut(ali1, ali2)
    mut2 = recup_mut(ali3, ali4)
    co = []
    for i in mut1 :
        for j in mut2 :
            if i[1] == j[1] and i[2] == j[2] and (i[0][0] == j[0][0] or i[0][0] == j[0][1] or i[0][1] == j[0][0] or i[0][1] == j[0][1]) :
                co.append((i,j))
    return co

