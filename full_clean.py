#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate complete clean TSCS demo HTML with proper UTF-8 Chinese"""
path = r'D:\workAIspace\openclaw\tscs-demo\index.html'

# We'll build the complete HTML as a Python string
# Using triple-quoted strings with actual Chinese
# (Python source files are UTF-8 by default on Windows)

S = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>TSCS v2.0 多端交互演示</title>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700&display=swap" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Noto Sans SC',sans-serif;background:#F0F2F5;font-size:14px;color:#262626}
:root{--bg:#F0F2F5;--c:#fff;--t:#262626;--t2:#595959;--b:#d9d9d9;--sh:0 1px 3px rgba(0,0,0,.08);--sh2:0 4px 16px rgba(0,0,0,.12);--a:#1677FF;--ae:#52C41A;--ad:#FA8C16;--af:#722ED1;--r:8px}
.top{background:#fff;height:56px;display:flex;align-items:center;padding:0 24px;box-shadow:var(--sh);position:fixed;top:0;left:0;right:0;z-index:100}
.logo{font-weight:700;font-size:18px;margin-right:40px}
.tabs{display:flex;gap:6px}
.tab{padding:6px 20px;border-radius:20px;cursor:pointer;font-size:13px;font-weight:500;border:2px solid transparent;transition:all .2s;background:transparent;color:#595959;font-family:inherit}
.tab:hover{opacity:.8}
.tp{background:rgba(22,119,255,.1);color:var(--a);border-color:var(--a)}
.te{background:rgba(82,196,26,.1);color:var(--ae);border-color:var(--ae)}
.td{background:rgba(250,140,22,.1);color:var(--ad);border-color:var(--ad)}
.tf{background:rgba(114,46,209,.1);color:var(--af);border-color:var(--af)}
.lay{display:flex;margin-top:56px;min-height:calc(100vh - 56px)}
.side{width:210px;background:#fff;border-right:1px solid var(--b);position:fixed;top:56px;left:0;bottom:0;overflow-y:auto;padding:16px 0}
.si{padding:9px 16px;cursor:pointer;font-size:12px;color:var(--t2);border-left:3px solid transparent;display:flex;align-items:center;gap:8px;white-space:nowrap;transition:all .15s}
.si:hover{background:var(--bg)}
.sa{color:var(--a);border-left-color:var(--a);background:rgba(22,119,255,.05);font-weight:500}
.ea{color:var(--ae);border-left-color:var(--ae);background:rgba(82,196,26,.05)}
.da{color:var(--ad);border-left-color:var(--ad);background:rgba(250,140,22,.05)}
.fa{color:var(--af);border-left-color:var(--af);background:rgba(114,46,209,.05)}
.sh{padding:0 16px 12px;border-bottom:1px solid var(--b);margin-bottom:12px}
.sn{font-weight:700;font-size:13px}
.ss{font-size:11px;color:var(--t2);margin-top:2px}
.main{flex:1;margin-left:210px;padding:20px;min-height:calc(100vh - 56px)}
.c{background:var(--c);border-radius:var(--r);box-shadow:var(--sh);padding:20px;margin-bottom:16px}
.sc{background:var(--c);border-radius:var(--r);box-shadow:var(--sh);padding:16px;display:flex;flex-direction:column;gap:4px}
.sl{font-size:11px;color:var(--t2)}
.sv{font-size:26px;font-weight:700}
.ss2{font-size:10px;color:#52C41A}
.ss2.red{color:#ff4d4f}
.sg{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-bottom:18px}
.sg2{grid-template-columns:repeat(2,1fr)}
.sg3{grid-template-columns:repeat(3,1fr)}
.st{font-size:15px;font-weight:700;margin-bottom:14px;display:flex;align-items:center;gap:8px}
.st::before{content:'';display:inline-block;width:3px;height:15px;background:var(--a);border-radius:2px}
.ese::before{background:var(--ae)}
.eds::before{background:var(--ad)}
.efs::before{background:var(--af)}
.tw{overflow-x:auto}
table{width:100%;border-collapse:collapse;font-size:12px}
th,td{padding:9px 10px;text-align:left;border-bottom:1px solid var(--b)}
th{background:#fafafa;font-weight:500;color:var(--t2);font-size:11px}
tr:hover{background:#fafafa}
.cr{cursor:pointer}
.bdg{display:inline-block;padding:2px 8px;border-radius:10px;font-size:10px;font-weight:500}
.ba{background:rgba(22,119,255,.1);color:var(--a)}
.be{background:rgba(82,196,26,.1);color:var(--ae)}
.bd{background:rgba(250,140,22,.1);color:var(--ad)}
.bf{background:rgba(114,46,209,.1);color:var(--af)}
.br{background:rgba(255,77,79,.1);color:#ff4d4f}
.by{background:rgba(250,140,22,.15);color:#d46b00}
.bk{background:#f0f0f0;color:var(--t2)}
.btn{display:inline-flex;align-items:center;gap:5px;padding:6px 14px;border-radius:5px;font-size:12px;font-weight:500;cursor:pointer;border:1px solid var(--b);background:#fff;color:var(--t);transition:all .15s;font-family:inherit}
.btn:hover{border-color:#40a9ff;color:#40a9ff}
.bp{background:var(--a);color:#fff;border-color:var(--a)}
.bp:hover{background:#4098ff}
.bn{background:var(--ae);color:#fff;border-color:var(--ae)}
.bn:hover{background:#73d13d}
.bdr{background:var(--ad);color:#fff;border-color:var(--ad)}
.bf2{background:var(--af);color:#fff;border-color:var(--af)}
.bsm{padding:3px 9px;font-size:11px}
.tb{display:flex;align-items:center;gap:10px;margin-bottom:14px;flex-wrap:wrap}
.in{padding:6px 10px;border:1px solid var(--b);border-radius:5px;font-size:12px;outline:none;font-family:inherit;width:180px;background:#fff}
.in:focus{border-color:#40a9ff}
select.in,textarea.in{width:100%;padding:7px 10px;border:1px solid var(--b);border-radius:5px;font-size:12px;font-family:inherit;outline:none;background:#fff;transition:border-color .15s}
select.in:focus,textarea.in:focus{border-color:#40a9ff}
.fg{margin-bottom:14px}
.fl{display:block;font-size:12px;font-weight:500;margin-bottom:5px}
.fr{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.tl{position:relative;padding-left:22px}
.tl::before{content:'';position:absolute;left:7px;top:4px;bottom:4px;width:2px;background:var(--b)}
.ti{position:relative;margin-bottom:18px}
.ti::before{content:'';position:absolute;left:-19px;top:4px;width:9px;height:9px;border-radius:50%;background:var(--b);border:2px solid #fff}
.td2::before{background:#52C41A}
.ta::before{background:var(--a);box-shadow:0 0 0 3px rgba(22,119,255,.2)}
.tp2::before{background:var(--b)}
.tt{font-size:10px;color:var(--t2);margin-bottom:1px}
.ti .tl2{font-weight:500;font-size:12px}
.td3{font-size:11px;color:var(--t2);margin-top:1px}
.pg{display:none;animation:fade .25s ease}
.pg.on{display:block}
@keyframes fade{from{opacity:0;transform:translateX(8px)}to{opacity:1;transform:translateX(0)}}
.mo{position:fixed;top:0;left:0;right:0;bottom:0;background:rgba(0,0,0,.45);display:flex;align-items:center;justify-content:center;z-index:200;display:none}
.mo.s{display:flex}
.mb{background:#fff;border-radius:12px;padding:22px;width:540px;max-width:90vw;max-height:80vh;overflow-y:auto;box-shadow:var(--sh2);animation:mb .2s ease}
.mb.lg{width:780px}
@keyframes mb{from{opacity:0;transform:scale(.95)}to{opacity:1;transform:scale(1)}}
.mh{font-size:15px;font-weight:700;margin-bottom:18px;display:flex;align-items:center;justify-content:space-between;padding-bottom:12px;border-bottom:1px solid var(--b)}
.mx{cursor:pointer;font-size:20px;color:var(--t2);background:none;border:none;font-family:inherit}
.mf{margin-top:18px;display:flex;justify-content:flex-end;gap:10px;padding-top:12px;border-top:1px solid var(--b)}
.toast{position:fixed;top:76px;right:20px;background:#fff;border-radius:var(--r);box-shadow:var(--sh2);padding:11px 18px;z-index:300;display:none;font-size:12px;max-width:280px;border-left:3px solid #52C41A}
.toast.s{display:flex;align-items:center;gap:8px;animation:ts .3s ease}
.toast.e{border-left-color:#ff4d4f}
@keyframes ts{from{opacity:0;transform:translateX(20px)}to{opacity:1;transform:translateX(0)}}
.fx{display:flex}.fxw{flex-wrap:wrap}.fxb{display:flex;align-items:center;justify-content:space-between}
.g8{gap:8px}.g12{gap:12px}.g16{gap:16px}
.mb8{margin-bottom:8px}.mb12{margin-bottom:12px}.mb16{margin-bottom:16px}.mb20{margin-bottom:20px}
.mt8{margin-top:8px}.mt12{margin-top:12px}.mt16{margin-top:16px}
.ts3{color:#52C41A}.te2{color:#ff4d4f}.tw3{color:#fa8c16}
.tm2{color:var(--t2);font-size:11px}.tr2{text-align:right}.tc2{text-align:center}
.fb2{font-weight:700}
.dv{height:1px;background:var(--b);margin:14px 0}
.es{text-align:center;padding:40px 0;color:var(--t2)}
.pgn{display:flex;align-items:center;justify-content:flex-end;gap:3px;margin-top:14px}
.pb{width:30px;height:30px;display:flex;align-items:center;justify-content:center;border:1px solid var(--b);border-radius:5px;cursor:pointer;font-size:12px;background:#fff;font-family:inherit;transition:all .15s}
.pb.on{background:var(--a);color:#fff;border-color:var(--a)}
.pb:hover:not(.on){border-color:#40a9ff;color:#40a9ff}
.pb2{height:7px;background:#f0f0f0;border-radius:4px;overflow:hidden}
.ig{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.ii{display:flex;flex-direction:column;gap:2px}
.il2{font-size:11px;color:var(--t2)}
.iv{font-size:13px;font-weight:500}
.iv.m{font-size:18px;font-weight:700}
.iv.l{font-size:22px;font-weight:700;color:#52C41A}
.fc{display:flex;gap:12px;padding:12px;border:1px solid var(--b);border-radius:var(--r);margin-bottom:10px;cursor:pointer;transition:all .15s}
.fc:hover{border-color:var(--a);box-shadow:var(--sh)}
.fc .fci{width:40px;height:40px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:18px;flex-shrink:0}
.fc .fcn{flex:1;min-width:0}
.fc .fct{font-weight:600;font-size:13px;margin-bottom:3px}
.fc .fcd{font-size:11px;color:var(--t2)}
.ap{display:flex;align-items:center;margin:16px 0}
.an{flex:1;text-align:center;padding:10px 6px;background:#fafafa;border-radius:8px}
.an .al{font-size:11px;color:var(--t2);margin-bottom:4px}
.an .av{font-size:14px;font-weight:700}
.an .as2{font-size:10px;color:var(--t2)}
.aa{font-size:14px;color:var(--b);flex-shrink:0}
.si3{display:flex;align-items:center;margin-bottom:20px}
.sd{width:28px;height:28px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:600;flex-shrink:0}
.sd.d{background:#52C41A;color:#fff}
.sd.a{background:var(--a);color:#fff}
.sd.p{background:#d9d9d9;color:#fff}
.sl2{flex:1;height:2px;background:#d9d9d9}
.sl2.d{background:#52C41A}
.cr3{background:#fafafa;border-radius:var(--r);padding:14px;margin-top:12px}
.cr4{display:flex;justify-content:space-between;padding:4px 0;font-size:12px;color:var(--t2)}
.cr4.t{font-size:14px;font-weight:700;color:var(--t);border-top:1px solid var(--b);margin-top:6px;padding-top:8px}
.cr4.t .v{color:#52C41A;font-size:18px}
.cwrap{position:relative;height:200px}
.pw{display:flex;justify-content:center;align-items:flex-start;padding:32px 20px;background:#d8d8d8;min-height:calc(100vh - 56px)}
.pf{width:390px;background:#fff;border-radius:36px;box-shadow:0 8px 40px rgba(0,0,0,.22),0 0 0 11px #1a1a1a;overflow:hidden;position:relative}
.pn{height:34px;background:#1a1a1a;display:flex;align-items:flex-end;justify-content:center;padding-bottom:6px}
.pn::after{content:'';width:90px;height:16px;background:#111;border-radius:0 0 10px 10px}
.pb3{height:calc(100vh - 90px);overflow-y:auto;background:#fff}
.pbb{position:absolute;bottom:0;left:0;right:0;height:58px;background:#fff;border-top:1px solid #eee;display:flex}
.pt{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2px;font-size:10px;color:#999;cursor:pointer;transition:color .15s}
.pt .ic{font-size:20px}
.dp .pt.on{color:#FA8C16}
.fp .pt.on{color:#722ED1}
.dp .pbb{background:#fffaf5}
.fp .pbb{background:#f5f0ff}
.ph{padding:10px 14px 8px;display:flex;align-items:center;gap:8px}
.ph .bk{font-size:16px;cursor:pointer;width:24px}
.ph .ttl{font-size:13px;font-weight:600}
</style>
</head>
<body>
<nav class="top">
  <div class="logo">TSCS <span style="font-size:12px;color:#595959;font-weight:400">v2.0 多端交互演示</span></div>
  <div class="tabs">
    <div class="tab tp" id="tab-p" onclick="st('p')">🏛 机构端</div>
    <div class="tab" id="tab-e" onclick="st('e')">🏢 企业端</div>
    <div class="tab" id="tab-d" onclick="st('d')">🚗 驾驶员端</div>
    <div class="tab" id="tab-f" onclick="st('f')">📱 现场端</div>
  </div>
</nav>
'''

# Write Part 1
with open(path, 'w', encoding='utf-8') as f:
    f.write(S)
print(f'Part 1 written: {len(S)} chars')

# Now append platform content
S2 = '''
<div id="t-p" class="lay">
<div class="side">
<div class="sh"><div class="sn">机构端</div><div class="ss">TSCS平台运营管理系统</div></div>
<div class="si sa" id="si-ph" onclick="sp('p','ph')">📊 数据面板</div>
<div class="si" id="si-pe" onclick="sp('p','pe')">🏢 企业管理</div>
<div class="si" id="si-pi" onclick="sp('p','pi')">📋 参统管理</div>
<div class="si" id="si-pc" onclick="sp('p','pc')">⚠ 事故报案</div>
<div class="si" id="si-pcd" onclick="sp('p','pcd')">🔍 案件详情</div>
<div class="si" id="si-pp" onclick="sp('p','pp')">💰 互助给付</div>
<div class="si" id="si-pf" onclick="sp('p','pf')">📈 财务报表</div>
<div class="si" id="si-pr" onclick="sp('p','pr')">🛡 风控评级</div>
<div class="si" id="si-pu" onclick="sp('p','pu')">👥 用户管理</div>
</div>
<div class="main">
'''

# Platform Home
S2 += '''
<div id="ph" class="pg on">
<div class="st">全局数据面板</div>
<div class="sg">
<div class="sc"><div class="sl">入驻企业总数</div><div class="sv" style="color:var(--a)">18</div><div class="ss2">本月+2</div></div>
<div class="sc"><div class="sl">在统车辆总数</div><div class="sv">28,634</div><div class="ss2">活跃凭证</div></div>
<div class="sc"><div class="sl">本月新增案件</div><div class="sv" style="color:#ff4d4f">127</div><div class="ss2 red">较上月+12</div></div>
<div class="sc"><div class="sl">本月给付金额</div><div class="sv" style="color:#ff4d4f">¥3,842,600</div><div class="ss2 red">较上月+8%</div></div>
</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px">
<div class="c"><div class="st">各企业关键指标对比</div><canvas id="ccomp" height="120"></canvas></div>
<div class="c"><div class="st">月度给付趋势（万元）</div><canvas id="ctrend" height="120"></canvas></div>
</div>
<div class="c mt16">
<div class="st">⚠ 风险预警</div>
<table><thead><tr><th>预警类型</th><th>企业</th><th>详情</th><th>处理</th></tr></thead>
<tbody>
<tr><td><span class="bdg br">高给付率</span></td><td>华通客运</td><td>近12月给付率91%，超过80%红线</td><td><button class="btn bsm bp" onclick="sp('p','pr')">查看</button></td></tr>
<tr><td><span class="bdg by">资金池不足</span></td><td>鹏程运输</td><td>互助资金池余额¥128万，低于预警线</td><td><button class="btn bsm bp">处理</button></td></tr>
<tr><td><span class="bdg bf">评分过低</span></td><td>星辰物流</td><td>企业驾驶评分均值62分，已连续3月低于70分</td><td><button class="btn bsm bp">查看</button></td></tr>
</tbody></table>
</div>
</div>
'''

# Platform Enterprise List
S2 += '''
<div id="pe" class="pg">
<div class="st">企业管理</div>
<div class="tb">
<input class="in" placeholder="搜索企业名称...">
<select class="in" style="width:140px"><option>全部状态</option><option>正常</option><option>待审核</option></select>
<button class="btn bp">+ 新增企业</button>
</div>
<div class="c">
<table><thead><tr><th>企业名称</th><th>行业</th><th>车辆规模</th><th>入驻时间</th><th>状态</th><th>操作</th></tr></thead>
<tbody>
<tr class="cr" onclick="sp('p','ped')"><td><b>鹏程运输</b></td><td>公路客运</td><td>3,200辆</td><td>2025-03-15</td><td><span class="bdg be">正常</span></td><td><button class="btn bsm">详情</button></td></tr>
<tr><td>星辰物流</td><td>货运</td><td>1,850辆</td><td>2025-05-20</td><td><span class="bdg be">正常</span></td><td><button class="btn bsm">详情</button></td></tr>
<tr><td>华通客运</td><td>旅游客运</td><td>2,100辆</td><td>2025-01-10</td><td><span class="bdg br">高风险</span></td><td><button class="btn bsm">详情</button></td></tr>
<tr><td>顺捷租赁</td><td>租赁</td><td>960辆</td><td>2025-08-01</td><td><span class="bdg be">正常</span></td><td><button class="btn bsm">详情</button></td></tr>
<tr><td>鑫安出租</td><td>出租客运</td><td>420辆</td><td>2025-11-15</td><td><span class="bdg be">正常</span></td><td><button class="btn bsm">详情</button></td></tr>
</tbody></table>
</div>
</div>
'''

# Platform Enterprise Detail
S2 += '''
<div id="ped" class="pg">
<div class="st">企业详情 - 鹏程运输</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px">
<div class="c">
<div class="st">基本信息</div>
<div class="ig">
<div class="ii"><div class="il2">企业名称</div><div class="iv">鹏程运输有限公司</div></div>
<div class="ii"><div class="il2">统一社会信用代码</div><div class="iv">91110105MA0xxxxxx</div></div>
<div class="ii"><div class="il2">行业类型</div><div class="iv">公路客运</div></div>
<div class="ii"><div class="il2">法人代表</div><div class="iv">李明</div></div>
<div class="ii"><div class="il2">联系方式</div><div class="iv">138-0013-8000</div></div>
</div>
</div>
<div class="c">
<div class="st">运营概况</div>
<div class="sg3">
<div class="sc"><div class="sl">在统车辆</div><div class="sv" style="color:var(--a)">3,200</div></div>
<div class="sc"><div class="sl">绑定驾驶员</div><div class="sv">3,410</div></div>
<div class="sc"><div class="sl">驾驶评分均值</div><div class="sv">78.5</div><div class="ss2">B级中低风险</div></div>
<div class="sc"><div class="sl">本月给付率</div><div class="sv">34.2%</div><div class="ss2 ts3">低于40%</div></div>
</div>
</div>
</div>
<div class="c mt16">
<div class="st">统筹单列表（最近3条）</div>
<table><thead><tr><th>凭证号</th><th>车牌</th><th>方案</th><th>生效日期</th><th>到期日期</th><th>状态</th></tr></thead>
<tbody>
<tr><td>PC-2026-001</td><td>京A·88888</td><td>标准方案</td><td>2026-01-01</td><td>2026-12-31</td><td><span class="bdg be">生效中</span></td></tr>
<tr><td>PC-2026-002</td><td>京B·12345</td><td>基础方案</td><td>2026-01-01</td><td>2026-12-31</td><td><span class="bdg be">生效中</span></td></tr>
<tr><td>PC-2026-003</td><td>京C·66789</td><td>全面方案</td><td>2026-01-01</td><td>2026-12-31</td><td><span class="bdg be">生效中</span></td></tr>
</tbody></table>
</div>
</div>
'''

# Insurance List + Case List + Case Detail + Payment
S2 += '''
<div id="pi" class="pg"><div class="st">参统记录</div><div class="tb"><input class="in" placeholder="搜索企业名称..."><select class="in" style="width:140px"><option>全部状态</option><option>生效中</option><option>已到期</option></select></div><div class="c"><table><thead><tr><th>企业名称</th><th>车辆数</th><th>统筹费合计</th><th>协议时间</th><th>状态</th><th>操作</th></tr></thead><tbody><tr><td>鹏程运输</td><td>3,200辆</td><td>¥12,800,000</td><td>2026-01-01~2026-12-31</td><td><span class="bdg be">生效中</span></td><td><button class="btn bsm">统筹单</button></td></tr><tr><td>星辰物流</td><td>1,850辆</td><td>¥6,650,000</td><td>2026-01-01~2026-12-31</td><td><span class="bdg be">生效中</span></td><td><button class="btn bsm">统筹单</button></td></tr></tbody></table></div></div>

<div id="pc" class="pg"><div class="st">事故报案受理</div><div class="tb"><input class="in" placeholder="搜索报案号/车牌..."><select class="in" style="width:130px"><option>全部通道</option><option>快速通道</option><option>标准通道</option><option>大案通道</option></select><select class="in" style="width:120px"><option>全部状态</option><option>待分配</option><option>处理中</option></select></div><div class="c"><table><thead><tr><th>报案号</th><th>时间</th><th>企业</th><th>车牌</th><th>通道</th><th>预估金额</th><th>状态</th><th>操作</th></tr></thead><tbody><tr class="cr" onclick="sp('p','pcd')"><td><b>TSCS-2026-0328-0088</b></td><td>2026-03-28 09:15</td><td>鹏程运输</td><td>京A·88888</td><td><span class="bdg ba">标准通道</span></td><td>¥15,800</td><td><span class="bdg by">核查中</span></td><td><button class="btn bsm bp">查看</button></td></tr><tr><td>TSCS-2026-0327-0087</td><td>2026-03-27 16:42</td><td>星辰物流</td><td>京B·66666</td><td><span class="bdg be">快速通道</span></td><td>¥1,800</td><td><span class="bdg bf">待分配</span></td><td><button class="btn bsm bp">分配</button></td></tr><tr><td>TSCS-2026-0326-0086</td><td>2026-03-26 11:30</td><td>华通客运</td><td>京C·11222</td><td><span class="bdg br">大案通道</span></td><td>¥186,000</td><td><span class="bdg by">材料审核</span></td><td><button class="btn bsm bp">查看</button></td></tr></tbody></table></div></div>

<div id="pcd" class="pg"><div class="st">案件详情 - TSCS-2026-0328-0088</div><div style="display:grid;grid-template-columns:1fr 1fr;gap:16px"><div class="c"><div class="st">报案信息</div><div class="ig"><div class="ii"><div class="il2">报案号</div><div class="iv">TSCS-2026-0328-0088</div></div><div class="ii"><div class="il2">企业</div><div class="iv">鹏程运输</div></div><div class="ii"><div class="il2">车牌</div><div class="iv">京A·88888</div></div><div class="ii"><div class="il2">责任划分</div><div class="iv"><span class="bdg by">主责 70%</span></div></div></div></div><div class="c"><div class="st">案件处理进度</div><div class="tl"><div class="ti td2"><div class="tt">2026-03-28 09:15</div><div class="tl2">驾驶员一键报案</div><div class="td3">驾驶员张三提交报案</div></div><div class="ti td2"><div class="tt">2026-03-28 10:02</div><div class="tl2">企业最终报案</div><div class="td3">分司安全员审核通过</div></div><div class="ti td2"><div class="tt">2026-03-28 10:30</div><div class="tl2">案件受理</div><div class="td3">调度员李娜分配至核损员赵强</div></div><div class="ti ta"><div class="tt">2026-03-28 11:15</div><div class="tl2">现场核查中</div><div class="td3">核损员已到达现场，正在取证</div></div><div class="ti tp2"><div class="tt">—</div><div class="tl2">损失评估</div><div class="td3">等待核损员提交评估单</div></div><div class="ti tp2"><div class="tt">—</div><div class="tl2">互助给付</div><div class="td3">等待材料审核与理算</div></div></div></div></div><div class="c mt16"><div class="st">核查任务分配</div><div style="display:flex;align-items:center;gap:16px"><div><div style="font-size:12px;color:var(--t2);margin-bottom:4px">当前核损员</div><div style="font-weight:600">赵强 <span class="bdg ba">现场核查中</span></div></div><div><div style="font-size:12px;color:var(--t2);margin-bottom:4px">当前状态</div><div style="font-weight:600">已到达 · 11:15签到</div></div><div><div style="font-size:12px;color:var(--t2);margin-bottom:4px">已拍照</div><div style="font-weight:600">8/20 张</div></div><button class="btn bp" style="margin-left:auto" onclick="sp('p','pp')">查看互助给付</button></div></div></div>
'''

# Payment
S2 += '''
<div id="pp" class="pg"><div class="st">互助给付 - TSCS-2026-0328-0088</div><div class="sg3 mb16"><div class="sc"><div class="sl">案件总数</div><div class="sv">127</div><div class="ss2">本月新增</div></div><div class="sc"><div class="sl">待审核</div><div class="sv" style="color:#fa8c16">23</div><div class="ss2">材料待审</div></div><div class="sc"><div class="sl">本月给付总额</div><div class="sv">¥3,842,600</div><div class="ss2">已支付</div></div></div><div class="c"><div class="st">互助理算</div><div class="ig mb16"><div class="ii"><div class="il2">损失额（取发票与评估较低者）</div><div class="iv m">¥15,800</div></div><div class="ii"><div class="il2">责任比例</div><div class="iv">主责 × 70%</div></div><div class="ii"><div class="il2">免给付额</div><div class="iv">¥500</div></div><div class="ii"><div class="il2">协议扣除比例</div><div class="iv">0%</div></div></div><div class="cr3"><div class="cr4"><span>损失额 × 责任比例</span><span>¥15,800 × 70% = ¥11,060</span></div><div class="cr4"><span>− 免给付额</span><span>¥11,060 − ¥500 = ¥10,560</span></div><div class="cr4"><span>× (1 − 协议扣除)</span><span>¥10,560 × 1.0 = ¥10,560</span></div><div class="cr4 t"><span>互助给付款</span><span class="v">¥10,560</span></div></div><div class="mt16"><div class="st" style="margin-bottom:12px">分级审批</div><div class="ap"><div class="an" style="background:rgba(82,196,26,.1)"><div class="al">互助给付员</div><div class="av ts3">✓ 审核通过</div></div><div class="aa">→</div><div class="an" style="background:rgba(22,119,255,.1)"><div class="al">企业确认</div><div class="av" style="color:var(--a)">待确认</div><div class="as2">≤2万自动通过</div></div><div class="aa">→</div><div class="an"><div class="al">最终审批</div><div class="av">自动通过</div><div class="as2">≤2万</div></div><div class="aa">→</div><div class="an"><div class="al">支付执行</div><div class="av">待执行</div></div></div></div><div class="fx g8 mt16"><button class="btn bn" onclick="toast('给付成功，已通知企业')">确认给付 ¥10,560</button><button class="btn" onclick="sp('p','pf')">查看支付记录</button></div></div>
'''

# Finance
S2 += '''
<div id="pf" class="pg"><div class="st">财务报表 - 三账户模型</div><div class="sg"><div class="sc" style="border-left:4px solid #1677FF"><div class="sl">互助互济资金池（70%）</div><div class="sv" style="color:#1677FF">¥28,640,000</div><div class="ss2">本月收入 ¥12,800,000 · 支出 ¥3,842,600</div></div><div class="sc" style="border-left:4px solid #fa8c16"><div class="sl">风险储备金（15%）</div><div class="sv" style="color:#fa8c16">¥6,140,000</div><div class="ss2">上月结转</div></div><div class="sc" style="border-left:4px solid #52C41A"><div class="sl">平台运营管理费（15%）</div><div class="sv" style="color:#52C41A">¥6,140,000</div><div class="ss2">本月收入 ¥2,742,857</div></div></div><div class="c"><div class="st">各企业三账户明细</div><table><thead><tr><th>企业</th><th>本月缴纳</th><th>资金池70%</th><th>储备金15%</th><th>运营费15%</th><th>给付支出</th><th>池余额</th></tr></thead><tbody><tr><td>鹏程运输</td><td>¥12,800,000</td><td>¥8,960,000</td><td>¥1,920,000</td><td>¥1,920,000</td><td>¥1,280,000</td><td><span class="ts3">¥7,680,000</span></td></tr><tr><td>星辰物流</td><td>¥6,650,000</td><td>¥4,655,000</td><td>¥997,500</td><td>¥997,500</td><td>¥680,000</td><td><span class="ts3">¥3,975,000</span></td></tr><tr><td>华通客运</td><td>¥8,400,000</td><td>¥5,880,000</td><td>¥1,260,000</td><td>¥1,260,000</td><td>¥2,480,000</td><td><span class="te2">¥3,400,000</span></td></tr></tbody></table></div></div>
'''

# Risk
S2 += '''
<div id="pr" class="pg"><div class="st">企业风控评级</div><div class="c"><table><thead><tr><th>企业</th><th>评级</th><th>给付率</th><th>评分均值</th><th>续约年限</th><th>挂靠比例</th><th>风险措施</th></tr></thead><tbody><tr><td>鹏程运输</td><td><span class="bdg be">A级</span></td><td>34.2%</td><td>78.5</td><td>2年</td><td>15%</td><td>优先续约·费率优惠10%</td></tr><tr><td>星辰物流</td><td><span class="bdg be">B级</span></td><td>52%</td><td>71</td><td>1年</td><td>32%</td><td>正常续约·标准费率</td></tr><tr><td>华通客运</td><td><span class="bdg br">D级</span></td><td>91%</td><td>58</td><td>3年</td><td>62%</td><td>暂停新增参统·约谈整改</td></tr><tr><td>顺捷租赁</td><td><span class="bdg by">C级</span></td><td>67%</td><td>65</td><td>1年</td><td>45%</td><td>续约审核加严·费率上浮</td></tr></tbody></table></div><div class="c mt16"><div class="st">企业风控雷达图</div><canvas id="crisk" height="180"></canvas></div></div>
'''

# Users
S2 += '''
<div id="pu" class="pg"><div class="st">用户管理</div><div class="tb"><input class="in" placeholder="搜索姓名/账号..."><select class="in" style="width:140px"><option>全部角色</option><option>调度员</option><option>互助给付员</option><option>财务</option><option>运营</option></select><button class="btn bp">+ 新增用户</button></div><div class="c"><table><thead><tr><th>姓名</th><th>账号</th><th>角色</th><th>企业</th><th>最后登录</th><th>状态</th><th>操作</th></tr></thead><tbody><tr><td>李娜</td><td>linana</td><td><span class="bdg ba">调度员</span></td><td>平台</td><td>2026-03-28 09:00</td><td><span class="bdg be">正常</span></td><td><button class="btn bsm">编辑</button></td></tr><tr><td>赵强</td><td>zhaoqiang</td><td><span class="bdg bf">核损员</span></td><td>平台</td><td>2026-03-28 11:20</td><td><span class="bdg be">正常</span></td><td><button class="btn bsm">编辑</button></td></tr><tr><td>王芳</td><td>wangfang</td><td><span class="bdg bd">互助给付员</span></td><td>平台</td><td>2026-03-28 08:45</td><td><span class="bdg be">正常</span></td><td><button class="btn bsm">编辑</button></td></tr><tr><td>陈伟</td><td>chenwei</td><td><span class="bdg be">财务</span></td><td>平台</td><td>2026-03-28 10:30</td><td><span class="bdg be">正常</span></td><td><button class="btn bsm">编辑</button></td></tr></tbody></table></div></div>
'''

with open(path, 'a', encoding='utf-8') as f:
    f.write(S2)
print(f'Platform done: {len(S2)} chars')
