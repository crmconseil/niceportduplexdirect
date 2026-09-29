#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fabrique les pages guide à partir de guides_contenu.py.

Chaque guide donne deux pages — une française, une anglaise — qui se déclarent
mutuellement par hreflang. Le style et la mesure d'audience sont injectés
ensuite par build.py, comme pour les autres pages du site.

Usage :  python3 guides.py && python3 build.py
"""
import pathlib, re, json, datetime
from guides_contenu import GUIDES

RACINE = pathlib.Path(__file__).parent
SITE = "https://niceportduplex.com"
AUJOURDHUI = datetime.date.today().isoformat()

LIBELLES = {
 'fr': dict(retour="← Retour au site", surtitre="Guide",
            cta_titre="Votre séjour au Port Lympia",
            cta_texte="Un duplex de 54 m² sur le quai Lunel, à cinq minutes du Vieux Nice et de la plage. Réservation en direct, sans commission de plateforme.",
            cta_bouton="Voir les disponibilités", reserver="/reserver/", accueil="/",
            autres="À lire aussi", maj="Informations vérifiées en septembre 2026 auprès des sources officielles. Tarifs et horaires sont susceptibles d'évoluer.",
            legal="Meublé de tourisme enregistré auprès de la Ville de Nice sous le numéro 06088005303PK."),
 'en': dict(retour="← Back to the site", surtitre="Guide",
            cta_titre="Your stay at Port Lympia",
            cta_texte="A 54 m² duplex on quai Lunel, five minutes from the Old Town and the beach. Book direct, without platform commission.",
            cta_bouton="Check availability", reserver="/en/book/", accueil="/en/",
            autres="Also worth reading", maj="Information verified in September 2026 against official sources. Prices and opening times may change.",
            legal="Registered with the City of Nice as a tourist rental under number 06088005303PK."),
}

GABARIT = """<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">

<title>{meta_titre}</title>
<meta name="description" content="{meta_desc}">
<link rel="canonical" href="{canon}">
<link rel="alternate" hreflang="fr" href="{url_fr}">
<link rel="alternate" hreflang="en" href="{url_en}">
<link rel="alternate" hreflang="x-default" href="{url_fr}">
<meta name="robots" content="index, follow">
<meta name="theme-color" content="#fbf9f6">

<meta property="og:type" content="article">
<meta property="og:locale" content="{locale}">
<meta property="og:site_name" content="Nice Port Duplex">
<meta property="og:url" content="{canon}">
<meta property="og:title" content="{titre}">
<meta property="og:description" content="{meta_desc}">
<meta property="og:image" content="{site}/images/opt/hero-1280.jpg">
<meta name="twitter:card" content="summary_large_image">

<link rel="preload" as="font" type="font/woff2" crossorigin href="{racine}fonts/cormorant-600.woff2">
<link rel="preload" as="font" type="font/woff2" crossorigin href="{racine}fonts/inter-400.woff2">
<link rel="preload" as="font" type="font/woff2" crossorigin href="{racine}fonts/inter-600.woff2">
<link rel="preload" as="font" type="font/woff2" crossorigin href="{racine}fonts/cormorant-400-italic.woff2">
<link rel="icon" href="{racine}images/favicon.png">
<!-- styles:debut -->
<!-- styles:fin -->
</head>
<body>

<div class="bookbar">
  <nav class="wrap nav">
    <a href="{accueil}" class="brand">Nice&nbsp;Port&nbsp;Duplex</a>
    <div class="nav-right">
      <a href="{accueil}">{retour}</a>
    </div>
  </nav>
</div>

<main id="contenu">

<div class="bookhero">
  <picture><source type="image/webp" srcset="{racine}images/opt/hero-640.webp 640w, {racine}images/opt/hero-1100.webp 1100w, {racine}images/opt/hero-1400.webp 1400w" sizes="100vw"><img src="{racine}images/opt/hero-760.jpg" alt="{alt_hero}" width="1920" height="1088" fetchpriority="high"></picture>
  <div class="wrap">
    <p class="eyebrow">{surtitre}</p>
    <h1>{titre}</h1>
  </div>
</div>

<article class="article">
  <p class="chapeau">{chapeau}</p>
{corps}
  <p class="maj">{maj}</p>

  <h2>{autres}</h2>
  <div class="guides">
{autres_liens}
  </div>
</article>

</main>

<div class="cta-guide">
  <p class="eyebrow" style="color:var(--gold)">{surtitre_cta}</p>
  <h2>{cta_titre}</h2>
  <p>{cta_texte}</p>
  <a href="{reserver}" class="btn btn-light">{cta_bouton}</a>
</div>

<footer>
  <div class="wrap">
    <div class="foot">
      <div>
        <p style="font-family:'Cormorant Garamond',serif;font-weight:600;font-size:1.35rem;color:#fff">Nice Port Duplex</p>
        <p>20 quai Lunel, 06300 Nice</p>
      </div>
      <div>
        <p><strong>Contact</strong></p>
        <p><a href="tel:+33622953137">+33 6 22 95 31 37</a></p>
        <p><a href="mailto:niceportduplex@gmail.com">niceportduplex@gmail.com</a></p>
      </div>
      <div>
        <p><strong>{surtitre}</strong></p>
        <p><a href="{accueil}">{retour_court}</a></p>
      </div>
    </div>
    <p class="legal">© 2026 Nice Port Duplex — {legal}</p>
  </div>
