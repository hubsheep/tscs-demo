# -*- coding: utf-8 -*-
with open(r'D:\workAIspace\openclaw\tscs-demo\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

for pid in ['pp-l', 'ph', 'dl', 'fl', 'ee-l', 'fh', 'pp-login', 'eh']:
    idx = content.find('id="' + pid + '"')
    if idx >= 0:
        print(pid + ': ' + repr(content[idx:idx+40]))
    else:
        print(pid + ': NOT FOUND')

# Check if onclick buttons exist in body of first page
ph_idx = content.find('id="ph"')
if ph_idx >= 0:
    chunk = content[ph_idx:ph_idx+500]
    print('\nph page chunk:')
    print(chunk[:300])
