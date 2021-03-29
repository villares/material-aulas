# Métodos das listas

Listas são coleções ordenadas, sequências mutáveis, e como quase tudo em Python, são objetos e por isso vem acompanhadas de uma série de funções que podem ser acionadas com a *sintaxe do ponto* (*dot syntax*).

<sub>Na programação orientada a objetos veremos que funções que acompanham objetos de uma determinada classe são conhecidas como métodos.</sub>

### Antes de chegar aqui

Provavelmente você já leu neste material que é possível acrescentar itens à uma lista escrevendo `lista.append(item)`, mas existem outras possibilidades!

### Mais métodos

`.extend(iterável)` - Prolonga a lista, adicionando no fim todos os elementos da coleção ou iterável passado como argumento.

`.insert(i, x)` - Insere um item `x` em uma dada posição `i`. O primeiro argumento é o índice do elemento antes do qual será feita a inserção, assim `a.insert(0, x)` insere um elemento na frente da lista e `a.insert(len(a), x)` e equivale a `a.append(x)`.

`.remove(x)` - Remove o primeiro item encontrado na lista cujo valor é igual a *x*. Se não existir valor igual, uma exceção [`ValueError`](https://docs.python.org/pt-br/3.8/library/exceptions.html#ValueError "ValueError") é levantada.

`.pop(i)` - Remove um item na posição `i` da lista e o devolve. Se nenhum índice é especificado, `.pop()` remove e devolve o último item da lista. 

`.clear()` - Remove todos os itens de uma lista. Equivalente a `del a[:]`.

`.index(*x*[, *inicio*[, *parada*]])` - Devolve o índice base-zero do primeiro item cujo valor é igual a *x*, levantando [`ValueError`](https://docs.python.org/pt-br/3.8/library/exceptions.html#ValueError "ValueError") se este valor não existe. Os argumentos opcionais *inicio* e *parada* são interpretados como nas notações de fatiamento e são usados para limitar a busca para uma subsequência específica da lista. O índice retornado é calculado relativo ao começo da sequência inteira e não referente ao argumento *parada*. (*Nota: Os colchetes na demonstração do método indicam que os parâmetros são opcionais, e não que é necessário escrever estes colchetes ao chamar o método. Você verá este tipo de notação frequentemente na documentação do Python.*)

`.count(a)` - Devolve o número de vezes em que `a` aparece na lista.

`.sort([key=None][, reverse=False])` - Ordena os itens na lista (os argumentos podem ser usados para personalizar a ordenação, veja a função [`sorted()`](https://docs.python.org/pt-br/3.8/library/functions.html#sorted "sorted") para maiores explicações).

`.reverse()` - Inverte a ordem dos elementos na lista.

`.copy()` - Devolve uma cópia rasa da lista. Equivalente a `a[:]`.

**Você pode ler mais na Documentação do Python sobre as listas e outras estruturas de dados em [5.1. Mais sobre listas](https://docs.python.org/pt-br/2.7/tutorial/datastructures.html#more-on-lists) (na documentação do Python).**