</footer>

<script type="application/ld+json">
{jsonld}
</script>

<!-- analytics:debut -->
<!-- analytics:fin -->
</body>
</html>
"""


def url(lang, g):
    return f"{SITE}/{g['slug_fr']}/" if lang == 'fr' else f"{SITE}/en/{g['slug_en']}/"


def chemin(lang, g):
    return RACINE / (f"{g['slug_fr']}/index.html" if lang == 'fr' else f"en/{g['slug_en']}/index.html")


def construire(lang, g):
    lib = LIBELLES[lang]
    d = g[lang]
    racine = '../' if lang == 'fr' else '../../'

    # cartes vers les autres guides, dans la même langue
    autres = []
    for a in GUIDES:
        if a is g:
            continue
        lien = f"/{a['slug_fr']}/" if lang == 'fr' else f"/en/{a['slug_en']}/"
        autres.append(f'    <a href="{lien}"><b>{a[lang]["carte_titre"]}</b>'
                      f'<span>{a[lang]["carte_desc"]}</span></a>')

    jsonld = {
      "@context": "https://schema.org", "@type": "Article",
      "headline": d['titre'],
      "description": d['meta_desc'],
      "inLanguage": "fr-FR" if lang == 'fr' else "en-GB",
      "mainEntityOfPage": {"@type": "WebPage", "@id": url(lang, g)},
      "image": f"{SITE}/images/opt/hero-1280.jpg",
      "datePublished": AUJOURDHUI, "dateModified": AUJOURDHUI,
      "author": {"@type": "Organization", "name": "Nice Port Duplex", "url": SITE + "/"},
      "publisher": {"@type": "Organization", "name": "Nice Port Duplex", "url": SITE + "/"},
    }

    return GABARIT.format(
        lang=lang, locale='fr_FR' if lang == 'fr' else 'en_GB',
        meta_titre=d['meta_titre'], meta_desc=d['meta_desc'],
        titre=d['titre'], chapeau=d['chapeau'], corps=d['corps'].rstrip(),
        canon=url(lang, g), url_fr=url('fr', g), url_en=url('en', g),
        site=SITE, racine=racine,
        alt_hero="Le port historique de Nice" if lang == 'fr' else "The historic port of Nice",
        surtitre=lib['surtitre'], surtitre_cta='Réservation' if lang == 'fr' else 'Booking',
        retour=lib['retour'], retour_court=lib['retour'].replace('← ', ''),
        accueil=lib['accueil'], reserver=lib['reserver'],
        cta_titre=lib['cta_titre'], cta_texte=lib['cta_texte'], cta_bouton=lib['cta_bouton'],
        autres=lib['autres'], autres_liens='\n'.join(autres),
        maj=lib['maj'], legal=lib['legal'],
        jsonld=json.dumps(jsonld, ensure_ascii=False, indent=2),
    )


def main():
    ecrits = []
    for g in GUIDES:
        for lang in ('fr', 'en'):
            f = chemin(lang, g)
            f.parent.mkdir(parents=True, exist_ok=True)
            f.write_text(construire(lang, g))
            ecrits.append(f.relative_to(RACINE))

    # sitemap : accueil, versions anglaises, et les huit guides
    lignes = ['<?xml version="1.0" encoding="UTF-8"?>',
              '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
              '        xmlns:xhtml="http://www.w3.org/1999/xhtml">']

    def entree(u_fr, u_en, courant, prio):
        alt = (f'    <xhtml:link rel="alternate" hreflang="fr" href="{u_fr}"/>\n'
               f'    <xhtml:link rel="alternate" hreflang="en" href="{u_en}"/>\n'
               f'    <xhtml:link rel="alternate" hreflang="x-default" href="{u_fr}"/>')
        return (f'  <url>\n    <loc>{courant}</loc>\n    <lastmod>{AUJOURDHUI}</lastmod>\n'
                f'    <changefreq>monthly</changefreq>\n    <priority>{prio}</priority>\n{alt}\n  </url>')

    lignes.append(entree(f'{SITE}/', f'{SITE}/en/', f'{SITE}/', '1.0'))
    lignes.append(entree(f'{SITE}/', f'{SITE}/en/', f'{SITE}/en/', '0.9'))
    for g in GUIDES:
        for lang, prio in (('fr', '0.8'), ('en', '0.7')):
            lignes.append(entree(url('fr', g), url('en', g), url(lang, g), prio))
    lignes.append('</urlset>')
    (RACINE / 'sitemap.xml').write_text('\n'.join(lignes) + '\n')

    for f in ecrits:
        print(f'  {f}')
    print(f'\n{len(ecrits)} pages guide + sitemap ({2 + len(GUIDES) * 2} URL)')


if __name__ == '__main__':
    main()
