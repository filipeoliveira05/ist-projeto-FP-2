'''
FP 23/24 Projeto 2
Filipe Oliveira, ist1110633

Descrição do projeto:
O seguinte código permite jogar um jogo completo de Go de dois jogadores.
Contém um conjunto de tipos abstratos de dados que são utilizados para manipular
informação necessária no decorrer do jogo, bem como um conjunto de funções adicionais.

Descrição do jogo Go:
Jogo de tabuleiro de estratégia para dois jogadores.
Os jogadores colocam alternadamente pedras da sua cor no tabuleiro.
O objetivo é formar territórios ao redor de regiões vazias no tabuleiro.
Ganha quem atingir a maior pontuação, ou seja. quem controlar um território maior.

Termos:
--> Goban) tabuleiro de Go, estrutura retangular de n x n linhas (n pode ser 9, 13 ou 19).
--> Interseção) ponto no goban onde as linhas se cruzam, identificadas por uma letra maiúscula de A a S, e por um número de 1 a 19.
--> Pedra) Branca ou preta, dependendo do jogador.
--> Interseções adjacentes) interseções conectadas por uma linha vertical/horizontal sem outras interseções entre elas.
--> Interseção livre) interseção não ocupada por uma pedra.
--> Interseção ocupada) interseção ocupada por uma pedra.
--> Ordem de leitura) da esquerda para a direita, seguida de baixo para cima.
--> Interseções conectadas) interseções com pedras do mesmo tipo em que é possível traçar um percurso entre elas, passando sempre por interseções do mesmo tipo.
--> Cadeia de pedras) conjunto de uma ou mais interseções ocupadas por pedras da mesma cor conectadas entre si e não conectadas a nenhuma outra pedra da mesma cor.
--> Liberdades de uma pedra) conjunto de interseções livres adjacentes a essa pedra ou adjacente a uma pedra da mesma cadeia.
--> Território) conjunto maximal de uma ou mais interseções livres que estão todas conectadas entre si e que não estão conectadas a nenhuma outra interseção livre.
--> Fronteira de um território) conjunto de todas as interseções ocupadas por pedras adjacentes a um território.
--> Território de um jogador) a sua fronteira está ocupada apenas por pedras da cor desse jogador. 

Regras do jogo:
1. No início do jogo, o tabuleiro está vazio.
2. O jogador com pedras pretas é o primeiro a jogar.
3. Os jogadores alternam em turnos subsequentes.
4. No seu turno, um jogador pode passar a vez ou jogar.
5. Uma jogada consiste na seguintes etapas, realizadas em ordem:
    a) Colocar: coloca uma pedra da sua cor numa interseção vazia.
    b) Capturar: retira do tabuleiro quaisquer pedras da cor do oponente que não tenham liberdades.
6. As pedras não podem ser movidas para outra interseção após serem jogadas.
7. As seguintes restrições devem ser consideradas na colocação das pedras:
    a) Suicídio: ilegal se uma ou mais pedras da cor do jogador ficarem sem liberdades após a resolução da jogada.
    b) Repetição (ko): ilegal se tiver o efeito de criar um estado do tabuleiro que ocorreu anteriormente no jogo.
8. Jogo termina quando ambos os jogadores tiverem passado a vez consecutivamente.
9. A pontuação de um jogador é obtida como a soma do número total de interseções que:
    a) Pertencem ao território desse jogador.
    b) Estão ocupadas por uma pedra da cor daquele jogador.
10. Ganha o jogador com maior pontuação.
11. Em caso de empate, o jogador branco é o vencedor.
'''


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

    #verifica a validade do caracter correspondente à coluna.
    if not isinstance(col, str) or not ord('A') <= ord(col) <= ord('S') or len(col) != 1:
        raise ValueError('cria_intersecao: argumentos invalidos')
    
    #verifica a validade dp inteiro correspondente à linha
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
    
    #verifica a validade do argumento, de modo a ser um TAD intersecao.
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

    #verifia se as colunas e linhas de cada interseção são iguais
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
    
    #obtém a coluna e linha do argumento.
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
    
    #obtém a coluna e linha da interseção.
    col = obtem_col(i)
    lin = obtem_lin(i)
    i_adjacents = []
    
    #obtém as quatro interseções adjacentes possíveis, independentemente de serem válidas no goban.
    i_adjacents_possible = [
        (chr(ord(col)), lin - 1),
        (chr(ord(col) - 1), lin),
        (chr(ord(col) + 1), lin),
        (chr(ord(col)), lin + 1),
    ]
    
    #verifica, entre as quatro interseções adjacentes possíveis, quais delas são válidas no goban.
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

    #se o tuplo dado estiver vazio, retorna um tuplo vazio
    if len(t) == 0:
        return ()
    
    #ordena primeiro pelo número da linha, e depois pela letra da coluna
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

    #verifica se o arguumento é uma das pedras possíveis
    return arg in [cria_pedra_branca(), cria_pedra_preta(), cria_pedra_neutra()]



