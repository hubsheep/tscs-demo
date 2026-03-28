html = '''

<div id='ccomp' class='card' style='display:none'>
<div class='hd'>案件详情</div>
<div class='ig mb12'>
<div class='ii'><div class='il'>报案号</div><div class='iv'>TSCS-2026-0328-0088</div></div>
<div class='ii'><div class='il'>企业</div><div class='iv'>鹏程运输</div></div>
<div class='ii'><div class='il'>车牌</div><div class='iv'>京A·88888</div></div>
<div class='ii'><div class='il'>责任</div><div class='iv'><span class='bdg y'>主责 70%</span></div></div>
</div>
<button class='btn' onclick='sp("p","ppay")'>查看给付</button>
</div>

</div>
</div>

<div class='toast' id='tst'></div>

<script>
var ct = 'p';
var charts = {};

function st(t) {
  ct = t;
  document.querySelectorAll('.tab').forEach(function(el){ el.classList.remove('on'); });
  document.getElementById('tab' + t).classList.add('on');
  document.querySelectorAll('.lay').forEach(function(el){ el.style.display = 'none'; });
  var el = document.getElementById('t' + t);
  if (el) {
    el.style.display = 'flex';
    if (t === 'd' || t === 'f') { el.style.justifyContent = 'center'; }
    else { el.style.justifyContent = ''; }
  }
  var firstPage = document.querySelector('#t' + t + ' .pg');
  if (firstPage) {
    firstPage.classList.add('on');
    firstPage.style.display = 'block';
  }
  if (!charts[t]) { initCharts(t); }
}

function sp(term, pageId) {
  var container = document.getElementById('t' + term);
  if (!container) return;
  container.querySelectorAll('.pg').forEach(function(el){ el.classList.remove('on'); el.style.display = 'none'; });
  var page = document.getElementById(pageId);
  if (page) { page.classList.add('on'); page.style.display = 'block'; }
  container.querySelectorAll('.si').forEach(function(el){ el.classList.remove('sa'); el.classList.remove('se'); el.classList.remove('sd'); el.classList.remove('sf'); });
  var si = container.querySelector('.si[onclick*="' + pageId + '"]');
  if (si) si.classList.add('sa');
}

function phNav(term, pageId, el) {
  var phframe = el.closest('.phf');
  if (!phframe) return;
  phframe.querySelectorAll('.pg').forEach(function(p){ p.classList.remove('on'); p.style.display = 'none'; });
  var page = document.getElementById(pageId);
  if (page) { page.classList.add('on'); page.style.display = 'block'; }
  phframe.querySelectorAll('.pht').forEach(function(t){ t.classList.remove('on'); });
  el.classList.add('on');
}

function toast(msg) {
  var t = document.getElementById('tst');
  t.textContent = msg;
  t.className = 'toast s';
  setTimeout(function(){ t.className = 'toast'; }, 3000);
}

function initCharts(term) {
  if (term === 'p') {
    if (!charts.p) {
      var ctx = document.getElementById('cc');
      if (ctx) {
        charts.p = new Chart(ctx, {
          type: 'bar',
          data: {
            labels: ['鹏程', '星辰', '华通', '顺捷', '鑫安'],
            datasets: [
              { label: '给付率(%)', data: [34, 52, 91, 67, 42], backgroundColor: 'rgba(22,119,255,0.7)', borderRadius: 4 },
              { label: '评分', data: [78, 71, 58, 65, 80], backgroundColor: 'rgba(82,196,26,0.7)', borderRadius: 4 }
            ]
          },
          options: { responsive: true, plugins: { legend: { font: { size: 10 } } } }
        });
      }
    }
    if (!charts.pt) {
      var ctt = document.getElementById('ct');
      if (ctt) {
        charts.pt = new Chart(ctt, {
          type: 'line',
          data: {
            labels: ['10月', '11月', '12月', '1月', '2月', '3月'],
            datasets: [{ label: '给付金额(万元)', data: [280, 310, 290, 340, 360, 384],
              borderColor: '#1677FF', backgroundColor: 'rgba(22,119,255,0.1)', fill: true, tension: 0.4 }]
          },
          options: { responsive: true }
        });
      }
    }
    if (!charts.pr) {
      var cr = document.getElementById('crisk');
      if (cr) {
        charts.pr = new Chart(cr, {
          type: 'radar',
          data: {
            labels: ['给付率', '安全评分', '续约率', '挂靠比', '赔付频次'],
            datasets: [{
              label: '鹏程运输',
              data: [34, 78, 95, 15, 12],
              borderColor: '#52C41A', backgroundColor: 'rgba(82,196,26,0.1)'
            }, {
              label: '华通客运',
              data: [91, 58, 60, 62, 48],
              borderColor: '#ff4d4f', backgroundColor: 'rgba(255,77,79,0.1)'
            }]
          },
          options: { responsive: true }
        });
      }
    }
    charts.p = true;
  }
  if (term === 'e') {
    if (!charts.ee) {
      var ees = document.getElementById('eesc');
      if (ees) {
        charts.ee = new Chart(ees, {
          type: 'doughnut',
          data: {
            labels: ['优秀', '良好', '一般', '较差'],
            datasets: [{ data: [820, 1580, 620, 180],
              backgroundColor: ['#52C41A', '#1677FF', '#fa8c16', '#ff4d4f'] }]
          },
          options: { responsive: true, cutout: '65%', plugins: { legend: { position: 'right', labels: { font: { size: 10 } } } } }
        });
      }
    }
    if (!charts.edd) {
      var edd = document.getElementById('eddist');
      if (edd) {
        charts.edd = new Chart(edd, {
          type: 'bar',
          data: {
            labels: ['<60', '60-70', '70-80', '80-90', '>90'],
            datasets: [{ label: '人数', data: [8, 42, 180, 620, 820],
              backgroundColor: ['#ff4d4f','#fa8c16','#1677FF','#52C41A','#52C41A'], borderRadius: 4 }]
          },
          options: { responsive: true, plugins: { legend: { display: false } } }
        });
      }
    }
    if (!charts.estr) {
      var estr = document.getElementById('estrend');
      if (estr) {
        charts.estr = new Chart(estr, {
          type: 'line',
          data: {
            labels: ['10月', '11月', '12月', '1月', '2月', '3月'],
            datasets: [{ label: '评分', data: [72, 74, 76, 75, 76, 78.5],
              borderColor: '#FA8C16', backgroundColor: 'rgba(250,140,22,0.1)', fill: true, tension: 0.4 }]
          },
          options: { responsive: true }
        });
      }
    }
    charts.e = true;
  }
  if (term === 'd') {
    if (!charts.dsc) {
      var dsc = document.getElementById('dschart');
      if (dsc) {
        charts.dsc = new Chart(dsc, {
          type: 'radar',
          data: {
            labels: ['急加速', '急刹车', '急转弯', '超速', '疲劳驾驶', '车道偏离'],
            datasets: [{ label: '得分', data: [85, 80, 90, 75, 95, 82],
              borderColor: '#FA8C16', backgroundColor: 'rgba(250,140,22,0.15)', pointBackgroundColor: '#FA8C16' }]
          },
          options: { responsive: true, scales: { r: { min: 0, max: 100 } } }
        });
      }
    }
    charts.d = true;
  }
}

st('p');
</script>
</body>
</html>
'''

with open(r'D:\workAIspace\openclaw\tscs-demo\c6.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('c6.html written, len=', len(html))
