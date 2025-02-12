# FP 23/24 - Projeto 2
**Filipe Oliveira**  
**Número de estudante**: ist1110633

## Descrição do Projeto
O seguinte código permite jogar um jogo completo de Go de dois jogadores. Contém um conjunto de tipos abstratos de dados que são utilizados para manipular a informação necessária no decorrer do jogo, bem como um conjunto de funções adicionais.

## Descrição do Jogo Go
O **Go** é um jogo de tabuleiro de estratégia para dois jogadores. Os jogadores colocam alternadamente pedras da sua cor no tabuleiro. O objetivo é formar territórios ao redor de regiões vazias no tabuleiro. Ganha quem atingir a maior pontuação, ou seja, quem controlar um território maior.

## Termos

### Goban
- Tabuleiro de Go, estrutura retangular de **n x n** linhas (n pode ser 9, 13 ou 19).

### Interseção
- Ponto no **goban** onde as linhas se cruzam, identificadas por uma letra maiúscula de A a S, e por um número de 1 a 19.

### Pedra
- Branca ou preta, dependendo do jogador.

### Interseções adjacentes
- Interseções conectadas por uma linha vertical/horizontal sem outras interseções entre elas.

### Interseção livre
- Interseção não ocupada por uma pedra.

### Interseção ocupada
- Interseção ocupada por uma pedra.

### Ordem de leitura
- Da esquerda para a direita, seguida de baixo para cima.

### Interseções conectadas
- Interseções com pedras do mesmo tipo em que é possível traçar um percurso entre elas, passando sempre por interseções do mesmo tipo.

### Cadeia de pedras
- Conjunto de uma ou mais interseções ocupadas por pedras da mesma cor conectadas entre si e não conectadas a nenhuma outra pedra da mesma cor.

### Liberdades de uma pedra
- Conjunto de interseções livres adjacentes a essa pedra ou adjacente a uma pedra da mesma cadeia.

### Território
- Conjunto maximal de uma ou mais interseções livres que estão todas conectadas entre si e que não estão conectadas a nenhuma outra interseção livre.

### Fronteira de um território
- Conjunto de todas as interseções ocupadas por pedras adjacentes a um território.

### Território de um jogador
- A sua fronteira está ocupada apenas por pedras da cor desse jogador.

---

## Regras do Jogo

1. No início do jogo, o tabuleiro está vazio.
2. O jogador com pedras **pretas** é o primeiro a jogar.
3. Os jogadores alternam em turnos subsequentes.
4. No seu turno, um jogador pode passar a vez ou jogar.
5. Uma jogada consiste nas seguintes etapas, realizadas em ordem:
    a) **Colocar**: Coloca uma pedra da sua cor numa interseção vazia.  
    b) **Capturar**: Retira do tabuleiro quaisquer pedras da cor do oponente que não tenham liberdades.
6. As pedras **não podem ser movidas** para outra interseção após serem jogadas.
7. As seguintes restrições devem ser consideradas na colocação das pedras:
    a) **Suicídio**: Ilegal se uma ou mais pedras da cor do jogador ficarem sem liberdades após a resolução da jogada.  
    b) **Repetição (ko)**: Ilegal se tiver o efeito de criar um estado do tabuleiro que ocorreu anteriormente no jogo.
8. O **jogo termina** quando ambos os jogadores tiverem passado a vez consecutivamente.
9. A **pontuação** de um jogador é obtida como a soma do número total de interseções que:
    a) Pertencem ao território desse jogador.  
    b) Estão ocupadas por uma pedra da cor daquele jogador.
10. **Ganha** o jogador com maior pontuação.
11. Em caso de **empate**, o jogador **branco** é o vencedor.