def eh_pedra_branca(p):
    """
    Devolve True caso a pedra p seja do jogador branco e False caso contrário.

    :param p: pedra
    :return: True/False (bool)
    """

    #verifica se é pedra e se é branca
    return eh_pedra(p) and p == cria_pedra_branca()



def eh_pedra_preta(p):
    """
    Devolve True caso a pedra p seja do jogador preto e False caso contrário.

    :param p: pedra
    :return: True/False (bool)
    """

    #verifica se é pedra e se é preta
    return eh_pedra(p) and p == cria_pedra_preta()



def pedras_iguais(p1, p2):
    """
    Devolve True apenas se p1 e p2 são pedras e são iguais.

    :param p1: argumento (universal)
    :param p2: argumento (universal)
    :return: True/False (bool)
    """

    #verifica se são pedras e se são iguais
    return eh_pedra(p1) and eh_pedra(p2) and p1 == p2



def pedra_para_str(p):
    """
    Devolve a cadeia de caracteres que representa o jogador dono da pedra.
    Devolve 'O', 'X' ou '.' para pedras do jogador branco, preto ou neutra respetivamente.

    :param p: pedra
    :return: cadeia de caracteres (str)
    """

    #verifica o tipo de pedra dada.
    if p == cria_pedra_branca():
        return 'O'
    elif p == cria_pedra_preta():
        return 'X'
    else:
        return '.'



def eh_pedra_jogador(p):
    """
    Devolve True caso a pedra p seja de um jogador e False caso contrário.

    :param p: pedra
    :return: True/False (bool)
    """

    #verifica se é pedra branca ou preta
    return eh_pedra_branca(p) or eh_pedra_preta(p)




#TAD Goban
def cria_goban_vazio(n):
    """
    Devolve um goban de tamanho n x n, sem interseções ocupadas.
    Caso o argumento não seja válido, gera um erro.

    :param n: dimensão do goban (int)
    :return: goban
    """

    #verifica se a dimensão do goban é válida
    if n not in [9, 13, 19]:
        raise ValueError('cria_goban_vazio: argumento invalido')
    
    #cria um goban vazio, representado como uma lista de listas.
    col = [cria_pedra_neutra(),] * int(n)
    g_empty = [col[:] for _ in range(int(n))]
    
    return g_empty



