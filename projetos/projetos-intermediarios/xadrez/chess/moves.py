import sys
import board

# CORES
branco = '\033[1;49;97m'
preto = '\033[1;30m'
vermelho = '\033[1;49;31m'
azul = '\033[0;49;94m'
stop = '\033[m'
roquepequenobranco = roquegrandebranco = roquepequenopreto = roquegrandepreto = 0

# ESSA FUNÇÃO VERIFICA SE A COR BRANCA OU PRETA PODE FAZER O ROQUE GRANDE OU PEQUENO
def casasroque(cor, roque):
    if cor == 'branca' and roque == 'roquepequeno':
        if board.tabuleiro['E1'] == f'{board.branco}R{board.stop}' and \
           board.tabuleiro['H1'] == f'{board.branco}T{board.stop}' and \
           board.tabuleiro['F1'] == '.' and \
           board.tabuleiro['G1'] == '.' and \
           roquepequenobranco == 0:
            return True
    elif cor == 'branca' and roque == 'roquegrande':
        if board.tabuleiro['E1'] == f'{board.branco}R{board.stop}' and \
            board.tabuleiro['A1'] == f'{board.branco}T{board.stop}' and \
            board.tabuleiro['D1'] == '.' and \
            board.tabuleiro['C1'] == '.' and \
            board.tabuleiro['B1'] == '.' and \
            roquegrandebranco == 0:
            return True
    else:
        if cor == 'preto' and roque == 'roquepequeno':
            if board.tabuleiro['E8'] == f'{board.preto}R{board.stop}' and \
               board.tabuleiro['H8'] == f'{board.preto}T{board.stop}' and \
               board.tabuleiro['F8'] == '.' and \
               board.tabuleiro['G8'] == '.' and \
               roquepequenopreto == 0:
                return True
        elif cor == 'preto' and roque == 'roquegrande':
            if board.tabuleiro['E8'] == f'{board.branco}R{board.stop}' and \
               board.tabuleiro['A8'] == f'{board.branco}T{board.stop}' and \
               board.tabuleiro['D8'] == '.' and \
               board.tabuleiro['C8'] == '.' and \
               board.tabuleiro['B8'] == '.' and \
               roquegrandepreto == 0:
                return True

# CASO A FUNÇÃO ANTERIOR RETORNE VERDADEIRO, ENTÃO É FEITO O ROQUE PEQUENO, MEDIANTE A INDICAÇÃO DA COR.
def roquepequeno(cor):
    global roquepequenobranco
    global roquepequenopreto
    if cor == 'branco':
        if casasroque('branca', 'roquepequeno'):
            temp1 = board.tabuleiro['G1']
            temp2 = board.tabuleiro['F1']
            board.tabuleiro['G1'] = board.tabuleiro['E1']
            board.tabuleiro['E1'] = temp1
            board.tabuleiro['F1'] = board.tabuleiro['H1']
            board.tabuleiro['H1'] = temp2
            roquepequenobranco += 1
    else:
        if casasroque('preto', 'roquepequeno'):
            temp1 = board.tabuleiro['G8']
            temp2 = board.tabuleiro['F8']
            board.tabuleiro['G8'] = board.tabuleiro['E8']
            board.tabuleiro['E8'] = temp1
            board.tabuleiro['F8'] = board.tabuleiro['H8']
            board.tabuleiro['H8'] = temp2
            roquepequenopreto += 1

# CASO A FUNÇÃO casasroque() RETORNE VERDADEIRO, ENTÃO É FEITO O ROQUE GRANDE, MEDIANTE A INDICAÇÃO DA COR.
def roquegrande(cor):
    global roquegrandebranco
    global roquegrandepreto
    if cor == 'branco':
        if casasroque('branca', 'roquegrande'):
            temp1 = board.tabuleiro['C1']
            temp2 = board.tabuleiro['D1']
            board.tabuleiro['C1'] = board.tabuleiro['E1']
            board.tabuleiro['E1'] = temp1
            board.tabuleiro['D1'] = board.tabuleiro['A1']
            board.tabuleiro['A1'] = temp2
            roquegrandebranco += 1
    else:
        if casasroque('preto', 'roquegrande'):
            temp1 = board.tabuleiro['D8']
            temp2 = board.tabuleiro['C8']
            board.tabuleiro['C8'] = board.tabuleiro['E8']
            board.tabuleiro['E8'] = temp2
            board.tabuleiro['D8'] = board.tabuleiro['A8']
            board.tabuleiro['A8'] = temp1
            roquegrandepreto += 1

# FUNÇÃO RESPONSÁVEL PELA CAPTURA DE PEÇAS
def captura(cf, ci):
    board.tabuleiro[cf] = board.tabuleiro[ci]
    board.tabuleiro[ci] = '.'


