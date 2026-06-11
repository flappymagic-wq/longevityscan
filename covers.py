"""
Inline SVG cover generator for LongevityScan article cards.
One motif per category, drawn in the category accent colour on a dark ground.
Returns a compact single-line SVG string (no newlines) for embedding.
"""

# Accent colours matching the site's acc-* / pill system
COL = {
    "g": "#7fff6e",   # green  — supplements, studies, epigenetik
    "o": "#ff9500",   # orange — biohacking, routine
    "b": "#6ea8ff",   # blue   — schlaf, wearables, protokoll
    "p": "#ff6b9d",   # pink   — ernaehrung
    "r": "#ff6b6b",   # red    — glp-1 / medication
}
# dark grounds per accent (very dark tint of the hue)
GROUND = {
    "g": "#0d120c", "o": "#161009", "b": "#0a0e16", "p": "#160a10", "r": "#160a0a",
}

def _wrap(body, ground, vb="0 0 300 150"):
    return (f'<svg viewBox="{vb}" xmlns="http://www.w3.org/2000/svg" '
            f'class="cover-svg" preserveAspectRatio="xMidYMid meet" '
            f'role="img" aria-hidden="true" style="background:{ground}">'
            f'{body}</svg>')

def molecule(c):
    col = COL[c]
    return (f'<g stroke="{col}" stroke-width="1.4" fill="{col}">'
            f'<circle cx="150" cy="75" r="7"/>'
            f'<circle cx="105" cy="48" r="5" opacity=".85"/>'
            f'<circle cx="108" cy="104" r="5" opacity=".7"/>'
            f'<circle cx="198" cy="55" r="5" opacity=".8"/>'
            f'<circle cx="195" cy="102" r="4" opacity=".6"/>'
            f'<circle cx="240" cy="78" r="4" opacity=".5"/>'
            f'<line x1="150" y1="75" x2="105" y2="48" opacity=".55"/>'
            f'<line x1="150" y1="75" x2="108" y2="104" opacity=".5"/>'
            f'<line x1="150" y1="75" x2="198" y2="55" opacity=".55"/>'
            f'<line x1="150" y1="75" x2="195" y2="102" opacity=".45"/>'
            f'<line x1="198" y1="55" x2="240" y2="78" opacity=".4"/>'
            f'<circle cx="62" cy="80" r="3" opacity=".4"/>'
            f'<line x1="105" y1="48" x2="62" y2="80" opacity=".3"/>'
            f'</g>')

def waves(c):
    col = COL[c]
    return (f'<g fill="none" stroke="{col}" stroke-width="2">'
            f'<path d="M20 95 Q60 40 100 95 Q140 40 180 95 Q220 40 260 95" opacity=".9"/>'
            f'<path d="M20 95 Q60 65 100 95 Q140 65 180 95 Q220 65 260 95" opacity=".4"/>'
            f'<path d="M20 110 Q70 85 120 110 Q170 85 220 110 Q260 95 280 110" opacity=".25"/>'
            f'</g>')

def pulse(c):
    col = COL[c]
    return (f'<polyline points="15,80 70,80 88,80 100,45 116,112 132,62 150,80 230,80 250,80 268,55 285,80" '
            f'fill="none" stroke="{col}" stroke-width="2.2" stroke-linejoin="round" stroke-linecap="round"/>'
            f'<circle cx="116" cy="112" r="3.5" fill="{col}"/>')

def helix(c):
    col = COL[c]
    rungs = ""
    import math
    for i in range(9):
        x = 60 + i*22
        ph = i*0.7
        y1 = 75 + 32*math.sin(ph)
        y2 = 75 - 32*math.sin(ph)
        op = 0.3 + 0.5*abs(math.cos(ph))
        rungs += f'<line x1="{x:.0f}" y1="{y1:.0f}" x2="{x:.0f}" y2="{y2:.0f}" stroke="{col}" stroke-width="1.3" opacity="{op:.2f}"/>'
    top = "M60 43 " + " ".join(f"Q{60+i*22+11:.0f} {75+32*math.sin(i*0.7+0.35):.0f} {60+(i+1)*22:.0f} {75+32*math.sin((i+1)*0.7):.0f}" for i in range(8))
    bot = "M60 107 " + " ".join(f"Q{60+i*22+11:.0f} {75-32*math.sin(i*0.7+0.35):.0f} {60+(i+1)*22:.0f} {75-32*math.sin((i+1)*0.7):.0f}" for i in range(8))
    return (f'<path d="{top}" fill="none" stroke="{col}" stroke-width="2"/>'
            f'<path d="{bot}" fill="none" stroke="{col}" stroke-width="2" opacity=".6"/>{rungs}')