def cria_goban(n, ib, ip):
    """
    Devolve um goban de tamanho n x n, com as interseções dos tuplos ib e ip ocupadas por pedras brancas e pretas, respetivamente.
    Caso os argumentos não sejam válidos, gera um erro.
    
    :param n: dimensão do goban (int)
    :param ib: tuplo de interseções 'brancas' (tuple)
    :param ip: tuplo de interseções 'pretas' (tuple)
    :return: goban
    """

    #verifica se a dimensão do goban é válida e se os argumentos ib e ip são tuplos.
    if n not in [9, 13, 19] or not isinstance(ib, tuple) or not isinstance(ip, tuple):
        raise ValueError('cria_goban: argumentos invalidos')
    
    # Verifica se existem elementos iguais em ib.
    el_ib = set()
    for el in ib:
        if el in el_ib:
            raise ValueError('cria_goban: argumentos invalidos')
        el_ib.add(el)

    # Verifica se existem elementos iguais em ip.
    el_ip = set()
    for el in ip:
        if el in el_ip:
            raise ValueError('cria_goban: argumentos invalidos')
        el_ip.add(el)

    # Verifica se existem elementos iguais em ambos os tuplos.
    if el_ib & el_ip:
        raise ValueError('cria_goban: argumentos invalidos')

    g = cria_goban_vazio(n)

    #preenche as interseções do tuplo ib com pedras brancas.
    for b in tuple(ib):
        col_index = ord(obtem_col(b)) - ord('A')
        lin_index = int(obtem_lin(b)) - 1
        if 0 <= col_index < n and 0 <= lin_index < n:
            g[col_index][lin_index] = cria_pedra_branca()

    #preenche as interseções do tuplo ip com pedras pretas.
    for p in tuple(ip):
        col_index = ord(obtem_col(p)) - ord('A')
        lin_index = int(obtem_lin(p)) - 1
        if 0 <= col_index < n and 0 <= lin_index < n:
            g[col_index][lin_index] = cria_pedra_preta()
    
    return g



def cria_copia_goban(t):
    """
    Recebe um goban.
    Devolve uma cópia do goban.

    :param t: goban
    :return: goban
    """

    #deep copy do goban dado.
    return [x if not isinstance(x, list) else x[:] for x in t]



def obtem_ultima_intersecao(g):
    """
    Recebe um goban.
    Devolve a intersecao que corresponde ao canto superior direito do goban.

    :param g: goban
    :return: interseção
    """

    #obtém coluna e linha da última interseção do goban.
    n = len(g)
    col = chr(ord('A') + n - 1)
    lin = n

    return (col, lin)



def obtem_pedra(g, i):
    """
    Recebe um goban e uma interseção.
    Devolve a pedra na interseção i do goban g.
    Caso a interseção não esteja ocupada, devolve uma pedra neutra.

    :param g: goban
    :param i: interseção
    :return: pedra
    """
    
    #obtém a coluna e linha da interseção
    col_index = ord(obtem_col(i)) - ord('A')
    lin_index = int(obtem_lin(i)) - 1
    
    p = g[col_index][lin_index]

    #verifica o tipo de pedra na interseção
    if eh_pedra_branca(p):
        return cria_pedra_branca()
    elif eh_pedra_preta(p):
        return cria_pedra_preta()
    else:
        return cria_pedra_neutra()



def obtem_cadeia(g, i):
    """
    Recebe um goban e uma interseção.
    Devolve o tuplo de interseções, em ordem de leitura, das pedras da mesma cor que formam a cadeia que passa pela interseção i.
    Se a posição não estiver ocupada, devolve a cadeia de interseções livres.

    :param g: goban
    :param i: interseção
    :return: interseções da cadeia (tuple)
    """

    #armazena o tipo da interseção (branca/preta/neutra)
    if obtem_pedra(g, i) == cria_pedra_branca():
        condition = cria_pedra_branca()
    elif obtem_pedra(g, i) == cria_pedra_preta():
        condition = cria_pedra_preta()
    else:
        condition = cria_pedra_neutra()
    
    #lista final que armazena as interseções da cadeia
    chain = []

    #lista com as interseções por 'validar', antes de poder entrar na lista final
    queue = [i]

    
    while queue:
        #remove a última interseção da queue e adiciona à chain
        i = queue.pop()
        chain.append(i)
        #obtém as interseções adjacentes à interseção atual
        for i_new in obtem_intersecoes_adjacentes(i, obtem_ultima_intersecao(g)):
            #se a interseção adjacente for do mesmo tipo e ainda não tiver na lista para 'validar', é adicionada ao queue
            if obtem_pedra(g, i_new) == condition and i_new not in chain + queue:
                queue.append(i_new)
        #processo repete-se até a queue não ter nenhum elemento

    return ordena_intersecoes(tuple(chain))



