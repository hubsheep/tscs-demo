# -*- coding: utf-8 -*-
with open(r'D:\workAIspace\openclaw\tscs-demo\index.html', 'r', encoding='utf-8') as f:
    content = f.read()
print(f'Current file size: {len(content)}')
print(f'Has driver: {"term-driver" in content}')
print(f'Has field: {"term-field" in content}')
