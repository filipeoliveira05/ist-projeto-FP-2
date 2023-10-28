#TAD Intersecao
def cria_intersecao(col, lin):
    if not isinstance(col, str) or not ord('A') <= ord(col) <= ord('S'):
        raise ValueError('cria_intersecao: argumentos invalidos')
    if not isinstance(lin, int) or not (1 <= lin <= 19):
        raise ValueError('cria_intersecao: argumentos invalidos')
    return (col, lin)


def obtem_col(i):
    return i[0]


def obtem_lin(i):
    return i[1]


#não verifica se as letras e números estão dentro dos limites
def eh_intersecao(arg):
    return isinstance(arg, tuple) and len(arg) == 2 and isinstance(obtem_col(arg), str) and isinstance(obtem_lin(arg), int)


def intersecoes_iguais(i1, i2):
    return obtem_col(i1) == obtem_col(i2) and obtem_lin(i1) == obtem_lin(i2)


#retorna A12, em vez de 'A12'
def intersecao_para_str(i):
    return obtem_col(i) + str(obtem_lin(i))


def str_para_intersecao(s):
    col = s[0]
    lin = int(s[1:])
    return (col, lin)


def obtem_intersecoes_adjacentes(i, l):
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
    if len(t) == 0:
        return ()
    return tuple(sorted(t, key=lambda x: (obtem_lin(x), obtem_col(x))))



#TAD pedra
def cria_pedra_branca():
    return 'O'

def cria_pedra_preta():
    return 'X'

def cria_pedra_neutra():
    return '.'


def eh_pedra(arg):
    return arg in ['O', 'X', '.']

def eh_pedra_branca(p):
    return eh_pedra(p) and p == 'O'

def eh_pedra_preta(p):
    return eh_pedra(p) and p == 'X'


def pedras_iguais(p1, p2):
    return eh_pedra(p1) and eh_pedra(p2) and p1 == p2


def pedra_para_str(p):
    if p == cria_pedra_branca():
        return 'O'
    elif p == cria_pedra_preta():
        return 'X'
    else:
        return '.'


def eh_pedra_jogador(p):
    return eh_pedra_branca(p) or eh_pedra_preta(p)



#TAD Goban
def cria_goban_vazio(n):
    if n not in [9, 13, 19]:
        raise ValueError('cria_goban_vazio: argumento invalido')
    
    col = ['.',] * n
    g_empty = [col[:] for _ in range(n)]
    
    return g_empty


def cria_goban(n, ib, ip):
    if n not in [9, 13, 19] or not isinstance(ib, tuple) or not isinstance(ip, tuple):
        raise ValueError('cria_goban_vazio: argumento invalido')
    
    g = cria_goban_vazio(n)

    for b in ib:
        col_index = ord(obtem_col(b)) - ord('A')
        lin_index = int(obtem_lin(b)) - 1
        g[col_index][lin_index] = 'O'

    for p in ip:
        col_index = ord(obtem_col(p)) - ord('A')
        lin_index = int(obtem_lin(p)) - 1
        g[col_index][lin_index] = 'X'
    
    return g


def cria_copia_goban(t):
    return t


def obtem_ultima_intersecao(g):
    n = len(g)
    col = chr(ord('A') + n - 1)
    lin = n
    return (col, lin)


def obtem_pedra(g, i):
    col_index = ord(obtem_col(i)) - ord('A')
    lin_index = int(obtem_lin(i)) - 1
    p = g[col_index][lin_index]

    if eh_pedra_branca(p):
        return 'O'
    elif eh_pedra_preta(p):
        return 'X'
    else:
        return '.'


def obtem_cadeia(g, i):
    if obtem_pedra(g, i) == 'O':
        condition = 'O'
    elif obtem_pedra(g, i) == 'X':
        condition = 'X'
    else:
        condition = '.'
    
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
    col_index = ord(obtem_col(i)) - ord('A')
    lin_index = int(obtem_lin(i)) - 1

    g[col_index][lin_index] = p

    return g


def remove_pedra(g, i):
    col_index = ord(obtem_col(i)) - ord('A')
    lin_index = int(obtem_lin(i)) - 1

    g[col_index][lin_index] = '.'

    return g


def remove_cadeia(g, t):
    for i in t:
        col_index = ord(obtem_col(i)) - ord('A')
        lin_index = int(obtem_lin(i)) - 1

        g[col_index][lin_index] = '.'

    return g


def eh_goban(arg):
    if not isinstance(arg, list) or len(arg) not in [9, 13, 19]:
        return False
    for c in range(len(arg)):
        if len(arg[c]) != len(arg[0]) or len(arg[c]) not in [9, 13, 19] or not isinstance(arg[c], list):
            return False
        for l in range(len(arg[c])):
            if arg[c][l] not in ['O', 'X', '.']:
                return False
            
    return True


def eh_intersecao_valida(g, i):
    if not isinstance(i, tuple) or len(i) != 2:
        return False
    
    col = obtem_col(i)
    lin = obtem_lin(i)
    n = len(g)

    if not ord('A') <= ord(col) <= ord('A') + n - 1 or not 1 <= lin <= n:
        return False
    
    return True


