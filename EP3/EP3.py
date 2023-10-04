"""
  AO PREENCHER ESSE CABEÇALHO COM O MEU NOME E O MEU NÚMERO USP, 
  DECLARO QUE SOU O ÚNICO AUTOR E RESPONSÁVEL POR ESSE PROGRAMA. 
  TODAS AS PARTES ORIGINAIS DESSE EXERCÍCIO PROGRAMA (EP) FORAM 
  DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUÇÕES
  DESSE EP E QUE PORTANTO NÃO CONSTITUEM DESONESTIDADE ACADÊMICA
  OU PLÁGIO.  
  DECLARO TAMBÉM QUE SOU RESPONSÁVEL POR TODAS AS CÓPIAS
  DESSE PROGRAMA E QUE EU NÃO DISTRIBUI OU FACILITEI A
  SUA DISTRIBUIÇÃO. ESTOU CIENTE QUE OS CASOS DE PLÁGIO E
  DESONESTIDADE ACADÊMICA SERÃO TRATADOS SEGUNDO OS CRITÉRIOS
  DIVULGADOS NA PÁGINA DA DISCIPLINA.
  ENTENDO QUE EPS SEM ASSINATURA NÃO SERÃO CORRIGIDOS E,
  AINDA ASSIM, PODERÃO SER PUNIDOS POR DESONESTIDADE ACADÊMICA.

  Nome : Fernando Campos Chaim
  NUSP : 11200608
  Turma: 08
  Prof.: Paulo Andre Vechiatto Miranda

  Referências: Com exceção das rotinas fornecidas no enunciado
  e em sala de aula, caso você tenha utilizado alguma refência,
  liste-as abaixo para que o seu programa não seja considerado
  plágio ou irregular.
  
  Exemplo:
  - O algoritmo Quicksort foi baseado em
  http://wiki.python.org.br/QuickSort
"""
import math

def SIR (N, Beta, Gama, Tmax) :
    Ls = []
    Lr = []
    Li = []
    S = float(N - 1)
    Ls.append(S)
    I = float(1)
    Li.append(I)
    R = float(0)
    Lr.append(R)
    for j in range (1,Tmax):
        Sant = float(S)
        Iant = float(I)
        Rant = float(R)
        S = float(Sant-Beta*((Sant*Iant)/N))
        Ls.append(S)
        I = float(Iant*(1-Gama+((Beta*Sant)/N)))
        Li.append(I)
        R = float(Rant + (Iant*Gama))
        Lr.append(R)
    return Ls,Li,Lr

def critic_SIR (N, Gama, Tmax, Beta_MIN, Beta_MAX, Beta_delta):
    Limax = []
    beta = Beta_MIN
    while beta <= Beta_MAX:
        s,i,l = SIR(N, beta, Gama, Tmax)
        imax = i[0]
        for j in range(1,len(i)):
            if i[j] > imax :
                imax = i[j]
        Limax.append(imax)
        beta += Beta_delta
    return Limax

def gera_grafico_simples(L):
    Y_min = 0
    L_max = L[0]
    for i in range(1,len(L)) :
        if L[i] > L_max :
            L_max = L[i]
    if L_max != int(L_max):
        Y_max = round(L_max+0.5)
    else:
        Y_max = int(L_max)
    m = Y_max - Y_min + 1
    n = len(L)
    M = cria_matriz(m,n,0)
    for k in range(len(L)):
        g = round(Y_max-L[k])
        M[g][k] = 255
    arquivo = open("graf_simples4.pgm","w")
    arquivo.write("P2\n")
    arquivo.write("%d %d\n"%(n,m))
    arquivo.write("255\n")
    for p in range(m):
        for o in range(n):
            arquivo.write("%4d"%(M[p][o]))
        arquivo.write("\n")
    arquivo.close()
    return M

def gera_grafico_composto(S, I, R):
    Y_max = R[0]
    for i in range(1,len(R)):
        if Y_max < R[i]:
            Y_max = R[i]
    for w in range(len(I)):
        if Y_max < I[w]:
            Y_max = I[w]
    for z in range(len(S)):
        if Y_max < S[z]:
            Y_max = S[z]
    if Y_max != int(Y_max):
        Y_max = round(Y_max + 0.5)
    else:
        Y_max = int(Y_max)
    m = Y_max + 1
    n = len(S)
    M = cria_matriz(m,3*n,0)
    for k in range(len(S)):
            g = round(Y_max-S[k])
            print(g)
            M[g][(k*3)+0] = 255
    for h in range (len(I)):
            u = round(Y_max-I[h])
            M[u][(h*3)+1] = 255
    for q in range (len(R)):
            t = round(Y_max-R[q])
            M[t][(q*3)+2] = 255
    arquivo = open("graf_composto.ppm","w")
    arquivo.write("P3\n")
    arquivo.write("%d %d\n"%(n,m))
    arquivo.write("255\n")
    for p in range(m):
        for o in range(3*n):
            arquivo.write("%4d"%(M[p][o]))
        arquivo.write("\n")
    arquivo.close()
    return M

def leitura_de_valores(nome_de_arquivo):
    arquivo = open(nome_de_arquivo, "r")
    x = arquivo.readlines()
    for i in range(len(x)):
        x[i] = float(x[i].strip())
        if x[i] == int(x[i]):
            x[i] = int(x[i])
    arquivo.close()
    return x[0], x[1], x[2], x[3], x[4], x[5]

