import re
from pathlib import Path

import py5

summary = Path("/home/villares/GitHub/material-aulas/Processing-Python-py5/README.md")

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

for entry in summary.read_text().splitlines():
    if entry.startswith('#'):
        print(entry)
    else:
        number, page = get_linked_page(entry)
        if page:
            if 'http' not in page:
                page = summary.parent / page
            try:
                lines = py5.load_strings(page)        
                img = get_first_image(lines)
                if img and img.startswith('assets'):
                    img = 'https://abav.lugaralgum.com/material-aulas/Processing-Python-py5/' + img
            except Exception as e:
                img = str(e)
            print(number, img)
