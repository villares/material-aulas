# Variáveis

Variáveis são nomes que inventamos quando estamos escrevendo um programa, e que apontam para valores na memória do computador. Esses valores podem ser simples como números inteiros (*int*/*integer*), textos (*str*/*string*) ou entidades que chamamos de *objetos*. Em Python, como seŕá possível perceber mais pra frente, todos os valores são objetos, até mesmo os números inteiros!

### Atribuição

Criamos uma variável, e também modificamos o valor para o qual ela aponta usando o operador de atribuição `=`

```python
lado = 50  # cria a variável `lado` que passa a valer 50
rect(10, 10, lado, lado)  # desenha um retângulo com 50 de largura e 50 de altura

nome = 'Guido'
text(nome, 20, 20)  # desenha o texto de `nome` na área de desenho
```
![exemplo 1](assets/variaveis_Guido.png)

```python
a = 10  # cria a variável `a` que passa a valer 10
rect(a, 10, 40, 40)  # desenha um retângulo em x:10, y:10
a = a + 50  # muda o valor de `a` para o valor atual somado de 50 (ou seja 60)
rect(a, 10, 40, 40)  # desenha um retângulo em x:60, y:10
```

### Convenções para os nomes das variáveis

Nomear uma variável é alog a se pensar com cuidado, devemos pensar em algo que descreva os valores para os quais ela vai apontar. Não queremos nem um nome muito longo, que dá preguiça de digitar no programa muitas vezes, nem um nome curto que vamos esquecer daqui alguns dias do que se trata... Veja abaixo algumas regras sintáticas do Python e recomendações estilísticas:

```python
minhaidademental = 13 # correto, mas não muito legível
minhaIdadeMental = 13  # correto, muito usado por programadores Java
minha_idade_mental = 13  # correto, muito usado por Progradores Python
d20 = 19
_idade = 42
x = 100
x_ = 200

# Funciona, mas não recomendado  
MinhaIdadeMental = 13  # Reservamos nomes com a primeira letra maiúscula para 'classes´  
IDADE_MAXIMA = 200  # Costumamos usar só para valores que não vão mudar chamados 'constantes'
_ = 13  # Usamos em alguns casos, quando queremos ignorar um valor

# Não funciona! Incorreto!
minha idade mental = 13 # palavras com espaços 
minha-idade-mental = 13 # palavra com hifens
2020idade_mental = 13 # não pode começar com números! idade_mental_2020 funciona.
a!idade = 13 # só letras e números e _ por favor!
```

### Assuntos relaciodados

- [Escopo de variáveis](escopo_py.md)
- [Valores e seus tipos](tipagem_py.md)
- [Qual a diferença entre `=` (atribuição) e `==` (comparação)?](/Processing-Python/atribuicao-e-comparacao.md)
