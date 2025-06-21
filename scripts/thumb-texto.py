f = create_font('Inconsolata Bold', 24)
text_font(f)
fill(0)

# nome = 'if-elif-else'
# texto = 'if:\nelif:\nelse:'

# nome = '='
# texto = '=\nigual?\n=='

nome = 'list-comp'
text_size(17)
texto = 'lista = [\n f(x) for x\n in outra\n if g(x)\n]'
text_align(LEFT, CENTER)
text(texto, 2, 50)

# nome = 'lambda'
# text_size(18)
# texto = """sorted()
# filter()
# lambda
# map()"""

# text_align(LEFT, CENTER)
# text(texto, 5, 50)

# nome = 'None'
# text_size(40)
# text_align(CENTER, CENTER)
# text(nome, 50, 50)


# nome = 'metodos-str'
# text_size(13)
# texto = """# strings!
# a = a.replace(
#      '//', '#')
# data.split('-')
# ''.join(items)
# f'Olá {nome}!'"""
# text_align(LEFT, CENTER)
# text(texto, 2, 50)


# nome = 'list-methods'
# text_size(14)
# texto = """.append(x)
# .extend([a,b])
# .insert(i, x)
# .remove(x)
# .pop(i)"""
# text_align(LEFT, CENTER)
# text(texto, 2, 50)

# nome = 'removendo'
# text_size(12)
# texto = """# cuidado!
# 
# c = a.copy()
# for n in c:
#   if  n == 0:
#     a.remove(n)
# """
# text_align(LEFT, CENTER)
# text(texto, 5, 50)


print(f'<!-- thumb para o sumário\n![](assets/thumb-{nome}.png)\n-->')
out = Path.cwd().parent / 'Processing-Python-py5' / 'assets' / f'thumb-{nome}.png'
save(out)