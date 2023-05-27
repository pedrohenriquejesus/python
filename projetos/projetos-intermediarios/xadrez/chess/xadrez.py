import board
import moves
# CORES
branco = '\033[1;49;97m'
preto = '\033[1;30m'
vermelho = '\033[1;49;31m'
azul = '\033[0;49;94m'
stop = '\033[m'

print('-'*100)
print(f'{branco}REGRAS{stop}'.center(100))
print('-'*100)
print(f'{branco}1.{stop} Nesta versão do jogo, há disponibilizado os dois tipos de roques e a captura "En Passant".')
print()
print(f'{branco}2.{stop} Para realizar o roque pequeno, basta digitar: "roque pequeno".')
print()
print(f'{branco}3.{stop} Para realizar o roque grande, basta digitar: "roque grande".')
print()
print(f'''{branco}4.{stop} As regras do xadrez vinculadas aos roques e à captura "En Passant" estão presentes nesta versão.
   Qualquer dúvida quanto ao funcionamento do programam quanto a essa duas regras basta consultar a documentação oficial do xadrez.''')
print()
print(f'{branco}5.{stop} Como esta versão não usa Programação Orientada a Objetos, as peças tem movimento livre no tabuleiro e essencialmente são as mesmas coisas, exceto nos casos do roque e da captura "En Passant".')
print()
print(f'{branco}6.{stop} Divirta-se!')

print('-'*100)
print(f'{branco}XADREZ{stop}'.center(100))
print('-'*100)

board.tab()

while True:
    while True:
        print(f'{branco}JOGADA DAS BRANCAS{stop}')

        casainicial = moves.tratamento_de_erros('casai')

        if casainicial == 'ROQUE PEQUENO':
            moves.roquepequeno('branco')
            board.tab()
            break
        if casainicial == 'ROQUE GRANDE':
            moves.roquegrande('branco')
            board.tab()
            break

        casafinal = moves.tratamento_de_erros('casaf')

        # ESTE DICIONÁRIO SERVE PARA ARMAZENAR O ÚLTIMO LANCE FEITO PELAS BRANCAS
        # QUE SERVE PARA UMA VERIFICAÇÃO QUE ANALISA SE É POSSÍVEL FAZER O LANCE "EN PASSANT"
        casasbranco = {'casainicial': casainicial, 'casafinal': casafinal}

        if moves.verificacaoenpassant(casafinal, casainicial) is True:
            if moves.enpassant('branco', casainicial, casafinal, casaspreto['casainicial'], casaspreto['casafinal']) is True:
                moves.capturaenpassant(casafinal, casainicial, 'branco')
                board.tab()
                break
            else:
                print(f'{vermelho}JOGADA INVÁLIDA!{stop}'.center(60))
                board.tab()
                continue
        # AQUI VERIFICA-SE SE A CASA DE DESTINO TEM UMA PEÇA OU NÃO,
        else:
            # SE TIVER, ELE CAPTURA.
            if board.tabuleiro[casafinal] not in '.':
                moves.captura(casafinal, casainicial)

            # SE NÃO, ELE MOVIMENTA.
            else:
                moves.movimento(casafinal, casainicial)
            board.tab()
            break

    while True:
        print(f'{branco}JOGADA DAS PRETAS{stop}')
        casainicial = moves.tratamento_de_erros('casai')

        if casainicial == 'ROQUE PEQUENO':
            moves.roquepequeno('preto')
            board.tab()
            break
        elif casainicial == 'ROQUE GRANDE':
            moves.roquegrande('preto')
            board.tab()
            break

        casafinal = moves.tratamento_de_erros('casaf')
        casaspreto = {'casainicial': casainicial, 'casafinal': casafinal}

        if moves.verificacaoenpassant(casafinal, casainicial):
            if moves.enpassant('preto', casasbranco['casainicial'], casasbranco['casafinal'], casainicial, casafinal):
                moves.capturaenpassant(casafinal, casainicial, 'preto')
                board.tab()
                break
            else:
                print(f'{vermelho}JOGADA INVÁLIDA!{stop}'.center(60))
                board.tab()
                continue
        else:
            if board.tabuleiro[casafinal] not in '.':
                moves.captura(casafinal, casainicial)
            else:
                moves.movimento(casafinal, casainicial)
            board.tab()
            break

