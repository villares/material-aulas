# Métodos dos objetos *string*

*strings * são um * tipo * de dado armazenado na memória do computador, e mais, em python, são acompanhados de uma série de funções e que podem ser acionadas com a * sintaxe do ponto * (*dot syntax*).

<sub > na programação orientada a objetos vemos que funções atreladas a objetos de uma classe são conhecidas como métodos. < /sub >

# Convertendo números em texto

é possível controlar a formatação da conversão de números em string, como o número de casas decimais ou com zeros à esquerda para garantir um certo número de dígitos, usando o método `.format()` e um string com uma notação especial entre as chaves `{}`:

```python
# Exibe valor com duas casas decimais
print("ângulo calculado: {:.2f}".format(ang))

# Produz um string para nome_arquivo: "arq00123.svg"
nome_arquivo = "arq{:0>5}.svg".format(123)
```

veja mais alguns exemplos.

```python
print(u"π: {:+n}".format(PI))  # com sinal, exibe π: +3.14159
# com vinte posições decimais, exibe 3.14159274101257324219
print("{:.20f}".format(PI))
print("{:.4f}".format(PI))  # com quatro posições decimais, exibe 3.1416
# preenche com zeros até 8 caracteres, exibe 003.1416
print("{:07.4f}".format(PI))
# interpreta o número como uma porcentagem e exibe 314.1593%
print("{:.4%}".format(PI))
```

# Convertendo caixa alta e baixa (maiúsculas e minúsculas)

```python
# str.lower() devolve string com a versão em caixa baixa
print('Alexandre'.lower())  # exibe: alexandre

# str.upper() devolve string com a versão em caixa alta
print('Alexandre'.upper())  # exibe: ALEXANDRE
```

# Checando prefixos e sufixos

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

é possível 'encadear' métodos, como no exemplo abaixo.

```python
# identifica arquivos que terminam tanto com .png como com .PNG
if nome_arquivo.lower().endswith('.png'):
     print("Arquivo tipo PNG")
```

# Procurando sub-strings

trecho da documentação:

> `str.find(sub[, start[, end]])`
> retorna o índice mais baixo na string onde a substring sub é encontrado dentro da fatia s[start:end]. argumntos opcionais como start e end são interpretados como umanotação de fatiamento. retorna - 1 se sub não for localizado. nota: O método find() deve ser usado apenas se precisarmos conhecer a posição de sub. para verificar se sub é ou não uma substring, use o operador `in`.
>
> `str.count(sub[, start[, end]])`
> retorna o número de ocorrências da sub-string sub que não se sobrepõem no intervalo[start, end]. argumentos opcionais start e end são interpretados como na notação de fatias.

# Dividindo e juntando *strings*

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

print('\n'.joint('xyz')  # \n indica uma quebra de linha
# exibe em 3 linhas: x\ny\n\z
```

# Substituições com `.replace()` e inserções com `.format()`

```python
# str.replace(velho, novo) # substitui todas as ocorrências de um texto
# dentro de outro, se houver
frase=u'as pessoas são estranhas'.replace('as', 'a')
frase=frase.replace(u'são', u'é')
print(frase)  # exibe: a pessoa é estranha

# str.format(valor, outro) substitui valores em pontos especiais do texto
nome, idade='Alexandre', 120  # repare que o nome é <str> e a idade <int>
print(u"Olá, {}, você tem mesmo {} anos?".format(nome, idade))
# exibe: Olá, Alexandre, você tem mesmo 120 anos?
```

# E tem mais coisas ainda!

voocê pode ler mais na documentação do python sobre os[métodos de string](https: // docs.python.org/pt-br/2.7/library/stdtypes.html  # string-methods) e a [mini-linguagem de formatação](https://docs.python.org/pt-br/3.6/library/string.html#formatstrings).
