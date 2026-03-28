parts = []
for i in range(1, 7):
    with open(r'D:\workAIspace\openclaw\tscs-demo\c' + str(i) + '.html', encoding='utf-8') as f:
        parts.append(f.read())
full = ''.join(parts)
with open(r'D:\workAIspace\openclaw\tscs-demo\index.html', 'w', encoding='utf-8') as f:
    f.write(full)
data = full
print('Total size:', len(data))
print('Has DOCTYPE:', data.startswith('<!DOCTYPE'))
print('Has </html>:', '</html>' in data)
print('Has st function:', 'function st' in data)
print('Has initCharts:', 'initCharts' in data)
print('Chinese lines:', sum(1 for l in data.split('\n') if any('\u4e00' <= c <= '\u9fff' for c in l)))
print('Has tabp:', 'tabp' in data)
print('Has tabe:', 'tabe' in data)
print('Has phwrap:', 'phwrap' in data)
print('Has field:', 'field' in data or '现场端' in data)
print('Last 100 repr:', repr(data[-100:]))
