# -*- coding: utf-8 -*-
"""Add phone frame styling to driver and field terminals"""

with open(r'D:\workAIspace\openclaw\tscs-demo\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

print(f'File size before: {len(content)}')

# Add phone frame CSS before </style>
phone_css = '''
/* Phone Frame */
.phone-wrap{
  display:flex;
  justify-content:center;
  align-items:flex-start;
  padding:30px 20px;
  background:#dcdcdc;
  min-height:calc(100vh - 56px);
}
.phone-frame{
  width:390px;
  background:#fff;
  border-radius:36px;
  box-shadow:0 8px 32px rgba(0,0,0,.2),0 0 0 10px #222;
  overflow:hidden;
  position:relative;
}
.phone-notch{
  height:32px;
  background:#222;
  display:flex;
  align-items:center;
  justify-content:center;
}
.phone-notch::after{
  content:'';
  width:100px;
  height:18px;
  background:#111;
  border-radius:0 0 12px 12px;
}
.phone-content{
  height:calc(100vh - 88px);
  overflow-y:auto;
  background:#fff;
}
.phone-home-bar{
  height:20px;
  background:#fff;
  display:flex;
  align-items:center;
  justify-content:center;
}
.phone-home-bar::after{
  content:'';
  width:120px;
  height:4px;
  background:#ccc;
  border-radius:2px;
}
.driver-frame .phone-notch{background:#222}
.driver-frame .phone-tab-bar{background:#fffaf5;border-top:1px solid #eee}
.field-frame .phone-notch{background:#222}
.field-frame .phone-tab-bar{background:#f5f0ff;border-top:1px solid #eee}
.phone-tab-bar{
  position:absolute;
  bottom:0;left:0;right:0;
  height:56px;
  display:flex;
  background:#fff;
}
.phone-tab-item{
  flex:1;
  display:flex;
  flex-direction:column;
  align-items:center;
  justify-content:center;
  gap:2px;
  font-size:10px;
  color:#999;
  cursor:pointer;
}
.phone-tab-item .icon{font-size:20px}
.phone-tab-item.active{color:#FA8C16}
.field-tab-item.active{color:#722ED1}
.driver-frame .phone-tab-item.active{color:#FA8C16}
.field-frame .phone-tab-item.active{color:#722ED1}
'''

# Insert before </style>
idx = content.rfind('</style>')
content = content[:idx] + phone_css + '\n' + content[idx:]
print(f'After CSS insert: {len(content)}')

# Now fix driver terminal - find and wrap it
d_start = content.find('<div id="term-driver"')
d_end = content.find('<div id="term-field"')
print(f'Driver section: {d_start} to {d_end}')

driver_orig = content[d_start:d_end]
# Replace sidebar in driver
driver_fixed = driver_orig.replace(
    '<div class="sidebar" style="background:#fff5e6">',
    '<div style="background:#fffaf5;padding:12px 16px 8px;border-bottom:1px solid #eee">'
).replace('</div>\n  </div>\n</div>\n\n<!-- ========== FIELD',
    '</div>\n  <div class="phone-tab-bar driver-tab-bar">\n    <div class="phone-tab-item active" onclick="phoneNav(\'driver\',\'drv-home\',this)"><span class="icon">🏠</span><span>首页</span></div>\n    <div class="phone-tab-item" onclick="phoneNav(\'driver\',\'drv-report\',this)"><span class="icon">📋</span><span>报案</span></div>\n    <div class="phone-tab-item" onclick="phoneNav(\'driver\',\'drv-case\',this)"><span class="icon">📂</span><span>案件</span></div>\n    <div class="phone-tab-item" onclick="phoneNav(\'driver\',\'drv-score\',this)"><span class="icon">📊</span><span>评分</span></div>\n  </div>\n</div>\n</div>\n\n<!-- ========== FIELD')

content = content[:d_start] + driver_fixed + content[d_end:]

# Fix field terminal
f_start = content.find('<div id="term-field"')
f_end = content.find('<!-- TOAST')
field_orig = content[f_start:f_end]
field_fixed = field_orig.replace(
    '<div class="sidebar" style="background:#f5f0ff">',
    '<div style="background:#f5f0ff;padding:12px 16px 8px;border-bottom:1px solid #eee">'
).replace('</div>\n  </div>\n</div>\n\n<!-- TOAST',
    '</div>\n  <div class="phone-tab-bar field-tab-bar">\n    <div class="phone-tab-item field-tab-item active" onclick="phoneNav(\'field\',\'field-home\',this)"><span class="icon">📋</span><span>工作台</span></div>\n    <div class="phone-tab-item field-tab-item" onclick="phoneNav(\'field\',\'field-task\',this)"><span class="icon">📝</span><span>任务</span></div>\n    <div class="phone-tab-item field-tab-item" onclick="phoneNav(\'field\',\'field-eval\',this)"><span class="icon">💰</span><span>评估</span></div>\n    <div class="phone-tab-item field-tab-item" onclick="phoneNav(\'field\',\'field-approval\',this)"><span class="icon">✅</span><span>审批</span></div>\n  </div>\n</div>\n</div>\n\n<!-- TOAST')

content = content[:f_start] + field_fixed + content[f_end:]

# Wrap driver and field in phone-frame div
# Find term-driver div start
d_start2 = content.find('<div id="term-driver"')
# Find the closing of the div before <!-- TOAST
toast_idx = content.find('<!-- TOAST')
# We need to find where the div that contains term-driver ends
# Find the last </div> before toast
last_div_before_toast = content.rfind('</div>', 0, toast_idx)
print(f'Last div before toast at: {last_div_before_toast}')

# Wrap everything from term-driver to before toast in phone-wrap
wrapped = '\n<div class="phone-wrap">\n' + content[d_start2:toast_idx] + '\n</div>\n\n<!-- TOAST'
content = content[:d_start2] + wrapped + content[toast_idx + len('\n<!-- TOAST'):]

# Update switchTerm to use phone-wrap
content = content.replace(
    "el.style.display = 'flex';",
    "el.style.display = 'flex';"
)
# Actually phone-wrap uses display:flex already via .phone-wrap rule

# Add phoneNav JS function before </script>
js_end = content.rfind('</script>')
phone_js = '''
function phoneNav(term, pageId, el) {
  // Remove active from all tabs
  document.querySelectorAll('.phone-tab-item').forEach(function(item){item.classList.remove('active')});
  el.classList.add('active');
  // Show the page
  showPage(term, pageId);
}
'''
content = content[:js_end] + phone_js + '\n' + content[js_end:]

print(f'Final size: {len(content)}')

with open(r'D:\workAIspace\openclaw\tscs-demo\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done!')
