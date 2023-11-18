# Métodos dos objetos *string*

*Strings* são um *tipo* de dado armazenado na memória do computador para representar texto (uma sequência de caracteres) e, mais que isso, em Python, são acompanhados de uma série de funções que podem ser acionadas com a *sintaxe do ponto* (*dot syntax*).

<sub>Na programação orientada a objetos vemos que funções atreladas a objetos de uma classe são conhecidas como métodos.</sub>

## Convertendo caixa alta e baixa (maiúsculas e minúsculas)

```python
# str.lower() devolve string com a versão em caixa baixa
print('Alexandre'.lower())  # exibe: alexandre

# str.upper() devolve string com a versão em caixa alta
print('Alexandre'.upper())  # exibe: ALEXANDRE
```

## Checando prefixos e sufixos

```python
# str.startswith(prefixo) informa se o texto inicia com um certo prefixo
nome_arquivo = "imagem1212.jpg"
print(nome_arquivo.startswith("image"))  # exibe: True
print(nome_arquivo.startswith("a"))  # exibe: False

# str.endswith(sufixo) informa se o texto termina com um certo sufixo
nome_arquivo = "imagem3434.jpg"
print(nome_arquivo.endswith(".jpg"))  # exibe: True
print(nome_arquivo.endswith(".gif"))  # exibe: False
```

É possível 'encadear' métodos, como no exemplo abaixo.

```python
# identifica arquivos que terminam tanto com .png como com .PNG
if nome_arquivo.lower().endswith('.png'):
     print("Arquivo tipo PNG")
```

## Procurando sub-strings

Trecho da documentação:

> `str.find(sub[, start[, end]])`
> Retorna o índice mais baixo na String onde a substring sub é encontrado dentro da fatia s[start:end]. Argumntos opcionais como start e end são interpretados como umanotação de fatiamento. Retorna - 1 se sub não for localizado. Nota: O método find() deve ser usado apenas se precisarmos conhecer a posição de sub. Para verificar se sub é ou não uma substring, use o operador `in`.
>
> `str.count(sub[, start[, end]])`
> Retorna o número de ocorrências da sub-string sub que não se sobrepõem no intervalo[start, end]. Argumentos opcionais start e end são interpretados como na notação de fatias.

## Dividindo e juntando *strings*

```python
# str.split(delimitador_opcional) devolve uma lista cujos itens são trechos do texto "divididos"
# Confira também str.splitlines() que divide em quebras de linha!

nome = 'Santos-Dumont'
lista = nome.split('-')  # .split(delimitador) devolve uma lista
print(lista)             # com os trechos de texto entre os delimitadores:
# ['Santos', 'Dumont']

print("a/b/c".split("/"))
# exibe: ['a', 'b', 'c']

itens = "A a B b".split()  # usado sem argumentos divide nos espaços
print(itens)
# exibe: ['A', 'a', 'B', 'b']

# str.join(coisas) use um string/caractere como delimitador para juntar
# uma coleção de textos!

coisas = ('a', 'b', 'c')
print('-'.join(coisas))
# exibe: a-b-c

print('\n'.join('xyz')  # \n indica uma quebra de linha
# exibe em 3 linhas:
# x
# y
# z
```

## Substituições com `.replace()`, inserções com `.format()` e *f-strings*

Para substituir toda as ocorrências, caso existam, de um *string* (uma sequência de caracteres) dentro de outro *string*, podemos usar `.replace()`. Lembrando que como *strings* são imutáveis, o texto original não é modificado e sim um novo *string* é produzido.
Não é problema se não existirem ocorrências do texto buscado, nada acontece, e o texto original é devolvido. 

```python
# str.replace(velho, novo) 
frase = 'as pessoas são estranhas'.replace('as', 'a')
frase = frase.replace('são', 'é')
print(frase)  # exibe: a pessoa é estranha
```

Se você quer inserir um *string*, ou um outro valor, que será convertido em *string* no meio de um *string*, existem várias maneiras, as duas que sugiro você conhecer e usar são, o método `.format()` e os *f-strings* que foram acrescentados no Python 3.6. Ambas as estratégias permitem substituir valores em pontos especiais do *string* original, marcados com chaves (`{}`).

```python
# repare que `nome` é um valor do tipo <str> e a `idade` <int>, a idade será convertida em <str>.
nome, idade = 'Alexandre', 120

# usando string_original_com_chaves.format(valor, outro_valor)
print('Olá, {}, você tem mesmo {} anos?'.format(nome, idade))
# exibe: Olá, Alexandre, você tem mesmo 120 anos?

# Usando um f-string, repare no  `f` antes das aspas
print('Olá, {nome}, você tem mesmo {idade} anos?')
# exibe: Olá, Alexandre, você tem mesmo 120 anos?
```

## Mais sobre a conversão de números em texto (*string*)

É possível controlar a formatação da conversão de números em string, como o número de casas decimais ou com zeros à esquerda para garantir um certo número de dígitos, usando o método `.format()` e um string com uma notação especial entre as chaves `{}`:

```python
# Ambas as formas exibem o valor valor com duas casas decimais
ang = 14.5
print("ângulo calculado: {:.2f}".format(ang)) 
print(f"ângulo calculado: {ang:.2f}"

# Produzindo um string para nome_arquivo: "arq00123.svg"
n = 123
nome_arquivo = "arq{:0>5}.svg".format(n)
# ou, equivalente nome_arquivo = f"arq{n:0>5}.svg"
```

Veja mais alguns exemplos.

```python
from math import pi  # Você pode também usar a constante PI da biblioteca py5
print("π: {:+n}".format(pi))  # com sinal, exibe π: +3.14159
# com vinte posições decimais, exibe 3.14159274101257324219
print("{:.20f}".format(pi))
print("{:.4f}".format(pi))  # com quatro posições decimais, exibe 3.1416
# preenche com zeros até 8 caracteres, exibe 003.1416
print("{:07.4f}".format(pi))
# interpreta o número como uma porcentagem e exibe 314.1593%
print("{:.4%}".format(pi))
```

## E tem mais coisas ainda!

Voocê pode ler mais na Documentação do Python sobre os [métodos de String](https://docs.python.org/pt-br/3.6/library/stdtypes.html#string-methods) e a [mini-linguagem de formatação](https://docs.python.org/pt-br/3.6/library/string.html#formatstrings).
