#JOGO DA VELHA
import math
import random

#*****
#*************
#******************************

#1) DECLARAÇÃO DE VARIÁVEIS ********************************************************************************************

#******************************
#*************
#*****
from time import sleep

t=[[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
final=0
jogadas=[]
registros=[]
vitoria=-1

#*****
#*************
#******************************

#2) FUNÇÕES ************************************************************************************************************

#******************************
#*************
#*****

def jogadas_possiveis():
    for linha in open('dados.txt'):
        # print(linha)
        jogadas.append(linha.split(','))
    #for lista in jogadas:
    #    for itens in lista:
    #        jogadas[lista]

jogadas_possiveis()

def verificaJogadaPronta(jogador_ver):
    l=-1
    c=-1
    #print(len(jogadas))
    for g in jogadas:
        k=0
        p1=p2=p3=0
        #print(g[0])
        l1=int(g[k][0])-1
        c1=int(g[k][1])-1
        k=k+1
        l2=int(g[k][0])-1
        c2=int(g[k][1])-1
        k = k + 1
        l3=int(g[k][0])-1
        c3=int(g[k][1])-1
        #print(l1,c1,l2,c2,l3,c3)
        if (t[l1][c1]==jogador_ver):
            p1=1
        if (t[l2][c2]==jogador_ver):
            p2=1
        if (t[l3][c3]==jogador_ver):
            p3=1
        soma=p1+p2+p3
        if soma==2:
            if (p1==0):
                l=l1
                c=c1
            if (p2==0):
                l=l2
                c=c2
            if (p3==0):
                l=l3
                c=c3
            if (t[l][c]==-1): 
                break
            else:
                l=-1
                c=-1
    return l,c
        
#l,c=verificaJogadaPronta()
#print(l,c)
        
def verificaJogada(jog,jogador):
    if (jogador==0):
        j=1
    else:
        j=0
    lh=-1
    pl=[]
    cv=-1
    pc=[]
    # somas de pontuação
    sh = 0  # horizontal
    sv = 1  # vertical
    sd = 1  # diagonal

    if jog==1:
        #primeira jogada
        # horizontal
        c = 1
        while c <= 3:

            if (t[c - 1][0] == t[c - 1][1] == t[c - 1][2] != j):
                lh=c
                pl.append(lh)
                sh = 3
            c = c + 1

        # vertical
        for col in range(len(t)):
            for l in range(len(t)):
                if (l > 0):
                    if (t[l][col] == t[l - 1][col] and t[l][col] != j):
                        sv = sv + 1
                        cv=col
                        pc.append(cv)
            if (sv < 3):
                sv = 1

        # diagonal
        for c in range(len(t)):
            if (c > 0):
                if (t[c][c] == t[c - 1][c - 1] == j):
                    sd = sd + 1
            # if (sd<3):
            #    sd=1
    else:
        #segunda
        #jogada defensiva

        # horizontal
        c = 1
        while c <= 3:

            if (t[c - 1][0] == t[c - 1][1] == j) or (t[c - 1][0] == t[c - 1][2] == j) or (t[c - 1][1] == t[c - 1][2] == j):
                lh=c
                pl.append(lh)
                sh = 3
            c = c + 1

        # vertical
        for col in range(len(t)):
            for l in range(len(t)):
                if (l > 0):
                    if (t[l][col] == t[l - 1][col] and t[l][col] == j):
                        sv = sv + 1
                        cv=col
                        pc.append(cv)
            #if (sv < 3):
            #    sv = 1

        # diagonal
        for c in range(len(t)):
            if (c > 0):
                if (t[c][c] == t[c - 1][c - 1] == j):
                    sd = sd + 1
            # if (sd<3):
            #    sd=1


        #fim jogada defensiva
        #return lh, cv, sd, pl, pc
        if (sh > 0 or sv > 1 or sd == 3):
            # if (sh == 3):
            #    return lh
            # elif (sv == 3):
            #    j = 2
            # print(f"\n#### O jogador {j} venceu o jogo! ####\n")
            print("jogada defensiva!")

        else:
            #jogada de ataque
            while c <= 3:

                if ((t[c - 1][0] == jogador or t[c - 1][1] == jogador or t[c - 1][2] == jogador) and (t[c - 1][0] == t[c - 1][1] == t[c - 1][2] != j)):
                    lh = c
                    pl.append(lh)
                    sh = 3
                c = c + 1

            # vertical
            for col in range(len(t)):
                for l in range(len(t)):
                    if (l > 0):
                        if ((t[l][col] == jogador or t[l - 1][col] == jogador) and (t[l][col] == t[l - 1][col] and t[l][col] != j and t[l][col] != j)):
                            sv = sv + 1
                            cv = col
                            pc.append(cv)
                #if (sv < 3):
                #    sv = 1

            # diagonal
            for c in range(len(t)):
                if (c > 0):
                    if (t[c][c] == t[c - 1][c - 1] != j):
                        sd = sd + 1
                # if (sd<3):
                #    sd=1
    if (sh > 0 or sv > 1 or sd == 3):
        #if (sh == 3):
        #    return lh
        #elif (sv == 3):
        #    j = 2
        #print(f"\n#### O jogador {j} venceu o jogo! ####\n")
        return lh,cv,sd,pl,pc
    else:
        return lh,cv,sd,pl,pc

def verificaVencedor(jogador):
   #  #somas de pontuação
   #  sh=0 #horizontal
   #  sv=1 #vertical
   #  sd=1 #diagonal
   #  jogador = jogador
   #  #horizontal
   #  c=1
   #  while c<=3:
        
   #      if (t[c-1][0]==t[c-1][1]==t[c-1][2]==jogador):
   #          sh=3
   #      c=c+1

   # #vertical
   #  for col in range(len(t)):
   #      for l in range(len(t)):
   #          if (l>0):
   #              if (t[l][col]==t[l-1][col] and t[l][col]==jogador):
   #                  sv=sv+1
   #      if (sv<3):
   #          sv=1
                   
   # #diagonal
   #  for c in range(len(t)):
   #     if (c>0):
   #         if (t[c][c]==t[c-1][c-1]==jogador):
   #             sd=sd+1
   #     #if (sd<3):
   #     #    sd=1
   #  if (sh==3 or sv==3 or sd==3):
   #      if (jogador==1):
   #          j=1
   #      elif (jogador==0):
   #          j=2
   #      imprimeTabela()
   #      print(f"\n#### O jogador {j} venceu o jogo! ####\n")
   #      return "vencedor"
   #  else:
   #      return "continuar"
   
    
    reg="continuar"
    for g in jogadas:
        k=0
        p1=p2=p3=0
        #print(g[0])
        l1=int(g[k][0])-1
        c1=int(g[k][1])-1
        k=k+1
        l2=int(g[k][0])-1
        c2=int(g[k][1])-1
        k = k + 1
        l3=int(g[k][0])-1
        c3=int(g[k][1])-1
        #print(f"verificando vencedor -> jogada: {l1,c1,l2,c2,l3,c3}")
        if (t[l1][c1]==jogador):
            p1=1
        if (t[l2][c2]==jogador):
            p2=1
        if (t[l3][c3]==jogador):
            p3=1
        soma=p1+p2+p3
        #print(f"soma = {soma}")
        if soma==3:
               
            if (jogador==1):
                j=1
            elif (jogador==0):
                j=2
            imprimeTabela()
            print(f"\n#### O jogador {j} venceu o jogo! ####\n")             
            reg = "vencedor"    
            break    
    return reg

#print(str(t[0][1]))
def verificarFinal():
    c=1
    final = 1
    while c<=3:
        #imprimindo tabela do jogo
        d=["-","-","-"]
        d[0] = t[c - 1][0]
        d[1] = t[c - 1][1]
        d[2] = t[c - 1][2]

        for i in range(len(t)):

            #print(d[i])
            if d[i]==1:
                d[i]="X"
            elif d[i]==0:
                d[i]="0"
            elif d[i]==-1:
                d[i]="-"
                final=0

        #print(f"| {d[0]} | {d[1]} | {d[2]} |")
        c=c+1
    return final

def imprimeTabela():
    c=1
    final = 1
    while c<=3:
        #imprimindo tabela do jogo
        d=["-","-","-"]
        d[0] = t[c - 1][0]
        d[1] = t[c - 1][1]
        d[2] = t[c - 1][2]

        for i in range(len(t)):

            #print(d[i])
            if d[i]==1:
                d[i]="X"
            elif d[i]==0:
                d[i]="0"
            elif d[i]==-1:
                d[i]="-"
                final=0

        print(f"| {d[0]} | {d[1]} | {d[2]} |")
        c=c+1

#*****
#*************
#******************************

#3) JOGO ************************************************************************************************************

#******************************
#*************
#*****


print("\nPosições de entrada\n####\n| 11 | 12 | 13 |\n| 21 | 22 | 23 |\n| 31 | 32 | 33 |\n####\n")
s=0
continua=1
while continua<100:
    while s==0 and final == 0:
        jog=1
        #entrada de dados JOGADOR 1
        imprimeTabela()
        l=0
        jogou = 0
        while l==0:
            #print(d)
            # j1=input("JOGADOR 1\nDigite o número da posição para inserir:")
            # linha=int(j1[0])-1
            # coluna=int(j1[1])-1
            # #Verificar se já existe dado lançado na posição
            # if (t[linha][coluna]==-1):
            #     #não há dado lançado ainda
            #     #registrar
            #     l=1
            #     t[linha][coluna]=1
            #     #print("lançadado jogador 1")
            #     if (verificaVencedor(1)=="vencedor"):
            #         s=1
            #     break
            # else:
            #     #já existe um dado lançado nesta posição
            #     print("Já existe um dado lançado nesta posição! Digite novamente uma posição válida.")
            # imprimeTabela()
            l = 0
            # print(verificaJogada(jog))

            #sleep(5)

            hor, vert, diag, pl, pc = verificaJogada(jog, 1)
            pl.sort
            pc.sort
            linha = -1
            coluna = -1
            jogou = 0
            # jogada de ATAQUE ###########################
            l1, c1 = verificaJogadaPronta(1)

            if (l1 > -1 and l == 0 and s == 0):
                print("\nJogada de Ataque identificada!\n")
                linha = l1
                coluna = c1
                l = 1
                t[linha][coluna] = 1
                jogou = 1
                if (verificaVencedor(1) == "vencedor"):
                    vitoria=1
                    s = 1

            # jogada de DEFESA #########################
            l1, c1 = verificaJogadaPronta(0)
            # print(l1)
            if (l1 > -1 and l == 0 and s == 0):
                print("\nJogada de defesa identificada!\n")
                linha = l1
                coluna = c1
                l = 1
                t[linha][coluna] = 1
                jogou = 1
                if (verificaVencedor(1) == "vencedor"):
                    vitoria=1
                    s = 1

            if (jogou == 0 and s == 0):
                print("\nJOGADA NÃO IDENTIFICADA!\n")
                # entrada automática

                if (hor > -1):
                    # jogada na linha hor
                    repeat = []
                    num = []
                    r = 0
                    cont = 0
                    # print(pl)

                    for i in range(0, len(pl) - 1):
                        if (pl[i] == pl[i + 1]):
                            r = r + 1
                            repeat[cont] = r
                            num[cont] = pl[i]
                        else:
                            r = 1
                            cont = cont + 1
                            repeat.append(r)
                            # repeat[cont]=r
                            # num[cont]=pl[i]
                            num.append(pl[i])

                    if (len(repeat) > 1):
                        imax = repeat.index(max(repeat))
                        linha = num[imax]  # pl[random.randint(0,len(pl)-1)]#int(hor-1)
                    else:
                        linha = pl[random.randint(0, len(pl) - 1)]

                    coluna = random.randint(0, 2)

                if (vert > -1 and linha == -1):
                    # jogada na vertical
                    linha = random.randint(0, 2)

                    repeat = []
                    num = []
                    r = 0
                    cont = 0
                    # print(pl)

                    for i in range(0, len(pc) - 1):
                        if (pc[i] == pc[i + 1] and len(repeat)>cont):
                            r = r + 1
                            repeat[cont] = r
                            num[cont] = pc[i]
                        else:
                            r = 1
                            cont = cont + 1
                            repeat.append(r)
                            # repeat[cont]=r
                            # num[cont]=pl[i]
                            num.append(pc[i])

                    if (len(repeat) > 1):
                        imax = repeat.index(max(repeat))
                        coluna = num[imax]  # pl[random.randint(0,len(pl)-1)]#int(hor-1)
                    else:
                        coluna = pc[random.randint(0, len(pc) - 1)]

                    # coluna=pc[random.randint(0,len(pc)-1)]#int(vert-1)

                if (diag == 3 and linha == -1):
                    # jogada na vertical
                    linha = random.randint(0, 2)
                    coluna = linha

                    # entrada manual
                    # j1=input("JOGADOR 2\nDigite o número da posição para inserir:")

            while l == 0 and s == 0 and final == 0:
                # Verificar se já existe dado lançado na posição
                if (linha == -1):
                    linha = random.randint(0, 2)
                if (coluna == -1):
                    coluna = random.randint(0, 2)
                if (linha > 2):
                    linha = 2
                if (coluna > 2):
                    coluna = 2
                # print(f"linha = {linha}, coluna = {coluna}")
                if (t[linha][coluna] == -1):
                    # não há dado lançado ainda
                    # registrar
                    l = 1
                    if l1 == -1:
                        t[linha][coluna] = 1
                    if (verificaVencedor(1) == "vencedor"):
                        vitoria = 1
                        s = 1
                    break
                else:
                    # já existe um dado lançado nesta posição
                    id = 0
                    if (hor > -1):
                        # linha = random.randint(0, 2)
                        coluna = random.randint(0, 2)
                        id == 1
                    if (vert > -1 and id == 0):
                        linha = random.randint(0, 2)
                        id == 1
                    if (diag == 3 and id == 0):
                        linha = random.randint(0, 2)
                        coluna = linha
                        id == 1
                    if (id == 0):
                        linha = random.randint(0, 2)
                        coluna = random.randint(0, 2)
                    final = verificarFinal()
                    print("Já existe um dado lançado nesta posição! Digite novamente uma posição válida.")















        #sleep(3)
        #entrada de dados JOGADOR 2
        #imprimeTabela()
        l=0
        #print(verificaJogada(jog))
        hor, vert, diag,pl,pc = verificaJogada(jog,0)
        pl.sort
        pc.sort
        linha = -1
        coluna = -1
        jogou=0
        #jogada de ATAQUE ###########################
        l1, c1 = verificaJogadaPronta(0)

        if(l1>-1 and l==0 and s == 0):
            print("\nJogada de Ataque identificada!\n")
            linha = l1
            coluna = c1
            l = 1
            t[linha][coluna] = 0
            jogou = 1
            if (verificaVencedor(0) == "vencedor"):
                vitoria = 0
                s = 1

        #jogada de DEFESA #########################
        l1, c1 = verificaJogadaPronta(1)
        #print(l1)
        if (l1 > -1 and l==0 and s == 0):
            print("\nJogada de defesa identificada!\n")
            linha = l1
            coluna = c1
            l = 1
            t[linha][coluna] = 0
            jogou = 1
            if (verificaVencedor(0) == "vencedor"):
                vitoria = 0
                s = 1


        if (jogou == 0 and s==0):
            print("\nJOGADA NÃO IDENTIFICADA!\n")
            #entrada automática

            if (hor>-1):
                #jogada na linha hor
                repeat = []
                num = []
                r=0
                cont=0
                #print(pl)

                for i in range(0,len(pl)-1):
                    if (pl[i]==pl[i+1]):
                        r = r + 1
                        repeat[cont]=r
                        num[cont]=pl[i]
                    else:
                        r=1
                        cont=cont+1
                        repeat.append(r)
                        #repeat[cont]=r
                        #num[cont]=pl[i]
                        num.append(pl[i])

                if (len(repeat)>1):
                    imax=repeat.index(max(repeat))
                    linha = num[imax]  # pl[random.randint(0,len(pl)-1)]#int(hor-1)
                else:
                    linha = pl[random.randint(0,len(pl)-1)]

                coluna=random.randint(0,2)

            if (vert>-1 and linha==-1):
                #jogada na vertical
                linha=random.randint(0,2)

                repeat = []
                num = []
                r=0
                cont=0
                repeat.append(0)
                num.append(0)
                #print(pl)

                for i in range(0,len(pc)-1):
                    if (pc[i]==pc[i+1]):
                        r = r + 1
                        repeat[cont]=r
                        num[cont]=pc[i]
                    else:
                        r=1
                        cont=cont+1
                        repeat.append(r)
                        #repeat[cont]=r
                        #num[cont]=pl[i]
                        num.append(pc[i])

                if (len(repeat)>1):
                    imax=repeat.index(max(repeat))
                    coluna = num[imax]  # pl[random.randint(0,len(pl)-1)]#int(hor-1)
                else:
                    coluna = pc[random.randint(0,len(pc)-1)]

                #coluna=pc[random.randint(0,len(pc)-1)]#int(vert-1)

            if (diag==3 and linha==-1):
                #jogada na vertical
                linha=random.randint(0,2)
                coluna=linha


                #entrada manual
                #j1=input("JOGADOR 2\nDigite o número da posição para inserir:")



        while l == 0 and s == 0 and final==0:
            #Verificar se já existe dado lançado na posição
            if (linha==-1):
                linha = random.randint(0, 2)
            if (coluna==-1):
                coluna = random.randint(0, 2)
            if (linha>2):
                linha = 2
            if (coluna>2):
                coluna = 2
            #print(f"linha = {linha}, coluna = {coluna}")
            if (t[linha][coluna]==-1):
                #não há dado lançado ainda
                #registrar
                l=1
                if l1==-1:
                    t[linha][coluna]=0
                if (verificaVencedor(0)=="vencedor"):
                    vitoria = 0
                    s=1
                break
            else:
                #já existe um dado lançado nesta posição
                id=0
                if (hor > -1):
                    #linha = random.randint(0, 2)
                    coluna = random.randint(0, 2)
                    id==1
                if (vert > -1 and id==0):
                    linha = random.randint(0, 2)
                    id==1
                if (diag==3 and id==0):
                    linha = random.randint(0, 2)
                    coluna = linha
                    id==1
                if (id==0):
                    linha = random.randint(0, 2)
                    coluna = random.randint(0, 2)
                final=verificarFinal()
                print("Já existe um dado lançado nesta posição! Digite novamente uma posição válida.")

        jog=jog+1

        if (final==1):
            imprimeTabela()
            print("\nFim de jogo!")
    continua=continua+1
    #continua=int(input("\n\n\n*********** Digite 1 para iniciar um novo jogo ou 0 para finalizar: "))
    #if (continua==1):
    registros.append(vitoria)
    vitoria=-1
    t = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
    s=0
    final=0


print(f"\n\n*****RESULTADOS******\n\nJogador 1 - Vitórias -> {round((registros.count(1)/len(registros))*100)} %\nJogador 2 - Vitórias -> {round((registros.count(0)/len(registros))*100)} %\nEmpates -> {round((registros.count(-1)/len(registros))*100)} %\n")
#print(registros)