def checklist(c):
    col = COL[c]
    rows = ""
    for i in range(4):
        y = 45 + i*22
        rows += (f'<rect x="92" y="{y-9}" width="16" height="16" rx="3" fill="none" stroke="{col}" stroke-width="1.6" opacity="{0.9-i*0.18:.2f}"/>'
                 f'<polyline points="95,{y} 99,{y+4} 105,{y-5}" fill="none" stroke="{col}" stroke-width="1.8" opacity="{0.9-i*0.18:.2f}"/>'
                 f'<line x1="120" y1="{y}" x2="{210-i*18}" y2="{y}" stroke="{col}" stroke-width="2" opacity="{0.5-i*0.1:.2f}"/>')
    return f'<g>{rows}</g>'

def chart(c):
    col = COL[c]
    bars = ""
    heights = [34, 52, 44, 70, 60, 86]
    for i,h in enumerate(heights):
        x = 80 + i*26
        bars += f'<rect x="{x}" y="{120-h}" width="15" height="{h}" rx="2" fill="{col}" opacity="{0.45+i*0.09:.2f}"/>'
    return (f'<g>{bars}<line x1="72" y1="120" x2="250" y2="120" stroke="{col}" stroke-width="1.4" opacity=".4"/>'
            f'<polyline points="87,86 113,68 139,76 165,50 191,60 217,34" fill="none" stroke="{col}" stroke-width="2" opacity=".9"/></g>')

def plate(c):
    col = COL[c]
    return (f'<g fill="none" stroke="{col}" stroke-width="2">'
            f'<circle cx="150" cy="75" r="40"/>'
            f'<circle cx="150" cy="75" r="27" opacity=".5"/>'
            f'<line x1="150" y1="35" x2="150" y2="115" opacity=".3"/>'
            f'<path d="M150 75 A40 40 0 0 1 178 113" stroke-width="6" opacity=".55"/>'
            f'</g>')

def ring(c):
    col = COL[c]
    return (f'<g fill="none" stroke="{col}" stroke-width="2.4">'
            f'<circle cx="150" cy="75" r="34"/>'
            f'<circle cx="150" cy="75" r="22" opacity=".35" stroke-width="8"/>'
            f'</g><circle cx="150" cy="41" r="3" fill="{col}"/>')

def capsule(c):
    col = COL[c]
    return (f'<g fill="none" stroke="{col}" stroke-width="2">'
            f'<rect x="108" y="58" width="84" height="34" rx="17"/>'
            f'<line x1="150" y1="58" x2="150" y2="92" opacity=".5"/>'
            f'<rect x="108" y="58" width="42" height="34" rx="17" fill="{col}" opacity=".18" stroke="none"/>'
            f'</g>'
            f'<circle cx="80" cy="48" r="4" fill="{col}" opacity=".4"/>'
            f'<circle cx="220" cy="104" r="5" fill="{col}" opacity=".35"/>'
            f'<circle cx="210" cy="40" r="3" fill="{col}" opacity=".5"/>')

# motif registry: keyword -> (fn, accent)
MOTIFS = {
    "molecule": molecule,
    "waves": waves,
    "pulse": pulse,
    "helix": helix,
    "checklist": checklist,
    "chart": chart,
    "plate": plate,
    "ring": ring,
    "capsule": capsule,
}

def cover(motif, accent, label="", sub=""):
    body = MOTIFS[motif](accent)
    col = COL[accent]
    txt = ""
    if label:
        txt += (f'<text x="20" y="124" fill="{col}" font-family="Space Mono,monospace" '
                f'font-size="11" opacity=".85" letter-spacing="1">{label}</text>')
    return _wrap(body + txt, GROUND[accent])

if __name__ == "__main__":
    # smoke test
    for m in MOTIFS:
        s = cover(m, "g", label=m.upper())
        assert s.startswith("<svg") and "\n" not in s
    print("ok", len(MOTIFS), "motifs")
