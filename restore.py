# -*- coding: utf-8 -*-
import subprocess, sys

# Get clean file from git
result = subprocess.run(
    ['git', 'show', 'HEAD:index.html'],
    cwd=r'D:\workAIspace\openclaw\tscs-demo',
    capture_output=True
)
data = result.stdout.decode('utf-8')
print(f'From git: {len(data)} bytes')

# Count Chinese lines
chinese_count = 0
for line in data.split('\n'):
    for c in line:
        if '\u4e00' <= c <= '\u9fff':
            chinese_count += 1
            break

print(f'Chinese lines: {chinese_count}')

# Write
with open(r'D:\workAIspace\openclaw\tscs-demo\index.html', 'w', encoding='utf-8') as f:
    f.write(data)
print('Written OK')
