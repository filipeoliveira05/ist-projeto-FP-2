#TAD Intersecao
def cria_intersecao(col, lin):
    """
    Recebe um caracter e um inteiro correspondentes à coluna, col, e à linha, lin.
    Devolve a interseção correspondente.
    Caso os argumentos não sejam válidos, gera um erro.

    :param col: coluna (str)
    :param lin: linha (int)
    :return: interseção
    """

    if not isinstance(col, str) or not ord('A') <= ord(col) <= ord('S') or len(col) != 1:
        raise ValueError('cria_intersecao: argumentos invalidos')
    if not isinstance(lin, int) or not (1 <= lin <= 19):
        raise ValueError('cria_intersecao: argumentos invalidos')
    return (col, lin)


def obtem_col(i):
    """
    Devolve a coluna da interseção i.

    :param i: interseção
    :return: coluna (str)
    """

    return i[0]


def obtem_lin(i):
    """
    Devolve a linha lin da interseção i.

    :param i: interseção
    :return: linha (int)
    """

    if isinstance(i, tuple):
        return i[1]
    elif isinstance(i, str):
        return i[1:]


def eh_intersecao(arg):
    """
    Devolve True caso o argumento seja um TAD intersecao e False caso contrário.

    :param arg: argumento (universal)
    :return: True/False (bool)
    """

    return (isinstance(arg, tuple) and len(arg) == 2 and 
            isinstance(obtem_col(arg), str) and isinstance(obtem_lin(arg), int) and 
            ord('A') <= ord(obtem_col(arg)) <= ord('S') and len(obtem_col) == 1 and 1 <= obtem_lin(arg) <= 19)


def intersecoes_iguais(i1, i2):
    """
    Devolve True apenas se i1 e i2 são interseções e são iguais, e False caso contrário.

    :param i1: argumento (universal)
    :param i2: argumento (universal)
    :return: True/False (bool)
    """

    return obtem_col(i1) == obtem_col(i2) and obtem_lin(i1) == obtem_lin(i2)


def intersecao_para_str(i):
    """
    Devolve a cadeia de caracteres que representa o argumento.

    :param i: interseção
    :return: cadeia de caracteres (str)
    """

    return obtem_col(i) + str(obtem_lin(i))


def str_para_intersecao(s):
    """
    Devolve a interseção representada pelo argumento.

    :param s: cadeia de caracteres (str)
    :return: interseção
    """

    col = s[0]
    lin = int(s[1:])
    return (col, lin)


def obtem_intersecoes_adjacentes(i, l):
    """
    Devolve um tuplo com as interseções adjacentes à interseção i, de acordo com a ordem de leitura.
    O argumento l corresponde à interseção superior direita do goban.

    :param i: interseção
    :param l: interseção
    :return: tuplo com interseções adjacentes a i (tuple)
    """

    col = obtem_col(i)
    lin = obtem_lin(i)
    i_adjacents = []
    
    i_adjacents_possible = [
        (chr(ord(col)), lin - 1),
        (chr(ord(col) - 1), lin),
        (chr(ord(col) + 1), lin),
        (chr(ord(col)), lin + 1),
    ]
    
    for a in i_adjacents_possible:
        if ord('A') <= ord(obtem_col(a)) <= ord(obtem_col(l)) and 1 <= obtem_lin(a) <= obtem_lin(l):
            i_adjacents.append(a)

    return tuple(i_adjacents)


def ordena_intersecoes(t):
    """
    Devolve um tuplo de interseções com as mesmas interseções, mas ordenadas de acordo com a ordem de leitura do goban.

    :param t: tuplo 'desordenado' (tuple)
    :return: tuplo 'ordenado' (tuple)
    """

    if len(t) == 0:
        return ()
    return tuple(sorted(t, key=lambda x: (obtem_lin(x), obtem_col(x))))



#TAD pedra
def cria_pedra_branca():
    """
    Devolve uma pedra pertencente ao jogador branco.

    :return: pedra branca (str)
    """

    return 'O'


