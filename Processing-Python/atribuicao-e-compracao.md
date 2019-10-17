##### O símbolo `=` é para "atribuição" 

```python
num = 3 # faça num ser uma referência ao valor 3`
# Resultado: Modificada a variável `num`.
```

Na prática do lado direito aparecem expressões que produzem valores diversos (e são avaliadas primeiro!).

```python
soma = a + b
media = (a + b) / 2`

# aumentando em 1 o contador
contador = contador + 1
contador += 1 # equivalente a expressão anterior
```

##### O símbolo `==` é para "comparação de igualdade"

```python
num == 3 # o valor de num é igual ao valor 3?`
# Resultado: é devolvido o valor `True` ou `False`.
```

Na prática  `==`   é muito usado dentro do comando  `if` que permite a execução condicional de outros comandos.

```python
if chances == 3:  # se valor de chances igual a 3
    print("você tem três chances")
```