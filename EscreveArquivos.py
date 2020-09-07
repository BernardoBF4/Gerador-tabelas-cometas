import Calculos as calc

inicio_tabela_entradas = r"""
    \begin{table}
        \begin{center}
            \caption{Dados de entrada}
            \begin{tabular}{lrrrrrrr}
                \hline

                Nome & P[anos] & q[U.A.] & e [adm.] & i[rad] & k[gs^-1(UA)^n] & n [adm.] & Referência \\

                \hline

    """

final_tabela_entradas = r"""

                \hline

            \end{tabular}
        \end{center}
    \end{table}
    """

conteudo_tabela_entradas = r"""
                #Nome & #P & #q & #e & #i & #k & #n & #Ref \\
    """
inicio_tabela_saidas = r"""
    \begin{table}
        \begin{center}
            \caption{Dados de saída}
            \begin{tabular}{lrrr}
                \hline

                Nome & L [kg] & Tj [adm.] & Massa depositada [kg]  \\

                \hline

    """

final_tabela_saidas = r"""

                \hline

            \end{tabular}
        \end{center}
    \end{table}
    """

conteudo_tabela_saidas = r"""
                #Nome & #L & #Tj & #Md \\
    """

rodape_tabela_saidas = r"""
                \hline

                \multicolumn{2}{l|}{Massa total depositada [kg]} & \multicolumn{2}{c}{#Massa_total} \\
                \multicolumn{2}{l|}{Número total de cometas [cometas]} & \multicolumn{2}{c}{#N_cometas} \\
    """

def gerarLaTeX():
    """
    Esta função grava os dados que estão escritos em dados_cometas.txt em um arquivo conteudo_latex.txt, com o header e footer da tabela em gerarLaTeX.

    Esta função não precisa de argumentos, pois lê os dados diretamente do arquivo dados_cometas.txt.

    Esta função não possui retorno, pois escreve a tabela em LaTeX.
    """

    arquivo_latex_entradas = open("entradas_latex.txt", "r+")
    arquivo_latex_saidas = open("saidas_latex.txt", "r+")
    arquivo_dados = open("dados_cometas.txt", "r")

    novas_linhas_entradas, novas_linhas_saidas = [], []

    novas_linhas_entradas.append(inicio_tabela_entradas)
    novas_linhas_saidas.append(inicio_tabela_saidas)

    atualizacao_dados_totais = rodape_tabela_saidas

    for linha in arquivo_dados:

        valores = linha.split(",")

        nova_linha_entrada, nova_linha_saida = conteudo_tabela_entradas, conteudo_tabela_saidas
        nova_linha_entrada = nova_linha_entrada.replace("#Nome", valores[0])
        nova_linha_entrada = nova_linha_entrada.replace("#P", valores[1])
        nova_linha_entrada = nova_linha_entrada.replace("#q", valores[2])
        nova_linha_entrada = nova_linha_entrada.replace("#e", valores[3])
        nova_linha_entrada = nova_linha_entrada.replace("#i", valores[4])
        nova_linha_entrada = nova_linha_entrada.replace("#k", valores[5])
        nova_linha_entrada = nova_linha_entrada.replace("#n", valores[6])
        nova_linha_entrada = nova_linha_entrada.replace("#Ref", valores[9])
        nova_linha_saida = nova_linha_saida.replace("#Nome", valores[0])
        nova_linha_saida = nova_linha_saida.replace("#L", valores[7])
        nova_linha_saida = nova_linha_saida.replace("#Tj", valores[8])
        nova_linha_saida = nova_linha_saida.replace("#Md", valores[11][:valores[11].find("\n")])

        arquivo_dados_totais = open("massa_e_n_cometas.txt", "r+")
        linhas = arquivo_dados_totais.readlines()
        linhas = linhas[0].split(",")
        linhas[0] = float(linhas[0])
        linhas[1] = float(linhas[1])
        print("linhas: ", linhas)
        linhas[0] += float(valores[11][:valores[11].find("\n")])
        linhas[1] = calc.numeroCometas(linhas[0])
        linhas[0] = str(linhas[0])
        linhas[1] = str(linhas[1])
        arquivo_dados_totais.seek(0)
        arquivo_dados_totais.truncate()
        arquivo_dados_totais.write(str(linhas[0] + "," + linhas[1]))

        novas_linhas_entradas.append(nova_linha_entrada)
        novas_linhas_saidas.append(nova_linha_saida)

    novas_linhas_entradas.append(final_tabela_entradas)

    atualizacao_dados_totais = atualizacao_dados_totais.replace("#Massa_total", linhas[0])
    atualizacao_dados_totais = atualizacao_dados_totais.replace("#N_cometas", linhas[1])
    print(atualizacao_dados_totais)
    novas_linhas_saidas.append(atualizacao_dados_totais)
    novas_linhas_saidas.append(final_tabela_saidas)

    arquivo_latex_saidas.seek(0)
    arquivo_latex_entradas.seek(0)
    arquivo_latex_saidas.truncate()
    arquivo_latex_entradas.truncate()

    arquivo_latex_entradas.writelines(novas_linhas_entradas)
    arquivo_latex_saidas.writelines(novas_linhas_saidas)

    arquivo_dados_totais.close()
    arquivo_latex_entradas.close()
    arquivo_latex_saidas.close()
    arquivo_dados.close()

    print("Tabela em LaTeX gravada no arquivo conteudo_latex.txt")

