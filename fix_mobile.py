# -*- coding: utf-8 -*-
"""Fix mobile phone frame styling for driver and field terminals"""

with open(r'D:\workAIspace\openclaw\tscs-demo\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add phone-frame CSS before </style>
phone_frame_css = '''
/* PHONE FRAME for mobile terminals */
.phone-frame{
  width:390px;
  min-height:700px;
  background:#fff;
  border-radius:40px;
  box-shadow:0 8px 32px rgba(0,0,0,.18),0 0 0 12px #1a1a1a;
  margin:0 auto;
  overflow:hidden;
  position:relative;
}
.phone-frame::before{
  content:'';
  position:absolute;
  top:0;left:50%;transform:translateX(-50%);
  width:120px;height:28px;
  background:#1a1a1a;
  border-radius:0 0 18px 18px;
  z-index:10;
}
.phone-screen{
  background:#fff;
  min-height:700px;
  display:flex;
  flex-direction:column;
}
.phone-topbar{
  height:52px;
  background:#fff;
  display:flex;
  align-items:center;
  justify-content:center;
  font-size:13px;
  font-weight:600;
  border-bottom:1px solid #eee;
  padding:0 16px;
  flex-shrink:0;
  margin-top:28px;
}
.phone-topbar .back{
  position:absolute;
  left:16px;
  font-size:16px;
  cursor:pointer;
}
.phone-body{
  flex:1;
  overflow-y:auto;
  padding:12px 14px 80px;
  background:#f5f5f5;
}
.phone-bottom-nav{
  position:absolute;
  bottom:0;left:0;right:0;
  height:60px;
  background:#fff;
  border-top:1px solid #eee;
  display:flex;
  z-index:5;
}
.phone-nav-item{
  flex:1;
  display:flex;
  flex-direction:column;
  align-items:center;
  justify-content:center;
  gap:2px;
  font-size:10px;
  color:#999;
  cursor:pointer;
  transition:color .2s;
}
.phone-nav-item .icon{font-size:20px}
.phone-nav-item.active{color:var(--accent-driver)}
.phone-nav-item.active.field-nav{color:var(--accent-field)}
.driver-theme{--accent:var(--accent-driver)}
.field-theme{--accent:var(--accent-field)}

.term-content.frame-view{
  display:flex !important;
  justify-content:center;
  padding:30px 0;
  background:#e5e5e5;
}
'''

# Insert before the closing </style>
style_end = content.rfind('</style>')
content = content[:style_end] + phone_frame_css + '\n' + content[style_end:]

# 2. Fix driver terminal HTML - wrap content in phone-frame
# Find term-driver div
d_start = content.find('<div id="term-driver"')
d_end = content.find('</div>\n\n<!-- ========== FIELD', d_start)

# Wrap the term-driver content in a phone-frame structure
driver_content = content[d_start:d_end + len('</div>')]
phone_driver = f'''
<div class="term-content frame-view" data-term="driver">
  <div class="phone-frame driver-theme">
    <div class="phone-screen">
      <div class="phone-topbar">
        <span class="back" onclick="showPage('driver','drv-home')">←</span>
        <span id="driver-title">驾驶员端</span>
      </div>
      <div class="phone-body">
        {driver_content}
      </div>
      <div class="phone-bottom-nav">
        <div class="phone-nav-item active" onclick="switchDriverNav('drv-home','首页')">
          <span class="icon">🏠</span><span>首页</span>
        </div>
        <div class="phone-nav-item" onclick="switchDriverNav('drv-report','事故报案')">
          <span class="icon">📋</span><span>报案</span>
        </div>
        <div class="phone-nav-item" onclick="switchDriverNav('drv-case','案件')">
          <span class="icon">📂</span><span>案件</span>
        </div>
        <div class="phone-nav-item" onclick="switchDriverNav('drv-score','评分')">
          <span class="icon">📊</span><span>评分</span>
        </div>
      </div>
    </div>
  </div>
</div>
'''

content = content[:d_start] + phone_driver + content[d_end + len('</div>'):]

# 3. Fix field terminal HTML - wrap content in phone-frame
f_start = content.find('<div id="term-field"')
f_end = content.find('</div>\n\n<!-- TOAST', f_start)

field_content = content[f_start:f_end + len('</div>')]
phone_field = f'''
<div class="term-content frame-view" data-term="field">
  <div class="phone-frame field-theme">
    <div class="phone-screen">
      <div class="phone-topbar">
        <span class="back" onclick="showPage('field','field-home')">←</span>
        <span id="field-title">现场端</span>
      </div>
      <div class="phone-body">
        {field_content}
      </div>
      <div class="phone-bottom-nav">
        <div class="phone-nav-item active field-nav" onclick="switchFieldNav('field-home','工作台')">
          <span class="icon">📋</span><span>工作台</span>
        </div>
        <div class="phone-nav-item field-nav" onclick="switchFieldNav('field-task','任务')">
          <span class="icon">📝</span><span>任务</span>
        </div>
        <div class="phone-nav-item field-nav" onclick="switchFieldNav('field-checkin','签到')">
          <span class="icon">✔️</span><span>签到</span>
        </div>
        <div class="phone-nav-item field-nav" onclick="switchFieldNav('field-eval','评估')">
          <span class="icon">💰</span><span>评估</span>
        </div>
      </div>
    </div>
  </div>
</div>
'''

content = content[:f_start] + phone_field + content[f_end + len('</div>'):]

# 4. Add navigation functions to JS
js_end = content.rfind('</script>')
js_functions = '''
function switchDriverNav(pageId, title) {
  document.querySelectorAll('#term-driver .phone-nav-item').forEach(n=>n.classList.remove('active'));
  event.currentTarget.classList.add('active');
  document.getElementById('driver-title').textContent = title;
  showPage('driver', pageId);
}
function switchFieldNav(pageId, title) {
  document.querySelectorAll('#term-field .phone-nav-item').forEach(n=>n.classList.remove('active'));
  event.currentTarget.classList.add('active');
  document.getElementById('field-title').textContent = title;
  showPage('field', pageId);
}
'''

# Also fix switchTerm to hide frame-view properly
old_switch = "document.getElementById(`term-${term}`).style.display = 'flex';"
new_switch = """var el = document.getElementById(`term-${term}`);
  if (el) {
    var isFrame = el.classList.contains('frame-view');
    el.style.display = isFrame ? 'flex' : 'flex';
    el.style.justifyContent = isFrame ? 'center' : '';
  }"""

content = content[:content.rfind(js_functions) + len(js_functions)]  # remove duplicate if any
content = content[:js_end] + js_functions + '\n' + content[js_end:]

with open(r'D:\workAIspace\openclaw\tscs-demo\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done! File fixed.')
print(f'Size: {len(content)} bytes')
