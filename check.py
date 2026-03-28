# -*- coding: utf-8 -*-
import re

with open(r'D:\workAIspace\openclaw\tscs-demo\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

drv_pages = re.findall(r'id="drv-[^"]+"', content)
fld_pages = re.findall(r'id="field-[^"]+"', content)
plat_pages = re.findall(r'id="plat-[^"]+"', content)
ent_pages = re.findall(r'id="ent-[^"]+"', content)

print('=== Driver pages ===')
for p in drv_pages:
    print(' ', p)

print('\n=== Field pages ===')
for p in fld_pages:
    print(' ', p)

print('\n=== Platform pages ===')
for p in plat_pages:
    print(' ', p)

print('\n=== Enterprise pages ===')
for p in ent_pages:
    print(' ', p)

print(f'\nTotal file size: {len(content)} bytes')

# Check for mobile-specific CSS
mobile_check = ['375px', 'mobile', 'min-app', 'driver-accent', 'field-accent']
for m in mobile_check:
    found = m in content
    print(f'Contains "{m}": {found}')
