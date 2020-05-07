# Qual a diferença entre `=` e `==` em Python?

## O símbolo `=` é o operador de "atribuição" 

```python
num = 3 # faça `num` ser uma referência ao valor 3`
# Resultado: Modificada a variável `num`.
```

Na prática, do lado direito aparecem expressões que produzem valores diversos e que são avaliadas primeiro!

```python
soma = a + b
media = (a + b) / 2.

# aumentando em 1 o contador
contador = contador + 1
contador += 1 # equivalente a expressão anterior, usando o operador de atribuição aumentada.
```

## O símbolo `==` é o operador relacional que faz a "comparação de igualdade"

```python
num == 3 # o valor de `num` é igual ao valor 3?`
# Resultado: é devolvido o valor `True` ou `False`.
```

Na prática  `==`  é muito usado dentro da instruçao `if` que permite a execução condicional de outras instruções.

```python
if chances == 3:  # se valor de `chances` é igual a 3
    print("você tem três chances")
```

#### Assuntos relacionados

- [Variáveis](variaveis.md)!
- [Condicionais e outros operadores lógicos](condicionais_py.md)!

#### Glossário

[**variável**](https://penseallen.github.io/PensePython2e/02-vars-expr-instr.html#termo:variável) Um nome que se refere a um valor.

[**atribuição**](https://penseallen.github.io/PensePython2e/02-vars-expr-instr.html#termo:atribuição) Uma instrução que atribui um valor a uma variável.

[**operador relacional**](https://penseallen.github.io/PensePython2e/05-cond-recur.html#termo:operador%20relacional) Um destes operadores, que compara seus operandos: `==`, `!=`, `>`, `<`, `>=` e `<=`.

[**instrução condicional**](https://penseallen.github.io/PensePython2e/05-cond-recur.html#termo:instrução%20condicional) Uma instrução que controla o fluxo de execução, dependendo de alguma condição (expressão avaliada como `True` ou `False`).
