from math import *
from tkinter import * 
from tkinter import Button


# interface para fazer as contas
janela = Tk()
janela.geometry("650x350")
janela.title("Calculadora de Física")
janela["bg"] = "light blue"
janela.maxsize(650, 350)
janela.minsize(650, 350)


# Texto inicial
texto = Label(janela, text="Selecione qual informação será fornecida", bg="light blue", font="Arial 12 bold")
texto.place(x=1, y=10)

# Seleção da informação que será fornecida
informacao = IntVar()

rb_info_magnetico = Radiobutton(janela, text="Campo Magnético", value=1, bg="light blue", font="Arial 10", variable=informacao)
rb_info_magnetico.place(x=10, y=40)

rb_info_eletrico = Radiobutton(janela, text="Campo Elétrico", value=2, bg="light blue", font="Arial 10", variable=informacao)
rb_info_eletrico.place(x=10, y=70)

rb_info_intensidade = Radiobutton(janela, text="Intensidade", value=3, bg="light blue", font="Arial 10", variable=informacao)
rb_info_intensidade.place(x=10, y=100)

rb_info_frequencia = Radiobutton(janela, text="Frequência", value=4, bg="light blue", font="Arial 10", variable=informacao)
rb_info_frequencia.place(x=10, y=130)

rb_info_comprimento_onda = Radiobutton(janela, text="Comprimento de Onda", value=5, bg="light blue", font="Arial 10", variable=informacao)
rb_info_comprimento_onda.place(x=10, y=160)

rb_info_numero_ondas = Radiobutton(janela, text="Número de Ondas", value=6, bg="light blue", font="Arial 10", variable=informacao)
rb_info_numero_ondas.place(x=10, y=190)

rb_info_frequencia_angular = Radiobutton(janela, text="Frequência Angular", value=7, bg="light blue", font="Arial 10", variable=informacao)
rb_info_frequencia_angular.place(x=10, y=220)

# lugar para colocar o valor
texto_valor = Label(janela, text="Insira o valor desejado", bg="light blue", font="Arial 12 bold")
texto_valor.place(x=1, y=250)

valor = Entry(janela,width=15,font=("Arial",10))
valor.place(x=10, y=280)


# Lugar onde vão aparecer os resultados
texto_saida = Label(janela, text="Resultados do calculo", bg="light blue", font="Arial 12 bold")
texto_saida.place(x=350, y=10)

# Resultado do campo magnético
texto_mag = Label(janela, text="Campo Magnético:", bg="light blue", font="Arial 10")
texto_mag.place(x=360, y=40)
saida_magnetico = Entry(janela,width=8,font=("Arial",10))
saida_magnetico.place(x=480, y=40)

# Resultado do campo elétrico
texto_ele = Label(janela, text="Campo Elétrico:", bg="light blue", font="Arial 10")
texto_ele.place(x=360, y=70)
saida_eletrico = Entry(janela,width=8,font=("Arial",10))
saida_eletrico.place(x=480, y=70)

# Resultado da intensidade
texto_int = Label(janela, text="Intensidade:", bg="light blue", font="Arial 10")
texto_int.place(x=360, y=100)
saida_intensidade = Entry(janela,width=8,font=("Arial",10))
saida_intensidade.place(x=480, y=100)

# Resultado da frequência
texto_freq = Label(janela, text="Frequência:", bg="light blue", font="Arial 10")
texto_freq.place(x=360, y=130)
saida_frequencia = Entry(janela,width=8,font=("Arial",10))
saida_frequencia.place(x=480, y=130)

# Resultado do comprimento de onda
texto_comp = Label(janela, text="Compri. de Onda:", bg="light blue", font="Arial 10")
texto_comp.place(x=360, y=160)
saida_comprimento_onda = Entry(janela,width=8,font=("Arial",10))
saida_comprimento_onda.place(x=480, y=160)

# Resultado do número de ondas
texto_num = Label(janela, text="Número de Ondas:", bg="light blue", font="Arial 10")
texto_num.place(x=360, y=190)
saida_numero_ondas = Entry(janela,width=8,font=("Arial",10))
saida_numero_ondas.place(x=480, y=190)