#Bloco de funções auxiliares:
def cria_matriz(m,n,valor): 
    #cria uma matriz com m linhas e n colunas com um número especificado
    M = []
    for i in range(m):
        linha = []
        for j in range(n):
            linha.append(valor)
        M.append(linha)
    return M

# Opções
# 1: Calcular 'SIR' e imprimir os vetores S, I e R - leitura de teclado
# 2: Calcular 'critic_SIR' e imprimir o vetor c_SIR - leitura de teclado
# 3: Calcular 'critic_SIR' e imprimir o vetor c_SIR - leitura de arquivo
# 4: Calcular 'critic_SIR', testar matriz devolvida por 'gera_grafico_simples' - leitura de teclado
# 5: Calcular 'critic_SIR', testar arquivo PGM no disco por 'gera_grafico_simples' - leitura de teclado
# 6: Calcular 'SIR', testar matriz devolvida por 'gera_grafico_composto' - leitura de teclado
# 7: Calcular 'SIR', testar arquivo PPM no disco por 'gera_grafico_composto' - leitura de teclado

#Não altere as funções abaixo:
def imprimeLista(L) : 
    for i in range(len(L)):
      print("%.4f " % L[i], end=""); # usar apenas 4 digitos apos ponto
    print()

def main():
    Opt = int(input("Digite modo do programa: "))
    if (Opt == 1): # saida - SIR; entrada - teclado
        N = int(input("Digite N: ")) 
        Beta = float(input("Digite Beta: "))
        Gama = float(input("Digite Gama: "))
        Tmax = int(input("Digite Tmax: ")) 
        S,I,R = SIR(N, Beta, Gama, Tmax)
        print("S = ", end="")
        imprimeLista(S) 
        print("I = ", end="")
        imprimeLista(I)
        print("R = ", end="")
        imprimeLista(R)
    elif (Opt == 2): # saida - critic_SIR; entrada - teclado
        N = int(input("Digite N: "))
        Gama = float(input("Digite Gama: "))
        Tmax = int(input("Digite Tmax: "))
        Beta_MIN = float(input("Digite Beta_MIN: ")) 
        Beta_MAX = float(input("Digite Beta_MAX: "))
        Beta_delta = float(input("Digite Beta_delta: "))
        c_SIR = critic_SIR(N, Gama, Tmax, Beta_MIN, Beta_MAX, Beta_delta)
        imprimeLista(c_SIR)
    elif (Opt == 3): # saida - critic_SIR; entrada - arquivo
        Dados = input("Digite nome do arquivo: "); 
        N, Gama, Tmax, Beta_MIN, Beta_MAX, Beta_delta = leitura_de_valores(Dados)
        c_SIR = critic_SIR(N, Gama, Tmax, Beta_MIN, Beta_MAX, Beta_delta)
        imprimeLista(c_SIR)
    elif (Opt == 4): # grafico simples - critic_SIR; entrada - teclado
        N = int(input("Digite N: "))
        Gama = float(input("Digite Gama: "))
        Tmax = int(input("Digite Tmax: "))
        Beta_MIN = float(input("Digite Beta_MIN: ")) 
        Beta_MAX = float(input("Digite Beta_MAX: "))
        Beta_delta = float(input("Digite Beta_delta: "))
        c_SIR = critic_SIR(N, Gama, Tmax, Beta_MIN, Beta_MAX, Beta_delta)
        M_grafico = gera_grafico_simples(c_SIR)
        print(M_grafico)
    elif (Opt == 5): # PGM - grafico simples - critic_SIR; entrada - teclado
        N = int(input("Digite N: "))
        Gama = float(input("Digite Gama: "))
        Tmax = int(input("Digite Tmax: "))
        Beta_MIN = float(input("Digite Beta_MIN: ")) 
        Beta_MAX = float(input("Digite Beta_MAX: "))
        Beta_delta = float(input("Digite Beta_delta: "))
        c_SIR = critic_SIR(N, Gama, Tmax, Beta_MIN, Beta_MAX, Beta_delta)
        M_grafico = gera_grafico_simples(c_SIR)
        g = open("graf_simples4.pgm", "r")
        print(g.read())
        g.close()
    elif (Opt == 6): # grafico composto - SIR; entrada - teclado
        N = int(input("Digite N: ")) 
        Beta = float(input("Digite Beta: "))
        Gama = float(input("Digite Gama: "))
        Tmax = int(input("Digite Tmax: ")) 
        S,I,R = SIR(N, Beta, Gama, Tmax)
        M_grafico = gera_grafico_composto(S, I, R)
        print(M_grafico)
    elif (Opt == 7): # PPM - grafico composto - SIR; entrada - teclado
        N = int(input("Digite N: ")) 
        Beta = float(input("Digite Beta: "))
        Gama = float(input("Digite Gama: "))
        Tmax = int(input("Digite Tmax: ")) 
        S,I,R = SIR(N, Beta, Gama, Tmax)
        M_grafico = gera_grafico_composto(S, I, R)
        g = open("graf_composto.ppm", "r")
        print(g.read())
        g.close()

main()
