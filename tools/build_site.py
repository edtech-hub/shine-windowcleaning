#!/usr/bin/env python3
"""Shine of Fort Lauderdale pitch prototype. Generates plain HTML from WordPress core block markup.
Run: python3 tools/build_site.py .   (every fact comes from facts.md)"""
import hashlib, json, os, sys, time

OUT = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.getcwd()
PHONE, TEL = "(954) 881-0031", "+19548810031"
ADDRESS = "1150 SW 10th Ave, Suite 103E, Pompano Beach, FL 33069"
MAPS = "https://www.google.com/maps/search/?api=1&query=1150+SW+10th+Ave+Suite+103E+Pompano+Beach+FL+33069"
FB = "https://www.facebook.com/ShineExteriorCleaningLighting"
IG = "https://www.instagram.com/shineexteriorcleaninglighting/"
BUILD = time.strftime("%Y%m%d%H%M%S")
TOWNS = ["Boca Raton", "Coral Springs", "Davie", "Deerfield Beach", "Delray Beach", "Fort Lauderdale", "Hollywood",
         "Oakland Park", "Parkland", "Plantation", "Pembroke Pines", "Pompano Beach", "Southwest Ranches", "Weston"]


def ver(rel):
    with open(os.path.join(OUT, rel), "rb") as f:
        return hashlib.md5(f.read()).hexdigest()[:8]


S = 'xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false"'
LINE = S + ' fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"'
ICON = {
    "phone": '<svg ' + LINE + ' viewBox="0 0 24 24"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.8 19.8 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.12 4.18 2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/></svg>',
    "arrow": '<svg ' + LINE + ' viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"/></svg>',
    "check": '<svg ' + LINE + ' stroke-width="3" viewBox="0 0 24 24"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>',
    "menu": '<svg ' + S + ' viewBox="0 0 24 24"><path fill="currentColor" d="M5 5v1.5h14V5H5zm0 7.8h14v-1.5H5v1.5zM5 19h14v-1.5H5V19z"/></svg>',
    "close": '<svg ' + S + ' viewBox="0 0 24 24"><path fill="currentColor" d="m13.06 12 6.47-6.47-1.06-1.06L12 10.94 5.53 4.47 4.47 5.53 10.94 12l-6.47 6.47 1.06 1.06L12 13.06l6.47 6.47 1.06-1.06L13.06 12Z"/></svg>',
    "star": '<svg ' + S + ' viewBox="0 0 24 24"><path fill="currentColor" d="M12 2.5l2.94 5.96 6.56.95-4.75 4.63 1.12 6.54L12 17.5l-5.87 3.08 1.12-6.54L2.5 9.41l6.56-.95z"/></svg>',
    "dot": '<svg ' + S + ' viewBox="0 0 24 24"><circle cx="12" cy="12" r="4" fill="currentColor"/></svg>',
}
STARS = '<span class="stars" aria-label="5 out of 5 stars">' + ICON["star"] * 5 + '</span>'

# Hand-drawn line art for the service cards (navy line, red detail). Not an icon font.
N, R, G = "#1a2b39", "#c8102e", "#d9a441"
ART = {
    "windows": '<svg class="art" ' + S + ' viewBox="0 0 32 32" fill="none" stroke-width="1.8" stroke-linecap="round"><rect x="4" y="5" width="18" height="22" rx="1" stroke="' + N + '"/><path d="M13 5v22M4 16h18" stroke="' + N + '"/><path d="M17 23l11-11" stroke="' + R + '" stroke-width="2.6"/><path d="M24 8l5 5" stroke="' + R + '" stroke-width="2.2"/></svg>',
    "pressure": '<svg class="art" ' + S + ' viewBox="0 0 32 32" fill="none" stroke-width="1.8" stroke-linecap="round"><path d="M3 10h9l3 3v4H9l-2 6H4" stroke="' + N + '"/><path d="M15 13h7" stroke="' + N + '" stroke-width="2.4"/><path d="M24 10l5-3M24 13h6M24 16l5 3" stroke="' + R + '"/></svg>',
    "gutters": '<svg class="art" ' + S + ' viewBox="0 0 32 32" fill="none" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 7l13-4 13 4" stroke="' + N + '"/><path d="M3 11h24v3a3 3 0 0 1-3 3H6a3 3 0 0 1-3-3z" stroke="' + N + '"/><path d="M22 17v8" stroke="' + N + '"/><path d="M22 28.5v.5M18 22v1M26 22v1" stroke="' + R + '" stroke-width="2.4"/></svg>',
    "lighting": '<svg class="art" ' + S + ' viewBox="0 0 32 32" fill="none" stroke-width="1.8" stroke-linecap="round"><path d="M2 6c7 6 21 6 28 0" stroke="' + N + '"/><path d="M9 9.5v2M16 11v2M23 9.5v2" stroke="' + N + '"/><ellipse cx="9" cy="15.5" rx="2.4" ry="3.6" fill="' + G + '" stroke="none"/><ellipse cx="16" cy="17" rx="2.4" ry="3.6" fill="' + R + '" stroke="none"/><ellipse cx="23" cy="15.5" rx="2.4" ry="3.6" fill="' + G + '" stroke="none"/></svg>',
}
ART["roof"] = ('<svg class="art" ' + S + ' viewBox="0 0 32 32" fill="none" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M2 17L16 5l14 12" stroke="' + N + '"/><path d="M6 14v14h20V14" stroke="' + N + '"/>'
               '<path d="M10 11.5v4M14 8.5v5M18 8.5v3" stroke="' + R + '" stroke-width="2.2"/><path d="M13 28v-7h6v7" stroke="' + N + '"/></svg>')
