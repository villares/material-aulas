import re
from pathlib import Path

import py5
from markdown import markdown as md_to_html

summary = Path("/home/villares/GitHub/material-aulas/Processing-Python-py5/README.md")

li_template = """<li class="thumbnail"><img alt="{img_alt}" class="thumbnail" src="{img_src}"/>{entry}</li>""".format

def get_linked_page(txt):
    pattern = r'^\s*-\s*(?:(\d+(?:\.\d+)*)\s+)?.*?\[.*?\]\(([^)]+)\).*$'
    if match := re.match(pattern, txt):
        number = match.group(1)  # Will be None if no version number
        link_target = match.group(2)
        return number, link_target
    else:
        return None, None
    
def get_image_src(txt):
    pattern_md = r'!\[(?P<alt>[^\]]*)\]\((?P<src>[^)]+)\)'  # md image
    pattern_html = r'<img[^>]*\ssrc=["\'](?P<src>[^"\']+)["\'][^>]*>'
    for pattern in (pattern_md, pattern_html):
        if match := re.search(pattern, txt):
            return match.group('src')
    return None
    
def get_first_image(lines):
    for line in lines:
        if img_src := get_image_src(line):
            return img_src

def get_external_page(page):
    return py5.load_strings(page)

li_block = False
for entry in summary.read_text().splitlines():
    if entry.startswith('#'):
        print(md_to_html(entry))
        if li_block:
            print('</ul>')
            li_block = False       
    else:
        number, page = get_linked_page(entry)
        if page:
            if 'http' in page:
                page_path = page # URL 
            else:
                page_path = summary.parent / page # local path
            try:
                lines = py5.load_strings(page_path)        
                img = get_first_image(lines)
                if img and img.startswith('assets'):
                    img = 'https://abav.lugaralgum.com/material-aulas/Processing-Python-py5/' + img
            except Exception as e:
                img = str(e)
            #print(number, img)
            if not li_block:
                li_block = True
                print('<ul>')
            entry = entry.strip(' -0123456789.') # .replace('.md', '.html')
            li = li_template(img_alt=number, img_src=img, entry=md_to_html(entry))
            print(li)