def cria_pedra_preta():
    """
    Devolve uma pedra pertencente ao jogador preto.

    :return: pedra preta (str)
    """

    return 'X'


def cria_pedra_neutra():
    """
    Devolve uma pedra neutra.

    :return: pedra neutra (str)
    """

    return '.'


def eh_pedra(arg):
    """
    Devolve True caso o argumento seja um TAD pedra e False caso contrário.

    :param arg: argumento (universal)
    :return: True/False (bool)
    """

    return arg in [cria_pedra_branca(), cria_pedra_preta(), cria_pedra_neutra()]


def eh_pedra_branca(p):
    """
    Devolve True caso a pedra p seja do jogador branco e False caso contrário.

    :param p: pedra
    :return: True/False (bool)
    """

    return eh_pedra(p) and p == cria_pedra_branca()


def eh_pedra_preta(p):
    """
    Devolve True caso a pedra p seja do jogador preto e False caso contrário.

    :param p: pedra
    :return: True/False (bool)
    """

    return eh_pedra(p) and p == cria_pedra_preta()


def pedras_iguais(p1, p2):
    """
    Devolve True apenas se p1 e p2 são pedras e são iguais.

    :param p1: argumento (universal)
    :param p2: argumento (universal)
    :return: True/False (bool)
    """

    return eh_pedra(p1) and eh_pedra(p2) and p1 == p2


def pedra_para_str(p):
    """
    Devolve a cadeia de caracteres que representa o jogador dono da pedra.
    Devolve 'O', 'X' ou '.' para pedras do jogador branco, preto ou neutra respetivamente.

    :param p: pedra
    :return: cadeia de caracteres (str)
    """

    if p == cria_pedra_branca():
        return 'O'
    elif p == cria_pedra_preta():
        return 'X'
    else:
        return '.'


def eh_pedra_jogador(p):
    """
    Devolve True caso a pedra p seja de um jogador e False caso contrário

    :param p: pedra
    :return: True/False (bool)
    """

    return eh_pedra_branca(p) or eh_pedra_preta(p)



#TAD Goban
def cria_goban_vazio(n):
    """
    Add Description Here

    :param n: Add Type
    :return: Add Type
    """

    if n not in [9, 13, 19]:
        raise ValueError('cria_goban_vazio: argumento invalido')
    
    col = [cria_pedra_neutra(),] * int(n)
    g_empty = [col[:] for _ in range(int(n))]
    
    return g_empty


def cria_goban(n, ib, ip):
    """
    Add Description Here

    :param n: Add Type
    :param ib: Add Type
    :param ip: Add Type
    :return: Add Type
    """

    if n not in [9, 13, 19] or not isinstance(ib, tuple) or not isinstance(ip, tuple):
        raise ValueError('cria_goban: argumentos invalidos')
    
    # Verifica se existem elementos iguais em ib
    el_ib = set()
    for el in ib:
        if el in el_ib:
            raise ValueError('cria_goban: argumentos invalidos')
        el_ib.add(el)

    # Verifica se existem elementos iguais em ip
    el_ip = set()
    for el in ip:
        if el in el_ip:
            raise ValueError('cria_goban: argumentos invalidos')
        el_ip.add(el)

    # Verifica se existem elementos iguais em ambos os tuplos
    if el_ib & el_ip:
        raise ValueError('cria_goban: argumentos invalidos')

    g = cria_goban_vazio(n)

    for b in tuple(ib):
        col_index = ord(obtem_col(b)) - ord('A')
        lin_index = int(obtem_lin(b)) - 1
        if 0 <= col_index < n and 0 <= lin_index < n:
            g[col_index][lin_index] = cria_pedra_branca()


    for p in tuple(ip):
        col_index = ord(obtem_col(p)) - ord('A')
        lin_index = int(obtem_lin(p)) - 1
        if 0 <= col_index < n and 0 <= lin_index < n:
            g[col_index][lin_index] = cria_pedra_preta()
    
    return g


def cria_copia_goban(t):
    """
    Add Description Here

    :param t: Add Type
    :return: Add Type
    """

    return [x if not isinstance(x, list) else x[:] for x in t]



