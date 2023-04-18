#!/usr/bin/env python3

# modified from
# http://howto.philippkeller.com/files/link_checker.py

# /home/villares/GitHub/material-aulas/ https://abav.lugaralgum.com/material-aulas


import os, sys, re
import urllib.request

if len(sys.argv) < 3:
    print("Look for broken links in markdown files (*.md)\n")
    print("usage: {} root_path base_url\n".format(sys.argv[0]))
    print("i.e. {} source https://localhost:4000".format(sys.argv[0]))
    sys.exit(1)

print(sys.argv[1:])
search_dir = sys.argv[1]
base_url = sys.argv[2]


def red(s):
    return '\033[91m' + s + '\033[0m'

def green(s):
    return '\033[32m' + s + '\033[0m'



def check(url):
    try:
        req = urllib.request.Request(url, method='HEAD', headers={'User-Agent' : "link-checker"})
        resp = urllib.request.urlopen(req, timeout=3)
        if resp.code >= 400:
            return "Got HTTP response code {}".format(resp.code)
    except Exception as e:
        return "Got exception {}".format(e)
    return None

if check(base_url) is not None:
    print("base_url {} is returning {}. Do you have your webserver running?".format(base_url, check(base_url)))
    sys.exit(1)

try:
    for path, dirs, filenames in os.walk(search_dir):
        for filename in [i for i in filenames if i.endswith('.md')]:
            with open(os.path.join(path, filename)) as f:
                printed_filename = False
                content = f.read()
                urls = re.findall("""\[[^\]]+\]\(([^\)^"^']+)\)""", content)
                urls += re.findall('(?:href|src)\s*=\s*"\s*([^"]+)', content)
                for url in urls:
                    if url.startswith('#'):
                        # skip in-url reference
                        continue
                    if url.startswith('/') and not url.startswith('//'):
                        url = base_url + url
                    error = check(url)
                    if error is not None:
                        if not printed_filename:
                            print()
                            print("{} {}".format(filename, red('x')))
                            print('-'*len(filename))
                            printed_filename = True
                        print(url, error)
                if not printed_filename:
                    print("{} {}".format(filename, green('‎✔')))
                else:
                    print()

except KeyboardInterrupt:
    pass