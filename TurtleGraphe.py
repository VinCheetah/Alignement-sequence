from Tipe import *
import turtle as tl
from N_W_prog import *


def turt_ali (seqA, seqB, gap = 0, sim_mat = sim_mat_bas) :
    tl.Screen()
    tl.screensize(500,500)
    tl.clear()
    tl.speed(10)
    tl.up()
    tl.goto(251,251)
    tl.down()
    tl.goto(-251,251)
    tl.goto(-251,-251)
    tl.goto(251,-251)
    tl.goto(251,251)    
    x_ = 500 / len(seqA)
    y_ = 500 / len(seqB)
    x_co = 250
    y_co = 250
    mat = mat_ali_NW (seqA,seqB,gap,sim_mat)
    aliA, aliB, i, j = "", "", len(seqA), len(seqB)
    while i > 0 and j > 0 :
        if mat[i][j] == mat[i - 1][j] - gap :
            aliA, aliB = seqA[i - 1] + aliA, "_" + aliB
            i -= 1
            x_co -= x_
        elif mat[i][j] == mat[i][j - 1] - gap :
            aliB, aliA = seqB[j - 1] + aliB, "_" + aliA     
            j -= 1
            y_co -= y_
        elif mat[i][j] == mat[i - 1][j - 1] + sim_mat[dico (seqA[i - 1])][dico (seqB[j - 1])]:
            aliA, aliB = seqA[i - 1] + aliA, seqB[j - 1] + aliB
            i -= 1
            j -= 1
            x_co -= x_
            y_co -= y_
        tl.goto (x_co, y_co)
    while i > 0 :
        aliA, aliB = seqA[i - 1] + aliA, "_" + aliB
        i -= 1
        x_co -= x_
        tl.goto (x_co, y_co)
    while j > 0 :
        aliB, aliA = seqB[j - 1] + aliB, "_" + aliA     
        j -= 1
        y_co -= y_
        tl.goto (x_co, y_co)
    tl.up()
    if len(seqA) < 80 and len(seqB) < 80:
        for k in range(len(seqA)) :
            tl.goto(-250 + int (k * x_) + (x_ // 2), -265)
            tl.write(seqA[k])
    for k in range(len(seqB)) :
        tl.goto(-265, -250 + int(k*y_))
        tl.write(seqB[k])
    
    return aliA, aliB, mat[len(seqA)][len(seqB)]

def turt_ali_colo (seqA, seqB, gap = 0, sim_mat = sim_mat_bas,quadrillage = False,pointille = False) :
    tl.Screen()
    tl.screensize(500,500)
    tl.clear()
    tl.speed(3)
    tl.up()
    tl.goto(251,251)
    tl.down()
    tl.goto(-251,251)
    tl.goto(-251,-251)
    tl.goto(251,-251)
    tl.goto(251,251)    
    x_ = 500 / len(seqA)
    y_ = 500 / len(seqB)
    x_co = 250
    y_co = 250
    mat = mat_ali_NW (seqA,seqB,gap,sim_mat)
    aliA, aliB, i, j = "", "", len(seqA), len(seqB)
    while i > 0 and j > 0 :
        tl.color('black')
        tl.pensize(3)
        if mat[i][j] == mat[i - 1][j] - gap :
            aliA, aliB = seqA[i - 1] + aliA, "_" + aliB
            i -= 1
            x_co -= x_
        elif mat[i][j] == mat[i][j - 1] - gap :
            aliB, aliA = seqB[j - 1] + aliB, "_" + aliA     
            j -= 1
            y_co -= y_
        elif mat[i][j] == mat[i - 1][j - 1] + sim_mat[dico (seqA[i - 1])][dico (seqB[j - 1])]:
            aliA, aliB = seqA[i - 1] + aliA, seqB[j - 1] + aliB
            
            if seqA[i - 1]== seqB[j - 1]:
                tl.color('green')
                tl.pensize(4)
            else:
                tl.color('red')
            i -= 1
            j -= 1
            x_co -= x_
            y_co -= y_
        tl.goto (x_co, y_co)
    tl.color('black')
    while i > 0 :
        aliA, aliB = seqA[i - 1] + aliA, "_" + aliB
        i -= 1
        x_co -= x_
        tl.goto (x_co, y_co)
    while j > 0 :
        aliB, aliA = seqB[j - 1] + aliB, "_" + aliA     
        j -= 1
        y_co -= y_
        tl.goto (x_co, y_co)
    tl.up()
    if len(seqA) < 80 and len(seqB) < 80:
        for k in range(len(seqA)) :
            tl.goto(-250 + int (k * x_) + (x_ // 2), -265)
            tl.write(seqA[k])
        for k in range(len(seqB)) :
            tl.goto(-265, -250 + int(k*y_) + (y_ // 2)*(1 - len(seqB)/ 80))
            tl.write(seqB[k])
    if quadrillage and len(seqA) < 80 and len(seqB) < 80 :
        tl.pensize(0.1)
        tl.speed(100)
        for i in range(1,len(seqA)) :
            tl.up()
            tl.goto(-250 + int (i * x_),-250)
            if pointille :
                for j in range(1,51):
                    if j%2 == 0 :
                        tl.down()
                    else :
                        tl.up()
                    tl.goto( -250 + int (i* x_),-250 + 10*j)
            else :
                tl.down()
                tl.goto(-250 + int (i* x_),250)
        for i in range(1,len(seqB)) :
            tl.up()
            tl.goto(-250,-250 + int (i * y_))
            if pointille :
                for j in range(1,51):
                    if j%2 == 0 :
                        tl.down()
                    else :
                        tl.up()
                    tl.goto(-250 + 10*j,-250 + int (i* y_))    
            else :
                tl.down()
                tl.goto(250,-250 + int (i* y_))
    
    return aliA, aliB, mat[len(seqA)][len(seqB)]

def turt_ali_col (seqA, seqB, gap = 1, sim_mat = sim_mat_bas,quadrillage = False,pointille = False) :
    tl.pensize(1)
    tl.color("black")
    tl.screensize(140,700)
    tl.clear()
    tl.speed(5)
    tl.up()
    tl.goto(251,401)
    tl.down()
    tl.goto(-251,401)
    tl.goto(-251,-101)
    tl.goto(251,-101)
    tl.goto(251,401)    
    x_ = 500 / len(seqA)
    y_ = 500 / len(seqB)
    x_co = 250
    y_co = 400
    tl.up()
    if len(seqA) < 80 and len(seqB) < 80:
        for k in range(len(seqA)) :
            tl.goto(-250 + int (k * x_) + (x_ // 2), -115)
            tl.write(seqA[k],align = 'center')
        for k in range(len(seqB)) :
            tl.goto(-265, -100 + int(k*y_) + (y_ // 3))
            tl.write(seqB[k],align = "center")
    if quadrillage and len(seqA) < 80 and len(seqB) < 80 :
        tl.pensize(0.1)
        tl.speed(100)
        for i in range(1,len(seqA)) :
            tl.up()
            tl.goto(-250 + int (i * x_),-100)
            if pointille :
                for j in range(1,26):
                    if j%2 == 0 :
                        tl.down()
                    else :
                        tl.up()
                    tl.goto( -250 + int (i* x_),-100 + 20*j)
            else :
                tl.down()
                tl.goto(-250 + int (i* x_),400)
        for i in range(1,len(seqB)) :
            tl.up()
            tl.goto(-250,-100 + int (i * y_))
            if pointille :
                for j in range(1,26):
                    if j%2 == 0 :
                        tl.down()
                    else :
                        tl.up()
                    tl.goto(-250 + 20*j,-100 + int (i* y_))    
            else :
                tl.down()
                tl.goto(250,-100 + int (i* y_))
    tl.goto(250,400)
    tl.down()
    mat = mat_ali_NW (seqA,seqB,gap,sim_mat)
    aliA, aliB, i, j = "", "", len(seqA), len(seqB)
    while i > 0 and j > 0 :
        tl.color('black')
        tl.pensize(3)
        if mat[i][j] == mat[i - 1][j] - gap :
            aliA, aliB = seqA[i - 1] + aliA, "_" + aliB
            i -= 1
            x_co -= x_
        elif mat[i][j] == mat[i][j - 1] - gap :
            aliB, aliA = seqB[j - 1] + aliB, "_" + aliA     
            j -= 1
            y_co -= y_
        elif mat[i][j] == mat[i - 1][j - 1] + sim_mat[dico (seqA[i - 1])][dico (seqB[j - 1])]:
            aliA, aliB = seqA[i - 1] + aliA, seqB[j - 1] + aliB
            
            if seqA[i - 1]== seqB[j - 1]:
                tl.color('green')
                tl.pensize(4)
            else:
                tl.color('red')
            i -= 1
            j -= 1
            x_co -= x_
            y_co -= y_
        tl.goto (x_co, y_co)
    tl.color('black')
    while i > 0 :
        aliA, aliB = seqA[i - 1] + aliA, "_" + aliB
        i -= 1
        x_co -= x_
        tl.goto (x_co, y_co)
    while j > 0 :
        aliB, aliA = seqB[j - 1] + aliB, "_" + aliA     
        j -= 1
        y_co -= y_
        tl.goto (x_co, y_co)
    tl.up()
    tl.speed(1000)
    tl.goto (0,-130)
    tl.write('Séquence 1',False,"center",("Verdana",12,"normal") )
    tl.goto (-320,150)
    tl.write('Séquence 2',False,"center",("Verdana",12,"normal") )
    for j in range(len(aliA)//100 + 1) :
        tl.goto (- 330, -160 - 25 * j)
        tl.write('Séquence 1',False,"center",("Verdana",8,"normal") )
        tl.goto (- 330, -170 - 25 * j)
        tl.write('Séquence 2',False,"center",("Verdana",8,"normal") )
        for i in range(min (len(aliA)- 100 * j,100)) :
            tl.goto(-300 + i * 6,-160 - 25 * j)
            tl.write(aliA[i + 100 * j],font = ("Verdana",8,"normal"))
            tl.goto(-300 + i * 6,-170 - 25 * j)
            tl.write(aliB[i + 100 * j], font = ("Verdana",8,"normal"))
        
    
    return aliA, aliB, mat[len(seqA)][len(seqB)]

def turt_ali_NW (seqA, seqB, gap = 1, sim_mat = sim_mat_bas,
                 quadrillage = False,pointille = False,
                 nom_seq_A = "Séquence 1", nom_seq_B = "Séquence 2",
                 sim_ma = "", pen_trou = "") :
    tl.pensize(1)
    tl.color("black")
    tl.screensize(140,700)
    tl.clear()
    tl.speed(5)
    tl.up()
    tl.goto(251,401)
    tl.down()
    tl.goto(-251,401)
    tl.goto(-251,-101)
    tl.goto(251,-101)
    tl.goto(251,401)    
    x_ = 500 / len(seqA)
    y_ = 500 / len(seqB)
    x_co = 250
    y_co = 400
    tl.up()
    if len(seqA) < 80 and len(seqB) < 80:
        for k in range(len(seqA)) :
            tl.goto(-250 + int (k * x_) + (x_ // 2), -115)
            tl.write(seqA[k],align = 'center')
        for k in range(len(seqB)) :
            tl.goto(-265, -100 + int(k*y_) + (y_ // 3))
            tl.write(seqB[k],align = "center")
    if quadrillage and len(seqA) < 80 and len(seqB) < 80 :
        tl.pensize(0.1)
        tl.speed(100)
        for i in range(1,len(seqA)) :
            tl.up()
            tl.goto(-250 + int (i * x_),-100)
            if pointille :
                for j in range(1,26):
                    if j%2 == 0 :
                        tl.down()
                    else :
                        tl.up()
                    tl.goto( -250 + int (i* x_),-100 + 20*j)
            else :
                tl.down()
                tl.goto(-250 + int (i* x_),400)
        for i in range(1,len(seqB)) :
            tl.up()
            tl.goto(-250,-100 + int (i * y_))
            if pointille :
                for j in range(1,26):
                    if j%2 == 0 :
                        tl.down()
                    else :
                        tl.up()
                    tl.goto(-250 + 20*j,-100 + int (i* y_))    
            else :
                tl.down()
                tl.goto(250,-100 + int (i* y_))
    tl.goto(250,400)
    tl.down()
    mat = mat_ali_NW (seqA,seqB,gap,sim_mat)
    aliA, aliB, i, j = "", "", len(seqA), len(seqB)
    while i > 0 and j > 0 :
        tl.color('black')
        tl.pensize(3)
        if mat[i][j] == mat[i - 1][j] - gap :
            aliA, aliB = seqA[i - 1] + aliA, "_" + aliB
            i -= 1
            x_co -= x_
        elif mat[i][j] == mat[i][j - 1] - gap :
            aliB, aliA = seqB[j - 1] + aliB, "_" + aliA     
            j -= 1
            y_co -= y_
        elif mat[i][j] == mat[i-1][j-1]+sim_mat[dico(seqA[i-1])][dico(seqB[j-1])]:
            aliA, aliB = seqA[i - 1] + aliA, seqB[j - 1] + aliB
            
            if seqA[i - 1]== seqB[j - 1]:
                tl.color('green')
                tl.pensize(2)
            else:
                tl.color('red')
            i -= 1
            j -= 1
            x_co -= x_
            y_co -= y_
        tl.goto (x_co, y_co)
    tl.color('black')
    while i > 0 :
        aliA, aliB = seqA[i - 1] + aliA, "_" + aliB
        i -= 1
        x_co -= x_
        tl.goto (x_co, y_co)
    while j > 0 :
        aliB, aliA = seqB[j - 1] + aliB, "_" + aliA     
        j -= 1
        y_co -= y_
        tl.goto (x_co, y_co)
    tl.up()
    tl.speed(1000)
    tl.goto (0,-130)
    tl.write(nom_seq_A,False,"center",("Verdana",12,"normal") )
    tl.goto (-320,150)
    tl.write(nom_seq_B,False,"center",("Verdana",12,"normal") )
    tail = len(aliA)//100 + 1
    for j in range(tail) :
        tl.goto (- 330, -160 - 25 * j)
        tl.write('Séquence 1',False,"center",("Verdana",8,"normal") )
        tl.goto (- 330, -170 - 25 * j)
        tl.write('Séquence 2',False,"center",("Verdana",8,"normal") )
        tl.goto(-300,-160 - 25 * j)
        tl.write(aliA[j * 100 : min(len(aliA),(j + 1) * 100)],font = ("Verdana",8,"normal"))
        tl.goto(-300,-170 - 25 * j)
        tl.write(aliB[j * 100 : min(len(aliB),(j + 1) * 100)], font = ("Verdana",8,"normal"))        
    tl.goto (-300,-170 - (25 * tail))
    tl.write(sim_ma,font = ("Verdana",8,"normal"))
    tl.goto (-300,-180 - (25 * tail))
    tl.write(pen_trou,font = ("Verdana",8,"normal"))
    tl.goto (-300,-190 - (25 * tail))
    tl.write("Needleman - Wunsch",font = ("Verdana",8,"normal"))
        
    
    return aliA, aliB, mat[len(seqA)][len(seqB)]


