# Referência do desafio: https://wiki.python.org.br/ListaDeExerciciosProjetos
# Arthur Menezes - https://github.com/ThuiMenez

# BIBLIOTECAS ------------------------------------------------------------------------

from tkinter.font import names
import pandas as pd

# Arquivo de dados -------------------------------------------------------------------

cabecalho = ['USUÁRIO', 'ESPAÇO UTILIZADO', '% DE USO']
df = pd.read_csv("usuario.txt",
                 sep=' ', names=cabecalho)

# FUNÇÕES ----------------------------------------------------------------------------

# Converte Byte em MB e trunca os decimais


def conversao_dados(x):
    a = x/1e+6
    b = 2  # Numero de casas
    c = int(a * 10**b)/10**b
    return c

# Deixa a primeira letra da palavra em maiúsculo


def letra_maiuscula(x):
    return x.capitalize()

# Código -------------------------------------------------------------------------------


df['USUÁRIO'] = df['USUÁRIO'].apply(letra_maiuscula)

espaco_resultado = df['ESPAÇO UTILIZADO'] = df['ESPAÇO UTILIZADO'].apply(
    conversao_dados)
soma = espaco_resultado.sum()

porcentagem = round(espaco_resultado/soma*100, 2)
df['% DE USO'] = porcentagem

media = sum(espaco_resultado)/len(espaco_resultado)

# Layout ---------------------------------------------------------------------------------

print('ACME Inc.\n           USO DO ESPAÇO EM DISCO PELOS USUÁRIOS\n----------------------------------------------------------')
print(df)
print('\nEspaço total ocupado: %.2f' % (soma), 'mb')
print('Espaço médio ocupado: %.2f' % (media), 'mb')
