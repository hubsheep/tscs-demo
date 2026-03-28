# -*- coding: utf-8 -*-
# Read existing HTML + JS append and combine
path = r'D:\workAIspace\openclaw\tscs-demo\index.html'
with open(path, 'r', encoding='utf-8') as f:
    existing = f.read()
# The JS file
js_path = r'D:\workAIspace\openclaw\tscs-demo\append.js'
with open(js_path, 'r', encoding='utf-8') as f:
    js_content = f.read()
# Combine
combined = existing + js_content
print(f'Existing: {len(existing)}, JS: {len(js_content)}, Combined: {len(combined)}')
with open(path, 'w', encoding='utf-8') as f:
    f.write(combined)
print('Written')
