# Métodos das listas

listas são coleções ordenadas, sequências mutáveis, e como quase tudo em python, são objetos e por isso vem acompanhadas de uma série de funções que podem ser acionadas com a * sintaxe do ponto * (*dot syntax*).

<sub > na programação orientada a objetos vemos que funções atreladas a objetos de uma classe são conhecidas como métodos. < /sub >

# Antes de chegar aqui

provavelmente você já leu neste material que é possível acrescentar itens à uma lista escrevendo `lista.append(item)`, mas existem outras possibilidades!

# Mais métodos

`.extend(iterável)` - prolonga a lista, adicionando no fim todos os elementos da coleção ou iterável passado como argumento.

`.insert(i, x)` - insere um item `x` em uma dada posição `i`. O primeiro argumento é o índice do elemento antes do qual será feita a inserção, assim `a.insert(0, x)` insere um elemento na frente da lista e `a.insert(len(a), x)` e equivale a `a.append(x)`.

`.remove(x)` - remove o primeiro item encontrado na lista cujo valor é igual a * x*. se não existir valor igual, uma exceção[`value_error`](https: // docs.python.org/pt-br/3.8/library/exceptions.html  # ValueError "ValueError") é levantada.

`.pop(i)` - remove um item na posição `i` da lista e o devolve. se nenhum índice é especificado, `.pop()` remove e devolve o último item da lista.

`.index(*x*[, *inicio*[, *parada*]])` - devolve o índice base-zero do primeiro item cujo valor é igual a * x*, levantando[`value_error`](https: // docs.python.org/pt-br/3.8/library/exceptions.html  # ValueError "ValueError") se este valor não existe. Os argumentos opcionais *inicio* e *parada* são interpretados como nas notações de fatiamento e são usados para limitar a busca para uma subsequência específica da lista. O índice retornado é calculado relativo ao começo da sequência inteira e não referente ao argumento *parada*. (*Nota: Os colchetes na demonstração do método indicam que os parâmetros são opcionais, e não que é necessário escrever estes colchetes ao chamar o método. Você verá este tipo de notação frequentemente na documentação do Python.*)

`.count(a)` - devolve o número de vezes em que `a` aparece na lista.

`.sort([key=None][, reverse=False])` - ordena os itens na lista(os argumentos podem ser usados para personalizar a ordenação, veja a função[`sorted()`](https: // docs.python.org/pt-br/3.8/library/functions.html  # sorted "sorted") para maiores explicações).

`.reverse()` - inverte a ordem dos elementos na lista.

`.copy()` - devolve uma cópia rasa da lista. equivalente a `a[:]`.

**você pode ler mais na documentação do python sobre as listas e outras estruturas de dados em[5.1. mais sobre listas](https: // docs.python.org/pt-br/2.7/tutorial/datastructures.html  # more-on-lists) (na documentação do Python).**

> no python mais moderno, a partir do python 3.3, temos o método `.clear()`, que remove todos os itens de uma lista, equivale a `del a[:]`.
