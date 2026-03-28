# -*- coding: utf-8 -*-
import re
with open(r'D:\workAIspace\openclaw\tscs-demo\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

print('Size:', len(content))
print()

# Check if onclick handlers are correct
print('onclick="st(', content.count('onclick="st('))
print('onclick="sp(', content.count('onclick="sp('))
print('onclick="pn(', content.count('onclick="pn('))
print('onclick="tst(', content.count('onclick="tst('))

# Find problematic onclick
for m in re.finditer(r'onclick="([^"]+)"', content):
    val = m.group(1)
    if '(' not in val or ')' not in val:
        print(f'WEIRD onclick at {m.start()}: {repr(val)}')

# Check page divs
pages = re.findall(r'id="[a-z][a-z0-9]+" class="pg"', content)
print(f'\nPage divs: {len(pages)}')
for p in pages[:10]:
    print(' ', p)

# Check closing structure
print('\nLast 300 chars:')
print(repr(content[-300:]))
