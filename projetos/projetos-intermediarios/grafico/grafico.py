import sys

# CORES
branco = '\033[1;49m'
vermelho = '\033[1;31m'
verde = '\033[1;32m'
amarelo = '\033[1;33m'
stop = '\033[m'

print('='*100)
print('GRÁFICOS COM PYTHON'.center(100))
print('='*100)


# DADOS E TRATAMENTOS DE ERROS
ultcoordenada = 6
while True:
    try:
        graudafuncao = int(input(f'{branco}Grau da função: {stop}'))
    except ValueError:
        print(f'{vermelho}ATENÇÃO! O valor digitado é inválido.{stop}')
        continue
    except KeyboardInterrupt:
        print(f'\n{verde}O usuário decidiu finalizar o programa.{stop}')
        sys.exit()
    else:
        break


# DICIONÁRIOS
coeficientes = {}
alfabeto = {'1': 'A', '2': 'B', '3': 'C', '4': 'D', '5': 'E', '6': 'F',
            '7': 'G', '8': 'H', '9': 'I', '10': 'J', '11': 'K', '12': 'L',
            '13': 'M', '14': 'N', '15': 'O', '16': 'P', '17': 'Q', '18': 'R',
            '19': 'S', '20': 'T', '21': 'U', '22': 'V', '23': 'W', '24': 'X',
            '25': 'Y', '26': 'Z'}
grafico = {}

# LISTAS
coordx = []
coordy = []

# VARIÁVEIS
contador = 1
contador_dois = 0

if graudafuncao > 0:
    for c in range(graudafuncao, -1, -1):
        coeficientes[f'{c}'] = int(input(f'{branco}Coeficiente {amarelo}{alfabeto[f"{contador}"]}{stop}: '))
        contador += 1
        contador_dois = c
else:
    for c in range(graudafuncao, 1, 1):
        coeficientes[f'{c}'] = int(input(f'{branco}Coeficiente {amarelo}{alfabeto[f"{contador}"]}{stop}: '))
        contador += 1
        contador_dois = c


# CRIAÇÃO DAS COORDENADAS
for cont in range(0, ultcoordenada):
    coordx.append(float(cont))
    coordy.append(float(cont))
    for cont_two in range(1, 10):
        coordx.append(cont+(cont_two/10))
        coordy.append(cont+(cont_two/10))


# CRIAÇÃO DOS PARES ORDENADOS
def gerar_pares_ordenados(x, y):
    for coordenaday in y:
        for coordenadax in x:
            
            grafico[f'{coordenaday},{coordenadax}'] = ' '


# CRIAÇÃO DO DOMÍNIO IMAGEM DA FUNÇÃO
def gerar_imagem(grau):
    if grau > 0:
        for x in coordx:
            grau_funcao = grau
            y = 0
            for coeficiente in coeficientes.values():
                y = y + coeficiente*(x**grau_funcao)
                grau_funcao = grau_funcao - 1
            if y > ultcoordenada:
                pass
            else:
                if y == int(y):
                    grafico[f'{x},{y}'] = '*'
                else:
                    grafico[f'{x},{y:.1f}'] = '*'
    else:
        # PARA EVITAR DIVISÕES POR ZERO
        del coordx[0]
        for x in coordx:
            grau_funcao = grau
            y = 0
            for coeficiente in coeficientes.values():
                y = y + coeficiente * (x ** grau_funcao)
                grau_funcao = grau_funcao + 1
            if y > 5:
                pass
            else:
                if y == int(y):
                    grafico[f'{x},{y}'] = '*'
                else:
                    grafico[f'{x},{y:.1f}'] = '*'
    
    # FAZ AJUSTES NA CURVA DO GRÁFICO PARA QUE ELA NÃO SEJA DESCONTÍNUA.
    for y in range((len(coordy)-1), -1, -1):
        for x in range(0, len(coordx)):
            if grafico[f'{coordx[x]},{coordy[y]}'] == '*':
                while True:
                    if grafico[f'{coordx[x]},{coordy[(y-1)]}'] == '*':
                        break
                    else:
                        # VARRE O GRÁFICO DA ESQUERDA PARA A DIREITA                
                        c = 2
                        while True:
                            try:
                                coordx[(x+1)]
                                coordy[(y-c)] 
                            except IndexError:
                                break
                            else:
                                if grafico[f'{coordx[x+1]},{coordy[y-c]}'] == '*':
                                    ponto = y-c
                                    for p in range(y, ponto, -1):
                                        grafico[f'{coordx[x]},{coordy[p]}'] = '*'
                                    break
                                else:
                                    if c == 30:
                                        break
                                    else:
                                        c += 1
                                        pass
                                    
                        # VARRE O GRÁFICO DA DIREITA PARA A ESQUERDA
                        contador_dois = 2
                        while True:
                            try:
                                coordx[(x-1)]
                                coordy[(y-contador_dois)] 
                            except IndexError:
                                break
                            else:
                                if grafico[f'{coordx[x-1]},{coordy[y-contador_dois]}'] == '*':
                                    ponto = y-contador_dois
                                    for p in range(y, ponto, -1):
                                        grafico[f'{coordx[x]},{coordy[p]}'] = '*'
                                    break
                                else:
                                    if contador_dois == 30:
                                        break
                                    else:
                                        contador_dois += 1
                                        pass

                        break
            else:
                pass



# GERAÇÃO DO GRÁFICO PARA O USUÁRIO
def gerar_grafico():
    for y in range((len(coordy)-1), -1, -1):
        for x in range(0, len(coordx)):
            if x == len(coordx)-1:
                print(grafico[f'{coordx[x]},{coordy[y]}'])
            elif y > 0 and x == 0:
                print(f'{grafico[f"{coordx[x]},{coordy[y]}"]}', end='')
            elif x > 0 and y == 0:
                print(f'{grafico[f"{coordx[x]},{coordy[y]}"]}', end='')
            else:
                print(grafico[f'{coordx[x]},{coordy[y]}'], end='')


# PROGRAMA RODANDO
gerar_pares_ordenados(coordx, coordy)
gerar_imagem(graudafuncao)
print(f'{branco}GRÁFICO DA FUNÇÃO{stop}'.center(110, '-'))
gerar_grafico()
print(f'{branco}GRÁFICO DA FUNÇÃO{stop}'.center(110, '-'))