ART["landscape"] = ('<svg class="art" ' + S + ' viewBox="0 0 32 32" fill="none" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 4h8l-1.5 6h-5z" stroke="' + N + '"/><path d="M16 10v18M9 28h14" stroke="' + N + '"/>'
                    '<path d="M11 14l-3 4M21 14l3 4M16 14v3" stroke="' + G + '" stroke-width="2"/></svg>')
# (value, card label, art, quote-page line, services-row line)
FUNNEL = [
    ("windows", "Windows", "windows", "Inside, outside, screens", "Inside and out, screens included. Salt spray, water spots and storm grime off the glass."),
    ("pressure", "Pressure washing", "pressure", "Driveways, patios, pool decks", "Driveways, patios, pool decks and fences, with soft washing where high pressure would do damage."),
    ("roof", "Roof and house wash", "roof", "Algae streaks, mildew", "Gentle washing that lifts black algae streaks off the roof and mildew off the walls."),
    ("gutters", "Gutters", "gutters", "Debris, downspouts, covers", "Sand, leaves and storm debris out, downspouts cleared, drainage checked. Covers available."),
    ("holiday", "Holiday lights", "lighting", "Design, install, take down", "A display designed for your house, installed, looked after all season and taken down after."),
    ("lighting", "Landscape lighting", "landscape", "Paths, patios, permanent", "Walkways, garden beds, bistro strings over the patio, and permanent lighting."),
]
TRUST_ART = [
    ('<svg ' + S + ' viewBox="0 0 52 52" fill="none" stroke-width="1.8"><circle cx="26" cy="24" r="17" stroke="' + N + '"/><circle cx="26" cy="24" r="12.5" stroke="' + N + '" stroke-dasharray="2 3"/><path d="M17 38l-4 11 6-3 3 5 3-9M35 38l4 11-6-3-3 5-3-9" stroke="' + R + '" stroke-linejoin="round"/><path d="M20.5 24.5l4 4 7.5-8" stroke="' + R + '" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>',
     "100% money-back guarantee", "If you're not happy, we make it right or refund you."),
    ('<svg ' + S + ' viewBox="0 0 52 52" fill="none" stroke-width="1.8" stroke-linejoin="round"><path d="M6 26L26 9l20 17" stroke="' + N + '"/><path d="M11 22v22h30V22" stroke="' + N + '"/><path d="M26 41s-8-7.5-8-13a8 8 0 0 1 16 0c0 5.5-8 13-8 13z" stroke="' + R + '"/><circle cx="26" cy="28" r="2.6" fill="' + R + '"/></svg>',
     "Locally owned", "Run out of Pompano Beach, covering Boca to Pembroke Pines."),
    ('<svg ' + S + ' viewBox="0 0 52 52" fill="none" stroke-width="1.8" stroke-linecap="round"><rect x="7" y="6" width="38" height="40" rx="2" stroke="' + N + '"/><path d="M26 6v40M7 26h38" stroke="' + N + '"/><path d="M13 20l8-8M30 40l9-9M33 21l6-6" stroke="' + G + '" stroke-width="2.4"/></svg>',
     "Homes and businesses", "Houses, condos, storefronts, offices and HOAs."),
    ('<svg ' + S + ' viewBox="0 0 52 52" fill="none" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="10" y="8" width="32" height="38" rx="2" stroke="' + N + '"/><path d="M19 5h14v6H19z" stroke="' + N + '"/><path d="M17 20h18M17 27h18M17 34h9" stroke="' + N + '"/><path d="M30 36l3.5 3.5L41 32" stroke="' + R + '" stroke-width="2.6"/></svg>',
     "Free estimates", "No-obligation quote from the local team."),
]


