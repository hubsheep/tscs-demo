# -*- coding: utf-8 -*-
with open(r'D:\workAIspace\openclaw\tscs-demo\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')
print(f'Total lines: {len(lines)}')

# Find lines with Chinese
chinese_lines = []
for i, line in enumerate(lines):
    for c in line:
        if '\u4e00' <= c <= '\u9fff':
            chinese_lines.append((i, line[:80]))
            break

print(f'Lines with Chinese: {len(chinese_lines)}')
for i, l in chinese_lines[:10]:
    print(f'Line {i}: {repr(l)}')
