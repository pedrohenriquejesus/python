branco = '\033[1;49;97m'
preto = '\033[1;30m'
azul = '\033[0;49;94m'
stop = '\033[m'


tabuleiro = {f'A1': f'{branco}T{stop}', 'B1': f'{branco}C{stop}', 'C1': f'{branco}B{stop}', 'D1': f'{branco}D{stop}', 'E1': f'{branco}R{stop}', 'F1': f'{branco}B{stop}', 'G1': f'{branco}C{stop}', 'H1': f'{branco}T{stop}',
              'A2': f'{branco}P{stop}', 'B2': f'{branco}P{stop}', 'C2': f'{branco}P{stop}', 'D2': f'{branco}P{stop}', 'E2': f'{branco}P{stop}', 'F2': f'{branco}P{stop}', 'G2': f'{branco}P{stop}', 'H2': f'{branco}P{stop}',
              'A3': '.', 'B3': '.', 'C3': '.', 'D3': '.', 'E3': '.', 'F3': '.', 'G3': '.', 'H3': '.',
              'A4': '.', 'B4': '.', 'C4': '.', 'D4': '.', 'E4': '.', 'F4': '.', 'G4': '.', 'H4': '.',
              'A5': '.', 'B5': '.', 'C5': '.', 'D5': '.', 'E5': '.', 'F5': '.', 'G5': '.', 'H5': '.',
              'A6': '.', 'B6': '.', 'C6': '.', 'D6': '.', 'E6': '.', 'F6': '.', 'G6': '.', 'H6': '.',
              'A7': f'{preto}P{stop}', 'B7': f'{preto}P{stop}', 'C7': f'{preto}P{stop}', 'D7': f'{preto}P{stop}', 'E7': f'{preto}P{stop}', 'F7': f'{preto}P{stop}', 'G7': f'{preto}P{stop}', 'H7': f'{preto}P{stop}',
              'A8': f'{preto}T{stop}', 'B8': f'{preto}C{stop}', 'C8': f'{preto}B{stop}', 'D8': f'{preto}D{stop}', 'E8': f'{preto}R{stop}', 'F8': f'{preto}B{stop}', 'G8': f'{preto}C{stop}', 'H8': f'{preto}T{stop}'
             }


def tab():
    print(f'''
    {azul}8{stop}    {tabuleiro['A8']}  {tabuleiro['B8']}  {tabuleiro['C8']}  {tabuleiro['D8']}  {tabuleiro['E8']}  {tabuleiro['F8']}  {tabuleiro['G8']}  {tabuleiro['H8']}
    {azul}7{stop}    {tabuleiro['A7']}  {tabuleiro['B7']}  {tabuleiro['C7']}  {tabuleiro['D7']}  {tabuleiro['E7']}  {tabuleiro['F7']}  {tabuleiro['G7']}  {tabuleiro['H7']}
    {azul}6{stop}    {tabuleiro['A6']}  {tabuleiro['B6']}  {tabuleiro['C6']}  {tabuleiro['D6']}  {tabuleiro['E6']}  {tabuleiro['F6']}  {tabuleiro['G6']}  {tabuleiro['H6']}
    {azul}5{stop}    {tabuleiro['A5']}  {tabuleiro['B5']}  {tabuleiro['C5']}  {tabuleiro['D5']}  {tabuleiro['E5']}  {tabuleiro['F5']}  {tabuleiro['G5']}  {tabuleiro['H5']}
    {azul}4{stop}    {tabuleiro['A4']}  {tabuleiro['B4']}  {tabuleiro['C4']}  {tabuleiro['D4']}  {tabuleiro['E4']}  {tabuleiro['F4']}  {tabuleiro['G4']}  {tabuleiro['H4']}
    {azul}3{stop}    {tabuleiro['A3']}  {tabuleiro['B3']}  {tabuleiro['C3']}  {tabuleiro['D3']}  {tabuleiro['E3']}  {tabuleiro['F3']}  {tabuleiro['G3']}  {tabuleiro['H3']}
    {azul}2{stop}    {tabuleiro['A2']}  {tabuleiro['B2']}  {tabuleiro['C2']}  {tabuleiro['D2']}  {tabuleiro['E2']}  {tabuleiro['F2']}  {tabuleiro['G2']}  {tabuleiro['H2']}
    {azul}1{stop}    {tabuleiro['A1']}  {tabuleiro['B1']}  {tabuleiro['C1']}  {tabuleiro['D1']}  {tabuleiro['E1']}  {tabuleiro['F1']}  {tabuleiro['G1']}  {tabuleiro['H1']}

         {azul}A  B  C  D  E  F  G  H{stop}   
        ''')