def string_svg(n, w=1440, sag=26, y0=10, cls="string"):
    """A wire of holiday bulbs drawn as SVG. Used on the lights band and the header Easter egg."""
    parts = ['<svg class="' + cls + '" ' + S + ' viewBox="0 0 ' + str(w) + ' 90" preserveAspectRatio="none">']
    parts.append('<path class="wire" d="M0 ' + str(y0) + ' Q ' + str(w / 4) + ' ' + str(y0 + sag * 2) + ' ' + str(w / 2) + ' ' + str(y0) + ' T ' + str(w) + ' ' + str(y0) + '"/>')
    for i in range(n):
        x = (i + .5) * w / n
        t = (x % (w / 2)) / (w / 2)
        y = y0 + 4 * sag * t * (1 - t)
        parts.append('<rect class="cap" x="%.1f" y="%.1f" width="6" height="6" rx="1"/>' % (x - 3, y))
        parts.append('<ellipse class="bulb" cx="%.1f" cy="%.1f" rx="5.5" ry="9"/>' % (x, y + 14))
    parts.append('</svg>')
    return "".join(parts)


INLINE_HEAD = r'''<script type="speculationrules">{"prerender":[{"where":{"href_matches":"/*"},"eagerness":"moderate"}]}</script>'''


def head(title, desc, root):
    return ('<!doctype html>\n<html lang="en-US">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            '<meta name="robots" content="noindex, nofollow">\n'
            '<title>' + title + '</title>\n<meta name="description" content="' + desc + '">\n'
            '<meta name="theme-color" content="#0f1b25">\n'
            '<link rel="icon" href="' + root + 'assets/img/favicon.svg" type="image/svg+xml">\n'
            '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
            '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Literata:ital,opsz,wght@0,7..72,400;0,7..72,500;1,7..72,400&family=Ysabeau+Office:wght@400;450;600;700&display=swap">\n'
            '<link rel="stylesheet" href="' + root + 'assets/css/wp-blocks.css?ver=' + ver("assets/css/wp-blocks.css") + '">\n'
            '<link rel="stylesheet" href="' + root + 'assets/css/site.css?ver=' + ver("assets/css/site.css") + '">\n'
            + INLINE_HEAD + '\n<script src="' + root + 'assets/js/site.js?ver=' + ver("assets/js/site.js") + '" defer></script>\n</head>\n')


def header(root, cur):
    nav = [("Services", root + "#services", ""), ("Holiday lights", root + "#lights", ""),
           ("Reviews", root + "#reviews", ""), ("Service area", root + "#area", ""), ("Estimate", root + "quote/", "quote")]
    links = "".join('<a href="' + h + '"' + (' aria-current="page"' if k == cur else '') + '>' + t + '</a>' for t, h, k in nav[:4])
    over = '<a href="' + root + '">Home</a>' + "".join('<a href="' + h + '">' + t + '</a>' for t, h, k in nav)
    return ('<body>\n<a class="screen-reader-text" href="#main">Skip to content</a>\n'
            '<header class="site-header wp-block-template-part">\n<div class="inner wp-block-group alignwide">\n'
            '<a class="wp-block-site-logo" href="' + root + '" aria-label="Shine of Fort Lauderdale, home" data-logo><img src="' + root + 'assets/img/logo.svg" alt="Shine" width="116" height="50"></a>\n'
            '<nav class="wp-block-navigation" aria-label="Main">' + links + '</nav>\n'
            '<div class="header-actions"><a class="header-phone" href="tel:' + TEL + '">' + ICON["phone"] + PHONE + '</a>'
            '<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="' + root + 'quote/">Free estimate</a></div>'
            '<a class="icon-btn header-call" href="tel:' + TEL + '" aria-label="Call ' + PHONE + '">' + ICON["phone"] + '</a>'
            '<button class="icon-btn menu-toggle" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="menu">' + ICON["menu"] + '</button></div>\n'
            '</div>\n' + string_svg(48, sag=6, y0=2, cls="header-string") + '\n</header>\n'
            '<div class="menu-overlay" id="menu" hidden><button class="icon-btn menu-close" type="button" aria-label="Close menu">' + ICON["close"] + '</button>' + over +
            '<a href="tel:' + TEL + '">Call ' + PHONE + '</a></div>\n')


