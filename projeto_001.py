from random import choice

def inicia_jogo():
    print(ESPACO_INICIO_JOGO)
    print(" " *14 + "BATALHA NAVAL")
    print(ESPACO_INICIO_JOGO + "\n")


def cria_tabuleiro(matriz):
    

    for i in range(len(matriz)):
        for j in range(0, len(matriz[i]), 4):
            matriz[i][j] = "|"
        for h in range(len(matriz[i])):
            if matriz[i][h] != "|":
                matriz[i][h] = " "
        
    return matriz


def mostra_tabuleiro(tabuleiro, alfabeto, numeros):
    for a in range(len(numeros)):
        if a == 0:
            print(" ", end="")
            '''
            Coloquei um espaço para os números ficarem organizados com o tabuleiro
            '''
        print(f"   {numeros[a]}", end="")
    print()
    print(HIFEN_MOSTRA_TABULEIRO, end="")
    print()
    for i in range(len(tabuleiro)):
        print(alfabeto[i] + " ", end="")
        for j in range(len(tabuleiro[i])):
            print(tabuleiro[i][j], end="")
        print()
        print(HIFEN_MOSTRA_TABULEIRO)
    print()
        

def escolhendo_posicao_pc(tabuleiro, lista):
 
    par_posicao = choice(lista)
    a = par_posicao[0]
    b = par_posicao[1]
    tabuleiro[a][b] = "~"
    
    return tabuleiro

def monta_lista_posicao_tab_pc():

    lista1 = []
    lista2 = []
    for i in range(10):
        for j in range(2, 40, 4):
            lista1.append(i)
            lista1.append(j)
            lista2.append(lista1[:])
            lista1.clear()

    return lista2


def escolhendo_posicao_tab_inv_pc(lista_posicoes):

    posicao = choice(lista_posicoes)
    lin = posicao[0]
    col = posicao[1]

    return lin, col


def percorre_matriz(tabuleiro, tamanho_embarcacao, lin, col, escolha1, escolha2):

    if escolha1 == "horizontal":
        if escolha2 == "frente":
            if lin == 0:
                for i in range(len(tabuleiro)):
                    for j in range(2, 40, 4):
                        if i == 0 and j == col:
                            for c in range(j, 40, 4):
                                verifica = tabuleiro[i][c]
                                if verifica == " ":
                                    cont = c #acho que tenho que tirar 2, ou seja, cont = cont - 2 na em: if cont >= num:
    cont = (cont - col)/4
    print(cont)
    if cont >= tamanho_embarcacao - 1:
        return "sim"
    else:
        return "não"


def coloca_embarcacao(embarcacao, tabuleiro, lin, col, escolha1, escolha2):

    if escolha1 == "horizontal":
        if escolha2 == "frente":

            for i in range(1):
                for j in range(len(embarcacao)):
                    tabuleiro[lin][col] = embarcacao[j]
                    col += 4
    
    return tabuleiro
            

def espalha_embarcacoes_porta_avioes(tabuleiro, lista_posicoes):

    porta_avioes = ["X", "X", "X", "X", "X"]
    tamanho = 5
    ver_hor = ["horizontal", "vertical"]
    orientacao = ["frente", "tras"]
    

    #lin, col = escolhendo_posicao_tab_inv_pc(lista_posicoes)
    lin = 0
    col = 22
    """escolha1 = choice(ver_hor)
    escolha2 = choice(orientacao)"""
    escolha1 = "horizontal"
    escolha2 = "frente"
    
    resultado = percorre_matriz(tabuleiro, tamanho, lin, col, escolha1, escolha2)
    if resultado == "sim":
        tabuleiro = coloca_embarcacao(porta_avioes, tabuleiro, lin, col, escolha1, escolha2)

    return tabuleiro


ESPACO_INICIO_JOGO = "-" *43
HIFEN_MOSTRA_TABULEIRO = "  " + "-" *41


matriz = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

matriz_pc = matriz[:]
matriz_invisivel_pc = matriz[:]
matriz_jogador = matriz[:]

alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_pos1_coluna_pc = []
lista_pos2_linha_pc = []

# Esse tabuleiro não tem relação com os outros, é apenas para mostrar ao jogador como ele é
inicia_jogo()
tabuleiro = cria_tabuleiro(matriz)
mostra_tabuleiro(tabuleiro, alfabeto, numeros)

# Distribuição das embarcações do PC
tabuleiro_invisivel_pc = cria_tabuleiro(matriz_invisivel_pc)
lista_posicoes_para_tab_inv = monta_lista_posicao_tab_pc()

tabuleiro_invisivel_pc = espalha_embarcacoes_porta_avioes(tabuleiro_invisivel_pc, lista_posicoes_para_tab_inv)
mostra_tabuleiro(tabuleiro_invisivel_pc, alfabeto, numeros)

"""
# O PC vai fazer as escolhas das posições para tentar achar as embarcações do adversário
tabuleiro_pc = cria_tabuleiro(matriz_pc)
lista_posicoes = monta_lista_posicao_tab_pc()
tabuleiro_jogadas_pc = escolhendo_posicao_pc(tabuleiro_pc, lista_posicoes)
print(mostra_tabuleiro(tabuleiro_jogadas_pc, alfabeto, numeros))
"""

"""navios_tanque = ["x", "x", "x", "x"]
contratorpedeiro = ["x", "x", "x"]
submarino = ["x", "x"]"""