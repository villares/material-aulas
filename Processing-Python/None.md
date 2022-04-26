# O valor especial `None`

O Python tem um valor especial que é de um tipo só dele, o `None`, ele é em geral usado para representar "nada" ou "nenhum valor".

Funções que não tem a instrução `return` no corpo, ou tem `return` sem nada depois não devolvem nenhum valor quando são chamadas, quer dizer, na verdade, elas devolvem esse valor especial `None`.


```python
def area(a, b):
    resultado = a * b
    return resultado
    
print(area(20, 40) # exibe `800`

def area_estragada(a, b):
    resultado = a * b

print(area_estragada(20, 40) # exibe `None`

print(fill(255, 0, 0))  # muda a cor de preenchimento para vermelho, e exibe `None` no console

a = print('oi!')  # exibe: oi
print(a)          # exibe: None
```

Quando usamos dicionários, o método `get` procura por uma chave e devolve o valor atribuido a ela no dicionário, se não encontrar a chave devolve `None`.

```python
resultado = mydict.get(key)
if resultado is not None:
    print(resultado)
else:
    print('Chave não encontrada (ou o valor armazenado era None!)')
```

No meu [exemplo final sobre arrastar círculos](arrastando_circulos.md), se nenhum círculo está sendo arrastado, a variável que mantém o índice do círculo fica valendo `None`.
