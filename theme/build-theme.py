#!/usr/bin/env python3
"""Makes bolgebrud.css from bolgebrud.template.css and tokens.css (hex -> HSL or RGB triplets).
Run from this folder: python3 build-theme.py   (the Dockerfile copies the result, so run it before building)"""
import colorsys, re, sys
from pathlib import Path

here = Path(__file__).parent
tokens = dict(re.findall(r'(--bb-[\w-]+):\s*(#[0-9A-Fa-f]{6})\b', (here / 'tokens.css').read_text()))

def hsl(name, kind):
    if name not in tokens:
        sys.exit(f'unknown token {name} (not a hex colour in tokens.css)')
    if kind == 'r':
        return ' '.join(str(int(tokens[name][i:i + 2], 16)) for i in (1, 3, 5))
    comma = kind == 'c'
    r, g, b = (int(tokens[name][i:i + 2], 16) / 255 for i in (1, 3, 5))
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    f = lambda v: f'{v:.2f}'.rstrip('0').rstrip('.')
    sep = ', ' if comma else ' '
    return f'{f(h * 360)}{sep}{f(s * 100)}%{sep}{f(l * 100)}%'

out = re.sub(r'\{\{([hcr]):(--bb-[\w-]+)\}\}', lambda m: hsl(m.group(2), m.group(1)),
             (here / 'bolgebrud.template.css').read_text())
(here / 'bolgebrud.css').write_text(out)
print('bolgebrud.css written,', len(out), 'bytes')
