import math

def f(r, n, a, e):
    """
    Função a ser integrada.

    Seus argumentos são r, n, a e e, que serão passados como valores quando ela for chamada dentro da funçao que faz a integração pelo método de Simpson.

    Seu retorno é a própria expressão.
    """
    return 1 / (r**(n)* math.sqrt( ( (a*e)**2-(a-r)**2  )/(a*r**2)  ) )

def integracaoSimpson(limite_superior, limite_inferior, n, a, e):
    """
    Esta função faz a integração pelo método de Simpson.

    Seus argumentos são os limites superior e inferior de integração, n, a, e e, que serão passados na função que calcula a quantidade de H2O perdida por um cometa.

    Seu retorno é o valor (float) da integral.
    """
    n_particoes= 5.0
    h = (limite_superior - limite_inferior)/n_particoes

    r = list()
    fr = list()

    j = 0
    while j <= n_particoes:
        r.append(limite_inferior + j * h)
        #print(r[j])
        fr.append(f(r[j], n, a, e))
        #print("Valores de r e fr:", "r(",j,") =", r[j].real, "; f(",j,") =", f(r[j], n, a, e).real)
        j += 1

    res = 0
    j = 0
    while j<= n_particoes:
        if j == 0 or j == n_particoes:
            res+= fr[j]
        elif j % 2 != 0:
            res+= 4. * fr[j]
        else:
            res+= 2. * fr[j]
        j+= 1
    res = res * (h / 3)

    return res

def calcularLH2O(q, e, k, n):
    """
    Esta função calcula a quantidade de H2O perdida pelo cometa.

    Seus argumentos são q, e, k, e n, que serã passados quando ela for chamada detro da função que grava os dados do cometa em um arquivo.

    Seu retorno é a quantidade (float) de H2O perdida pelo cometa em uma órbita
    """

    limite_inferior = 1.51
    limite_superior = 3.0
    a = q / (1 - e)
    valor_integral = integracaoSimpson(limite_superior, limite_inferior, n, a, e).real
    l_H2O = (1.0e7 * k * valor_integral) / 1000

    return l_H2O

def calcularTisserand(q, e, i):
    a = q / (1 - e)
    aj = 5.20336301
    i = math.radians(i)
    return (( aj / a ) + 2 * math.sqrt( (1 - e**2) * ( a / aj ) ) * math.cos(i))

def calcularMassaDepEPassagens(P, l_H2O):
    n_passagens = ((4.5 * (10 ** 9)) - (3.9 * (10 ** 9))) / (P)
    m_depositada = n_passagens * l_H2O
    return [m_depositada, n_passagens]

def numeroCometas(total):
    n_cometas = ((5.98 * (10 ** 24)) / 4400) / total

    return float(n_cometas)

def calcularEConverterDados(nome, periodo, q, e, i, k, n, ref):

    lost = calcularLH2O(float(q), float(e), float(k), float(n))
    tj = calcularTisserand(float(q), float(e), float(i))
    massa_passagens = calcularMassaDepEPassagens(float(periodo), float(lost))
    massa_depositada = massa_passagens[0]
    n_passagens = massa_passagens[1]

    nome = str(nome)
    periodo = f"{float(periodo):.2e}" if float(periodo) >= 1 else round(float(periodo), 2)
    q = f"{float(q):.2e}" if float(q) >= 10 else round(float(q), 2)
    e = f"{float(e):.2e}" if float(e) >= 10 else round(float(e), 2)
    i = f"{float(i):.2e}" if float(i) >= 10 else round(float(i), 2)
    k = f"{float(k):.2e}" if float(k) >= 10 else round(float(k), 2)
    n = f"{float(n):.2e}" if float(n) >= 10 else round(float(n), 2)
    ref = str(ref)
    lost = f"{lost:.2e}" if float(lost) >= 10 else round(lost, 2)
    tj = f"{tj:.2e}" if float(lost) >= 10 else round(tj, 2)
    massa_depositada = f"{massa_depositada:.2e}" if float(massa_depositada) >= 10 else round(massa_depositada, 2)
    n_passagens = f"{n_passagens:.2e}" if float(n_passagens) >= 10 else round(n_passagens, 2)

    return [nome, periodo, q, e, i, k, n, lost, tj, ref, n_passagens, massa_depositada]