def footer(root):
    towns = "".join("<li>" + t + "</li>" for t in TOWNS[:7])
    return ('<footer class="site-footer wp-block-template-part">\n<div class="alignwide">\n<div class="footer-cols">\n'
            '<div><img src="' + root + 'assets/img/logo.svg" alt="Shine" width="116" height="50" style="height:46px;width:auto;margin-bottom:14px">'
            '<p>Shine of Fort Lauderdale. Window cleaning, pressure washing, gutters and lighting for homes and businesses in Broward and south Palm Beach County.</p>'
            '<ul class="wp-block-social-links"><li><a href="' + FB + '">Facebook</a></li><li><a href="' + IG + '">Instagram</a></li></ul></div>\n'
            '<div><h4>Services</h4><ul><li><a href="' + root + '#services">Window cleaning</a></li><li><a href="' + root + '#services">Pressure washing</a></li><li><a href="' + root + '#services">Roof and house washing</a></li><li><a href="' + root + '#services">Gutter cleaning</a></li><li><a href="' + root + '#lights">Holiday and landscape lighting</a></li></ul></div>\n'
            '<div><h4>Areas</h4><ul>' + towns + '<li><a href="' + root + '#area">All 14 areas</a></li></ul></div>\n'
            '<div><h4>Contact</h4><ul><li><a href="tel:' + TEL + '">' + PHONE + '</a></li><li><a href="' + MAPS + '">1150 SW 10th Ave, Suite 103E<br>Pompano Beach, FL 33069</a></li><li><a href="' + root + 'quote/">Get a free estimate</a></li></ul></div>\n'
            '</div>\n<div class="footer-base"><span>Shine of Fort Lauderdale is a locally owned and operated Shine franchise.</span>'
            '<span>Design prototype by White Phoenix. Not the live site.</span></div>\n</div>\n</footer>\n'
            '<div class="action-bar" aria-label="Quick actions"><div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="tel:' + TEL + '">' + ICON["phone"] + 'Call</a></div>'
            '<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="' + root + 'quote/">Free estimate</a></div></div>\n'
            '</body>\n</html>\n')


def choice(name, val, label, art, typ="radio", desc=""):
    inner = '<span>' + label + ('<small>' + desc + '</small>' if desc else '') + '</span>' if desc else label
    return ('<label class="choice"><input type="' + typ + '" name="' + name + '" value="' + val + '">' + ART.get(art, "") + inner +
            '<span class="tick">' + ICON["check"] + '</span></label>')


