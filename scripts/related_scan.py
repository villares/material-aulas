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

li_block_open = False
primeira_coluna = ''
segunda_coluna = ''
primeira = True

for entry in summary.read_text().splitlines():
    entry = entry.strip()

    if entry.startswith('#'):
        h = md_to_html(entry)
        if 'Mais sobre' in entry:
            primeira = False
        if li_block_open:
            h = '</ul>\n' + h  # Close list before adding heading
            li_block_open = False  
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
                    img = f'https://abav.lugaralgum.com/material-aulas/Processing-Python-py5/{img}'
            except Exception:
                img = ''

            #entry = entry.lstrip('-0123456789. ')
            entry = entry.lstrip('- ')
            li = li_template(img_alt=number or '', img_src=img or '', entry=md_to_html(entry))

            if not li_block_open:
                li_block_open = True
                li = '<ul>\n' + li
            
            if primeira:
                primeira_coluna += li +'\n'
            else:
                segunda_coluna += li +'\n'
if li_block_open:
    if primeira:
        primeira_coluna += '</ul>\n'
    else:
        segunda_coluna += '</ul>\n'

Path('index.html').write_text(
    template.replace('{primeira_coluna}', primeira_coluna)
            .replace('{segunda_coluna}', segunda_coluna)
)