# Resultado da frequência angular
texto_freq_ang = Label(janela, text="Frequência Angular:", bg="light blue", font="Arial 10")
texto_freq_ang.place(x=360, y=220)
saida_frequencia_angular = Entry(janela,width=8,font=("Arial",10))
saida_frequencia_angular.place(x=480, y=220)


# funções com as formulas
# Constantes
velocidade_vacuo_luz = 3 * 10**8
constante_magnetica = 4 * pi * 10**(-7)

# Esta função recebe a informação do campo magnético e calcula o campo elétrico e a intensidade
def entrada_campo_magnetico(campo_magnetico):
    campo_eletrico = campo_magnetico * velocidade_vacuo_luz
    intensidade = (velocidade_vacuo_luz * campo_magnetico ** 2) / (2 * constante_magnetica)
    saida_eletrico.delete(0,"end")
    saida_eletrico.insert(0, "{:.2e}".format(campo_eletrico))
    saida_intensidade.delete(0,"end")
    saida_intensidade.insert(0, "{:.2e}".format(intensidade))
    saida_magnetico.delete(0,"end")
    saida_frequencia_angular.delete(0,"end")
    saida_comprimento_onda.delete(0,"end")
    saida_numero_ondas.delete(0,"end")
    saida_frequencia.delete(0,"end")



# Esta função recebe a informação do campo elétrico e calcula o campo magnético e a intensidade
def entrada_campo_eletrico(campo_eletrico):
    campo_magnetico = campo_eletrico / velocidade_vacuo_luz
    intensidade = (campo_eletrico ** 2)/(2 * constante_magnetica * velocidade_vacuo_luz)
    saida_magnetico.delete(0,"end")
    saida_magnetico.insert(0, "{:.2e}".format(campo_magnetico))
    saida_intensidade.delete(0,"end")
    saida_intensidade.insert(0, "{:.2e}".format(intensidade))
    saida_eletrico.delete(0,"end")
    saida_frequencia_angular.delete(0,"end")
    saida_comprimento_onda.delete(0,"end")
    saida_numero_ondas.delete(0,"end")
    saida_frequencia.delete(0,"end")
    

# Esta função recebe a informação da intensidade e calcula o campo magnético e o campo elétrico
def entrada_intensidade(intensidade):
    campo_magnetico = sqrt(((2 * constante_magnetica) * intensidade) / velocidade_vacuo_luz)
    campo_eletrico = sqrt(2 * constante_magnetica * velocidade_vacuo_luz * intensidade)
    saida_magnetico.delete(0,"end")
    saida_magnetico.insert(0, "{:.2e}".format(campo_magnetico))
    saida_eletrico.delete(0,"end")
    saida_eletrico.insert(0, "{:.2e}".format(campo_eletrico))
    saida_intensidade.delete(0,"end")
    saida_frequencia_angular.delete(0,"end")
    saida_comprimento_onda.delete(0,"end")
    saida_numero_ondas.delete(0,"end")
    saida_frequencia.delete(0,"end")


# Esta função recebe a informação da frequência e calcula o comprimento da onda, numero de ondas e a frequência angular
def entrada_frequencia(frequencia):
    comprimento_onda = velocidade_vacuo_luz / frequencia
    numero_ondas = (2*pi) / comprimento_onda
    frequencia_angular = 2 * pi * frequencia
    saida_comprimento_onda.delete(0,"end")
    saida_comprimento_onda.insert(0, "{:.2e}".format(comprimento_onda))
    saida_numero_ondas.delete(0,"end")
    saida_numero_ondas.insert(0,  "{:.2e}".format(numero_ondas))
    saida_frequencia_angular.delete(0,"end")
    saida_frequencia_angular.insert(0, "{:.2e}".format(frequencia_angular))
    saida_frequencia.delete(0,"end")
    saida_eletrico.delete(0,"end")
    saida_intensidade.delete(0,"end")
    saida_magnetico.delete(0,"end")


