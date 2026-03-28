# -*- coding: utf-8 -*-
with open(r'D:\workAIspace\openclaw\tscs-demo\index.html', 'rb') as f:
    raw = f.read()
print('Size:', len(raw))
print('BOM check:', raw[:3])
# Check for UTF-8 BOM
if raw[:3] == b'\xef\xbb\xbf':
    print('Has UTF-8 BOM - might cause issues')
    content = raw[3:].decode('utf-8')
else:
    try:
        content = raw.decode('utf-8')
        print('Decodes as UTF-8 OK, size:', len(content))
    except:
        print('UTF-8 decode FAILED')
