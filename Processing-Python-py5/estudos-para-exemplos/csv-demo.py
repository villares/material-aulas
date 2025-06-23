import csv

with open('dados.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    print(reader.fieldnames)
    # ['nome', 'valor', 'largura', 'comprimento', 'x', 'y']
    linhas = list(reader)
    
def setup():
    size(750, 750)
    for item in linhas:
        nome = item['nome']
        x = int(item['x'])
        y = int(item['y'])
        w = int(item['largura'])
        h = int(item['comprimento'])
        v = float(item['valor'])
        rect(x, y, w, h)
        
        
        