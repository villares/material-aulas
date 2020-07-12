## Vetores

Vetores no fundo são são listas de números, algo como `[105, 42]` ou `[120, 81, 35]`. Os números são os *componentes* e os vetores, que podem ter o número de componentes que você quiser, mas nos interessam mais neste momento os vetores com 2 ou 3 componentes pois eles são úteis para representar coordenadas, velocidades e acelerações em duas e três dimensões. 

Podemos visualizá-los como pontos ou como segmentos de reta orientados (como uma seta!).







> <sub> É possível trabalhar com vetores de muito mais dimensôes, que não são fáceis de visualizar, mas são muito usados em computação científica, da álgebra linear à representação de palavras para processamento de linguagem natural e tradução automatizada.</sub> 

#### `PVector`

Os vetores 2-D e 3-D, de duas e três dimensões, podem ser expressos no Processing como objetos da classe `PVector`, construídos com `PVector(x, y)`e `PVector(x, y, z)`, respectivamente. Acredito que em breve você vai concordar comigo que essa classe vai facilitar muito fazer operações, contas e transformações, com vetores, o que é especialmente útil para animar partículas e calcular diversas geometrias.





É possível somar e subtrair vetores somando os componentes de cada um nas mesmas posições, é fácil também multiplicar ou dividir um vetor por um número comum, multiplicando cada componente pelo número (e isso multiplica ou divide a magnitude do vetor). Já para multiplicar vetores entre si tem mais de uma maneira de fazer, o chamado produto escalar (*dot product*) e o produto vetorial (*cross product*). Mas podemos pedir para o computador fazer para nós essas operações!

