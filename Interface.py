import tkinter
from tkinter import *
from cmath import sqrt
import clipboard
import EscreveArquivos as esc_arq

##<--------------------------------------------------- INTERFACE ---------------------------------------------------->

largura_entrada = 30
pady_entradas_rotulos = (2, 2)

#Inicia o tkinter sempre maximizado e com título
tela = tkinter.Tk()
tela.state("zoomed")
tela.title("Gerador de Tabelas")

#Frame do lado esquerdo da tela do tkinter
frame_esquerdo = Frame(tela)
frame_esquerdo.grid(column = 0, row = 0)

#Fame do lado direito da tela do tkinter
frame_direito = Frame(tela)
frame_direito.grid(column = 1, row = 0)

#Frame onde ficam as entradas, rótulos das entradas, e os botões Gravar e gerar LaTeX e Gravar sozinho
frame_entradas = Frame(frame_esquerdo)
frame_entradas.grid(column = 0, row = 1, padx = (5, 5), pady = (10, 30))

#Saída onde ficará exposto o código em LaTeX da tabela
output_latex = Text(frame_direito, width = 100, height = 40, wrap = "none")
output_latex.grid(sticky = E, padx = (40, 10), pady = (10, 0))

#Barras de rolagem da saída em LaTeX
scrollbar_y = Scrollbar(output_latex, orient = "vertical")
scrollbar_y.grid(sticky = E, ipady = 290)

scrollbar_x = Scrollbar(output_latex, orient = "horizontal")
scrollbar_x.grid(sticky = S, ipadx = 440)

output_latex.config(yscrollcommand = scrollbar_y.set, xscrollcommand = scrollbar_x.set)

scrollbar_x.config(command = output_latex.xview)
scrollbar_y.config(command = output_latex.yview)

#Título da interface
titulo = Label(frame_esquerdo, text = "Gerador de Tabelas", fg = "black", font = ("Times New Roman", 23))
titulo.grid(column = 0, row = 0)

#Entrada e rótulo do nome do cometa
rotulo_nome_cometa = Label(frame_entradas, text = "Nome do cometa")
rotulo_nome_cometa.grid(column = 0, row = 0, sticky = W, pady = pady_entradas_rotulos)
entrada_nome_cometa = Entry(frame_entradas, width = largura_entrada)
entrada_nome_cometa.grid(column = 1, row = 0, sticky = E, pady = pady_entradas_rotulos)

#Entrada e rótulo do período do cometa
rotulo_p = Label(frame_entradas, text = "Período do cometa, P")
rotulo_p.grid(column = 0, row = 1, sticky = W, pady = pady_entradas_rotulos)
entrada_p = Entry(frame_entradas, width = largura_entrada)
entrada_p.grid(column = 1, row = 1, sticky = E, pady = pady_entradas_rotulos)

#Entrada e rótulo da distância periélica do cometa, q
rotulo_q = Label(frame_entradas, text = "Distância periélica, q")
rotulo_q.grid(column = 0, row = 2, sticky = W, pady = pady_entradas_rotulos)
entrada_q = Entry(frame_entradas, width = largura_entrada)
entrada_q.grid(column = 1, row = 2, sticky = E, pady = pady_entradas_rotulos)

#Entrada e rótulo da excentricidade da órbita do cometa, e
rotulo_e = Label(frame_entradas, text = "Excentricidade da órbita, e")
rotulo_e.grid(column = 0, row = 3, sticky = W, pady = pady_entradas_rotulos)
entrada_e = Entry(frame_entradas, width = largura_entrada)
entrada_e.grid(column = 1, row = 3, sticky = E, pady = pady_entradas_rotulos)

#Entrada e rótulo da inclinação do cometa, i
rotulo_i = Label(frame_entradas, text = "Inclinação em relação à elíptica , i")
rotulo_i.grid(column = 0, row = 4, sticky = W, pady = pady_entradas_rotulos)
entrada_i = Entry(frame_entradas, width = largura_entrada)
entrada_i.grid(column = 1, row = 4, sticky = E, pady = pady_entradas_rotulos)

#Entrada e rótulo do k do cometa
rotulo_k = Label(frame_entradas, text = "k")
rotulo_k.grid(column = 0, row = 5, sticky = W, pady = pady_entradas_rotulos)
entrada_k = Entry(frame_entradas, width = largura_entrada)
entrada_k.grid(column = 1, row = 5, sticky = E, pady = pady_entradas_rotulos)

