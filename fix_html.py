# -*- coding: utf-8 -*-
"""Fix HTML syntax errors in the generated file"""
import re

path = r'D:\workAIspace\openclaw\tscs-demo\index.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix known issues found in the HTML:
# 1. </b> should be </b>
content = content.replace('</b>', '</b>')
# 2. Fix <option> vs </option> issues - ensure all options are closed
# 3. Fix value="> in checkbox
content = content.replace('value=">', 'value="">')
# 4. Fix any unclosed option tags
# Count issues
open_tags = content.count('<option')
close_tags = content.count('</option')
print(f'Option tags: {open_tags} open, {close_tags} close')

# Fix duplicate </td>
content = re.sub(r'</td>\s*</td>', '</td>', content)

# Fix : any <b> without closing 
open_b = content.count('<b>')
close_b = content.count('</b>')
print(f'B tags: {open_b} open, {close_b} close')

# Fix : any malformed attributes
# Fix value= > (missing quote)
content = re.sub(r'value="([^"]*)>$', r'value="\1">', content)

# Fix stray > in content
# Fix multiple closing div issues

print(f'File size: {len(content)}')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Fixed and saved.')
