html = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>TSCS v2.0 多端交互演示</title>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700&display=swap" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:"Noto Sans SC",sans-serif;background:#F0F2F5;font-size:14px;color:#262626}
:root{--a:#1677FF;--ae:#52C41A;--ad:#FA8C16;--af:#722ED1;--r:8px;--b:#d9d9d9;--t:#262626;--t2:#595959;--bg:#F0F2F5;--c:#fff;--sh:0 1px 3px rgba(0,0,0,.08);--sh2:0 4px 16px rgba(0,0,0,.12)}
.nav{background:#fff;height:56px;display:flex;align-items:center;padding:0 24px;box-shadow:var(--sh);position:fixed;top:0;left:0;right:0;z-index:100}
.nav .logo{font-size:18px;font-weight:700;margin-right:40px}
.nav .logo span{font-size:12px;color:var(--t2);font-weight:400}
.tabs{display:flex;gap:6px}
.tab{padding:6px 20px;border-radius:20px;cursor:pointer;font-size:13px;font-weight:500;border:2px solid transparent;color:var(--t2);background:transparent;font-family:inherit;transition:all .2s}
.tab:hover{opacity:.8}
.tab.tp{background:rgba(22,119,255,.1);color:var(--a);border-color:var(--a)}
.tab.te{background:rgba(82,196,26,.1);color:var(--ae);border-color:var(--ae)}
.tab.td{background:rgba(250,140,22,.1);color:var(--ad);border-color:var(--ad)}
.tab.tf{background:rgba(114,46,209,.1);color:var(--af);border-color:var(--af)}
.lay{display:flex;margin-top:56px;min-height:calc(100vh - 56px)}
.side{width:215px;background:var(--c);border-right:1px solid var(--b);padding:16px 0;position:fixed;top:56px;left:0;bottom:0;overflow-y:auto}
.side .sht{padding:0 16px 12px;border-bottom:1px solid var(--b);margin-bottom:12px}
.side .sht .sn{font-weight:700;font-size:13px}
.side .sht .ss{font-size:11px;color:var(--t2);margin-top:2px}
.side .si{padding:9px 16px;font-size:12px;color:var(--t2);cursor:pointer;border-left:3px solid transparent;display:flex;align-items:center;gap:8px;white-space:nowrap;transition:all .15s}
.side .si:hover{background:var(--bg);color:var(--t)}
.side .si.sa{color:var(--a);border-left-color:var(--a);background:rgba(22,119,255,.05);font-weight:500}
.side .si.se{color:var(--ae);border-left-color:var(--ae);background:rgba(82,196,26,.05)}
.side .si.sd{color:var(--ad);border-left-color:var(--ad);background:rgba(250,140,22,.05)}
.side .si.sf{color:var(--af);border-left-color:var(--af);background:rgba(114,46,209,.05)}
.main{flex:1;margin-left:215px;padding:20px;min-height:calc(100vh - 56px)}
.card{background:var(--c);border-radius:var(--r);box-shadow:var(--sh);padding:20px;margin-bottom:16px}
.stat{background:var(--c);border-radius:var(--r);box-shadow:var(--sh);padding:16px;display:flex;flex-direction:column;gap:4px}
.stat .lbl{font-size:11px;color:var(--t2)}
.stat .val{font-size:26px;font-weight:700}
.stat .sub{font-size:10px}
.stat .sub.r{color:#52C41A}
.stat .sub.r2{color:#ff4d4f}
.grid4{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-bottom:18px}
.grid2{grid-template-columns:1fr 1fr}
.grid3{grid-template-columns:repeat(3,1fr)}
.hd{font-size:15px;font-weight:700;margin-bottom:14px;display:flex;align-items:center;gap:8px}
.hd::before{content:"";display:inline-block;width:3px;height:15px;background:var(--a);border-radius:2px;flex-shrink:0}
.hd.e::before{background:var(--ae)}
.hd.d::before{background:var(--ad)}
.hd.f::before{background:var(--af)}
.tbl{overflow-x:auto}
table{width:100%;border-collapse:collapse;font-size:12px}
th,td{padding:9px 10px;text-align:left;border-bottom:1px solid var(--b)}
th{background:#fafafa;font-weight:500;color:var(--t2);font-size:11px}
tr:hover{background:#fafafa}
.cr{cursor:pointer}
.bdg{display:inline-block;padding:2px 8px;border-radius:10px;font-size:10px;font-weight:500}
.bdg.ba{background:rgba(22,119,255,.1);color:var(--a)}
.bdg.ae{background:rgba(82,196,26,.1);color:var(--ae)}
.bdg.ad{background:rgba(250,140,22,.1);color:var(--ad)}
.bdg.af2{background:rgba(114,46,209,.1);color:var(--af)}
.bdg.r{background:rgba(255,77,79,.1);color:#ff4d4f}
.bdg.y{background:rgba(250,140,22,.15);color:#d46b00}
.bdg.k{background:#f0f0f0;color:var(--t2)}
.btn{display:inline-flex;align-items:center;gap:5px;padding:6px 14px;border-radius:5px;font-size:12px;font-weight:500;cursor:pointer;border:1px solid var(--b);background:var(--c);color:var(--t);transition:all .15s;font-family:inherit}
.btn:hover{border-color:#40a9ff;color:#40a9ff}
.btn.p{background:var(--a);color:#fff;border-color:var(--a)}
.btn.p:hover{background:#4098ff}
.btn.e{background:var(--ae);color:#fff;border-color:var(--ae)}
.btn.e:hover{background:#73d13d}
.btn.d{background:var(--ad);color:#fff;border-color:var(--ad)}
.btn.d:hover{background:#fb9224}
.btn.f2{background:var(--af);color:#fff;border-color:var(--af)}
.btn.f2:hover{background:#9254de}
.btn.sm{padding:3px 9px;font-size:11px}
.tb{display:flex;align-items:center;gap:10px;margin-bottom:14px;flex-wrap:wrap}
.in{padding:6px 10px;border:1px solid var(--b);border-radius:5px;font-size:12px;outline:none;font-family:inherit;width:180px;background:#fff}
select.in,textarea.in{width:100%;padding:7px 10px;border:1px solid var(--b);border-radius:5px;font-size:12px;font-family:inherit;outline:none;background:#fff}
select.in:focus,textarea.in:focus{border-color:#40a9ff}
.fg{margin-bottom:14px}
.fl{display:block;font-size:12px;font-weight:500;margin-bottom:5px}
.fr{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.tl{position:relative;padding-left:22px}
.tl::before{content:"";position:absolute;left:7px;top:4px;bottom:4px;width:2px;background:var(--b)}
.ti{position:relative;margin-bottom:18px}
.ti::before{content:"";position:absolute;left:-19px;top:4px;width:9px;height:9px;border-radius:50%;background:var(--b);border:2px solid #fff}
.ti.done::before{background:#52C41A}
.ti.active::before{background:var(--a);box-shadow:0 0 0 3px rgba(22,119,255,.2)}
.ti.pending::before{background:var(--b)}
.tt{font-size:10px;color:var(--t2);margin-bottom:1px}
.ti .ttl{font-weight:500;font-size:12px}
.ti .td{font-size:11px;color:var(--t2);margin-top:1px}
.pg{display:none;animation:fade .25s ease}
.pg.on{display:block}
@keyframes fade{from{opacity:0;transform:translateX(8px)}to{opacity:1;transform:translateX(0)}}
.toast{position:fixed;top:76px;right:20px;background:#fff;border-radius:var(--r);box-shadow:var(--sh2);padding:11px 18px;z-index:300;display:none;font-size:12px;max-width:280px;border-left:3px solid #52C41A}
.toast.s{display:flex;align-items:center;gap:8px;animation:ti .3s ease}
.toast.e{border-left-color:#ff4d4f}
@keyframes ti{from{opacity:0;transform:translateX(20px)}to{opacity:1;transform:translateX(0)}}
.fx{display:flex;flex-wrap:wrap}
.fxb{display:flex;align-items:center;justify-content:space-between}
.g8{gap:8px}.g12{gap:12px}.g16{gap:16px}
.mb8{margin-bottom:8px}.mb12{margin-bottom:12px}.mb16{margin-bottom:16px}.mb20{margin-bottom:20px}
.mt8{margin-top:8px}.mt12{margin-top:12px}.mt16{margin-top:16px}
.ts2{color:#52C41A}.te2{color:#ff4d4f}.tw2{color:#fa8c16}
.tm{font-size:11px;color:var(--t2)}
.tr2{text-align:right}.tc2{text-align:center}
.fb{font-weight:700}
.dv2{height:1px;background:var(--b);margin:14px 0}
.es{text-align:center;padding:40px 0;color:var(--t2)}
.pgn{display:flex;align-items:center;justify-content:flex-end;gap:3px;margin-top:14px}
.pb{width:30px;height:30px;display:flex;align-items:center;justify-content:center;border:1px solid var(--b);border-radius:5px;cursor:pointer;font-size:12px;background:#fff;font-family:inherit;transition:all .15s}
.pb.on{background:var(--a);color:#fff;border-color:var(--a)}
.pb:hover:not(.on){border-color:#40a9ff;color:#40a9ff}
.ig{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.ii{display:flex;flex-direction:column;gap:2px}
.il{font-size:11px;color:var(--t2)}
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
.an .as{font-size:10px;color:var(--t2)}
.aa{font-size:14px;color:var(--b);flex-shrink:0}
.cr3{background:#fafafa;border-radius:var(--r);padding:14px;margin-top:12px}
.cr4{display:flex;justify-content:space-between;padding:4px 0;font-size:12px;color:var(--t2)}
.cr4.t{font-size:14px;font-weight:700;color:var(--t);border-top:1px solid var(--b);margin-top:6px;padding-top:8px}
.cr4.t .v{color:#52C41A;font-size:18px}
.cw{position:relative;height:200px}
.phwrap{display:flex;justify-content:center;align-items:flex-start;padding:32px 20px;background:#d8d8d8;min-height:calc(100vh - 56px)}
.phf{width:390px;background:#fff;border-radius:36px;box-shadow:0 8px 40px rgba(0,0,0,.22),0 0 0 11px #1a1a1a;overflow:hidden;position:relative}
.pn{height:34px;background:#1a1a1a;display:flex;align-items:flex-end;justify-content:center;padding-bottom:6px}
.pn::after{content:"";width:90px;height:16px;background:#111;border-radius:0 0 10px 10px}
.phb{height:calc(100vh - 90px);overflow-y:auto;background:#fff}
.phbb{position:absolute;bottom:0;left:0;right:0;height:58px;background:#fff;border-top:1px solid #eee;display:flex}
.pht{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2px;font-size:10px;color:#999;cursor:pointer;transition:color .15s}
.pht .ic{font-size:20px}
.dpht.on{color:#FA8C16}
.fpht.on{color:#722ED1}
.dp .phbb{background:#fffaf5}
.fp .phbb{background:#f5f0ff}
.phdr{padding:10px 14px 8px;display:flex;align-items:center;gap:8px}
.phdr .bk{font-size:16px;cursor:pointer;width:24px}
.phdr .ttl{font-size:13px;font-weight:600}
</style>
</head>
<body>

<nav class="nav">
  <div class="logo">TSCS <span>v2.0 多端交互演示</span></div>
  <div class="tabs">
    <div class="tab tp on" id="tabp" onclick="st("p")">🏛 机构端</div>
    <div class="tab" id="tabe" onclick="st("e")">🏢 企业端</div>
    <div class="tab" id="tabd" onclick="st("d")">🚗 驾驶员端</div>
    <div class="tab" id="tabf" onclick="st("f")">📱 现场端</div>
  </div>
</nav>

<!-- 机构端 -->
<div id="tp" class="lay">
<div class="side">
<div class="sht"><div class="sn">机构端</div><div class="ss">TSCS平台运营管理系统</div></div>
<div class="si sa" onclick="sp("p","ph")">📊 数据面板</div>
<div class="si" onclick="sp("p","pe")">🏢 企业管理</div>
<div class="si" onclick="sp("p","pc")">⚠ 事故报案</div>
<div class="si" onclick="sp("p","pcd")">🔍 案件详情</div>
<div class="si" onclick="sp("p","ppay")">💰 互助给付</div>
<div class="si" onclick="sp("p","pf")">📈 财务报表</div>
<div class="si" onclick="sp("p","pr")">🛡 风控评级</div>
<div class="si" onclick="sp("p","pu")">👥 用户管理</div>
</div>
<div class="main">

<!-- 数据面板 -->
<div id="ph" class="pg on">
<div class="hd">全局数据面板</div>
<div class="grid4">
<div class="stat"><div class="val" style="color:var(--a)">18</div><div class="lbl">入驻企业总数</div><div class="sub">本月+2</div></div>
<div class="stat"><div class="val">28,634</div><div class="lbl">在统车辆总数</div><div class="sub">活跃凭证</div></div>
<div class="stat"><div class="val" style="color:#ff4d4f">127</div><div class="lbl">本月新增案件</div><div class="sub r2">较上月+12</div></div>
<div class="stat"><div class="val" style="color:#ff4d4f">¥3,842,600</div><div class="lbl">本月给付金额</div><div class="sub r2">较上月+8%</div></div>
</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px">
<div class="card"><div class="hd">各企业关键指标对比</div><canvas id="cc" height="120"></canvas></div>
<div class="card"><div class="hd">月度给付趋势（万元）</div><canvas id="ct" height="120"></canvas></div>
</div>
<div class="card mt16">
<div class="hd">⚠ 风险预警</div>
<table><thead><tr><th>预警类型</th><th>企业</th><th>详情</th><th>操作</th></tr></thead>
<tbody>
<tr><td><span class="bdg r">高给付率</span></td><td>华通客运</td><td>近12月给付率91%，超过80%红线</td><td><button class="btn sm p" onclick="sp("p","pr")">查看</button></td></tr>
<tr><td><span class="bdg y">资金池不足</span></td><td>鹏程运输</td><td>互助资金池余额¥128万，低于预警线</td><td><button class="btn sm p">处理</button></td></tr>
<tr><td><span class="bdg af2">评分过低</span></td><td>星辰物流</td><td>企业驾驶评分均值62分，已连续3月低于70分</td><td><button class="btn sm p">查看</button></td></tr>
</tbody></table>
</div>
</div>

<!-- 企业列表 -->
<div id="pe" class="pg">
<div class="hd">企业管理</div>
<div class="tb"><input class="in" placeholder="搜索企业名称..."><select class="in" style="width:140px"><option>全部状态</option><option>正常</option><option>待审核</option></select><button class="btn p">+ 新增企业</button></div>
<div class="card">
<table><thead><tr><th>企业名称</th><th>行业</th><th>车辆规模</th><th>入驻时间</th><th>状态</th><th>操作</th></tr></thead>
<tbody>
<tr class="cr" onclick="sp("p","ped")"><td><b>鹏程运输</b></td><td>公路客运</td><td>3,200辆</td><td>2025-03-15</td><td><span class="bdg ae">正常</span></td><td><button class="btn sm">详情</button></td></tr>
<tr><td>星辰物流</td><td>货运</td><td>1,850辆</td><td>2025-05-20</td><td><span class="bdg ae">正常</span></td><td><button class="btn sm">详情</button></td></tr>
<tr><td>华通客运</td><td>旅游客运</td><td>2,100辆</td><td>2025-01-10</td><td><span class="bdg r">高风险</span></td><td><button class="btn sm">详情</button></td></tr>
<tr><td>顺捷租赁</td><td>租赁</td><td>960辆</td><td>2025-08-01</td><td><span class="bdg ae">正常</span></td><td><button class="btn sm">详情</button></td></tr>
<tr><td>鑫安出租</td><td>出租客运</td><td>420辆</td><td>2025-11-15</td><td><span class="bdg ae">正常</span></td><td><button class="btn sm">详情</button></td></tr>
</tbody></table>
</div>
</div>

<!-- 案件列表 -->
<div id="pc" class="pg">
<div class="hd">事故报案受理</div>
<div class="tb"><input class="in" placeholder="搜索报案号/车牌..."><select class="in" style="width:130px"><option>全部通道</option><option>快速通道</option><option>标准通道</option><option>大案通道</option></select><select class="in" style="width:120px"><option>全部状态</option><option>待分配</option><option>处理中</option></select></div>
<div class="card">
<table><thead><tr><th>报案号</th><th>时间</th><th>企业</th><th>车牌</th><th>通道</th><th>预估金额</th><th>状态</th><th>操作</th></tr></thead>
<tbody>
<tr class="cr" onclick="sp("p","pcd")"><td><b>TSCS-2026-0328-0088</b></td><td>2026-03-28 09:15</td><td>鹏程运输</td><td>京A·88888</td><td><span class="bdg ba">标准通道</span></td><td>¥15,800</td><td><span class="bdg y">核查中</span></td><td><button class="btn sm p">查看</button></td></tr>
<tr><td>TSCS-2026-0327-0087</td><td>2026-03-27 16:42</td><td>星辰物流</td><td>京B·66666</td><td><span class="bdg ae">快速通道</span></td><td>¥1,800</td><td><span class="bdg af2">待分配</span></td><td><button class="btn sm p">分配</button></td></tr>
<tr><td>TSCS-2026-0326-0086</td><td>2026-03-26 11:30</td><td>华通客运</td><td>京C·11222</td><td><span class="bdg r">大案通道</span></td><td>¥186,000</td><td><span class="bdg y">材料审核</span></td><td><button class="btn sm p">查看</button></td></tr>
</tbody></table>
</div>
</div>

<!-- 案件详情 -->
<div id="pcd" class="pg">
<div class="hd">案件详情 - TSCS-2026-0328-0088</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px">
<div class="card">
<div class="hd">报案信息</div>
<div class="ig mb12">
<div class="ii"><div class="il">报案号</div><div class="iv">TSCS-2026-0328-0088</div></div>
<div class="ii"><div class="il">企业</div><div class="iv">鹏程运输</div></div>
<div class="ii"><div class="il">车牌</div><div class="iv">京A·88888</div></div>
<div class="ii"><div class="il">责任划分</div><div class="iv"><span class="bdg y">主责 70%</span></div></div>
</div>
</div>
<div class="card">
<div class="hd">案件处理进度</div>
<div class="tl">
<div class="ti done"><div class="tt">2026-03-28 09:15</div><div class="ttl">驾驶员一键报案</div><div class="td">驾驶员张三提交报案</div></div>
<div class="ti done"><div class="tt">2026-03-28 10:02</div><div class="ttl">企业最终报案</div><div class="td">分司安全员审核通过</div></div>
<div class="ti done"><div class="tt">2026-03-28 10:30</div><div class="ttl">案件受理</div><div class="td">调度员李娜分配至核损员赵强</div></div>
<div class="ti active"><div class="tt">2026-03-28 11:15</div><div class="ttl">现场核查中</div><div class="td">核损员已到达现场，正在取证</div></div>
<div class="ti pending"><div class="tt">—</div><div class="ttl">损失评估</div><div class="td">等待核损员提交评估单</div></div>
<div class="ti pending"><div class="tt">—</div><div class="ttl">互助给付</div><div class="td">等待材料审核与理算</div></div>
</div>
</div>
</div>
<div class="card mt16">
<div class="hd">核查任务分配</div>
<div style="display:flex;align-items:center;gap:16px">
<div><div class="tm mb8">当前核损员</div><div class="fb">赵强 <span class="bdg ba">现场核查中</span></div></div>
<div><div class="tm mb8">当前状态</div><div class="fb">已到达 · 11:15签到</div></div>
<div><div class="tm mb8">已拍照</div><div class="fb">8/20 张</div></div>
<button class="btn p" style="margin-left:auto" onclick="sp("p","ppay")">查看互助给付</button>
</div>
</div>
</div>

<!-- 互助给付 -->
<div id="ppay" class="pg">
<div class="hd">互助给付 - TSCS-2026-0328-0088</div>
<div class="grid3 mb16">
<div class="stat"><div class="val">127</div><div class="lbl">案件总数</div><div class="sub">本月新增</div></div>
<div class="stat"><div class="val" style="color:#fa8c16">23</div><div class="lbl">待审核</div><div class="sub">材料待审</div></div>
<div class="stat"><div class="val">¥3,842,600</div><div class="lbl">本月给付总额</div><div class="sub">已支付</div></div>
</div>
<div class="card">
<div class="hd">互助理算</div>
<div class="ig mb16">
<div class="ii"><div class="il">损失额（取发票与评估较低者）</div><div class="iv m">¥15,800</div></div>
<div class="ii"><div class="il">责任比例</div><div class="iv">主责 × 70%</div></div>
<div class="ii"><div class="il">免给付额</div><div class="iv">¥500</div></div>
<div class="ii"><div class="il">协议扣除比例</div><div class="iv">0%</div></div>
</div>
<div class="cr3">
<div class="cr4"><span>损失额 × 责任比例</span><span>¥15,800 × 70% = ¥11,060</span></div>
<div class="cr4"><span>− 免给付额</span><span>¥11,060 − ¥500 = ¥10,560</span></div>
<div class="cr4"><span>× (1 − 协议扣除)</span><span>¥10,560 × 1.0 = ¥10,560</span></div>
<div class="cr4 t"><span>互助给付款</span><span class="v">¥10,560</span></div>
</div>
<div class="mt16">
<div class="hd" style="margin-bottom:12px">分级审批</div>
<div class="ap">
<div class="an" style="background:rgba(82,196,26,.1)"><div class="al">互助给付员</div><div class="av ts2">✓ 审核通过</div></div>
<div class="aa">→</div>
<div class="an" style="background:rgba(22,119,255,.1)"><div class="al">企业确认</div><div class="av" style="color:var(--a)">待确认</div><div class="as">≤2万自动通过</div></div>
<div class="aa">→</div>
<div class="an"><div class="al">最终审批</div><div class="av">自动通过</div><div class="as">≤2万</div></div>
<div class="aa">→</div>
<div class="an"><div class="al">支付执行</div><div class="av">待执行</div></div>
</div>
</div>
<div class="fx g8 mt16">
<button class="btn e" onclick="toast("给付成功，已通知企业")">确认给付 ¥10,560</button>
<button class="btn" onclick="sp("p","pf")">查看支付记录</button>
</div>
</div>

<!-- 财务报表 -->
<div id="pf" class="pg">
<div class="hd">财务报表 - 三账户模型</div>
<div class="grid4">
<div class="stat" style="border-left:4px solid #1677FF"><div class="val" style="color:#1677FF">¥28,640,000</div><div class="lbl">互助互济资金池（70%）</div><div class="sub">本月收入 ¥12,800,000 · 支出 ¥3,842,600</div></div>
<div class="stat" style="border-left:4px solid #fa8c16"><div class="val" style="color:#fa8c16">¥6,140,000</div><div class="lbl">风险储备金（15%）</div><div class="sub">上月结转</div></div>
<div class="stat" style="border-left:4px solid #52C41A"><div class="val" style="color:#52C41A">¥6,140,000</div><div class="lbl">平台运营管理费（15%）</div><div class="sub">本月收入 ¥2,742,857</div></div>
</div>
<div class="card mt16">
<div class="hd">各企业三账户明细</div>
<table><thead><tr><th>企业</th><th>本月缴纳</th><th>资金池70%</th><th>储备金15%</th><th>运营费15%</th><th>给付支出</th><th>池余额</th></tr></thead>
<tbody>
<tr><td>鹏程运输</td><td>¥12,800,000</td><td>¥8,960,000</td><td>¥1,920,000</td><td>¥1,920,000</td><td>¥1,280,000</td><td><span class="ts2">¥7,680,000</span></td></tr>
<tr><td>星辰物流</td><td>¥6,650,000</td><td>¥4,655,000</td><td>¥997,500</td><td>¥997,500</td><td>¥680,000</td><td><span class="ts2">¥3,975,000</span></td></tr>
<tr><td>华通客运</td><td>¥8,400,000</td><td>¥5,880,000</td><td>¥1,260,000</td><td>¥1,260,000</td><td>¥2,480,000</td><td><span class="te2">¥3,400,000</span></td></tr>
</tbody></table>
</div>
</div>

<!-- 风控评级 -->
<div id="pr" class="pg">
<div class="hd">企业风控评级</div>
<div class="card">
<table><thead><tr><th>企业</th><th>评级</th><th>给付率</th><th>评分均值</th><th>续约年限</th><th>挂靠比例</th><th>风险措施</th></tr></thead>
<tbody>
<tr><td>鹏程运输</td><td><span class="bdg ae">A级</span></td><td>34.2%</td><td>78.5</td><td>2年</td><td>15%</td><td>优先续约·费率优惠10%</td></tr>
<tr><td>星辰物流</td><td><span class="bdg ae">B级</span></td><td>52%</td><td>71</td><td>1年</td><td>32%</td><td>正常续约·标准费率</td></tr>
<tr><td>华通客运</td><td><span class="bdg r">D级</span></td><td>91%</td><td>58</td><td>3年</td><td>62%</td><td>暂停新增参统·约谈整改</td></tr>
<tr><td>顺捷租赁</td><td><span class="bdg y">C级</span></td><td>67%</td><td>65</td><td>1年</td><td>45%</td><td>续约审核加严·费率上浮</td></tr>
</tbody></table>
</div>
<div class="card mt16">
<div class="hd">企业风控雷达图</div>
<canvas id="crisk" height="180"></canvas>
</div>
</div>

<!-- 用户管理 -->
<div id="pu" class="pg">
<div class="hd">用户管理</div>
<div class="tb"><input class="in" placeholder="搜索姓名/账号..."><select class="in" style="width:140px"><option>全部角色</option><option>调度员</option><option>互助给付员</option><option>财务</option><option>运营</option></select><button class="btn p">+ 新增用户</button></div>
<div class="card">
<table><thead><tr><th>姓名</th><th>账号</th><th>角色</th><th>企业</th><th>最后登录</th><th>状态</th><th>操作</th></tr></thead>
<tbody>
<tr><td>李娜</td><td>linana</td><td><span class="bdg ba">调度员</span></td><td>平台</td><td>2026-03-28 09:00</td><td><span class="bdg ae">正常</td><td><button class="btn sm">编辑</button></td></tr>
<tr><td>赵强</td><td>zhaoqiang</td><td><span class="bdg af2">核损员</span></td><td>平台</td><td>2026-03-28 11:20</td><td><span class="bdg ae">正常</td><td><button class="btn sm">编辑</button></td></tr>
<tr><td>王芳</td><td>wangfang</td><td><span class="bdg ad">互助给付员</span></td><td>平台</td><td>2026-03-28 08:45</td><td><span class="bdg ae">正常</td><td><button class="btn sm">编辑</button></td></tr>
<tr><td>陈伟</td><td>chenwei</td><td><span class="bdg ae">财务</span></td><td>平台</td><td>2026-03-28 10:30</td><td><span class="bdg ae">正常</td><td><button class="btn sm">编辑</button></td></tr>
</tbody></table>
</div>
</div>

</div>
</div>

<!-- 企业端 -->
<div id="te" class="lay" style="display:none">
<div class="side">
<div class="sht"><div class="sn">企业端</div><div class="ss">鹏程运输 · 管理员</div></div>
<div class="si sa" onclick="sp("e","eh")">📊 工作台</div>
<div class="si" onclick="sp("e","ev")">🚗 车辆管理</div>
<div class="si" onclick="sp("e","ed")">👤 驾驶员管理</div>
<div class="si" onclick="sp("e","es")">🛡 安全看板</div>
<div class="si" onclick="sp("e","ec")">⚠ 案件管理</div>
<div class="si" onclick="sp("e","er")">📋 事故报案</div>
<div class="si" onclick="sp("e","efn")">🔄 续统管理</div>
</div>
<div class="main">

<div id="eh" class="pg on">
<div class="hd e">企业工作台</div>
<div class="grid4">
<div class="stat"><div class="val" style="color:var(--ae)">3,200</div><div class="lbl">在统车辆</div><div class="sub">本月+120</div></div>
<div class="stat"><div class="val" style="color:#fa8c16">3</div><div class="lbl">待处理事故报案</div><div class="sub r2">需及时处理</div></div>
<div class="stat"><div class="val" style="color:var(--a)">2</div><div class="lbl">待确认给付</div><div class="sub">待确认金额¥23,400</div></div>
<div class="stat"><div class="val" style="color:#ff4d4f">15</div><div class="lbl">即将到期车辆</div><div class="sub r2">未来15天内</div></div>
</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px">
<div class="card">
<div class="hd e">驾驶评分总览</div>
<div style="display:flex;align-items:center;gap:16px">
<div style="text-align:center">
<div style="font-size:42px;font-weight:700;color:var(--ae)">78.5</div>
<span class="bdg ae">B级·良好</span>
</div>
<canvas id="eesc" height="80"></canvas>
</div>
</div>
<div class="card">
<div class="hd e">本月安全事故统计</div>
<div class="grid3" style="gap:8px">
<div class="stat"><div class="val" style="color:#ff4d4f">12</div><div class="lbl">事故次数</div></div>
<div class="stat"><div class="val">0.38%</div><div class="lbl">安全事故率</div></div>
<div class="stat"><div class="val" style="color:#ff4d4f">¥128,600</div><div class="lbl">给付金额</div></div>
</div>
</div>
</div>
<div class="card mt16">
<div class="hd e">📋 待办事项</div>
<div class="fc" onclick="sp("e","ec")">
<div class="fci" style="background:rgba(255,77,79,.1)">⚠</div>
<div class="fcn"><div class="fct">待审核事故报案 <span class="bdg r">3</span></div><div class="fcd">驾驶员提交的报案需在24小时内完成审核并提交至平台</div></div>
</div>
<div class="fc" onclick="toast("建议已发，您很重要")">
<div class="fci" style="background:rgba(22,119,255,.1)">💰</div>
<div class="fcn"><div class="fct">待确认给付 <span class="bdg ba">2</span></div><div class="fcd">互助理算单已生成，请确认：¥10,560 / ¥12,840</div></div>
</div>
<div class="fc" onclick="sp("e","efn")">
<div class="fci" style="background:rgba(250,140,22,.1)">🔄</div>
<div class="fcn"><div class="fct">即将到期车辆 <span class="bdg y">15</span></div><div class="fcd">15辆车统筹单将在未来15天内到期，请及时处理续统</div></div>
</div>
</div>
</div>

<div id="ev" class="pg">
<div class="hd e">车辆管理</div>
<div class="tb"><input class="in" placeholder="搜索车牌号/VIN..."><select class="in" style="width:120px"><option>全部状态</option><option>在统</option><option>即将到期</option><option>已过期</option></select><button class="btn e">+ 批量导入</button><button class="btn e">+ 新增车辆</button></div>
<div class="card">
<table><thead><tr><th>车牌</th><th>车型</th><th>使用性质</th><th>绑定驾驶员</th><th>参统状态</th><th>到期日期</th><th>操作</th></tr></thead>
<tbody>
<tr><td><b>京A·88888</b></td><td>大型普通客车</td><td>公路客运</td><td>张伟</td><td><span class="bdg ae">在统</span></td><td>2026-12-31</td><td><button class="btn sm">详情</button></td></tr>
<tr><td>京B·12345</td><td>中型普通客车</td><td>旅游客运</td><td>李娜</td><td><span class="bdg ae">在统</td><td>2026-12-31</td><td><button class="btn sm">详情</button></td></tr>
<tr><td>京C·66789</td><td>轻型厢式货车</td><td>货运</td><td>王强</td><td><span class="bdg y">即将到期</span></td><td>2026-04-10</td><td><button class="btn sm">详情</button></td></tr>
<tr><td>京D·88001</td><td>小型轿车</td><td>出租客运</td><td>—</td><td><span class="bdg k">未绑定</span></td><td>2026-12-31</td><td><button class="btn sm e">绑定</button></td></tr>
</tbody></table>
<div class="pgn"><span class="pb" style="opacity:.4">‹</span><span class="pb on">1</span><span class="pb">2</span><span class="pb">3</span><span class="pb">...</span><span class="pb">128</span><span class="pb">›</span></div>
</div>
</div>

<div id="ed" class="pg">
<div class="hd e">驾驶员管理</div>
<div class="tb"><input class="in" placeholder="搜索姓名/手机号..."><select class="in" style="width:120px"><option>全部评分</option><option>优秀(90+)</option><option>良好(80+)</option><option>较差(<70)</option></select><button class="btn e">+ 批量导入</button></div>
<div class="card">
<table><thead><tr><th>姓名</th><th>手机号</th><th>准驾车型</th><th>绑定车辆</th><th>驾驶评分</th><th>等级</th><th>状态</th><th>操作</th></tr></thead>
<tbody>
<tr><td><b>张伟</b></td><td>138****5678</td><td>A1</td><td>京A·88888</td><td><b style="color:#52C41A">92</b></td><td><span class="bdg ae">优秀</span></td><td><span class="bdg ae">正常</span></td><td><button class="btn sm">详情</button></td></tr>
<tr><td>李娜</td><td>139****2233</td><td>B1</td><td>京B·12345</td><td><b style="color:#52C41A">88</b></td><td><span class="bdg ae">良好</span></td><td><span class="bdg ae">正常</span></td><td><button class="btn sm">详情</button></td></tr>
<tr><td>王强</td><td>137****8899</td><td>B2</td><td>京C·66789</td><td><b style="color:#fa8c16">68</b></td><td><span class="bdg y">较差</span></td><td><span class="bdg ae">正常</span></td><td><button class="btn sm">详情</button></td></tr>
<tr><td>赵雷</td><td>136****1155</td><td>A2</td><td>京A·99901</td><td><b style="color:#ff4d4f">58</b></td><td><span class="bdg r">差</span></td><td><span class="bdg r">高风险</span></td><td><button class="btn sm d">查看</button></td></tr>
</tbody></table>
</div>
<div class="card mt16">
<div class="hd e">驾驶评分分布</div>
<canvas id="eddist" height="140"></canvas>
</div>
</div>

<div id="es" class="pg">
<div class="hd e">安全管理看板</div>
<div class="grid3">
<div class="stat"><div class="val" style="color:var(--ae)">78.5</div><div class="lbl">企业评分均值</div><div class="sub">较上月↑2.3分</div></div>
<div class="stat"><div class="val">0.38%</div><div class="lbl">安全事故率</div><div class="sub">行业均值0.52%</div></div>
<div class="stat"><div class="val" style="color:#ff4d4f">8人</div><div class="lbl">风险驾驶员</div><div class="sub r2">评分低于70分</div></div>
</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px">
<div class="card"><div class="hd e">月度驾驶评分趋势</div><canvas id="estrend" height="100"></canvas></div>
<div class="card"><div class="hd e">风险驾驶员预警</div>
<table><thead><tr><th>姓名</th><th>评分</th><th>风险原因</th><th>操作</th></tr></thead>
<tbody>
<tr><td>赵雷</td><td><span class="bdg r">58</span></td><td>连续3月低于60分</td><td><button class="btn sm e">约谈</button></td></tr>
<tr><td>孙鹏</td><td><span class="bdg y">63</span></td><td>本月发生主责事故</td><td><button class="btn sm">查看</button></td></tr>
</tbody></table>
</div>
</div>
</div>

<div id="ec" class="pg">
<div class="hd e">案件管理</div>
<div class="tb"><input class="in" placeholder="搜索报案号/车牌..."><select class="in" style="width:120px"><option>全部状态</option><option>处理中</option><option>待确认</option><option>已完成</option></select></div>
<div class="card">
<table><thead><tr><th>报案号</th><th>时间</th><th>车牌</th><th>类型</th><th>金额</th><th>状态</th><th>操作</th></tr></thead>
<tbody>
<tr><td><b>TSCS-2026-0328-0088</b></td><td>2026-03-28 09:15</td><td>京A·88888</td><td>财产损失</td><td>¥15,800</td><td><span class="bdg y">核查中</span></td><td><button class="btn sm e">详情</button></td></tr>
<tr><td>TSCS-2026-0327-0087</td><td>2026-03-27 16:42</td><td>京B·12345</td><td>财产损失</td><td>¥1,800</td><td><span class="bdg ae">待确认</span></td><td><button class="btn sm e">确认</button></td></tr>
<tr><td>TSCS-2026-0325-0085</td><td>2026-03-25 14:20</td><td>京C·66789</td><td>财产损失</td><td>¥8,200</td><td><span class="bdg ae">已完成</span></td><td><button class="btn sm">详情</button></td></tr>
</tbody></table>
</div>
</div>

<div id="er" class="pg">
<div class="hd e">新增事故报案</div>
<div class="card">
<div style="display:flex;align-items:center;margin-bottom:20px">
<div style="width:28px;height:28px;border-radius:50%;background:var(--ae);color:#fff;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;flex-shrink:0">1</div>
<div style="flex:1;height:2px;background:#d9d9d9;margin:0 8px"></div>
<div style="width:28px;height:28px;border-radius:50%;background:var(--a);color:#fff;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;flex-shrink:0">2</div>
<div style="flex:1;height:2px;background:#d9d9d9;margin:0 8px"></div>
<div style="width:28px;height:28px;border-radius:50%;background:#d9d9d9;color:#fff;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;flex-shrink:0">3</div>
</div>
<div class="fg"><div class="fl">事故车辆 *</div><select class="in"><option>京A·88888 - 张伟</option><option>京B·12345 - 李娜</option></select></div>
<div class="fr">
<div class="fg"><div class="fl">事故时间 *</div><input class="in" type="datetime-local" value="2026-03-28T09:15"></div>
<div class="fg"><div class="fl">事故地点 *</div><input class="in" placeholder="GPS定位中..." value="北京市朝阳区京通快速路"></div>
</div>
<div class="fg"><div class="fl">责任划分 *</div>
<div style="display:flex;gap:8px">
<label style="display:flex;align-items:center;gap:4px;cursor:pointer;font-size:12px"><input type="radio" name="eresp" checked> 全责</label>
<label style="display:flex;align-items:center;gap:4px;cursor:pointer;font-size:12px"><input type="radio" name="eresp"> 主责</label>
<label style="display:flex;align-items:center;gap:4px;cursor:pointer;font-size:12px"><input type="radio" name="eresp"> 同责</label>
<label style="display:flex;align-items:center;gap:4px;cursor:pointer;font-size:12px"><input type="radio" name="eresp"> 次责</label>
</div>
</div>
<div class="fg"><div class="fl">事故描述</div><textarea class="in" rows="3" placeholder="请描述..."></textarea></div>
<div class="fg"><div class="fl">现场照片（最多9张）</div>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:8px">
<div style="height:80px;border:2px dashed var(--b);border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:24px;color:var(--t2);cursor:pointer">+</div>
</div>
<div class="tm mt8">已上传 0/9 张（必须：全景1+双方受损部位各1）</div>
</div>
<div class="fx g8 mt16">
<button class="btn" onclick="sp("e","eh")">取消</button>
<button class="btn e" onclick="toast("提交成功，已通知平台")">提交报案</button>
</div>
</div>
</div>

<div id="efn" class="pg">
<div class="hd e">续统管理</div>
<div class="card">
<div class="hd e" style="font-size:13px">即将到期车辆（未来30天）</div>
<table><thead><tr><th><input type="checkbox" checked> 全选</th><th>车牌</th><th>车型</th><th>方案</th><th>到期日</th><th>预估新费</th></tr></thead>
<tbody>
<tr><td><input type="checkbox" checked></td><td>京C·66789</td><td>轻型厢式货车</td><td>标准方案</td><td>2026-04-10</td><td>¥4,212</td></tr>
<tr><td><input type="checkbox" checked></td><td>京E·11230</td><td>中型普通客车</td><td>基础方案</td><td>2026-04-15</td><td>¥3,510</td></tr>
<tr><td><input type="checkbox"></td><td>京F·33880</td><td>大型普通客车</td><td>标准方案</td><td>2026-04-20</td><td>¥5,860</td></tr>
</tbody></table>
<div class="fx g8 mt16">
<button class="btn e" onclick="toast("续统缴费单已生成，请确认后对公转账")">生成续统缴费单</button>
</div>
</div>
</div>

</div>
</div>

<!-- 驾驶员端手机框架 -->
<div id="td" class="phwrap" style="display:none">
<div class="phf dp">
<div class="pn"></div>
<div class="phb">

<div id="dl" class="card" style="margin:12px">
<div style="text-align:center;font-size:13px;font-weight:600;margin-bottom:12px">登录小程序</div>
<input class="in mb12" placeholder="手机号" value="138****5678">
<div style="display:flex;gap:8px">
<input class="in" style="flex:1" placeholder="验证码">
<button class="btn" style="white-space:nowrap">获取验证码</button>
</div>
<button class="btn d" style="width:100%;margin-top:12px;justify-content:center" onclick="sp("d","dh")">登录</button>
</div>

<div id="dh" class="card" style="margin:12px;display:none">
<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px">
<div>
<div style="font-size:15px;font-weight:700">京A·88888</div>
<div style="font-size:11px;color:var(--t2)">绑定车辆 · 大型普通客车</div>
</div>
<div style="text-align:right">
<div style="font-size:28px;font-weight:700;color:var(--ad)">78</div>
<div style="font-size:10px;color:var(--t2)">驾驶评分</div>
</div>
</div>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-bottom:14px">
<div class="stat" style="text-align:center;padding:10px;cursor:pointer" onclick="sp("d","dcs")">
<div style="font-size:20px;margin-bottom:4px">📋</div><div style="font-size:10px;color:var(--t2)">我的案件</div><div style="font-size:16px;font-weight:700;color:var(--ad)">1</div>
</div>
<div class="stat" style="text-align:center;padding:10px">
<div style="font-size:20px;margin-bottom:4px">💚</div><div style="font-size:10px;color:var(--t2)">安全天数</div><div style="font-size:16px;font-weight:700;color:#52C41A">92</div>
</div>
<div class="stat" style="text-align:center;padding:10px">
<div style="font-size:20px;margin-bottom:4px">👤</div><div style="font-size:10px;color:var(--t2)">车队排名</div><div style="font-size:16px;font-weight:700">前15%</div>
</div>
</div>
<div class="fc" onclick="sp("d","dr")" style="margin-bottom:0">
<div class="fci" style="background:rgba(250,140,22,.15)">📋</div>
<div class="fcn"><div class="fct">事故报案</div><div class="fcd">一键快速报案，5分钟搞定</div></div>
</div>
</div>

<div id="dr" class="card" style="margin:12px;display:none">
<div class="hd d">事故报案</div>
<div style="display:flex;align-items:center;margin-bottom:14px">
<div style="width:24px;height:24px;border-radius:50%;background:var(--ad);color:#fff;display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:700">1</div>
<div style="flex:1;height:2px;background:#d9d9d9;margin:0 6px"></div>
<div style="width:24px;height:24px;border-radius:50%;background:#d9d9d9;color:#fff;display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:700">2</div>
<div style="flex:1;height:2px;background:#d9d9d9;margin:0 6px"></div>
<div style="width:24px;height:24px;border-radius:50%;background:#d9d9d9;color:#fff;display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:700">3</div>
</div>
<div class="fg"><div class="fl">事故车辆</div><select class="in"><option selected>京A·88888 - 张伟</option></select></div>
<div class="fr">
<div class="fg"><div class="fl">事故时间</div><input class="in" type="datetime-local" value="2026-03-28T09:15"></div>
<div class="fg"><div class="fl">事故地点</div><input class="in" value="北京市朝阳区京通快速路"></div>
</div>
<div class="fg"><div class="fl">责任划分</div>
<div style="display:flex;gap:6px;flex-wrap:wrap">
<label style="display:flex;align-items:center;gap:4px;cursor:pointer;font-size:12px"><input type="radio" name="dr" checked> 全责</label>
<label style="display:flex;align-items:center;gap:4px;cursor:pointer;font-size:12px"><input type="radio" name="dr"> 主责</label>
<label style="display:flex;align-items:center;gap:4px;cursor:pointer;font-size:12px"><input type="radio" name="dr"> 同责</label>
<label style="display:flex;align-items:center;gap:4px;cursor:pointer;font-size:12px"><input type="radio" name="dr"> 次责</label>
</div>
</div>
<div class="fg"><div class="fl">事故描述</div><textarea class="in" rows="2">前车突然变道导致追尾，右后保险杠受损，前保受损，无人伤。</textarea></div>
<div class="fg"><div class="fl">现场照片（必填：全景1+双方受损各1）</div>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:6px">
<div style="height:64px;border:2px dashed var(--b);border-radius:6px;display:flex;align-items:center;justify-content:center;font-size:20px;color:var(--t2);cursor:pointer">📷</div>
<div style="height:64px;border:2px dashed var(--b);border-radius:6px;display:flex;align-items:center;justify-content:center;font-size:20px;color:var(--t2);cursor:pointer">📷</div>
<div style="height:64px;border:2px dashed var(--b);border-radius:6px;display:flex;align-items:center;justify-content:center;font-size:20px;color:var(--t2);cursor:pointer">📷</div>
</div>
<div class="tm mt8">已上传 0/9 张</div>
<button class="btn d" style="width:100%;margin-top:16px;justify-content:center" onclick="toast("报案成功！案件号：TSCS-2026-0328-0088")">提交报案</button>
</div>

<div id="dcs" class="card" style="margin:12px;display:none">
<div class="hd d">我的案件</div>
<table><thead><tr><th>报案号</th><th>时间</th><th>状态</th><th></th></tr></thead>
<tbody>
<tr><td><b>TSCS-2026-0328-0088</b></td><td>2026-03-28</td><td><span class="bdg y">处理中</span></td><td><button class="btn sm d">查看</button></td></tr>
</tbody></table>
</div>

<div id="ds" class="card" style="margin:12px;display:none">
<div class="hd d">驾驶评分详情</div>
<div style="text-align:center;margin-bottom:14px">
<div style="font-size:48px;font-weight:700;color:var(--ad)">78</div>
<span class="bdg ae" style="font-size:12px;padding:4px 12px">B级 · 良好</span>
<div class="tm mt8">超过 85% 同类车型驾驶员</div>
</div>
<canvas id="dschart" height="140"></canvas>
</div>

</div>
<div class="phbb">
<div class="pht dpht on" onclick="phNav("d","dh",this)"><span class="ic">🏠</span><span>首页</span></div>
<div class="pht dpht" onclick="phNav("d","dr",this)"><span class="ic">📋</span><span>报案</span></div>
<div class="pht dpht" onclick="phNav("d","dcs",this)"><span class="ic">📂</span><span>案件</span></div>
<div class="pht dpht" onclick="phNav("d","ds",this)"><span class="ic">📊</span><span>评分</span></div>
</div>
</div>
</div>

<!-- 现场端手机框架 -->
<div id="tf" class="phwrap" style="display:none">
<div class="phf fp">
<div class="pn"></div>
<div class="phb">

<div id="fh" class="card" style="margin:12px">
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-bottom:14px">
<div class="stat" style="text-align:center;padding:10px"><div style="font-size:22px;font-weight:700;color:var(--af)">3</div><div style="font-size:10px;color:var(--t2)">今日任务</div></div>
<div class="stat" style="text-align:center;padding:10px"><div style="font-size:22px;font-weight:700">48</div><div style="font-size:10px;color:var(--t2)">本月完成</div></div>
<div class="stat" style="text-align:center;padding:10px"><div style="font-size:22px;font-weight:700">4.2h</div><div style="font-size:10px;color:var(--t2)">平均时长</div></div>
</div>
<div class="hd f">待处理任务</div>
<div class="fc" onclick="sp("f","ft")">
<div class="fci" style="background:rgba(114,46,209,.15)">🚨</div>
<div class="fcn"><div class="fct">TSCS-2026-0328-0088 <span class="bdg r">紧急</span></div><div class="fcd">京A·88888 · 北京市朝阳区京通快速路</div><div><span class="bdg y">待出发</span> <span class="tm">分配：10:30</span></div></div>
</div>
<div class="fc" onclick="sp("f","ft")">
<div class="fci" style="background:rgba(114,46,209,.1)">⚠</div>
<div class="fcn"><div class="fct">TSCS-2026-0327-0087 <span class="bdg y">标准</span></div><div class="fcd">京B·66666 · 海淀区学院路</div><div><span class="bdg y">待出发</span> <span class="tm">分配：昨天17:00</span></div></div>
</div>
</div>

<div id="ft" class="card" style="margin:12px;display:none">
<div class="hd f">任务详情</div>
<div class="ig mb12">
<div class="ii"><div class="il">报案号</div><div class="iv">TSCS-2026-0328-0088</div></div>
<div class="ii"><div class="il">事故地点</div><div class="iv">北京市朝阳区京通快速路</div></div>
<div class="ii"><div class="il">车辆</div><div class="iv">京A·88888</div></div>
<div class="ii"><div class="il">报案人</div><div class="iv">张伟 138****5678</div></div>
<div class="ii"><div class="il">责任</div><div class="iv"><span class="bdg y">主责 70%</span></div></div>
</div>
<div class="fx g8">
<button class="btn" onclick="sp("f","fh")">返回</button>
<button class="btn f2" onclick="sp("f","fci")">接受任务并导航</button>
</div>
</div>

<div id="fci" class="card" style="margin:12px;display:none">
<div class="hd f">到达签到</div>
<div style="text-align:center;padding:20px 0">
<div style="font-size:42px;margin-bottom:10px">📍</div>
<div style="font-size:13px;font-weight:600;margin-bottom:6px">北京市朝阳区京通快速路</div>
<div class="tm mb16">GPS定位成功，已到达事故现场</div>
<button class="btn f2" style="width:200px;justify-content:center" onclick="sp("f","fph")">确认签到</button>
</div>
</div>

<div id="fph" class="card" style="margin:12px;display:none">
<div class="hd f">现场拍照</div>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-bottom:10px">
<div style="height:72px;border:2px dashed var(--b);border-radius:6px;display:flex;align-items:center;justify-content:center;font-size:22px;color:var(--t2);cursor:pointer;background:#fafafa">📷</div>
<div style="height:72px;border:2px dashed var(--b);border-radius:6px;display:flex;align-items:center;justify-content:center;font-size:22px;color:var(--t2);cursor:pointer;background:#fafafa">📷</div>