#Entrada e rótulo da lei de potências do cometa, n
rotulo_n = Label(frame_entradas, text = "Lei de potências, n")
rotulo_n.grid(column = 0, row = 6, sticky = W, pady = pady_entradas_rotulos)
entrada_n = Entry(frame_entradas, width = largura_entrada)
entrada_n.grid(column = 1, row = 6, sticky = E, pady = pady_entradas_rotulos)

#Entrada e rótulo para a referência dos dados do cometa
rotulo_referencia_cometa = Label(frame_entradas, text = "Referência dos dados")
rotulo_referencia_cometa.grid(column = 0, row = 7, sticky = W, pady = pady_entradas_rotulos)
entrada_referencia_cometa = Entry(frame_entradas, width = largura_entrada)
entrada_referencia_cometa.grid(column = 1, row = 7, sticky = E, pady = pady_entradas_rotulos)

#Entrada para o nome do arquivo de onde serão importados os dados
entrada_nome_arquivo = Entry(frame_esquerdo, width = largura_entrada)
entrada_nome_arquivo.grid(column = 0, row = 9, sticky = W, padx = (5, 5), pady = pady_entradas_rotulos)

##<------------------------------------------------ COPIAR E COLAR ------------------------------------------------->

def copiar():
    """
    Esta função permite copiar e colar quando se clica no botão Copiar.
    """
    clipboard.copy(output_latex.get(1.0, END))
    clipboard.paste()

##<---------------------------------------------------- FUNÇÕES INVOCADORAS ----------------------------------------------------->

def mostrarSaida():
    output_latex.delete(1.0, END)
    arquivo_latex_entradas = open("entradas_latex.txt", "r")
    arquivo_latex_saidas = open("saidas_latex.txt", "r")
    for linha in arquivo_latex_entradas:
        output_latex.insert(END, linha)
    output_latex.insert(END, "\n\n\n\n")
    for linha in arquivo_latex_saidas:
        output_latex.insert(END, linha)
    arquivo_latex_entradas.close()
    arquivo_latex_saidas.close()

def gravarArquivo():
    nome = entrada_nome_cometa.get()
    periodo = entrada_p.get()
    q = float(entrada_q.get())
    e = float(entrada_e.get())
    i = float(entrada_i.get())
    k = float(entrada_k.get())
    n = float(entrada_n.get())
    ref = entrada_referencia_cometa.get()
    esc_arq.gravarDadosNoArquivo(nome, periodo, q, e, i, k, n, ref)
    mostrarSaida()

def gravarSolo():
    nome = entrada_nome_cometa.get()
    periodo = entrada_p.get()
    q = float(entrada_q.get())
    e = float(entrada_e.get())
    i = float(entrada_i.get())
    k = float(entrada_k.get())
    n = float(entrada_n.get())
    ref = entrada_referencia_cometa.get()
    esc_arq.gravarSozinho(nome, periodo, q, e, i, k, n, ref)
    mostrarSaida()

def importar():
    esc_arq.importarDados(entrada_nome_arquivo.get())
    mostrarSaida()

##<---------------------------------------------------- BOTÕES ----------------------------------------------------->

#Botão para gravar os dados das entradas de um cometa e gerar sua tabela LaTeX
button_dados_latex = Button(frame_entradas, text = "Gravar e gerar LaTeX", command = gravarArquivo)
button_dados_latex.grid(column = 0, row = 8, pady = pady_entradas_rotulos)

#Botão para gravar os dados de um cometa em um arquivo separado sem LaTeX
button_gravar_sozinho = Button(frame_entradas, text = "Gravar sozinho", command = gravarSolo)
button_gravar_sozinho.grid(column = 1, row = 8, pady = pady_entradas_rotulos)

#Botão para importar dados de outro arquivo.
button_importar = Button(frame_esquerdo, text = "Importar Dados", command = importar)
button_importar.grid(column = 0, row = 9, sticky = E, pady = pady_entradas_rotulos)

#Botão para copiar o código da tabela em LaTeX da saída
button_copiar = Button(frame_direito, text = "Copiar", command = copiar)
button_copiar.grid()

mostrarSaida()



#Loop principal do tkinter
tela.mainloop()