def gravarSozinho(nome, periodo, q, e, i, k, n, ref):
    """
    Esta função cria uma arquivo chamado dados_ + (nome do cometa) e grava seus dados nele.

    Esta função não tem argumentos, pois lê os dados diretamente das entradas.

    A função não tem retorno.

    ATENÇÃO: a função não grava os dados do cometa no arquivo principal dados_cometas.
    """

    resultado = calc.calcularEConverterDados(nome, periodo, q, e, i, k, n, ref)

    arquivo_sozinho = open("dados_" + nome + ".txt", "a")

    arquivo_sozinho.write(str(resultado[0]) + "," + str(resultado[1]) + "," + str(resultado[2]) + "," +
                          str(resultado[3]) + "," + str(resultado[4]) + "," + str(resultado[5]) + "," +
                          str(resultado[6]) + "," + str(resultado[7]) + "," + str(resultado[8]) + "," +
                          str(resultado[9]) + "," + str(resultado[10]) + "," + str(resultado[11]) + "\n")

    arquivo_sozinho.close()

    print("Arquivo dados_" + nome, "criado e dados do cometa já estão salvos nele")

def gravarDadosNoArquivo(nome, periodo, q, e, i, k, n, ref):
    """
    Esta função grava os dados de entrada do cometa (nome, período, q, e, i, k, e n) junto com os calculados (L e Tj) em um arquivo LaTeX.

    A função não precisa de argumentos, pois lê os dados direto das entradas.

    A função não tem retorno, pois faz a gravação dos dados no arquivo dados_cometas.txt.
    """

    resultado = calc.calcularEConverterDados(nome, periodo, q, e, i, k, n, ref)

    arquivo_dados_cometas = open("dados_cometas.txt", "r+")
    linhas = arquivo_dados_cometas.readlines()

    linhas.append(str(resultado[0]) + "," + str(resultado[1]) + "," + str(resultado[2]) + "," +
                  str(resultado[3]) + "," + str(resultado[4]) + "," + str(resultado[5]) + "," +
                  str(resultado[6]) + "," + str(resultado[7]) + "," + str(resultado[8]) + "," +
                  str(resultado[9]) + "," + str(resultado[10]) + "," + str(resultado[11]) + "\n")

    arquivo_dados_cometas.seek(0)
    arquivo_dados_cometas.truncate()
    arquivo_dados_cometas.writelines(linhas)

    arquivo_dados_cometas.close()

    print("Dados do cometa gravados no arquivo dados_cometas.txt")

    gerarLaTeX()

def importarDados(entrada_nome_arquivo):
    """
    Esta função lê os dados de entrada (nome, período, q, e, i, k, n) de um arquivo .csv e os grava no arquivo .txt princiapl e no .txt para o LaTeX.

    Esta função nao precisa de argumentos, pois lê os dados diretamente do arquivo.

    A função não tem retorno.
    """

    arquivo_importar = open(entrada_nome_arquivo + ".csv", "r")
    arquivo_dados_cometas = open("dados_cometas.txt", "r+")
    linhas = arquivo_dados_cometas.readlines()

    for linha in arquivo_importar:

        valores = linha.split(",")
        resultado = calc.calcularEConverterDados(valores[0], valores[1], valores[2],
                                                 valores[3], valores[4], valores[5],
                                                 valores[6], valores[7])
        resultado[9] = resultado[9][:resultado[9].find("\n")]
        linhas.append(str(resultado[0]) + "," + str(resultado[1]) + "," + str(resultado[2]) + "," +
                      str(resultado[3]) + "," + str(resultado[4]) + "," + str(resultado[5]) + "," +
                      str(resultado[6]) + "," + str(resultado[7]) + "," + str(resultado[8]) + "," +
                      str(resultado[9]) + "," + str(resultado[10]) + "," + str(resultado[11]) + "\n")


    arquivo_dados_cometas.seek(0)
    arquivo_dados_cometas.truncate()
    arquivo_dados_cometas.writelines(linhas)

    arquivo_importar.close()
    arquivo_dados_cometas.close()

    gerarLaTeX()

    print("Dados importados e gravados no arquivo principal dados_cometas.txt e LaTeX pronto para todos os dados")
