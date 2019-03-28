import sys
print(sys.argv[1])
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
    _clausulas = ""
    __clausulas = ""
    for x in tabela:
        for y in x:
            for z in y:
                __clausulas = __clausulas +str(z) + ' '
                for a in y:
                    if z != a:
                        _clausulas = _clausulas + '-'+str(z)+' -'+str(a)+' '+str(0)+'\n'
            __clausulas = __clausulas + str(0) + '\n'
    return _clausulas,__clausulas

#inicializando conjunto com n conjuntos vazios
def inicialiando_conj(N):
    conj = []
    for x in range(N):
        conj.append([])
    return conj
    
    


#regra para ter um por linha
def um_por_linha(tabela):
    _clausulas = ""
    __clausulas = ""
    tam_linha =  N*N
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
                __clausulas = __clausulas +str(z) + ' '
                for a in y:
                    if a != z:
                        if a == y[len(y)-1] and y == x[len(x)-1]:
                            _clausulas = _clausulas + '-'+str(z) + ' -' + str(a) + ' ' + str(0) + '\n'
                        else:
                            _clausulas = _clausulas + '-'+str(z) + ' -' + str(a) + ' ' + str(0)+ '\n'

            __clausulas = __clausulas + str(0) + '\n'
    
    return _clausulas,__clausulas
                    

#regra para ter um por coluna
def um_por_coluna(tabela):
    _clausulas = ""
    __clausulas = ""
    _tabela = []
    for x in tabela:
        _tabela.append([])
    for x in tabela:
        for y in range(len(x)):
            _tabela[y].append(x[y])
    
    _conj = []
    conj =  inicialiando_conj(N)
    
    for x in tabela:
        for y in range(len(x)):
            conj[y].append(x[y])
        
    print(conj)
    for x in _conj:
        for y in x:
            for z in y:
                __clausulas = __clausulas +str(z) + ' '
                for a in y:
                    if a != z:
                        _clausulas = _clausulas + '-'+str(z) + ' -' + str(a) + ' ' + str(0)+ '\n'
            __clausulas = __clausulas + str(0) + '\n'
    
    return _clausulas,__clausulas
def teste(tabela):
    conj = inicialiando_conj(N)
    for x in tabela:
        for y in range(len(x)):
            conj[y % N].append(x[y])

    return conj




tabela = construir_tabela(N)
print("UM POR POSICAO+++++==================")
clausulas,clausulas2 = um_por_posicao(tabela)
print("C1========+++++")
print(clausulas2)
print("C2==============+++++++")
print(clausulas)
print("+==================+")
Um_pl,um_pl2 = um_por_linha(tabela)
#print(tabela)

a = teste(tabela)
Um_pc , um_pc2 = um_por_linha(a)

print("UM POR COLUNA+++++==================")
print("C1========+++++")
print(Um_pc)
print("C2========+++++")
print(um_pc2)
print("+==================+")

print("UM POR LINHA+++++==================")
print("C1========+++++")
print(Um_pl)
print("C2========+++++")
print(um_pl2)
print("+==================+")

clausulas_final = Um_pc + um_pc2 + Um_pl + um_pl2 + clausulas + clausulas2[:len(clausulas2)-1]

print(clausulas_final)