# FUNÇÃO RESPONSÁVEL PELO MOVIMENTO DAS PEÇAS NO TABULEIRO, QUANDO A CASA FINAL NÃO ATINGE NENHUMA PEÇA ADVERSÁRIA
def movimento(cf, ci):
    temp = board.tabuleiro[cf]
    board.tabuleiro[cf] = board.tabuleiro[ci]
    board.tabuleiro[ci] = temp

# DICIONÁRIO CRIADO PARA A FACILITAÇÃO NA VERIFICAÇÃO DO LANCE "EN PASSANT"
casas = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}


# FUNÇÃO RESPONSÁVEL PELA VERIFICAÇÃO DE SE O JOGADOR NA SUA JOGADA FEZ UM LANCE "EN PASSANT" OU NÃO.
def verificacaoenpassant(cf, ci):
    if abs(casas[cf[0]] - casas[ci[0]]) == 1 and abs(int(cf[1]) - int(ci[1])) == 1 and board.tabuleiro[cf] == '.' and (board.tabuleiro[ci] == f'{branco}P{stop}' or board.tabuleiro[ci] == f'{preto}P{stop}'):
        return True
    else:
        return False


# FUNÇÃO RESPONSÁVEL PELA ANÁLISE DO TABULEIRO PARA O LANCE "EN PASSANT"
def enpassant(cor, cibranco, cfbranco, cipreto, cfpreto):
    if cor == 'branco':
        # VERIFICA SE O LANCE ANTERIOR DO ADVERSÁRIO AO "EN PASSANT" DO JOGADOR CUMPRE AS REGRAS DO XADREZ
        if cipreto[0] == cfpreto[0] and abs(int(cfpreto[1]) - int(cipreto[1])) == 2 and abs(casas[f'{cibranco[0]}'] - casas[f'{cfpreto[0]}']) == 1 and cibranco[1] == cfpreto[1]:
            return True
        else:
            return False
    else:
        if cibranco[0] == cfbranco[0] and abs(int(cfbranco[1]) - int(cibranco[1])) == 2 and abs(casas[f'{cfbranco[0]}'] - casas[f'{cipreto[0]}']) == 1 and cfbranco[1] == cipreto[1]:
            return True
        else:
            return False


# FUNÇÃO RESPONSÁVEL PELA CAPTURA "EN PASSANT"
def capturaenpassant(cf, ci, cor):
    if cor == 'branco':
        # ESSA VARIÁVEL ABAIXO PEGA A COLUNA DA CASA FINAL E CONCATENA COM A LINHA DA CASA INICIAL
        peaopretocapturado = cf[0] + ci[1]
        board.tabuleiro[cf] = board.tabuleiro[ci]
        board.tabuleiro[f'{peaopretocapturado}'] = '.'
        board.tabuleiro[ci] = '.'
    else:
        # ESSA VARIÁVEL ABAIXO PEGA A COLUNA DA CASA FINAL E CONCATENA COM A LINHA DA CASA INICIAL
        peaobrancocapturado = cf[0] + ci[1]
        board.tabuleiro[cf] = board.tabuleiro[ci]
        board.tabuleiro[f'{peaobrancocapturado}'] = '.'
        board.tabuleiro[ci] = '.'


# FUNÇÃO CRIADA PARA FACILITAR O TRATAMENTO DE ERROS NO CÓDIGO, E PARA DEIXÁ-LO MAIS LIMPO
def tratamento_de_erros(argumento):
    casai = ''
    casaf = ''
    if argumento == 'casai':
        while True:
            try:
                while casai not in board.tabuleiro.keys():
                    casai = str(input('Qual casa você quer mover? ')).upper()
                    if casai == 'ROQUE PEQUENO' and casasroque('branca', 'roquepequeno') is True:
                        break
                    elif casai == 'ROQUE GRANDE' and casasroque('branca', 'roquegrande') is True:
                        break
                    elif casai == 'ROQUE PEQUENO' and casasroque('preto', 'roquepequeno') is True:
                        break
                    elif casai == 'ROQUE GRANDE' and casasroque('preto', 'roquegrande') is True:
                        break
            except (ValueError, TypeError):
                print('Você digitou alguma coisa errada!')
                continue
            except KeyboardInterrupt:
                print(f'\n{vermelho}O JOGO FOI FINALIZADO.{stop}')
                sys.exit()
            else:
                return casai
    else:
        while True:
            try:
                while casaf not in board.tabuleiro.keys():
                    casaf = str(input('Para onde você quer movê-la? ')).upper()
            except (ValueError, TypeError):
                print('Você digitou alguma coisa errada!')
            except KeyboardInterrupt:
                print(f'\n{vermelho}O JOGO FOI FINALIZADO.{stop}')
                sys.exit()
            else:
                return casaf

