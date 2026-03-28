
<div style="height:64px;background:#f0f0f0;border-radius:6px;display:flex;align-items:center;justify-content:center;font-size:20px;color:#595959;cursor:pointer">🖼️</div>
<div style="height:64px;background:#f0f0f0;border-radius:6px;display:flex;align-items:center;justify-content:center;font-size:20px;color:#595959;cursor:pointer">🖼️</div>
<div style="height:64px;background:#f0f0f0;border-radius:6px;display:flex;align-items:center;justify-content:center;font-size:20px;color:#595959;cursor:pointer">🖼️</div>
</div>
<div style="background:#fafafa;border-radius:8px;padding:10px;font-size:12px;color:#59599;margin-bottom:12px"><b>拍照要求：</b>必须包含：①现场全景1张 ②涉事车辆全景（正侧面45度）各1张 ③受损部位特写（含参照物）各1张 ④道路环境照 ⑤如有认定书需拍摄认定书</div>
<div style="display:flex;gap:8px">
<button class="btn" style="flex:1;justify-content:center">📷 拍照</button>
<button class="btn" style="flex:1;justify-content:center">🖼️ 相册</button>
</div>
</div>
<div class="fx g8 mt16">
<button class="btn" onclick="sp('f','fci')">上一步</button>
<button class="btn bf2" onclick="sp('f','frec')">下一步：笔录定责</button>
</div>
</div>

<div id="frec" class="pg">
<div style="padding:12px 14px 0">
<div class="st" style="font-size:14px">当事人笔录与初步定责</div>
<div class="c">
<div class="fg"><div class="fl">当事人姓名 *</div><input class="in" placeholder="请输入"></div>
<div class="fr">
<div class="fg"><div class="fl">驾驶证号 *</div><input class="in" placeholder="请输入"></div>
<div class="fg"><div class="fl">联系方式 *</div><input class="in" placeholder="请输入"></div>
</div>
<div class="fg">
<div class="fl">事故经过（口述自动转文字）</div>
<div style="display:flex;gap:8px">
<textarea class="in" rows="3" placeholder="请描述事故经过..." style="flex:1">前车突然变道，我方躲避不及追尾，前车右后保险杠受损，本车前保险杠受损，无人伤。</textarea>
<button class="btn" style="align-self:flex-end;white-space:nowrap">🎤 语音</button>
</div>
</div>
<div class="fg"><div class="fl">初步定责 *</div>
<div style="display:flex;gap:6px;flex-wrap:wrap">
<label style="display:flex;align-items:center;gap:4px;cursor:pointer;font-size:12px"><input type="radio" name="frep"> 全部责任</label>
<label style="display:flex;align-items:center;gap:4px;cursor:pointer;font-size:12px"><input type="radio" name="frep" checked> 主要责任</label>
<label style="display:flex;align-items:center;gap:4px;cursor:pointer;font-size:12px"><input type="radio" name="frep"> 同等责任</label>
<label style="display:flex;align-items:center;gap:4px;cursor:pointer;font-size:12px"><input type="radio" name="frep"> 次要责任</label>
</div>
</div>
<div class="fg"><div class="fl">电子签名</div>
<div style="height:50px;border:2px dashed #d9d9d9;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:12px;color:#595959;cursor:pointer">点击签名（当事人）</div>
</div>
<div class="fx g8 mt16">
<button class="btn" onclick="sp('f','fph')">上一步</button>
<button class="btn bf2" onclick="sp('f','fev')">下一步：损失评估</button>
</div>
</div>
</div>
</div>

<div id="fev" class="pg">
<div style="padding:12px 14px 0">
<div class="st" style="font-size:14px">损失评估</div>
<div class="c">
<div class="st" style="font-size:13px">逐项损失评估</div>
<table><thead><tr><th>损失部位</th><th>损失类型</th><th>预估金额</th></tr></thead>
<tbody>
<tr><td>前保险杠</td><td>钣金修复+喷漆</td><td>¥3,200</td></tr>
<tr><td>左前大灯</td><td>更换零件</td><td>¥4,800</td></tr>
<tr><td>前舱盖</td><td>钣金修复</td><td>¥2,100</td></tr>
<tr><td>水箱框架</td><td>更换零件</td><td>¥1,800</td></tr>
</tbody>
<tfoot><tr style="background:#fafafa;font-weight:700"><td colspan="2">合计</td><td style="color:var(--af)">¥11,900</td></tr></tfoot>
</table>
<div class="fg"><div class="fl">评估备注</div><textarea class="in" rows="2" placeholder="如有特殊情况请说明..."></textarea></div>
<div class="fx g8 mt16">
<button class="btn" onclick="sp('f','frec')">上一步</button>
<button class="btn bf2" style="margin-left:auto" onclick="toast('核查报告已提交！');sp('f','fh')">提交核查报告</button>
</div>
</div>
</div>

</div>
</div>
<div class="pbb">
<div class="pt" onclick="pn('f','fh',this)"><span class="ic">📋</span><span>工作台</span></div>
<div class="pt" onclick="pn('f','ft',this)"><span class="ic">📝</span><span>任务</span></div>
<div class="pt" onclick="pn('f','fev',this)"><span class="ic">💰</span><span>评估</span></div>
<div class="pt" onclick="pn('f','fap',this)"><span class="ic">✅</span><span>审批</span></div>
</div>
</div>
</div>
</div>