def coloca_pedra(g, i, p):
    """
    Recebe um goban, uma interseção e uma pedra.
    Modifica destrutivamente o goban g colocando a pedra do jogador p na interseção i, devolvendo o próprio goban.

    :param g: goban
    :param i: interseção
    :param p: pedra
    :return: goban
    """

    #obtém a coluna e linha da interseção
    col_index = ord(obtem_col(i)) - ord('A')
    lin_index = int(obtem_lin(i)) - 1
    n = len(g) 

    #coloca a pedra na interseção, caso seja válida
    if 0 <= col_index < n and 0 <= lin_index < n:
        g[col_index][lin_index] = p

    return g



def remove_pedra(g, i):
    """
    Recebe um goban e uma interseção.
    Modifica destrutivamente o goban g, removendo a pedra da interseção i, devolvendo o próprio goban.

    :param g: goban
    :param i: interseção
    :return: goban
    """

    #obtém a coluna e linha da interseção
    col_index = ord(obtem_col(i)) - ord('A')
    lin_index = int(obtem_lin(i)) - 1
    n = len(g)

    #remove a pedra na interseção, caso seja válida
    if 0 <= col_index < n and 0 <= lin_index < n:
        g[col_index][lin_index] = cria_pedra_neutra()

    return g



def remove_cadeia(g, t):
    """
    Recebe um goban e um tuplo de interseções.
    Modifica destrutivamente o goban g, removendo as pedras nas interseções do tuplo t, devolvendo o próprio goban.

    :param g: goban
    :param t: tuplo de interseções (tuple)
    :return: goban
    """
    
    #por cada interseção no tuplo, remove a pedra presente
    for i in t:
        remove_pedra(g, i)

    return g



def eh_goban(arg):
    """
    Devolve True caso o argumento seja um TAD goban e False caso contrário.

    :param arg: argumento (universal)
    :return: True/False (bool)
    """

    #verifica se o argumento corresponde a um goban
    if not isinstance(arg, list) or len(arg) not in [9, 13, 19]:
        return False
    
    #verifica se cada elemento dentro do argumento corresponde a colunas válidas do goban 
    for c in range(len(arg)):
        if len(arg[c]) != len(arg[0]) or len(arg[c]) not in [9, 13, 19] or not isinstance(arg[c], list):
            return False
        #verifica se cada elemento dentro das colunas corresponde a pedras
        for l in range(len(arg[c])):
            if arg[c][l] not in [cria_pedra_branca(), cria_pedra_preta(), cria_pedra_neutra()]:
                return False
            
    return True



def eh_intersecao_valida(g, i):
    """
    Recebe um goban, g, e uma interseção, i.
    Devolve True se i é uma interseção válida dentro do goban e False caso contrário.

    :param g: goban
    :param i: interseção
    :return: True/False (bool)
    """

    #verifica se o argumento é uma interseção
    if not isinstance(i, tuple) or len(i) != 2:
        return False
    
    #obtém a coluna e linha da interseção
    col = obtem_col(i)
    lin = obtem_lin(i)
    n = len(g)

    #verifica se a coluna e linha são válidas
    if not ord('A') <= ord(col) <= ord('A') + n - 1 or not 1 <= lin <= n:
        return False
    
    return True



