# -*- coding: utf-8 -*-
path = r'D:\workAIspace\openclaw\tscs-demo\index.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Get second script (the navigation JS)
scripts = []
start = 0
while True:
    s = content.find('<script', start)
    e = content.find('</script>', start)
    if s < 0: break
    scripts.append((s, e, content[s:e+9]))
    start = e + 9

print(f'Found {len(scripts)} script tags')
for i, (s, e, tag) in enumerate(scripts):
    print(f'Script {i}: pos {s}-{e}, tag: {repr(tag[:50])}')

# The second script starts the actual navigation JS
js = content[scripts[1][0]:scripts[1][1]]
print(f'\nNavigation JS length: {len(js)}')

# Check the key functions
print('st() function:')
s = js.find('function st(')
print(js[s:s+400])

print('\n\nsp() function:')
s = js.find('function sp(')
print(js[s:s+400])

print('\n\npn() function:')
s = js.find('function pn(')
print(js[s:s+300])

print('\n\nst("p") call:')
idx = js.find('st("p")')
print(repr(js[idx-50:idx+20]))
