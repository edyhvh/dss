from fontTools.ttLib import TTFont

f = TTFont('Deadseascrolls-Regular.ttf')
glyphs = set(f.getGlyphNames())

# Basic ASCII set (GF Latin Core requirement for non-Latin fonts)
ascii_needed = set([
    '.notdef', 'space', 'exclam', 'quotedbl', 'numbersign', 'dollar', 'percent', 
    'ampersand', 'quotesingle', 'parenleft', 'parenright', 'asterisk', 'plus', 
    'comma', 'hyphen', 'period', 'slash', 'zero', 'one', 'two', 'three', 'four', 
    'five', 'six', 'seven', 'eight', 'nine', 'colon', 'semicolon', 'less', 'equal', 
    'greater', 'question', 'at', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
    'bracketleft', 'backslash', 'bracketright', 'asciicircum', 'underscore', 
    'grave', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'braceleft', 'bar', 
    'braceright', 'asciitilde'
])

missing = ascii_needed - glyphs
present = ascii_needed & glyphs

print(f'\n=== ASCII COVERAGE ===')
print(f'Required: {len(ascii_needed)} glyphs')
print(f'Present: {len(present)} glyphs')
print(f'Missing: {len(missing)} glyphs')

if missing:
    print(f'\nMissing glyphs: {sorted(missing)}')
else:
    print("\n✅ All required ASCII glyphs are present!")

# Check Hebrew coverage
hebrew_glyphs = [g for g in glyphs if g.startswith('afii576')]
print(f'\n=== HEBREW COVERAGE ===')
print(f'Hebrew glyphs found: {len(hebrew_glyphs)}')
print(f'Hebrew glyphs: {sorted(hebrew_glyphs)}')