def gobans_iguais(g1, g2):
    """
    Recebe dois gobans, g1 e g2.
    Devolve True apenas se g1 e g2 forem gobans e forem iguais.

    :param g1: primeiro goban
    :param g2: segundo goban
    :return: True/False (bool)
    """

    #verifica se ambos os argumentos são gobans
    if not eh_goban(g1) or not eh_goban(g2):
        return False
    
    #armazena cada elemento dentro de cada goban, para os comparar posteriormente
    str_g1 = list(map("".join, g1))
    str_g2 = list(map("".join, g2))
    
    return str_g1 == str_g2



def goban_para_str(g):
    """
    Recebe um goban g.
    Devolve a cadeia de caracteres que representa o goban.

    :param g: goban
    :return: cadeia de caracteres (str)
    """

    LETTERS = tuple('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    #obtém o número de colunas e linhas do goban
    n_c, n_l = len(g), len(g[0])

    #variável que armazena a representação final do goban
    #inicialmente apenas com as letras das colunas da parte superior do goban
    cad = '   ' + ''.join(f'{l} ' for l in LETTERS[:n_l]).rstrip() + '\n'

    #itera pelas linhas do goban de cima para baixo
    for i in range(n_c - 1, -1, -1):
        #adiciona o número da linha com espaço à esquerda
        cad += '{:>2} '.format(i + 1)
        
        #itera pelas colunas do goban
        for j in range(n_l):
            #obtém o estado da pedra na interseção atual, e adiciona-o à cadeia
            estado_pedra = obtem_pedra(g, f'{LETTERS[j]}{i + 1}')
            cad += estado_pedra + ' '
        #adiciona o número da linha com espaço à direita
        cad += '{:>2}\n'.format(i + 1)
    
    #adiciona as letras das colunas na parte inferior do goban
    cad += '   ' + ''.join(f'{l} ' for l in LETTERS[:n_l]).rstrip()
    
    return cad



def obtem_territorios(g):
    """
    Recebe um goban g.
    Devolve o tuplo formado pelos tuplos com as interseções de cada território de g.
    Devolve as interseções de cada território ordenadas em ordem de leitura do tabuleiro de Go.
    Devolve os territórios ordenados em ordem de leitura da primeira interseção do território.

    :param g: goban
    :return: tuplo com territórios (tuple)
    """

    #lista que armazena os territóris encontrados
    territorios = []

    #conjunto que armazena as interseções já visitadas
    visitadas = set()

    def explorar_territorio(i, territorio):
        """
        Função auxiliar para explorar um território a partir de uma interseção.

        :param i: interseção
        :param territorio: território 
        """

        #marca a interseção como visitada e adiciona-a ao território
        visitadas.add(i)
        territorio.add(i)

        #obtém interseções adjacentes à interseção atual
        adjacentes = obtem_intersecoes_adjacentes(i, obtem_ultima_intersecao(g))
        
        #itera pelas interseções adjacentes
        for adjacente in adjacentes:
            #se a interseção adjacente estiver vazia e não foi 'visitada', explora o território a partir dela
            if obtem_pedra(g, adjacente) == cria_pedra_neutra() and adjacente not in visitadas:
                explorar_territorio(adjacente, territorio)
    
    #itera pelas iterseções do goban
    for col in range(len(g)):
        for lin in range(len(g[0])):
            #cria uma interseção a partir da coluna e linha atual
            i = cria_intersecao(chr(ord('A') + col), lin + 1)

            #se a interseção estiver vazia e se ainda não foi 'visitada', explora o território a partir dela
            if obtem_pedra(g, i) == cria_pedra_neutra() and i not in visitadas:
                territorio = set()
                explorar_territorio(i, territorio)

                #adiciona as interseções do território à lista final de territórios
                territorios.append(ordena_intersecoes(tuple(territorio)))

    return ordena_intersecoes(territorios)



def obtem_adjacentes_diferentes(g, t):
    """
    Recebe um goban, g, e um tuplo com interseções, t.
    Devolve o tuplo ordenado formado pelas interseções adjacentes às interseções do tuplo t:
        a) livres, se as interseções do tuplo t estão ocupadas por pedras de jogador (liberdades de uma cadeia de pedras).
        b) ocupadas por pedras de jogador, se as interseções do tuplo t estão livres (fronteira de um terrritório).

    :param g: goban
    :param t: tuplo com interseções (tuple)
    :return: tuplo com interseções (tuple)
    """

    #conjunto que armazena interseções adjacentes diferentes
    adjacentes_diferentes = set()

    #itera pelas interseções do tuplo dado
    for i in t:
        #obtém as interseções adjacentes à interseção atual
        adjacentes = obtem_intersecoes_adjacentes(i, obtem_ultima_intersecao(g))

        #itera pelas interseções adjacentes
        for adjacente in adjacentes:
            #verifica se a interseção adjacente é válida
            if eh_intersecao_valida(g, adjacente):
                #se a interseção do tuplo estiver vazia e a adjacente não, ou vice-versa, adiciona a adjacente ao conjunto final
                if obtem_pedra(g, i) == cria_pedra_neutra() and obtem_pedra(g, adjacente) != cria_pedra_neutra():
                    adjacentes_diferentes.add(adjacente)
                elif obtem_pedra(g, i) != cria_pedra_neutra() and obtem_pedra(g, adjacente) == cria_pedra_neutra():
                    adjacentes_diferentes.add(adjacente)

    return ordena_intersecoes(tuple(sorted(adjacentes_diferentes)))



def jogada(g, i, p):
    """
    Recebe um goban, g, uma interseção, i, e uma pedra de jogador, p.
    Modifica destrutivamente o goban g, colocando a pedra de jogador p na interseção i.
    Remove todas as pedras do jogador contrário pertencentes a cadeias adjacentes à interseção sem liberdades.
    Devolve o próprio goban.

    :param g: goban
    :param i: interseção
    :param p: pedra
    :return: goban alterado
    """

    #coloca a pedra dada na interseção dada
    g = coloca_pedra(g, i, p)
    
    #lista para armazenar cadeias adjacentes à interseção i
    cadeias_adjacentes = []

    #obtém interseções adjacentes à interseção i, e itera por elas
    for adjacente in obtem_intersecoes_adjacentes(i, obtem_ultima_intersecao(g)):
        #se a interseção adjacente não estiver vazia e se a sua cadeia não estiver na lista de cadeias adjacentes, adiciona-a a essa lista
        if obtem_pedra(g, adjacente) != cria_pedra_neutra() and obtem_cadeia(g, adjacente) not in cadeias_adjacentes:
            cadeias_adjacentes.append(obtem_cadeia(g, adjacente))
    
    #determina o adversário do jogador atual
    if p == cria_pedra_preta():
        adversario = cria_pedra_branca()
    else:
        adversario = cria_pedra_preta()

    #remove cadeias do adversário sem liberdades, através da função auxiliar tem_liberdade
    for cadeia in cadeias_adjacentes:
        if obtem_pedra(g, cadeia[0]) == adversario and not tem_liberdade(g, cadeia):
            g = remove_cadeia(g, cadeia)
    
    return g


def tem_liberdade(g, cadeia):
    """
    Recebe um goban g e uma cadeia de pedras do goban.
    Devolve True se a cadeia de pedras têm liberdade, e False caso contrário.

    :param g: goban
    :param cadeia: cadeia de pedras
    :return: True/False (bool)
    """

    #itera pelas interseções da cadeia
    for intersecao in cadeia:
        #obtém as interseções adjacentes à interseção atual
        adjacentes = obtem_intersecoes_adjacentes(intersecao, obtem_ultima_intersecao(g))

        #itera pelas interseções adjacentes
        for adjacente in adjacentes:
            #verifica se a interseção adjacente é válida
            if eh_intersecao_valida(g, adjacente):
                #se a interseção adjacente está vazia, a cadeia tem liberdade e retorna True
                if obtem_pedra(g, adjacente) == cria_pedra_neutra():
                    return True
    
    #se não houver interseções adjacentes vazias, a cadeia não tem liberdade e retorna False
    return False



def obtem_pedras_jogadores(g):
    """
    Recebe um goban, g.
    Devolve um tuplo de dois inteiros:
        1º inteiro) número de interseções ocupadas por pedras do jogador branco.
        2º inteiro) número de interseções ocupadas por pedras do jogador preto.

    :param g: goban
    :return: tuplo de dois inteiros (tuple)
    """

    #variáveis que armazenam o número de pedras que cada jogador tem
    p_b = 0
    p_p = 0

    #itera pelas interseções do goban
    for col in g:
        for i in col:
            #contabiliza o número de pedras de cada cor nas interseções do goban
            if i == cria_pedra_branca():
                p_b += 1
            elif i == cria_pedra_preta():
                p_p += 1

    return (p_b, p_p)




#Funções adicionais
def calcula_pontos(g):
    """
    Recebe um goban, g.
    Devolve um tuplo de dois inteiros:
        1º inteiro) pontuação do jogador branco.
        2º inteiro) pontuação do jogador preto.

    :param g: goban
    :return: tuplo de dois inteiros (tuple)
    """

    #obtém a última interseção do goban para determinar a dimensão do mesmo
    i_u = obtem_ultima_intersecao(g)
    n = i_u[1]

    #se o goban estiver vazio, a pontuação é nula para ambos os jogadores
    if g == cria_goban_vazio(n):
        return (0,0)
    
    #obtém o número de pedras brancas e pretas no goban, adicionando-o à pontuação final
    pedras = obtem_pedras_jogadores(g)
    pontos_branco = pedras[0]
    pontos_preto = pedras[1]
    
    #obtém os territórios do goban, iterando por eles
    territorios = obtem_territorios(g)
    for territorio in territorios:
        #obtém as interseções adjacentes diferentes de cada território
        fronteira = obtem_adjacentes_diferentes(g, territorio)
        
        #verifica se todas as interseções da fronteira são do mesmo tipo
        mesma_cor = all(obtem_pedra(g, i) == obtem_pedra(g, fronteira[0]) for i in fronteira)
        
        #se a fronteira for do mesmo tipo e for 'branca', adiciona pontos ao jogador branco
        if mesma_cor and obtem_pedra(g, fronteira[0]) == cria_pedra_branca():
            pontos_branco += len(territorio)

        #se a fronteira for do mesmo tipo e for 'preta', adiciona pontos ao jogador preto
        elif mesma_cor and obtem_pedra(g, fronteira[0]) == cria_pedra_preta():
            pontos_preto += len(territorio)
    
    return (pontos_branco, pontos_preto)



def eh_jogada_legal(g, i, p, l):
    """
    Recebe um goban, g, uma interseção, i, uma pedra de jogador, p, e um outro goban, l.
    Devolve True se a jogada for legal ou False caso contrário, sem modificar g ou l.
    O goban l representa o estado do tabuleiro que não pode ser obtido após a resolução completa da jogada.

    :param g: goban
    :param i: interseção
    :param p: pedra
    :param l: goban que não pode ser obtido
    :return: True/False (bool)
    """

    #verifica se a interseção dada é válida e está vazia
    if not eh_intersecao_valida(g, i) or obtem_pedra(g, i) != cria_pedra_neutra():
        return False
    
    #verifica se a jogada resulta em suicídio (deixar a cadeia sem liberdades), através de uma cópia do goban
    g_copia = cria_copia_goban(g)
    g_copia = jogada(g_copia, i, p)
    cadeia = obtem_cadeia(g_copia, i)
    if not tem_liberdade(g_copia, cadeia):
        return False
    
    #verifica se a jogada repete o estado anterior do tabuleiro (repetição, ko)
    if gobans_iguais(g_copia, l):
        return False
    
    return True



def turno_jogador(g, p, l):    
    """
    Recebe um goban, g, uma pedra de jogador, p, e um outro goban, l.
    Oferece ao jogador das pedras p a opção de passar ou de colocar uma pedra própria numa interseção.
    Se o jogador passar, devolve False, sem modificar os argumentos.
    Se o jogador não passar, devolve True, modificando destrutivamente g, de acordo com a jogada realizada.
    Apresenta uma mensagem até que o jogador introduza:
        a)'P' (passar)
        ou
        b) representação externa de uma interseção do goban que corresponda a uma jogada legal.
    O goban l representa o estado do tabuleiro que não pode ser obtido após a resolução completa da jogada.

    :param g: goban
    :param p: pedra
    :param l: goban que não pode ser obtido
    :return: True/False (bool)
    """

    #loop até que o jogador passe ou faça uma jogada válida
    while True:
        #mensagem apresentada
        move = input(f"Escreva uma intersecao ou 'P' para passar [{pedra_para_str(p)}]:").strip().upper()

        #caso so jogador decidir passar
        if move == 'P':
            return False
        
        #caso do jogador decidir fazer uma jogada válida
        elif eh_intersecao_valida(g, str_para_intersecao(move)) and eh_jogada_legal(g, str_para_intersecao(move), p, l):
            jogada(g, str_para_intersecao(move), p)
            return True



def go(n, tb, tp):
    """
    Permite jogar um jogo completo de Go de dois jogadores.
    Recebe um inteiro (dimensão do tabuleiro), n, e dois tuplos, tb e tp, potencialmente vazios:
        tb) contém a representação externa das interseções ocupadas por pedras brancas;
        tp) contém a representação externa das interseções ocupadas por pedras pretas.
    O jogo termina quando os dois jogadores passam a vez de jogar consecutivamente.
    Devolve True se o jogador das pedras brancas conseguir ganhar o jogo, ou False caso contrário.
    Caso os argumentos não sejam válidos, gera um erro.

    :param n: dimensão do goban (int) 
    :param tb: tuplo de interseções 'brancas' (tuple)
    :param tp: tuplo de interseções 'pretas' (tuple)
    :return: True/False (bool)
    """

    #cria o estado inicial do goban, gerando um erro caso os argumentos não sejam válidos
    try:
        g = cria_goban(n, tb, tp)
    except ValueError:
        raise ValueError('go: argumentos invalidos')
    
    #representação da pedra branca e preta
    jogador_branco = cria_pedra_branca()
    jogador_preto = cria_pedra_preta()

    #estado do goban antes da última jogada
    ultimo_estado = None

    while True:
        #mostra a pontuação e o estado atual do goban
        pontos = calcula_pontos(g)
        pontos_branco = pontos[0]
        pontos_preto = pontos [1]
        print(f"Branco (O) tem {pontos_branco} pontos")
        print(f"Preto (X) tem {pontos_preto} pontos")
        print(goban_para_str(g))
        
        #turno do jogador preto
        turno_preto = turno_jogador(g, jogador_preto, ultimo_estado)
        if not turno_preto:
            break

        #mostra a pontuação e o estado atual do goban, após a jogada do jogador preto
        pontos = calcula_pontos(g)
        pontos_branco = pontos[0]
        pontos_preto = pontos [1]
        print(f"Branco (O) tem {pontos_branco} pontos")
        print(f"Preto (X) tem {pontos_preto} pontos")
        print(goban_para_str(g))
        
        #turno do jogador branco
        turno_branco = turno_jogador(g, jogador_branco, ultimo_estado)
        if not turno_branco:
            break
        
        #atualiza o último estado do goban antes da próxima jogada
        ultimo_estado = cria_copia_goban(g)

    #calcula a pontuação final e determina o vencedor
    pontos = calcula_pontos(g)
    pontos_branco = pontos[0]
    pontos_preto = pontos [1]

    return pontos_branco > pontos_preto