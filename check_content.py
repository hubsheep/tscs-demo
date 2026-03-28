# -*- coding: utf-8 -*-
with open(r'D:\workAIspace\openclaw\tscs-demo\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Check Chinese chars
lines = content.split('\n')
print(f'Total lines: {len(lines)}')
print(f'Total size: {len(content)}')

# Print some lines with Chinese
for i, line in enumerate(lines[:30]):
    if any('\u4e00' <= c <= '\u9fff' for c in line):
        print(f'Line {i}: {line[:100]}')
