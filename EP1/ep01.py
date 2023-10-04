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
  Turma: 8 
  Prof.: Paulo Andre Vechiatto de Miranda

  Referências: Com exceção das rotinas fornecidas no enunciado
  e em sala de aula, caso você tenha utilizado alguma refência,
  liste-as abaixo para que o seu programa não seja considerado
  plágio ou irregular.
  
  Exemplo:
  - O algoritmo Quicksort foi baseado em
  http://www.ime.usp.br/~pf/algoritmos/aulas/quick.html
"""

# ======================================================================
#
#   M A I N 
#
# ======================================================================

def main():
    modo = int(input("modo: "))
    if modo == 1:
        n1 = int(input("n1: "))
        n2 = int(input("n2: "))
        n3 = int(input("n3: "))
        n4 = int(input("n4: "))
        n = int(input("n: "))
        if n1*n1+n2*n2+n3*n3+n4*n4 == n:
            print ("verdadeiro")
        else: 
            print ("falso")
    elif modo == 2:
        n = int(input("n: "))
        p = 0
        p1 = 2
        p2 = 3
        p3 = 5
        p4 = 7
        soma = p1*p1 + p2*p2 + p3*p3 + p4*p4
        while soma < n:
            p1 = p2
            p2 = p3
            p3 = p4
            p = p3 + 1
            achou = False
            d = 2 
            while achou == False: 
                if ((p % d == 0) and (p != d)) :
                    p += 1
                    d = 2
                elif d % p != 0:
                    d += 1
                else:
                    achou = True 
                    p4 = p
                    soma = p1*p1 + p2*p2 + p3*p3 + p4*p4
            if soma == n :
                print(p1, p2, p3, p4)
            else:
                print("falso")
main()