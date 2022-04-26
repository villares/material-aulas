# O valor especial `None`

O Python tem um valor especial chamado `None`, que é um objeto único do tipo `NoneType`, e é em geral usado para representar "nada" ou "nenhum valor".

Pode ser usado para indicar a ausência de um valor válido, ou o final de uma sequência de valores (uma estratégia conhecida como "valor sentinela").

### O exemplo da função que carrega uma imagem no Processing

A função `loadImage()` do Processing, quando consegue carregar os dados de uma imagem, devolve um objeto do tipo `PImage`, quando não consegue ela devolve `None`.

```python
# https://cc0.photo/2016/10/05/striped-cat-meadow/
img_a = loadImage('cat.jpg')  # arquivo na pasta /data/ do sketch
img_b = loadImage('cat.Jpg')  # não existe na pasta este arquivo com J maiúsculo na extensão!

print(img_a)  # exibe: processing.core.PImage@XXXXXXX
print(img_b)  # exibe: None

image(img_a, 0, 0)  # exibe na área de desenho a imagem
# image(img_b, 0, 0)  # quebra o sketch, para e exibe o erro:
# NullPointerException at processing.core.PGraphics.image(PGraphics...
```

![image](https://user-images.githubusercontent.com/3694604/165303439-bf04975d-551c-46a6-8afc-9f59230841ae.png)

### Funções e métodos que não devolvem nenhum valor

`None` é o que nos entregam funções que não foram feitas para devolver um vlalor. 

```python
print(fill(255, 0, 0))  # muda a cor de preenchimento para vermelho, e exibe `None` no console

a = print('oi!')  # exibe: oi
print(a)          # exibe: None
```

Funções que não tem a instrução `return` no corpo, ou tem `return` sem nada depois, quando são chamadas não devolvem nenhum valor, quer dizer, na verdade, elas devolvem esse valor especial `None`. 

```python
def print_triplicado(texto):
    print(texto * 3)
    
print(texto_triplicado('oi')) 
# Exibe:
# oioioi
# None

def area(a, b):
    resultado = a * b
    return resultado
    
print(area(20, 40)) # exibe `800`

def area_estragada(a, b):
    resultado = a * b

print(area_estragada(20, 40)) # exibe `None`
```
### Método `get()` dos dicionários

Quando usamos dicionários, o método `get` procura por uma chave e devolve o valor atribuido a ela no dicionário, se não encontrar a chave devolve `None`.

```python
ddd = {'SP' : 11, 'RJ' : 21, 'BH' : 31} 

prefixo = ddd.get(key)
if prefixo is not None:
    print(resultado)
else:
    print('Chave não encontrada!')
```

### Um exemplo mais longo

No [exemplo final sobre arrastar círculos](arrastando_circulos.md), se nenhum círculo está sendo arrastado, a variável que mantém o índice do círculo fica valendo `None`.