def home():
    root = ""
    trust = "".join('<div class="wp-reveal">' + a + '<div><h3>' + h + '</h3><p>' + p + '</p></div></div>' for a, h, p in TRUST_ART)
    towns = "".join("<li>" + t + "</li>" for t in TOWNS)
    faqs = [
        ("Which areas do you cover?", "Fourteen communities across Broward and south Palm Beach County, from Boca Raton and Delray Beach down to Hollywood and Pembroke Pines. The full list is above. Outside it? Call and we'll point you to the nearest Shine."),
        ("Do you work on businesses as well as homes?", "Yes. We clean and light homes and commercial properties: storefronts, offices, apartment buildings and more."),
        ("What happens if I'm not happy with the job?", "Tell us. Every job is covered by Shine's 100% money-back guarantee: we come back and make it right, or we refund you."),
        ("Do you take the holiday lights down too?", "Yes. We design the display, install it, look after it through the season and take it down when the holidays are over."),
        ("Can you clean my roof without damaging it?", "That's why we soft wash. Low pressure and the right cleaner lift the algae streaks without forcing water under tiles or shingles."),
    ]
    faq = "".join('<details class="wp-block-details is-style-arrow-icon-details"><summary>' + q + '</summary><p>' + a + '</p></details>' for q, a in faqs)
    # Funnel step 1: low-commitment picker (services + ZIP). Name and phone come later, on the quote page.
    picks = "".join(choice("services", k, t, a, "checkbox") for k, t, a, d, _ in FUNNEL)
    hero_form = (
        '<div class="gform_wrapper gravity-theme start-box" data-form="start">'
        '<form novalidate action="quote/"><div class="gform_validation_errors" hidden role="alert">Pick at least one service and enter a 5-digit ZIP code.</div>'
        '<fieldset class="gfield gfield_contains_required" data-group><legend class="gfield_label">What needs a shine? <span class="gfield_description">Choose one or more</span></legend>'
        '<div class="choice-cards is-picker">' + picks + '</div></fieldset>'
        '<div class="zip-row"><div class="gfield gfield_contains_required"><label class="gfield_label" for="h-zip">Your ZIP code</label><input id="h-zip" name="zip" inputmode="numeric" maxlength="5" autocomplete="postal-code" placeholder="e.g. 33301" required></div>'
        '<button class="wp-block-button__link wp-element-button" type="submit">Get my free estimate ' + ICON["arrow"] + '</button></div>'
        '</form></div>')
    svc_rows = "".join(
        '<li class="svc-row wp-reveal"><div class="svc-name">' + ART[a].replace('class="art"', 'class="art lg"') + '<h3>' + t + '</h3></div>'
        '<p>' + d + '</p><a class="text-link" href="quote/?services=' + k + '">Get a price ' + ICON["arrow"] + '</a></li>'
        for k, t, a, _, d in FUNNEL)
    body = (
        '<main id="main">\n'
        # Hero: core Media & Text (media right, image fill)
        '<section class="wp-block-media-text has-media-on-the-right is-stacked-on-mobile is-image-fill-element hero">\n'
        '<div class="wp-block-media-text__content">'
        '<h1>Window cleaning and exterior care in Fort Lauderdale</h1>'
        '<p class="lede">Clear glass, clean roofs and driveways, and holiday lights hung for you. Pick what you need and get a free estimate from the local crew.</p>'
        + hero_form +
        '<ul class="hero-meta"><li>' + ICON["check"] + '100% money-back guarantee</li><li>' + ICON["check"] + 'Free, no-obligation estimate</li><li>' + ICON["check"] + 'Locally owned</li></ul>'
        '</div>\n<figure class="wp-block-media-text__media"><img src="assets/img/hero.webp" srcset="assets/img/hero-1000.webp 1000w, assets/img/hero.webp 2000w" sizes="(max-width: 781px) 100vw, 50vw" alt="Shine technician cleaning the windows of a patio" width="2000" height="982" fetchpriority="high"></figure>\n'
        '</section>\n'
        # Trust row
        '<section class="wp-block-group"><div class="trust alignwide">' + trust + '</div></section>\n'
        # Services: TT24 cta-services-image-left
        '<section class="wp-block-group section has-base-2-background-color" id="services"><div class="alignwide">\n'
        '<div class="section-head"><h2>Everything on the outside of the house, and the glass on the inside</h2>'
        '<p class="is-muted">Salt air, storms and algae work on a South Florida building every day. Book one service, or put a few together on the same visit.</p></div>\n'
        '<ul class="svc-list">' + svc_rows + '</ul>\n'
        '<p class="svc-foot">Not sure what you need? Call <a href="tel:' + TEL + '">' + PHONE + '</a> and describe it. We\'ll tell you.</p>\n'
        '</div></section>\n'
        # Lights band
        '<section class="lights" id="lights" data-lights>' + string_svg(26) + '\n<div class="inner wp-block-group"><div class="alignwide grid">\n'
        '<div class="wp-reveal"><p class="is-style-text-annotation">Booking now for the holidays</p><h2>Holiday lights, designed, hung and taken down for you</h2>'
        '<p>No ladders, no tangled strings in the garage. We design a display that suits your house, install it, look after it through the season and take it all down after.</p>'
        '<ul class="wp-block-list"><li>A custom design for your roofline, palms and entrance</li><li>Installed and maintained by our crew</li><li>Taken down when the season is over</li></ul>'
        '<div class="wp-block-buttons"><div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="quote/?service=holiday">Book a holiday lighting estimate</a></div></div>'
        '<p class="switch-note">These are the only lights on this page we hung ourselves. <button type="button" data-switch>Turn them off</button></p></div>\n'
        '<div class="light-kinds wp-reveal"><div><h3>Holiday and Christmas</h3><p>Rooflines, trees, wreaths and entrances, for the season.</p></div>'
        '<div><h3>Landscape</h3><p>Walkways, garden beds and the best features of the house.</p></div>'
        '<div><h3>Bistro and string</h3><p>Patios, pool decks and backyards that get used after dark.</p></div>'
        '<div><h3>Permanent</h3><p>Installed once, on all year, ready for any occasion.</p></div></div>\n'
        '</div></div></section>\n'
        # About: media-text
        '<section class="wp-block-group section"><div class="alignwide wp-block-media-text about">\n'
        '<figure class="wp-block-media-text__media wp-reveal"><img src="assets/img/van.webp" alt="A red Shine van with the script logo on the side" width="1100" height="1100" loading="lazy"></figure>\n'
        '<div class="wp-block-media-text__content"><p class="is-style-text-annotation">Shine of Fort Lauderdale</p>'
        '<h2>A local crew behind a name you see on the road</h2>'
        '<p>We\'re locally owned and operated, working out of Pompano Beach. You get the training, equipment and guarantee of a national brand, and the people who turn up know what sea salt and a rainy season do to a house here.</p>'
        '<p>Homeowners call us for clear windows and clean roofs. Property managers call us for storefronts, offices and apartment buildings that need to look cared for.</p>'
        '<div class="wp-block-buttons"><div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="tel:' + TEL + '">' + ICON["phone"] + 'Call ' + PHONE + '</a></div></div>'
        '</div>\n</div></section>\n'
        # Steps + guarantee
        '<section class="wp-block-group section has-accent-4-background-color"><div class="alignwide">\n'
        '<h2 class="wp-reveal">From to-do to done in three steps</h2><p class="is-muted" style="margin-bottom:2.2rem">Get your weekends back. Here is how it works.</p>'
        '<div class="steps"><div class="step wp-reveal"><h3>Get a free estimate</h3><p>Tell us what needs doing. Your local team sends a no-obligation quote.</p></div>'
        '<div class="step wp-reveal"><h3>Pick a time</h3><p>We book a visit that suits you, home or not.</p></div>'
        '<div class="step wp-reveal"><h3>We make it shine</h3><p>A uniformed crew arrives on time, does the work and leaves the place tidy.</p></div>'
        '<div class="seal wp-reveal"><img src="assets/img/guarantee.svg" alt="100% satisfaction guaranteed seal" width="96" height="120"><p><strong>Our guarantee</strong>If you\'re not completely satisfied, we\'ll make it right or refund your money.</p></div></div>\n'
        '</div></section>\n'
        # Reviews
        '<section class="wp-block-group section has-base-2-background-color" id="reviews"><div class="alignwide">\n'
        '<div class="review-big"><figure class="wp-block-image wp-reveal"><img src="assets/img/house.webp" alt="A clean grey two-story house with a white porch" width="1800" height="762" loading="lazy"></figure>'
        '<figure class="wp-reveal"><blockquote class="wp-block-quote is-style-plain">' + STARS +
        '<p>This is the second time I have used SHINE, and as before they did a great job cleaning our windows and screens. The young men who washed our windows were polite, efficient, and thorough. The pure water they used truly made our windows SHINE!</p>'
        '<cite>Billye Putnam<small>Window and screen cleaning</small></cite></blockquote></figure></div>\n'
        '<div class="review-row">'
        '<blockquote class="wp-block-quote is-style-plain wp-reveal">' + STARS + '<p>Shine did an outstanding job again on our windows! They also cleaned all of the outside coach lights of which a pair are two stories high! Looks fantastic!! We are using them on a regular basis.</p><cite>Carla Templeton<small>Regular window cleaning</small></cite></blockquote>'
        '<blockquote class="wp-block-quote is-style-plain wp-reveal">' + STARS + '<p>These guys always do a fantastic job making sure everything is clean and sparkling! They have done window cleaning and pressure washing for me more than once. They are very professional and helpful.</p><cite>Allison Crossley<small>Windows and pressure washing</small></cite></blockquote>'
        '</div>\n</div></section>\n'
        # Area: cover with parallax
        '<section class="wp-block-cover has-parallax" id="area" style="background-image:url(assets/img/canal.webp)"><span aria-hidden="true" class="wp-block-cover__background has-background-dim-70"></span>'
        '<div class="wp-block-cover__inner-container"><div class="alignwide"><p class="is-style-text-annotation">Service area</p>'
        '<h2>From Boca and Delray down to Hollywood and Pembroke Pines</h2>'
        '<p style="max-width:40em">Waterfront homes, gated communities, condos and Main Street shops. If your address is in one of these 14 areas, the Fort Lauderdale crew comes to you.</p>'
        '<ul class="towns">' + towns + '</ul></div></div></section>\n'
        # FAQ
        '<section class="wp-block-group section"><div class="alignwide faq"><div><p class="is-style-text-annotation">Questions</p><h2>Things people ask before they book</h2>'
        '<p class="is-muted">Something else on your mind? Call <a href="tel:' + TEL + '">' + PHONE + '</a>.</p></div><div>' + faq + '</div></div></section>\n'
        # Contact
        '<section class="wp-block-group section has-accent-3-background-color" id="contact"><div class="alignwide contact-grid">\n'
        '<div><h2>Ready for clear glass and a clean house?</h2><p class="is-muted">Ask for a free, no-obligation estimate. We\'ll get back to you with a price and a time.</p>'
        '<ul class="contact-list"><li><span>Call</span><a href="tel:' + TEL + '">' + PHONE + '</a></li>'
        '<li><span>Office</span><a href="' + MAPS + '">1150 SW 10th Ave, Suite 103E, Pompano Beach, FL 33069</a></li>'
        '<li><span>Covering</span>14 communities in Broward and south Palm Beach County</li></ul>'
        '<div class="wp-block-buttons"><div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="quote/">Get a free estimate</a></div>'
        '<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="tel:' + TEL + '">' + ICON["phone"] + 'Call us</a></div></div></div>\n'
        '<figure class="map-card wp-block-image wp-reveal"><img src="assets/img/map.webp" alt="Map of the Shine of Fort Lauderdale territory from Boca Raton to Pembroke Pines" width="1400" height="850" loading="lazy"></figure>\n'
        '</div></section>\n</main>\n')
    return (head("Window Cleaning, Pressure Washing &amp; Lighting in Fort Lauderdale | Shine",
                 "Window cleaning, pressure washing, roof and gutter cleaning and holiday lighting for homes and businesses from Boca Raton to Pembroke Pines. Free estimates.", root)
            + header(root, "home") + body + footer(root))