def obtem_ultima_intersecao(g):
    """
    Add Description Here

    :param g: Add Type
    :return: Add Type
    """

    n = len(g)
    col = chr(ord('A') + n - 1)
    lin = n
    return (col, lin)


def obtem_pedra(g, i):
    """
    Add Description Here

    :param g: Add Type
    :param i: Add Type
    :return: Add Type
    """

    col_index = ord(obtem_col(i)) - ord('A')
    lin_index = int(obtem_lin(i)) - 1
    p = g[col_index][lin_index]

    if eh_pedra_branca(p):
        return cria_pedra_branca()
    elif eh_pedra_preta(p):
        return cria_pedra_preta()
    else:
        return cria_pedra_neutra()


def obtem_cadeia(g, i):
    """
    Add Description Here

    :param g: Add Type
    :param i: Add Type
    :return: Add Type
    """

    if obtem_pedra(g, i) == cria_pedra_branca():
        condition = cria_pedra_branca()
    elif obtem_pedra(g, i) == cria_pedra_preta():
        condition = cria_pedra_preta()
    else:
        condition = cria_pedra_neutra()
    
    chain = []
    queue = [i]

    while queue:
        i = queue.pop()
        chain.append(i)
        for i_new in obtem_intersecoes_adjacentes(i, obtem_ultima_intersecao(g)):
            if obtem_pedra(g, i_new) == condition and i_new not in chain + queue:
                queue.append(i_new)

    return ordena_intersecoes(tuple(chain))


def coloca_pedra(g, i, p):
    """
    Add Description Here

    :param g: Add Type
    :param i: Add Type
    :param p: Add Type
    :return: Add Type
    """

    col_index = ord(obtem_col(i)) - ord('A')
    lin_index = int(obtem_lin(i)) - 1
    n = len(g)

    if 0 <= col_index < n and 0 <= lin_index < n:
        g[col_index][lin_index] = p

    return g


def remove_pedra(g, i):
    """
    Add Description Here

    :param g: Add Type
    :param i: Add Type
    :return: Add Type
    """

    col_index = ord(obtem_col(i)) - ord('A')
    lin_index = int(obtem_lin(i)) - 1
    n = len(g)

    if 0 <= col_index < n and 0 <= lin_index < n:
        g[col_index][lin_index] = cria_pedra_neutra()

    return g


def remove_cadeia(g, t):
    """
    Add Description Here

    :param g: Add Type
    :param t: Add Type
    :return: Add Type
    """

    n = len(g)
    for i in t:
        col_index = ord(obtem_col(i)) - ord('A')
        lin_index = int(obtem_lin(i)) - 1
        
        if 0 <= col_index < n and 0 <= lin_index < n:
            g[col_index][lin_index] = cria_pedra_neutra()

    return g


def eh_goban(arg):
    """
    Add Description Here

    :param arg: Add Type
    :return: Add Type
    """

    if not isinstance(arg, list) or len(arg) not in [9, 13, 19]:
        return False
    for c in range(len(arg)):
        if len(arg[c]) != len(arg[0]) or len(arg[c]) not in [9, 13, 19] or not isinstance(arg[c], list):
            return False
        for l in range(len(arg[c])):
            if arg[c][l] not in [cria_pedra_branca(), cria_pedra_preta(), cria_pedra_neutra()]:
                return False
            
    return True


def eh_intersecao_valida(g, i):
    """
    Add Description Here

    :param g: Add Type
    :param i: Add Type
    :return: Add Type
    """

    if not isinstance(i, tuple) or len(i) != 2:
        return False
    
    col = obtem_col(i)
    lin = obtem_lin(i)
    n = len(g)

    if not ord('A') <= ord(col) <= ord('A') + n - 1 or not 1 <= lin <= n:
        return False
    
    return True


def gobans_iguais(g1, g2):
    """
    Add Description Here

    :param g1: Add Type
    :param g2: Add Type
    :return: Add Type
    """

    if not eh_goban(g1) or not eh_goban(g2):
        return False
    
    str_g1 = list(map("".join, g1))
    str_g2 = list(map("".join, g2))
    
    return str_g1 == str_g2


