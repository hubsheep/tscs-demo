# -*- coding: utf-8 -*-
path = r'D:\workAIspace\openclaw\tscs-demo\index.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

body_start = content.find('<body>')
print('Body start:', body_start)
print('After body (first 800 chars):')
print(content[body_start:body_start+800])