def quote():
    root = "../"
    cards = "".join(choice("services", k, t, a, "checkbox", d) for k, t, a, d, _ in FUNNEL)
    body = (
        '<main id="main">\n<section class="page-banner is-compact"><div class="alignwide"><h1>Get your free estimate</h1>'
        '<p style="max-width:38em;color:#c9cfd4">Three short steps, about a minute. The Fort Lauderdale team calls you back with a price and a time.</p></div></section>\n'
        '<section class="wp-block-group section" style="padding-top:var(--wp--preset--spacing--50)"><div class="alignwide quote-layout">\n'
        '<div class="gform_wrapper gravity-theme" data-form="multi"><form novalidate>'
        '<p class="gf_progressbar_title">Step <span data-step>1</span> of 3</p><div class="gf_progressbar" aria-hidden="true"><div class="gf_progressbar_percentage" style="width:33%"></div></div>'
        '<div class="gform_validation_errors" hidden role="alert">There was a problem with your submission. Please review the fields below.</div>\n'
        '<div class="gform_page" data-page="1"><h3>What do you need?</h3><div class="gform_fields"><fieldset class="gfield gfield_contains_required" data-group><legend class="gfield_label">Services<span class="gfield_required">*</span></legend>'
        '<div class="choice-cards is-list">' + cards + '</div><div class="gfield_description">Pick as many as you like. Several services on one visit is common.</div></fieldset></div>'
        '<div class="gform_page_footer"><button type="button" class="wp-block-button__link wp-element-button" data-next>Next</button></div></div>\n'
        '<div class="gform_page" data-page="2" hidden><h3>The property</h3><div class="gform_fields">'
        '<fieldset class="gfield gfield_contains_required" data-group><legend class="gfield_label">Type of property<span class="gfield_required">*</span></legend><div class="choice-cards">'
        + "".join(choice("ptype", v, v, "") for v in ["House", "Condo or townhome", "Business", "HOA or building"]) + '</div></fieldset>'
        '<div class="gfield gfield--width-half"><label class="gfield_label" for="q-stories">Stories</label><select id="q-stories" name="stories"><option value="">Select</option><option>1</option><option>2</option><option>3 or more</option></select></div>'
        '<div class="gfield gfield--width-half gfield_contains_required"><label class="gfield_label" for="q-zip">ZIP code<span class="gfield_required">*</span></label><input id="q-zip" name="zip" inputmode="numeric" maxlength="5" required></div>'
        '<div class="gfield"><label class="gfield_label" for="q-notes">Anything we should know?</label><textarea id="q-notes" name="notes" placeholder="Number of windows, gate code, the stain on the driveway..."></textarea></div>'
        '</div><div class="gform_page_footer"><button type="button" class="wp-block-button__link wp-element-button is-style-outline-btn" data-prev style="background:transparent;color:inherit;border-color:currentColor">Previous</button><button type="button" class="wp-block-button__link wp-element-button" data-next>Next</button></div></div>\n'
        '<div class="gform_page" data-page="3" hidden><h3>Your details</h3><div class="gform_fields">'
        '<div class="gfield gfield--width-half gfield_contains_required"><label class="gfield_label" for="q-name">Name<span class="gfield_required">*</span></label><input id="q-name" name="name" autocomplete="name" required></div>'
        '<div class="gfield gfield--width-half gfield_contains_required"><label class="gfield_label" for="q-phone">Phone<span class="gfield_required">*</span></label><input id="q-phone" name="phone" type="tel" autocomplete="tel" required></div>'
        '<div class="gfield gfield--width-half"><label class="gfield_label" for="q-email">Email</label><input id="q-email" name="email" type="email" autocomplete="email"></div>'
        '<div class="gfield gfield--width-half"><label class="gfield_label" for="q-when">Best time to call</label><select id="q-when" name="when"><option>Any time</option><option>Morning</option><option>Afternoon</option><option>Evening</option></select></div>'
        '</div><div class="gform_page_footer"><button type="button" class="wp-block-button__link wp-element-button" data-prev style="background:transparent;color:inherit;border-color:currentColor">Previous</button><button type="submit" class="wp-block-button__link wp-element-button">Send my request</button></div></div>\n'
        '</form></div>\n'
        '<aside><div class="widget is-dark"><h3>Rather talk it through?</h3><p>Call the Fort Lauderdale team.</p><div class="wp-block-buttons"><div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="tel:' + TEL + '">' + ICON["phone"] + PHONE + '</a></div></div></div>'
        '<div class="widget"><div class="seal" style="background:transparent;border:0;padding:0"><img src="../assets/img/guarantee.svg" alt="100% satisfaction guaranteed seal" width="96" height="120"><p style="color:inherit"><strong style="color:inherit">100% money-back guarantee</strong>Not happy? We make it right or refund your money.</p></div></div>'
        '<div class="widget"><blockquote class="wp-block-quote is-style-plain">' + STARS + '<p>They have done window cleaning and pressure washing for me more than once. They are very professional and helpful.</p><cite>Allison Crossley</cite></blockquote></div></aside>\n'
        '</div></section>\n</main>\n')
    return head("Free Estimate | Shine of Fort Lauderdale", "Request a free, no-obligation estimate for window cleaning, pressure washing, gutters or lighting.", root) + header(root, "quote") + body + footer(root)


def notfound():
    root = "/"
    body = ('<main id="main"><section class="page-banner" style="min-height:60vh"><div class="alignwide"><h1>This page has gone streaky</h1>'
            '<p style="color:#c9cfd4">We couldn\'t find it. Try the home page, or call and we\'ll help you out.</p>'
            '<div class="wp-block-buttons"><div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="/">Home</a></div>'
            '<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="tel:' + TEL + '">Call ' + PHONE + '</a></div></div></div></section></main>\n')
    return head("Page not found | Shine of Fort Lauderdale", "Page not found.", root) + header(root, "") + body + footer(root)


def write(rel, html):
    p = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w") as f:
        f.write(html)
    print("wrote", rel)


write("index.html", home())
write("quote/index.html", quote())
write("404.html", notfound())
with open(os.path.join(OUT, "version.json"), "w") as f:
    json.dump({"build": BUILD}, f)
