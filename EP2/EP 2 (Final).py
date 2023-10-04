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
  http://www.ime.usp.br/~pf/algoritmos/aulas/quick.html
"""
# ======================================================================
# FUNÇÕES OBRIGATÓRIAS
# Implemente  neste bloco as funções obrigatórias do EP2.
# NÃO modifique os nomes e parâmetros dessas funções.
# ======================================================================
def polinomioComRaiz(p,b):
    """Devolve True se b é raiz do polinômio representado pela lista p, 
       ou False no caso contrário.
       
       p -- a lista dos coeficientes do polinômio       
       b -- o número a ser testado como raiz
    """
    
    # Escreva aqui o corpo da função
    #Este código foi feito baseado no Algorítimo (Teorema) de Briot-Ruffini
    m = []
    o = p + []
    o.reverse()
    m.append(o[0])
    z = o[0]
    i = 0
    while i < len(o) - 1 :
        z = (m[i] * b) + o[i + 1]
        m.append(z)
        i += 1
    if m[len(m) - 1] == 0:
        return True
    else:
        return False
# ======================================================================

def polinomioQuociente(p,b):
    """Devolve a lista que representa o polinômio quociente da divisão
       p(x)/(x-b), onde p(x) é o polinômio cujos coeficientes estão na 
       lista p e b é uma raiz de p(x). 
       
       p -- a lista dos coeficientes do polinômio a ser dividido      
       b -- a raiz a ser usada como divisor
    """
    
    # Escreva aqui o corpo da função
    #Este código foi feito baseado no Algorítimo (Teorema) de Briot-Ruffini
    m = []
    o = p + []
    o.reverse()
    m.append(o[0])
    z = o[0]
    i = 0
    while i < len(o) - 2 :
        z = (m[i] * b) + o[i + 1]
        m.append(z)
        i += 1
    m.reverse()
    return m
# ======================================================================
def listaCanonicaDeRaizes(p):
    """Devolve a lista canônica de raízes inteiras do polinômio 
       representado pela lista p.
       
       p -- a lista dos coeficientes do polinômios
    """
    
    # Escreva aqui o corpo da função
    i = 0
    m = []
    o = p
    while len (o) > 1:
        if abs(o[0]) >= i or o[0] == 0 :
            if polinomioComRaiz(o,-i) == True:
                m.append(-i)
                o = polinomioQuociente(o,-i)
                i = 0
            elif polinomioComRaiz(o,i) == True:
                m.append(i)
                o = polinomioQuociente(o,i)
                i = 0
            else:
                i += 1
        else:
            return (m)
    return m
# ======================================================================
def polinomioQuocienteRacional(p,b,a):
    """Devolve a lista que representa o polinômio quociente da divisão
       p(x)/(ax-b) e o resto dessa divisão, onde p(x) é o polinômio 
       cujos coeficientes estão na lista p e b/a é uma raiz de p(x). 
       
       p -- a lista dos coeficientes do polinômio a ser dividido
       b -- numerador da raiz a ser usada como divisor
       a -- denominador da raiz a ser usada como divisor
    """
    
    # Escreva aqui o corpo da função
    #Este código foi feito baseado no Algorítimo (Teorema) de Briot-Ruffini
    m = []
    u = []
    o = p + []
    o.reverse()
    m.append(o[0])
    z = o[0]
    i = 0
    if len(o) > 1:
        while i < len(o) - 1 :
            z = (m[i] * b/a) + o[i + 1]
            m.append(z)
            i += 1
        m.reverse()
        w = m[0]
        t = m[1:len(m)]
        for v in range (len(t)):
            t[v] = t[v]/a
            u.append(t[v])
        return u,w
    else:
        return None,-1 
# ======================================================================
def listaRaizesRacionais(p):
    """Devolve a lista canônica de raízes racionais do polinômio 
       representado pela lista p.
       
       p -- a lista dos coeficientes do polinômio
    """
    
    # Escreva aqui o corpo da função
    o = p + []
    r = []
    b = 0
    a = 1
    while abs(o[len(o)-1]) >= a :
        while abs(b) <= abs(o[0]):
            k,w = polinomioQuocienteRacional(o,b/a,1)
            j,l = polinomioQuocienteRacional(o,-b/a,1)
            if l == 0 :
                r.append(-b/a)
                o = j
                b = 0
            elif w == 0 :
                r.append(b/a)
                o = k
                b = 0
            else:                
                b += 1
        a += 1
        b = 0
    return r
# ======================================================================
def racionalToString(pn,r):
    """Devolve uma string que apresenta a raiz r do polinômio do qual pn 
       é o coeficiente de maior grau como:
        - um inteiro, caso r seja inteiro
        - na forma b/a, com b e a primos entre si e a > 0, caso contrário

       pn -- coeficiente de maior grau do polinômio
       r -- uma raiz do polinômio
    """
    
    # Escreva aqui o corpo da função
    if r == int(r) :
       r = int(r)
       return str(r)
    else:
        m = ''
        x = round(r*pn)
        u = MDC(abs(pn),abs(x))
        g = str(int(x / u))
        y = str(int(pn / u))
        m += g
        m += '/'
        m += y
        return m
# ======================================================================
# FIM DO BLOCO DE FUNÇÕES OBRIGATÓRIAS
# ======================================================================


# ======================================================================
# FUNÇÕES ADICIONAIS
# Implemente neste bloco as funções adicionais às obrigatórias do EP2.
# Duas funções desse tipo (a polinomioToString e a sig) foram 
# fornecidas no próprio enunciado do EP.
# ======================================================================
def polinomioToString(p):
    """Devolve uma string que representa o polinômio em um formato 
       legível para humanos.
       
       p -- a lista dos coeficientes do polinômio
    """
    n = len(p)-1
    s = ""
    for m in range(n-1):
        if p[n-m] != 0:
            s = "%s%s%dx^%d " % (s, sig(m,p[n-m]), p[n-m], n-m)
    if p[1] != 0:
        s = "%s%s%dx " % (s, sig(n-1,p[1]), p[1])
    if p[0] != 0:
        s = "%s%s%d" % (s, sig(n,p[0]), p[0])
    return s

# ======================================================================
def sig(nTermAnte,coef):
    """Devolve '+' se coef não é negativo e existe termo anterior ao
       termo dele no polinômio. Devolve '' (string vazia) no caso
       contrário. Usado para determinar se o '+' deve aparecer antes
       de coef na string que representa o polinômio.
       
       nTermAnte -- expoente de x no termo anterior ao termo do coef
       coef -- coeficiente de um termo do polinômio 
    """
    if nTermAnte > 0 and coef >= 0:
        return "+"
    else:
        return ""
def MDC (p,o):
    if p < o :
        i = p
        p = o
        o = i 
    while o > 0 :
        l = p % o
        p = o
        o = l
    return p
# ======================================================================
# FIM DO BLOCO DE FUNÇÕES ADICIONAIS
# ======================================================================


# ======================================================================
# FUNÇÃO MAIN 
# Escreva dentro da função main() o código que quiser para testar suas 
# demais funções.
# Somente dentro da função main() você pode usar as funções print e
# input.     
# O código da função main() NÃO será avaliado.
# ======================================================================
def main():
    n = int(input("Digite o grau: "))
    
    # Lê os coeficientes do polinômio
    p = []
    for i in range(n+1):
        p.append(float(input("Digite p["+str(i)+"]: ")))
        i += 1
        
    # Obtém a lista de raízes
    if p[n] == 1:
        raizes = listaCanonicaDeRaizes(p)
        print( 'A lista canonica das raizes inteiras de p(x) =',
               polinomioToString(p), 'eh:')
    else:
        raizes = listaRaizesRacionais(p)
        print( 'A lista canonica das raizes racionais de p(x) =',
               polinomioToString(p), 'eh:')
    
    # Imprime a lista canônica de raízes
    for raiz in raizes:
        s = racionalToString(p[n],raiz)
        print(s, end=" ")
        
    print()
        
                
# ======================================================================
# FIM DA FUNÇÃO MAIN 
# ======================================================================


# ======================================================================
# CHAMADA DA FUNÇÃO MAIN
# NÃO modifique os comandos deste bloco!
# ======================================================================
if __name__ == "__main__":
    main()
# ======================================================================
# FIM DO BLOCO DE CHAMADA DA FUNÇÃO MAIN 
# ======================================================================