import re
from pathlib import Path
import py5
from markdown import markdown as md_to_html

summary = Path("/home/villares/GitHub/material-aulas/Processing-Python-py5/README.md")
template = Path('index_template.html').read_text()

li_template = """<li class="thumbnail"><img alt="{img_alt}" class="thumbnail" src="{img_src}"/>{entry}</li>""".format

def get_linked_page(txt):
    pattern = r'^\s*-\s*(?:(\d+(?:\.\d+)*)\s+)?.*?\[.*?\]\(([^)]+)\).*$'
    if match := re.match(pattern, txt):
        return match.group(1), match.group(2)  # Number and link target
    return None, None

def replace_md_target(entry):
    base = 'Processing-Python-py5/'
    number, target = get_linked_page(entry)
    if not target:
        return entry  # No replacement needed
    new_target = base + target[:-3] + '.html'  # Convert to .html path
    return entry.replace(target, new_target)

def get_image_src(txt):
    patterns = [
        r'!\[(?P<alt>[^\]]*)\]\((?P<src>[^)]+)\)',  # Markdown image
        r'<img[^>]*\ssrc=["\'](?P<src>[^"\']+)["\'][^>]*>'  # HTML image
    ]
    for pattern in patterns:
        if match := re.search(pattern, txt):
            return match.group('src')
    return None
    
def get_first_image(lines):
    for line in lines:
        if img_src := get_image_src(line):
            return img_src

primeira_coluna = ''
segunda_coluna = ''
primeira = True

for entry in summary.read_text().splitlines():
    entry = entry.strip()
    if entry.startswith('#'):
        h = md_to_html(entry) 
        if 'Mais sobre' in entry:  ### Preimeira secçao da segunda coluna
            primeira = False
        if primeira:
                primeira_coluna += h +'\n'
        else:
                segunda_coluna += h +'\n'
    else:
        number, page = get_linked_page(entry)
        if page:
            page_path = page if 'http' in page else summary.parent / page
            try:
                lines = py5.load_strings(page_path)
                img = get_first_image(lines)
                if img and img.startswith('assets'):
                    img = f'/material-aulas/Processing-Python-py5/{img}'
            except Exception:
                print(img)
            #entry = entry.lstrip('-0123456789. ')
            if not 'http' in entry:
                entry = replace_md_target(entry)
            html_entry = md_to_html(entry.strip(' -'))
            li = li_template(img_alt=number or '',
                             img_src=img or '/material-aulas/Processing-Python-py5/assets/thumb-bullet.png',
                             entry=html_entry)
            if primeira:
                primeira_coluna += li +'\n'
            else:
                segunda_coluna += li +'\n'


output_path = Path.cwd().parent / 'index.html'
output_path.write_text(
    template.replace('{primeira_coluna}', primeira_coluna)
            .replace('{segunda_coluna}', segunda_coluna)
)
