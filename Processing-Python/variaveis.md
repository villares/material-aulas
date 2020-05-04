# Variáveis

Variáveis são nomes que inventamos quando estamos escrevendo um programa, e que apontam para valores na memória do computador. Esses valores podem ser simples como números inteiros (*int*) ou entidades que chamamos de *objetos*. Em Python, como seŕá possível perceber mais pra frente, todos os valores são objetos, até mesmo os números inteiros!

### Convenções para os nomes das variáveis

Nomear uma variável é uma arte, não queremos nem um nome muito longo que dá preguiça de digitar, nem um nome curto que vamos esquecer daqui alguns dias do que se trata... Veja abaixo algumas regras sintáticas do Python e recomendações estilísticas

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
```