def goban_para_str(g):
    """
    Add Description Here

    :param g: Add Type
    :return: Add Type
    """

    LETTERS = tuple('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    n_c, n_l = len(g), len(g[0])
    cad = '   ' + ''.join(f'{l} ' for l in LETTERS[:n_l]).rstrip() + '\n'

    for i in range(n_c - 1, -1, -1):
        cad += '{:>2} '.format(i + 1)
        for j in range(n_l):
            estado_pedra = obtem_pedra(g, f'{LETTERS[j]}{i + 1}')
            cad += estado_pedra + ' '
        cad += '{:>2}\n'.format(i + 1)
    cad += '   ' + ''.join(f'{l} ' for l in LETTERS[:n_l]).rstrip()
    
    return cad


def obtem_territorios(g):
    """
    Add Description Here

    :param g: Add Type
    :return: Add Type
    """

    territorios = []
    visitadas = set()

    def explorar_territorio(i, territorio):
        """
        Add Description Here

        :param i: Add Type
        :param territorio: Add Type
        :return: Add Type
        """

        visitadas.add(i)
        territorio.add(i)
        vizinhas = obtem_intersecoes_adjacentes(i, obtem_ultima_intersecao(g))
        for vizinha in vizinhas:
            if obtem_pedra(g, vizinha) == cria_pedra_neutra() and vizinha not in visitadas:
                explorar_territorio(vizinha, territorio)
    
    for col in range(len(g)):
        for lin in range(len(g[0])):
            i = cria_intersecao(chr(ord('A') + col), lin + 1)
            if obtem_pedra(g, i) == cria_pedra_neutra() and i not in visitadas:
                territorio = set()
                explorar_territorio(i, territorio)
                territorios.append(ordena_intersecoes(tuple(territorio)))

    return ordena_intersecoes(territorios)



def obtem_adjacentes_diferentes(g, t):
    """
    Add Description Here

    :param g: Add Type
    :param t: Add Type
    :return: Add Type
    """

    adjacentes = set()

    for i in t:
        vizinhas = obtem_intersecoes_adjacentes(i, obtem_ultima_intersecao(g))
        for vizinha in vizinhas:
            if eh_intersecao_valida(g, vizinha):
                if obtem_pedra(g, i) == cria_pedra_neutra() and obtem_pedra(g, vizinha) != cria_pedra_neutra():
                    adjacentes.add(vizinha)
                elif obtem_pedra(g, i) != cria_pedra_neutra() and obtem_pedra(g, vizinha) == cria_pedra_neutra():
                    adjacentes.add(vizinha)

    return ordena_intersecoes(tuple(sorted(adjacentes)))



def jogada(g, i, p):
    """
    Add Description Here

    :param g: Add Type
    :param i: Add Type
    :param p: Add Type
    :return: Add Type
    """

    g = coloca_pedra(g, i, p)
    
    cadeias_adjacentes = []
    for adjacente in obtem_intersecoes_adjacentes(i, obtem_ultima_intersecao(g)):
        if obtem_pedra(g, adjacente) != cria_pedra_neutra() and obtem_cadeia(g, adjacente) not in cadeias_adjacentes:
            cadeias_adjacentes.append(obtem_cadeia(g, adjacente))
    
    if p == cria_pedra_preta():
        adversario = cria_pedra_branca()
    else:
        adversario = cria_pedra_preta()

    for cadeia in cadeias_adjacentes:
        if obtem_pedra(g, cadeia[0]) == adversario and not tem_liberdade(g, cadeia):
            g = remove_cadeia(g, cadeia)
    
    return g


def tem_liberdade(g, cadeia):
    """
    Add Description Here

    :param g: Add Type
    :param cadeia: Add Type
    :return: Add Type
    """

    for intersecao in cadeia:
        adjacentes = obtem_intersecoes_adjacentes(intersecao, obtem_ultima_intersecao(g))
        for adjacente in adjacentes:
            if eh_intersecao_valida(g, adjacente):
                if obtem_pedra(g, adjacente) == cria_pedra_neutra():
                    return True
    return False


def obtem_pedras_jogadores(g):
    """
    Add Description Here

    :param g: Add Type
    :return: Add Type
    """

    p_b = 0
    p_p = 0

    for col in g:
        for i in col:
            if i == cria_pedra_branca():
                p_b += 1
            elif i == cria_pedra_preta():
                p_p += 1

    return (p_b, p_p)



def calcula_pontos(g):
    """
    Add Description Here

    :param g: Add Type
    :return: Add Type
    """

    i_u = obtem_ultima_intersecao(g)
    n = i_u[1]
    if g == cria_goban_vazio(n):
        return (0,0)
    
    pontos = obtem_pedras_jogadores(g)
    pontos_branco = pontos[0]
    pontos_preto = pontos[1]
    
    territorios = obtem_territorios(g)
    
    for territorio in territorios:
        fronteira = obtem_adjacentes_diferentes(g, territorio)
        
        mesma_cor = all(obtem_pedra(g, i) == obtem_pedra(g, fronteira[0]) for i in fronteira)
        
        if mesma_cor and obtem_pedra(g, fronteira[0]) == cria_pedra_branca():
            pontos_branco += len(territorio)
        elif mesma_cor and obtem_pedra(g, fronteira[0]) == cria_pedra_preta():
            pontos_preto += len(territorio)
    
    return (pontos_branco, pontos_preto)



def eh_jogada_legal(g, i, p, l):
    """
    Add Description Here

    :param g: Add Type
    :param i: Add Type
    :param p: Add Type
    :param l: Add Type
    :return: Add Type
    """

    if not eh_intersecao_valida(g, i) or obtem_pedra(g, i) != cria_pedra_neutra():
        return False
    
    # Suicídio
    g_copia = cria_copia_goban(g)
    g_copia = jogada(g_copia, i, p)
    cadeia = obtem_cadeia(g_copia, i)
    if not tem_liberdade(g_copia, cadeia):
        return False
    
    # Repetição (ko)
    if gobans_iguais(g_copia, l):
        return False
    
    return True


def turno_jogador(g, p, l):    
    """
    Add Description Here

    :param g: Add Type
    :param p: Add Type
    :param l: Add Type
    :return: Add Type
    """

    while True:
        move = input(f"Escreva uma intersecao ou 'P' para passar [{pedra_para_str(p)}]:").strip().upper()

        if move == 'P':
            return False
        elif eh_intersecao_valida(g, str_para_intersecao(move)) and eh_jogada_legal(g, str_para_intersecao(move), p, l):
            jogada(g, str_para_intersecao(move), p)
            return True



def go(n, tb, tp):
    """
    Add Description Here

    :param n: Add Type
    :param tb: Add Type
    :param tp: Add Type
    :return: Add Type
    """

    try:
        g = cria_goban(n, tb, tp)
    except ValueError:
        raise ValueError('go: argumentos invalidos')
    
    jogador_branco = cria_pedra_branca()
    jogador_preto = cria_pedra_preta()
    ultimo_estado = None

    while True:
        pontos_branco, pontos_preto = calcula_pontos(g)
        print(f"Branco (O) tem {pontos_branco} pontos")
        print(f"Preto (X) tem {pontos_preto} pontos")
        print(goban_para_str(g))
        
        turno_preto = turno_jogador(g, jogador_preto, ultimo_estado)
        if not turno_preto:
            break

        pontos_branco, pontos_preto = calcula_pontos(g)
        print(f"Branco (O) tem {pontos_branco} pontos")
        print(f"Preto (X) tem {pontos_preto} pontos")
        print(goban_para_str(g))
        
        turno_branco = turno_jogador(g, jogador_branco, ultimo_estado)
        if not turno_branco:
            break
        
        ultimo_estado = cria_copia_goban(g)

    pontos_branco, pontos_preto = calcula_pontos(g)
    return pontos_branco > pontos_preto