<!-- toast -->
<div id="toast" class="toast"></div>

<script>
var cur = 'p';
var charts = {};

function st(t) {
  cur = t;
  document.querySelectorAll('.tab').forEach(function(e){ e.classList.remove('on') });
  document.getElementById('tab-'+t).classList.add('on');
  document.querySelectorAll('.lay').forEach(function(e){ e.style.display = 'none' });
  var el = document.getElementById('t-'+t);
  if (el) {
    var isPhone = (t === 'd' || t === 'f');
    el.style.display = 'flex';
    if (isPhone) { el.style.justifyContent = 'center'; }
    else { el.style.justifyContent = ''; }
  }
  var first = document.querySelector('#t-'+t+' .pg');
  if (first) { first.classList.add('on'); }
  initCharts(t);
}

function sp(t, pid) {
  document.querySelectorAll('#t-'+t+' .pg').forEach(function(e){ e.classList.remove('on') });
  var p = document.getElementById(pid);
  if (p) p.classList.add('on');
  initCharts(t);
}

function pn(t, pid, el) {
  if (el) {
    el.parentElement.querySelectorAll('.pt').forEach(function(e){ e.classList.remove('on') });
    el.classList.add('on');
  }
  sp(t, pid);
}

function toast(msg) {
  var t = document.getElementById('toast');
  t.textContent = msg;
  t.className = 'toast s';
  setTimeout(function(){ t.className = 'toast'; }, 3000);
}

function initCharts(t) {
  if (charts[t]) return;
  charts[t] = true;

  if (t === 'p' || t === 'all') {
    var ccomp = document.getElementById('ccomp');
    if (ccomp) {
      new Chart(ccomp, {
        type:'bar',
        data:{
          labels:['鹏程','星辰','华通','顺捷','鑫安'],
          datasets:[{label:'给付率%',data:[34,52,91,67,42],backgroundColor:['#52C41A','#52C41A','#ff4d4f','#fa8c16','#52C41A']}]
        },
        options:{responsive:true,plugins:{legend:{display:false}}}
      );
    }
    var ctrend = document.getElementById('ctrend');
    if (ctrend) {
      new Chart(ctrend, {
        type:'line',
        data:{
          labels:['10月','11月','12月','1月','2月','3月'],
          datasets:[{label:'给付额(万元)',data:[280,310,290,340,360,384],borderColor:'#1677FF',backgroundColor:'rgba(22,119,255,.1)',fill:true,tension:.4}]
        },
        options:{responsive:true}
      });
    }
    var crisk = document.getElementById('crisk');
    if (crisk) {
      new Chart(crisk, {
        type:'radar',
        data:{
          labels:['给付率','评分','续约年限','挂靠比例','赔付速度'],
          datasets:[
            {label:'鹏程',data:[85,78,90,95,88],backgroundColor:'rgba(22,119,255,.2)',borderColor:'#1677FF'},
            {label:'华通',data:[30,45,70,50,60],backgroundColor:'rgba(255,77,79,.2)',borderColor:'#ff4d4f'}
          ]
        },
        options:{responsive:true}
      });
    }
  }

  if (t === 'e' || t === 'all') {
    var eesc = document.getElementById('eesc');
    if (eesc) {
      new Chart(eesc, {
        type:'bar',
        data:{labels:['一分司','二分司','三分司','四分司'],datasets:[{label:'评分',data:[82,78,75,71],backgroundColor:'#52C41A'}]},
        options:{responsive:true,plugins:{legend:{display:false}}}
      );
    }
    var eddist = document.getElementById('eddist');
    if (eddist) {
      new Chart(eddist, {
        type:'doughnut',
        data:{labels:['优秀(90+)','良好(80+)','一般(70+)','较差(60+)','差(<60)'],datasets:[{data:[320,1100,1400,480,110],backgroundColor:['#52C41A','#73d13d','#fa8c16','#ff7a45','#ff4d4f'}]},
        options:{responsive:true}
      });
    }
    var estrend = document.getElementById('estrend');
    if (estrend) {
      new Chart(estrend, {
        type:'line',
        data:{labels:['10月','11月','12月','1月','2月','3月'],datasets:[{label:'均分',data:[75,76,74,77,76.2,78.5],borderColor:'#52C41A',backgroundColor:'rgba(82,196,26,.1)',fill:true,tension:.4}]},
        options:{responsive:true}
      });
    }
  }

  if (t === 'd' || t === 'all') {
    var dschart = document.getElementById('dschart');
    if (dschart) {
      new Chart(dschart, {
        type:'radar',
        data:{labels:['安全驾驶','事故记录','合规记录'],datasets:[{label:'张伟',data:[85,90,95],backgroundColor:'rgba(250,140,22,.2)',borderColor:'#FA8C16'}]},
        options:{responsive:true,scales:{r:{min:0,max:100}}}
      );
    }
    var dstrend = document.getElementById('dstrend');
    if (dstrend) {
      new Chart(dstrend, {
        type:'line',
        data:{labels:['10月','11月','12月','1月','2月','3月'],datasets:[{label:'评分',data:[72,74,76,75,76,78],borderColor:'#FA8C16',backgroundColor:'rgba(250,140,22,.1)',fill:true,tension:.4}]},
        options:{responsive:true}
      });
    }
  }
}

st('p');
</script>
</body>
</html>
