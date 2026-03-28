# -*- coding: utf-8 -*-
"""Generate clean TSCS demo HTML - using Python file write with UTF-8 encoding"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

HTML = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>TSCS 交通安全统筹系统 v2.0 - 多端交互演示</title>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700&display=swap" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<style>
:root{
--bg:#F0F2F5;--card:#fff;--text:#262626;--text2:#595959;--border:#d9d9d9;
--shadow:0 1px 3px rgba(0,0,0,.08);--shadow-lg:0 4px 16px rgba(0,0,0,.12);
--accent:#1677FF;--accent-e:#52C41A;--accent-d:#FA8C16;--accent-f:#722ED1;
--radius:8px;--radius-lg:12px;
}
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Noto Sans SC',sans-serif;background:var(--bg);color:var(--text);font-size:14px}

/* TOP NAV */
.top-nav{background:#fff;height:56px;display:flex;align-items:center;padding:0 24px;box-shadow:var(--shadow);position:fixed;top:0;left:0;right:0;z-index:100}
.top-nav .logo{font-weight:700;font-size:18px;color:#1a1a2e;margin-right:40px}
.top-nav .logo span{font-size:12px;color:var(--text2);font-weight:400}
.term-tabs{display:flex;gap:6px}
.term-tab{padding:6px 20px;border-radius:20px;cursor:pointer;font-size:13px;font-weight:500;border:2px solid transparent;color:var(--text2);font-family:inherit;background:transparent;transition:all .2s}
.term-tab:hover{opacity:.8}
.term-tab.active[data-t="platform"]{background:rgba(22,119,255,.1);color:var(--accent);border-color:var(--accent)}
.term-tab.active[data-t="enterprise"]{background:rgba(82,196,26,.1);color:var(--accent-e);border-color:var(--accent-e)}
.term-tab.active[data-t="driver"]{background:rgba(250,140,22,.1);color:var(--accent-d);border-color:var(--accent-d)}
.term-tab.active[data-t="field"]{background:rgba(114,46,209,.1);color:var(--accent-f);border-color:var(--accent-f)}

/* LAYOUT */
.layout{display:flex;margin-top:56px;min-height:calc(100vh - 56px)}
.sidebar{width:210px;background:#fff;border-right:1px solid var(--border);padding:16px 0;flex-shrink:0;position:fixed;top:56px;left:0;bottom:0;overflow-y:auto}
.sidebar-item{padding:9px 16px;cursor:pointer;font-size:12px;color:var(--text2);border-left:3px solid transparent;display:flex;align-items:center;gap:8px;white-space:nowrap;transition:all .15s}
.sidebar-item:hover{background:var(--bg);color:var(--text)}
.sidebar-item.active{color:var(--accent);border-left-color:var(--accent);background:rgba(22,119,255,.05);font-weight:500}
[data-t="enterprise"] .sidebar-item.active{color:var(--accent-e);border-left-color:var(--accent-e);background:rgba(82,196,26,.05)}
[data-t="driver"] .sidebar-item.active{color:var(--accent-d);border-left-color:var(--accent-d);background:rgba(250,140,22,.05)}
[data-t="field"] .sidebar-item.active{color:var(--accent-f);border-left-color:var(--accent-f);background:rgba(114,46,209,.05)}
.sidebar-hdr{padding:0 16px 12px;border-bottom:1px solid var(--border);margin-bottom:12px}
.sidebar-hdr .name{font-weight:700;font-size:13px}
.sidebar-hdr .sub{font-size:11px;color:var(--text2);margin-top:2px}
.main{flex:1;margin-left:210px;padding:20px;min-height:calc(100vh - 56px)}
.breadcrumb{font-size:12px;color:var(--text2);margin-bottom:14px}

/* CARD */
.card{background:var(--card);border-radius:var(--radius);box-shadow:var(--shadow);padding:20px;margin-bottom:16px}
.stat-card{background:var(--card);border-radius:var(--radius);box-shadow:var(--shadow);padding:16px;display:flex;flex-direction:column;gap:4px}
.stat-card .label{font-size:11px;color:var(--text2)}
.stat-card .value{font-size:26px;font-weight:700}
.stat-card .sub{font-size:10px;color:#52C41A}
.stat-card .sub.red{color:#ff4d4f}
.stat-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-bottom:18px}
.stat-grid-3{grid-template-columns:repeat(3,1fr)}
.section-title{font-size:15px;font-weight:700;margin-bottom:14px;display:flex;align-items:center;gap:8px}
.section-title::before{content:'';display:inline-block;width:3px;height:15px;background:var(--accent);border-radius:2px}
[data-t="enterprise"] .section-title::before{background:var(--accent-e)}
[data-t="driver"] .section-title::before{background:var(--accent-d)}
[data-t="field"] .section-title::before{background:var(--accent-f)}

/* TABLE */
.table-wrap{overflow-x:auto}
table{width:100%;border-collapse:collapse;font-size:12px}
th,td{padding:9px 10px;text-align:left;border-bottom:1px solid var(--border)}
th{background:#fafafa;font-weight:500;color:var(--text2);font-size:11px}
tr:hover{background:#fafafa}
.clickable-row{cursor:pointer}

/* BADGE */
.badge{display:inline-block;padding:2px 8px;border-radius:10px;font-size:10px;font-weight:500}
.badge-blue{background:rgba(22,119,255,.1);color:var(--accent)}
.badge-green{background:rgba(82,196,26,.1);color:var(--accent-e)}
.badge-orange{background:rgba(250,140,22,.1);color:var(--accent-d)}
.badge-purple{background:rgba(114,46,209,.1);color:var(--accent-f)}
.badge-red{background:rgba(255,77,79,.1);color:#ff4d4f}
.badge-yellow{background:rgba(250,140,22,.15);color:#d46b00}
.badge-gray{background:#f0f0f0;color:var(--text2)}

/* BUTTON */
.btn{display:inline-flex;align-items:center;gap:5px;padding:6px 14px;border-radius:5px;font-size:12px;font-weight:500;cursor:pointer;border:1px solid var(--border);background:#fff;color:var(--text);transition:all .15s;font-family:inherit}
.btn:hover{border-color:#40a9ff;color:#40a9ff}
.btn-primary{background:var(--accent);color:#fff;border-color:var(--accent)}
.btn-primary:hover{background:#4098ff}
.btn-e{background:var(--accent-e);color:#fff;border-color:var(--accent-e)}
.btn-e:hover{background:#73d13d}
.btn-d{background:var(--accent-d);color:#fff;border-color:var(--accent-d)}
.btn-d:hover{background:#fb9224}
.btn-f{background:var(--accent-f);color:#fff;border-color:var(--accent-f)}
.btn-f:hover{background:#9254de}
.btn-sm{padding:3px 9px;font-size:11px}
.toolbar{display:flex;align-items:center;gap:10px;margin-bottom:14px;flex-wrap:wrap}
.search-input{padding:6px 10px;border:1px solid var(--border);border-radius:5px;font-size:12px;outline:none;font-family:inherit;width:180px}
input.form-control,select.form-control,textarea.form-control{width:100%;padding:7px 10px;border:1px solid var(--border);border-radius:5px;font-size:12px;font-family:inherit;outline:none;background:#fff;transition:border-color .15s}
input.form-control:focus,select.form-control:focus{border-color:#40a9ff}
.form-group{margin-bottom:14px}
.form-label{display:block;font-size:12px;font-weight:500;margin-bottom:5px}
.form-row{display:grid;grid-template-columns:1fr 1fr;gap:14px}

/* TIMELINE */
.timeline{position:relative;padding-left:22px}
.timeline::before{content:'';position:absolute;left:7px;top:4px;bottom:4px;width:2px;background:var(--border)}
.timeline-item{position:relative;margin-bottom:18px}
.timeline-item::before{content:'';position:absolute;left:-19px;top:4px;width:9px;height:9px;border-radius:50%;background:var(--border);border:2px solid #fff}
.timeline-item.done::before{background:#52C41A}
.timeline-item.active::before{background:var(--accent);box-shadow:0 0 0 3px rgba(22,119,255,.2)}
.timeline-item.pending::before{background:var(--border)}
.timeline-time{font-size:10px;color:var(--text2);margin-bottom:1px}
.timeline-title{font-weight:500;font-size:12px}
.timeline-desc{font-size:11px;color:var(--text2);margin-top:1px}

/* PAGE */
.page{display:none;animation:fadeIn .25s ease}
.page.active{display:block}
@keyframes fadeIn{from{opacity:0;transform:translateX(8px)}to{opacity:1;transform:translateX(0)}}

/* MODAL */
.modal-overlay{position:fixed;top:0;left:0;right:0;bottom:0;background:rgba(0,0,0,.45);display:flex;align-items:center;justify-content:center;z-index:200;display:none}
.modal-overlay.show{display:flex}
.modal{background:#fff;border-radius:var(--radius-lg);padding:22px;width:540px;max-width:90vw;max-height:80vh;overflow-y:auto;box-shadow:var(--shadow-lg);animation:modalIn .2s ease}
.modal-lg{width:780px}
@keyframes modalIn{from{opacity:0;transform:scale(.95)}to{opacity:1;transform:scale(1)}}
.modal-header{font-size:15px;font-weight:700;margin-bottom:18px;display:flex;align-items:center;justify-content:space-between;padding-bottom:12px;border-bottom:1px solid var(--border)}
.modal-close{cursor:pointer;font-size:20px;color:var(--text2);line-height:1;background:none;border:none;font-family:inherit}
.modal-footer{margin-top:18px;display:flex;justify-content:flex-end;gap:10px;padding-top:12px;border-top:1px solid var(--border)}

/* TOAST */
.toast{position:fixed;top:76px;right:20px;background:#fff;border-radius:var(--radius);box-shadow:var(--shadow-lg);padding:11px 18px;z-index:300;display:none;font-size:12px;max-width:280px;border-left:3px solid #52C41A}
.toast.show{display:flex;align-items:center;gap:8px;animation:toastIn .3s ease}
.toast.error{border-left-color:#ff4d4f}
@keyframes toastIn{from{opacity:0;transform:translateX(20px)}to{opacity:1;transform:translateX(0)}}

/* HELPERS */
.flex{display:flex}.flex-wrap{flex-wrap:wrap}
.flex-between{display:flex;align-items:center;justify-content:space-between}
.gap-8{gap:8px}.gap-12{gap:12px}.gap-16{gap:16px}
.mb-8{margin-bottom:8px}.mb-12{margin-bottom:12px}.mb-16{margin-bottom:16px}.mb-20{margin-bottom:20px}
.mt-8{margin-top:8px}.mt-12{margin-top:12px}.mt-16{margin-top:16px}
.text-success{color:#52C41A}.text-error{color:#ff4d4f}.text-warning{color:#fa8c16}
.text-muted{color:var(--text2);font-size:11px}.text-right{text-align:right}.text-center{text-align:center}
.font-bold{font-weight:700}
.divider{height:1px;background:var(--border);margin:14px 0}
.empty-state{text-align:center;padding:40px 0;color:var(--text2)}
.pagination{display:flex;align-items:center;justify-content:flex-end;gap:3px;margin-top:14px}
.page-btn{width:30px;height:30px;display:flex;align-items:center;justify-content:center;border:1px solid var(--border);border-radius:5px;cursor:pointer;font-size:12px;background:#fff;font-family:inherit;transition:all .15s}
.page-btn.active{background:var(--accent);color:#fff;border-color:var(--accent)}
.page-btn:hover:not(.active){border-color:#40a9ff;color:#40a9ff}
.progress-bar{height:7px;background:#f0f0f0;border-radius:4px;overflow:hidden}
.info-grid{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.info-item{display:flex;flex-direction:column;gap:2px}
.info-label{font-size:11px;color:var(--text2)}
.info-value{font-size:13px;font-weight:500}
.info-value.money{font-size:18px;font-weight:700}
.info-value.money-lg{font-size:22px;font-weight:700;color:#52C41A}

/* FLOW CARDS */
.flow-card{display:flex;gap:12px;padding:12px;border:1px solid var(--border);border-radius:var(--radius);margin-bottom:10px;cursor:pointer;transition:all .15s}
.flow-card:hover{border-color:var(--accent);box-shadow:var(--shadow)}
.flow-card .fc-icon{width:40px;height:40px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:18px;flex-shrink:0}
.flow-card .fc-info{flex:1;min-width:0}
.flow-card .fc-title{font-weight:600;font-size:13px;margin-bottom:3px}
.flow-card .fc-desc{font-size:11px;color:var(--text2)}

/* APPROVAL FLOW */
.approval-flow{display:flex;align-items:center;margin:16px 0}
.approval-node{flex:1;text-align:center;padding:10px 6px;background:#fafafa;border-radius:8px}
.approval-node .an-label{font-size:11px;color:var(--text2);margin-bottom:4px}
.approval-node .an-value{font-size:14px;font-weight:700}
.approval-node .an-sub{font-size:10px;color:var(--text2)}
.approval-arrow{font-size:14px;color:var(--border);flex-shrink:0}

/* STEP */
.step-indicator{display:flex;align-items:center;margin-bottom:20px}
.step-dot{width:28px;height:28px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:600;flex-shrink:0}
.step-dot.done{background:#52C41A;color:#fff}
.step-dot.active{background:var(--accent);color:#fff}
.step-dot.pending{background:#d9d9d9;color:#fff}
.step-line{flex:1;height:2px;background:#d9d9d9}
.step-line.done{background:#52C41A}

/* CALC */
.calc-result{background:#fafafa;border-radius:var(--radius);padding:14px;margin-top:12px}
.calc-row{display:flex;justify-content:space-between;padding:4px 0;font-size:12px;color:var(--text2)}
.calc-row.total{font-size:14px;font-weight:700;color:var(--text);border-top:1px solid var(--border);margin-top:6px;padding-top:8px}
.calc-row.total .val{color:#52C41A;font-size:18px}
.chart-wrap{position:relative;height:200px}

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
.driver-phone .phone-body{background:#fff}
.field-phone .phone-body{background:#fff}

/* PHONE HEADER */
.phone-hdr{padding:10px 14px 8px;display:flex;align-items:center;gap:8px;border-bottom:1px solid #eee}
.phone-hdr .back{font-size:16px;cursor:pointer;width:24px}
.phone-hdr .title{font-size:13px;font-weight:600}
</style>
</head>
<body>
'''

# Now write HTML in chunks to avoid encoding issues
# Using python file write directly

with open(r'D:\workAIspace\openclaw\tscs-demo\index.html', 'w', encoding='utf-8') as f:
    f.write(HTML)

print(f'Header written: {len(HTML)}')

# Write nav
NAV = '''<!-- TOP NAV -->
<nav class="top-nav">
  <div class="logo">TSCS <span>v2.0 交互演示</span></div>
  <div class="term-tabs">
    <div class="term-tab active" data-t="platform" onclick="switchTerm('platform')">🏛 机构端</div>
    <div class="term-tab" data-t="enterprise" onclick="switchTerm('enterprise')">🏢 企业端</div>
    <div class="term-tab" data-t="driver" onclick="switchTerm('driver')">🚗 驾驶员端</div>
    <div class="term-tab" data-t="field" onclick="switchTerm('field')">📱 现场端</div>
  </div>
</nav>
'''
with open(r'D:\workAIspace\openclaw\tscs-demo\index.html', 'a', encoding='utf-8') as f:
    f.write(NAV)
print('Nav written')

print('Done - use JS to inject content')
print('Writing complete HTML now...')