# Esta função recebe a informação do comprimento da onda e calcula a frequencia, numero de ondas e a frequência angular
def entrada_comprimento_onda(comprimento_onda):
    frequencia = velocidade_vacuo_luz / comprimento_onda
    numero_ondas = (2 * pi) / comprimento_onda
    frequencia_angular = frequencia_angular = 2 * pi * frequencia
    saida_frequencia.delete(0,"end")
    saida_frequencia.insert(0, "{:.2e}".format(frequencia))
    saida_numero_ondas.delete(0,"end")
    saida_numero_ondas.insert(0, "{:.2e}".format(numero_ondas))
    saida_frequencia_angular.delete(0,"end")
    saida_frequencia_angular.insert(0, "{:.2e}".format(frequencia_angular))
    saida_comprimento_onda.delete(0,"end")
    saida_eletrico.delete(0,"end")
    saida_intensidade.delete(0,"end")
    saida_magnetico.delete(0,"end")


# Esta função recebe a informação do número de ondas e calcula a frequencia, comprimento da onda e a frequência angular
def entrada_numero_ondas(numero_ondas):
    comprimento_onda = (2 * pi) / numero_ondas
    frequencia = velocidade_vacuo_luz / comprimento_onda
    frequencia_angular = 2 * pi * frequencia
    saida_frequencia.delete(0,"end")
    saida_frequencia.insert(0, "{:.2e}".format(frequencia))
    saida_comprimento_onda.delete(0,"end")
    saida_comprimento_onda.insert(0, "{:.2e}".format(comprimento_onda))
    saida_frequencia_angular.delete(0,"end")
    saida_frequencia_angular.insert(0, "{:.2e}".format(frequencia_angular))
    saida_numero_ondas.delete(0,"end")
    saida_eletrico.delete(0,"end")
    saida_intensidade.delete(0,"end")
    saida_magnetico.delete(0,"end")


# Esta função recebe a informação da frequencia angular e calcula a frequencia, comprimento da onda e o número das ondas
def entrada_frequencia_agular(frequencia_angular):
    frequencia = frequencia_angular / (2 * pi)
    comprimento_onda = velocidade_vacuo_luz / frequencia
    numero_ondas = (2 * pi) / comprimento_onda
    saida_frequencia.delete(0,"end")
    saida_frequencia.insert(0, "{:.2e}".format(frequencia))
    saida_numero_ondas.delete(0,"end")
    saida_numero_ondas.insert(0, "{:.2e}".format(numero_ondas))
    saida_comprimento_onda.delete(0,"end")
    saida_comprimento_onda.insert(0, "{:.2e}".format(comprimento_onda))
    saida_frequencia_angular.delete(0,"end")
    saida_eletrico.delete(0,"end")
    saida_intensidade.delete(0,"end")
    saida_magnetico.delete(0,"end")


# Lógica para receber a informação e fazer o cálculo
def calcular():
    recebe_info = informacao.get()
    if recebe_info == 1:
        valor_mag = valor.get()
        entrada_campo_magnetico(float(valor_mag))
    elif recebe_info == 2:
        valor_elet = valor.get()
        entrada_campo_eletrico(float(valor_elet))
    elif recebe_info == 3:
        valor_inten = valor.get()
        entrada_intensidade(float(valor_inten))
    elif recebe_info == 4:
        valor_frequencia = valor.get()
        entrada_frequencia(float(valor_frequencia))
    elif recebe_info == 5:
        valor_compri = valor.get()
        entrada_comprimento_onda(float(valor_compri))
    elif recebe_info == 6:
        valor_num_onda = valor.get()
        entrada_numero_ondas(float(valor_num_onda))
    elif recebe_info == 7:
        valor_frequencia_angular = valor.get()
        entrada_frequencia_agular(float(valor_frequencia_angular))
    else:
        print("Escolha uma opção para realizar os calculos")


# se der errado por conta da versão do python substituir todas as funções por essa
# if recebe_info == 1:
#     valor_mag = valor.get()
#     numero, expoente = valor_mag.split('E')
#     numero = float(numero)
#     expoente = int(expoente)
#     resultado = numero * (10 ** expoente)
#     entrada_campo_magnetico(float(resultado))


# botão para calcular
botao = Button(janela, text="Calcular", font="Arial 10 bold", bg="light green", command=calcular)
botao.place(x=10, y=310)

janela.mainloop()