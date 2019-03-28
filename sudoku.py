N = 2
len_table = N**3
clausulas = ""

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


def mostrar_tabela(tabela):
    for x in tabela:
        print(x)

def mostrar_tabela2(tabela):
    for x in tabela:
        for y in x:
            print(y)

def apenas_um_na_linha_e_coluna(i,n,Tabela):
    aux = i
    elementos_que_tem_que_estar_negados = []
    count = 0
    if i > n:
        count = i - n
        while(i > n and i > 0):
            i = count
            elementos_que_tem_que_estar_negados.append(i)
            count = i - n
        i = aux
        if i < (len_table - 3):
            count = i + n
            while(i < len_table ):
                i = count
                elementos_que_tem_que_estar_negados.append(i)
                count = i + n
        i = aux


    elif i <= n:
        count = i + n
        while(i < len_table ):
            i = count
            elementos_que_tem_que_estar_negados.append(i)
            count = i + n
        i = aux

    return elementos_que_tem_que_estar_negados            

def regra_um(tabela):
    variaveis = []
    for x in tabela:
        i = 0
        while(i < 3):
            variaveis.append(x[i])
            i = i + 1


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

tabela = construir_tabela(N)
#mostrar_tabela2(tabela)
# negados = apenas_um_na_linha_e_coluna(15,N,tabela)
# for x in negados:
#     print(x)
#clausulas,clausulas2 = um_por_posicao(tabela)
#print(clausulas2)
#print(clausulas)
Um_pl,um_pl2 = um_por_linha(tabela)
#Um_pc, Um_pc2 = um_por_coluna(tabela)
# print(Um_pc)
# print(Um_pc2)
# print(Um_pl)
# print(um_pl2)
#print(tabela)

def teste(tabela):
    conj = inicialiando_conj(N)
    for x in tabela:
        for y in range(len(x)):
            conj[y % N].append(x[y])

    return conj

# for x in range(N):
#     for y in range(N):
#         for z in range(N):
#             print(tabela[x][y][z])
#print(tabela[0][0][0])

a = teste(tabela)
Um_pc , um_pc2 = um_por_linha(a)
print(Um_pc)
print(um_pc2)
print(Um_pl,um_pl2,Um_pc,um_pc2)