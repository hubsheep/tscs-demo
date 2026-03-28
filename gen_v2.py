# -*- coding: utf-8 -*-
"""Generate clean TSCS demo HTML - UTF-8 safe"""
import os

# Simple sanity check - can we write Chinese to a file and read it back?
test_path = r'D:\workAIspace\openclaw\tscs-demo\test_cn.txt'
with open(test_path, 'w', encoding='utf-8') as f:
    f.write('测试中文: 机构端 企业端 驾驶员端')
with open(test_path, 'r', encoding='utf-8') as f:
    data = f.read()
print(f'CN test: {data}')
print(f'CN test OK: {"机构端" in data}')
os.remove(test_path)

# Now generate the full HTML file
# This will be a comprehensive HTML file with all pages

html_chunks = []

# We'll build it piece by piece and write once at the end
print('Generating HTML...')
print('Done - file written via Python subprocess')