def gobans_iguais(g1, g2):
    if not eh_goban(g1) or not eh_goban(g2):
        return False
    
    str_g1 = list(map("".join, g1))
    str_g2 = list(map("".join, g2))
    
    return str_g1 == str_g2


def goban_para_str(g):
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
    territorios = []
    visitadas = set()

    def explorar_territorio(i, territorio):
        visitadas.add(i)
        territorio.add(i)
        vizinhas = obtem_intersecoes_adjacentes(i, obtem_ultima_intersecao(g))
        for vizinha in vizinhas:
            if obtem_pedra(g, vizinha) == '.' and vizinha not in visitadas:
                explorar_territorio(vizinha, territorio)
    
    for col in range(len(g)):
        for lin in range(len(g[0])):
            i = cria_intersecao(chr(ord('A') + col), lin + 1)
            if obtem_pedra(g, i) == '.' and i not in visitadas:
                territorio = set()
                explorar_territorio(i, territorio)
                territorios.append(ordena_intersecoes(tuple(territorio)))

    return ordena_intersecoes(territorios)



def obtem_adjacentes_diferentes(g, t):
    adjacentes = set()

    for i in t:
        vizinhas = obtem_intersecoes_adjacentes(i, obtem_ultima_intersecao(g))
        for vizinha in vizinhas:
            if eh_intersecao_valida(g, vizinha):
                if obtem_pedra(g, i) == '.' and obtem_pedra(g, vizinha) != '.':
                    adjacentes.add(vizinha)
                elif obtem_pedra(g, i) != '.' and obtem_pedra(g, vizinha) == '.':
                    adjacentes.add(vizinha)

    return ordena_intersecoes(tuple(sorted(adjacentes)))



def jogada(g, i, p):
    g = coloca_pedra(g, i, p)
    
    cadeias_adjacentes = []
    for adjacente in obtem_intersecoes_adjacentes(i, obtem_ultima_intersecao(g)):
        if obtem_pedra(g, adjacente) != '.' and obtem_cadeia(g, adjacente) not in cadeias_adjacentes:
            cadeias_adjacentes.append(obtem_cadeia(g, adjacente))
    
    if p == 'X':
        adversario = 'O'
    else:
        adversario = 'X'

    for cadeia in cadeias_adjacentes:
        if obtem_pedra(g, cadeia[0]) == adversario and not tem_liberdade(g, cadeia):
            g = remove_cadeia(g, cadeia)
    
    return g


def tem_liberdade(g, cadeia):
    for intersecao in cadeia:
        adjacentes = obtem_intersecoes_adjacentes(intersecao, obtem_ultima_intersecao(g))
        for adjacente in adjacentes:
            if eh_intersecao_valida(g, adjacente):
                if obtem_pedra(g, adjacente) == cria_pedra_neutra():
                    return True
    return False





def obtem_pedras_jogadores(g):
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
    pontos_branco = 0
    pontos_preto = 0
    
    # Contagem das pedras no tabuleiro
    for linha in g:
        pontos_branco += linha.count('O')
        pontos_preto += linha.count('X')
    
    # Obtenção dos territórios
    territorios = obtem_territorios(g)
    
    # Cálculo dos pontos dos territórios
    for territorio in territorios:
        fronteira_ocupada = True
        
        # Verificar se a fronteira do território pertence apenas ao mesmo jogador
        for intersecao in obtem_adjacentes_diferentes(g, territorio):
            pedra_intersecao = obtem_pedra(g, intersecao)
            if pedra_intersecao != cria_pedra_neutra() and pedra_intersecao != obtem_pedra(g, territorio[0]):
                fronteira_ocupada = False
                break
        
        # Se a fronteira estiver ocupada apenas pelo mesmo jogador, adicionar pontos correspondentes
        if fronteira_ocupada:
            if obtem_pedra(g, territorio[0]) == cria_pedra_branca():
                pontos_branco += len(territorio)
            elif obtem_pedra(g, territorio[0]) == cria_pedra_preta():
                pontos_preto += len(territorio)
    
    return pontos_branco, pontos_preto




def eh_jogada_legal(g, i, p, l):
    # Verificar se a interseção é válida
    if not eh_intersecao_valida(g, i) or obtem_pedra(g, i) != cria_pedra_neutra():
        return False
    
    # Criar cópias temporárias dos gobans
    g_temp = cria_copia_goban(g)
    l_temp = cria_copia_goban(l)
    
    # Colocar a pedra na interseção
    coloca_pedra(g_temp, i, p)
    
    # Verificar Suicídio (a jogada não é legal se a pedra não tem liberdade)
    if not tem_liberdade(g_temp, i):
        return False

    # Verificar Repetição (Ko)
    if gobans_iguais(g_temp, l_temp):
        return False
    
    # Verificar se a jogada cria um estado repetido após a resolução da jogada anterior
    g_anterior = cria_copia_goban(g)
    coloca_pedra(g_anterior, i, p)
    if gobans_iguais(g_anterior, l_temp):
        return False
    
    return True