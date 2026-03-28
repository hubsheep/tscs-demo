# -*- coding: utf-8 -*-
"""Add phone frame styling to driver and field terminals - clean version"""

with open(r'D:\workAIspace\openclaw\tscs-demo\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

print(f'Original size: {len(content)}')

# Add CSS
phone_css = '''
/* PHONE FRAME */
.phone-wrap{display:flex;justify-content:center;align-items:flex-start;padding:32px 20px;background:#d8d8d8;min-height:calc(100vh - 56px)}
.phone-frame{width:390px;background:#fff;border-radius:36px;box-shadow:0 8px 40px rgba(0,0,0,.22),0 0 0 11px #1a1a1a;overflow:hidden;position:relative}
.phone-notch{height:34px;background:#1a1a1a;display:flex;align-items:flex-end;justify-content:center;padding-bottom:6px}
.phone-notch::after{content:'';width:90px;height:16px;background:#111;border-radius:0 0 10px 10px}
.phone-body{height:calc(100vh - 90px);overflow-y:auto;background:#fff}
.phone-bottom-bar{position:absolute;bottom:0;left:0;right:0;height:58px;background:#fff;border-top:1px solid #eee;display:flex}
.phone-tab{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2px;font-size:10px;color:#999;cursor:pointer;transition:color .15s}
.phone-tab .icon{font-size:20px}
.driver-phone .phone-tab.active{color:#FA8C16}
.field-phone .phone-tab.active{color:#722ED1}
.driver-phone .phone-bottom-bar{background:#fffaf5}
.field-phone .phone-bottom-bar{background:#f5f0ff}
'''

# Insert before </style>
idx = content.rfind('</style>')
content = content[:idx] + phone_css + content[idx:]
print(f'After CSS: {len(content)}')

# --- Wrap driver terminal in phone frame ---
d_start = content.find('<div id="term-driver"')
d_end = content.find('<!-- ========== FIELD')
driver_section = content[d_start:d_end]

# Remove old sidebar from driver
driver_section = driver_section.replace(
    '<div class="sidebar" style="background:#fff5e6">',
    '<div style="background:#fffaf5;padding:10px 14px 6px;border-bottom:1px solid #eee;font-size:13px;font-weight:600;color:#FA8C16">驾驶员端</div><div style="padding:8px 0;background:#fffaf5">'
)
# Remove sidebar class rest
driver_section = driver_section.replace('<div class="sidebar-item active" onclick="showPage', 
    '<div style="padding:8px 14px;font-size:12px;color:#FA8C16;font-weight:500;border-left:3px solid #FA8C16;background:rgba(250,140,22,.05)" onclick="showPage')

# Fix sidebar items in driver to plain style  
import re
# Replace all sidebar-item classes in driver section
driver_section = re.sub(r'<div class="sidebar-item" onclick="showPage',
    '<div style="padding:8px 14px;font-size:12px;color:#666;border-left:3px solid transparent" onclick="showPage',
    driver_section)
driver_section = re.sub(r'class="sidebar-item"',
    'style="padding:8px 14px;font-size:12px;color:#666;border-left:3px solid transparent"', 
    driver_section)

# Add bottom nav bar before closing divs
driver_section = driver_section.replace(
    '<!-- ========== FIELD',
    '<div class="phone-bottom-bar driver-phone-bar"><div class="phone-tab active" onclick="phNav(\'driver\',\'drv-home\',this)"><span class="icon">🏠</span><span>首页</span></div><div class="phone-tab" onclick="phNav(\'driver\',\'drv-report\',this)"><span class="icon">📋</span><span>报案</span></div><div class="phone-tab" onclick="phNav(\'driver\',\'drv-case\',this)"><span class="icon">📂</span><span>案件</span></div><div class="phone-tab" onclick="phNav(\'driver\',\'drv-score\',this)"><span class="icon">📊</span><span>评分</span></div></div></div></div><!-- ========== FIELD'
)

# Wrap driver in phone frame
driver_wrapped = '<div class="phone-wrap"><div class="phone-frame driver-phone"><div class="phone-notch"></div><div class="phone-body">' + driver_section + '</div><!-- ========== FIELD'

content = content[:d_start] + driver_wrapped + content[d_end:]

# --- Wrap field terminal in phone frame ---
f_start = content.find('<div id="term-field"')
f_end = content.find('<!-- TOAST')
field_section = content[f_start:f_end]

# Remove old sidebar from field
field_section = field_section.replace(
    '<div class="sidebar" style="background:#f5f0ff">',
    '<div style="background:#f5f0ff;padding:10px 14px 6px;border-bottom:1px solid #eee;font-size:13px;font-weight:600;color:#722ED1">现场端</div><div style="padding:8px 0;background:#f5f0ff">'
)
field_section = re.sub(r'<div class="sidebar-item"',
    '<div style="padding:8px 14px;font-size:12px;color:#666;border-left:3px solid transparent"', 
    field_section)
field_section = field_section.replace(
    '<!-- TOAST',
    '<div class="phone-bottom-bar field-phone-bar"><div class="phone-tab field-tab active" onclick="phNav(\'field\',\'field-home\',this)"><span class="icon">📋</span><span>工作台</span></div><div class="phone-tab field-tab" onclick="phNav(\'field\',\'field-task\',this)"><span class="icon">📝</span><span>任务</span></div><div class="phone-tab field-tab" onclick="phNav(\'field\',\'field-eval\',this)"><span class="icon">💰</span><span>评估</span></div><div class="phone-tab field-tab" onclick="phNav(\'field\',\'field-approval\',this)"><span class="icon">✅</span><span>审批</span></div></div></div></div><!-- TOAST'
)

field_wrapped = '<div class="phone-wrap"><div class="phone-frame field-phone"><div class="phone-notch"></div><div class="phone-body">' + field_section + '<!-- TOAST'

content = content[:f_start] + field_wrapped + content[f_end:]

# Add JS function before </script>
js_end = content.rfind('</script>')
phNav_js = '''
function phNav(term, pageId, el) {
  var tabs = el.parentElement.querySelectorAll('.phone-tab');
  for (var i = 0; i < tabs.length; i++) tabs[i].classList.remove('active');
  el.classList.add('active');
  showPage(term, pageId);
}
'''
content = content[:js_end] + phNav_js + content[js_end:]

print(f'Final size: {len(content)}')

with open(r'D:\workAIspace\openclaw\tscs-demo\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done! Phone frames added.')
print(f'drv-home in file: {"drv-home" in content}')
print(f'field-home in file: {"field-home" in content}')
print(f'phone-frame in file: {"phone-frame" in content}')
