# -*- coding: utf-8 -*-
import subprocess, re

path = r'D:\workAIspace\openclaw\tscs-demo\index.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Check first script tag
first_script_start = content.find('<script')
first_script_end = content.find('</script>')
print(f'First script: {first_script_start} to {first_script_end}')
first_js = content[first_script_start:first_script_end+9]
print('First JS snippet:')
print(first_js[:500])

# Check the nav HTML
nav_idx = content.find('class="top-nav"')
print('\nNav HTML:')
print(content[nav_idx:nav_idx+600])
