#!/usr/bin/env python3
"""
Assemble les pages du site.

styles.css et analytics.html sont les SOURCES : on les modifie là, jamais
dans les pages. Ce script recopie leur contenu entre les balises repères
de chaque page, ce qui supprime toute ressource bloquant l'affichage.

Usage :  python3 build.py
"""
import pathlib, re

ROOT = pathlib.Path(__file__).parent
PAGES = ['index.html', 'en/index.html', 'reserver/index.html', 'en/book/index.html']

def inject(text, tag, payload):
    start, end = f'<!-- {tag}:debut -->', f'<!-- {tag}:fin -->'
    block = f'{start}\n{payload}\n{end}'
    if start in text:
        return re.sub(re.escape(start) + r'.*?' + re.escape(end), lambda _: block, text, flags=re.S)
    return text

css = (ROOT / 'styles.css').read_text().strip()
ga_fr = (ROOT / 'analytics.html').read_text().strip()
ga_en = (ROOT / 'analytics.en.html').read_text().strip()

for page in PAGES:
    p = ROOT / page
    t = p.read_text()
    profondeur = '../' * page.count('/')
    t = inject(t, 'styles', '<style>' + css.replace('FONTS/', profondeur + 'fonts/') + '</style>')
    t = inject(t, 'analytics', ga_en if page.startswith('en/') else ga_fr)
    p.write_text(t)
    print(f'{page:22} styles {len(css)//1024} Ko + analytics')
