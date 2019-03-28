import sys
import time
#print(sys.argv[1])
N = sys.argv[1]
N = int(float(N))
len_table = N**3
clausulas = ""

# tabela para representar o tabuleiro do sudoku NxN na forma (N x N x N)
def construir_tabela(N):
    tam = 1
    tabela = []
    
    for i in range(N):
        conj_i = []
        for j in range(N):
            conj_j = []
            for k in range(N):
                conj_j.append(tam)
                tam = tam + 1
            conj_i.append(conj_j)
        tabela.append(conj_i)
            
    return tabela

#regra para ter pelo menos um em cada posicao
def um_por_posicao(tabela):
    #No maximo um por posicao
    _maximo_um_pp = ""
    #Pelo menos um por posicao
    _ao_menos_um_pp = ""
    for x in tabela:
        for y in x:
            for z in y:
                _ao_menos_um_pp = _ao_menos_um_pp +str(z) + ' '
                for a in y:
                    if z != a:
                        _maximo_um_pp = _maximo_um_pp + '-'+str(z)+' -'+str(a)+' '+str(0)+'\n'
            _ao_menos_um_pp = _ao_menos_um_pp + str(0) + '\n'
    return _ao_menos_um_pp,_maximo_um_pp


#Funcao Auxiliar
#Inicializando conjunto com n conjuntos vazios
def inicialiando_conj(N):
    conj = []
    for x in range(N):
        conj.append([])
    return conj
    
    


#Regra para ter um por linha
def um_por_linha(tabela):
    #No maximo um por linha
    _maximo_um_pl = ""
    #Pelo menos um por linha
    _ao_menos_um_pl = ""
    _conj = []
    conj =  inicialiando_conj(N)
    
    for x in tabela:
        for y in x:
            for z in y:
                conj[z % N].append(z)
        _conj.append(conj)
        conj = inicialiando_conj(N)
    
    for x in _conj:
        for y in x:
            for z in y:
                _ao_menos_um_pl = _ao_menos_um_pl +str(z) + ' '
                for a in y:
                    if a != z:
                        if a == y[len(y)-1] and y == x[len(x)-1]:
                            _maximo_um_pl = _maximo_um_pl + '-'+str(z) + ' -' + str(a) + ' ' + str(0) + '\n'
                        else:
                            _maximo_um_pl = _maximo_um_pl + '-'+str(z) + ' -' + str(a) + ' ' + str(0)+ '\n'

            _ao_menos_um_pl = _ao_menos_um_pl + str(0) + '\n'
    
    return _ao_menos_um_pl,_maximo_um_pl
                    

#regra para ter um por coluna (UTILIZA UM POR LINHA)
def um_por_coluna(tabela):
    conj = inicialiando_conj(N)
    for x in tabela:
        for y in range(len(x)):
            conj[y % N].append(x[y])
    
    _ao_menos_um_pl,_maximo_um_pl = um_por_linha(conj)

    return _ao_menos_um_pl,_maximo_um_pl

    

# a = teste(tabela)
# Um_pc , um_pc2 = um_por_linha(a)

#Construindo a tabela
tabela = construir_tabela(N)

#Regra 1 e 2 : Um por posicao
#1 Pelo menos um por posicao
#2 No maximo Um por posicao
# verifica o tempo de resposta da função
ini = time.time()
regra_1, regra_2 = um_por_posicao(tabela)
fim = time.time()
t_1_2 = fim-ini
#print(regra_1)
#print(regra_2)

#Regra 3 e 4 : Um por linha
#3 Pelo menos um por linha(um mesmo elemento)
#4 No maximo um por linha(um mesmo elemento)
# verifica o tempo de resposta da função
ini = time.time()
regra_3, regra_4 = um_por_linha(tabela)
fim = time.time()
t_3_4 = fim-ini
# print(regra_3)
# print(regra_4)

#Regra 5 e 6 : Um por Coluna
#5 Pelo menos um por Coluna(um mesmo elemento)
#6 No maximo um por Coluna(um mesmo elemento)
# verifica o tempo de resposta da função
ini = time.time()
regra_5, regra_6 = um_por_coluna(tabela)
fim = time.time()
t_5_6 = fim-ini
# print(regra_5)
# print(regra_6)


clausulas_final = regra_1 + regra_2 + regra_3 + regra_4 + regra_5 + regra_6[:len(regra_6)-1]

print(clausulas_final)
# print(len(clausulas_final))
print ("Regra 1-2: ",t_1_2,"Regra 3-4: ",t_3_4,"Regra 5-6: ",t_5_6)

