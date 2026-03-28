#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys
# Fix path spacing issue
path = r'D:\workAIspace\openclaw\tscs-demo\index.html'
js = '''<!-- TOAST -->
<div id="tst" class="tst"></div>
<script>
var ct = 'p';
var charts = {};

function st(t) {
  ct = t;
  document.querySelectorAll(".tab").forEach(function(el){el.classList.remove("active")});
  document.querySelector(".tab[data-t=\\""""+t+"\""""]").classList.add("active");
  document.querySelectorAll(".lay").forEach(function(el){el.style.display = "none"});
  var el = document.getElementById("t-"+t);
  if (el) {
    el.style.display = "flex";
    if (t === "d" || t === "f") { el.style.justifyContent = "center"; }
    else { el.style.justifyContent = ""; }
  }
  var firstPage = document.querySelector("#t-"+t+" .pg");
  if (firstPage) { firstPage.classList.add("on"); }
  initCharts(t);
}

function sp(t, pid) {
  document.querySelectorAll("#t-"+t+" .pg").forEach(function(el){el.classList.remove("on")});
  var p = document.getElementById(pid);
  if (p) p.classList.add("on");
  var side = document.getElementById("t-"+t);
  if (side) {
    side.querySelectorAll(".si").forEach(function(el){el.classList.remove("active")});
    var sis = side.querySelectorAll(".si");
    for (var i=0;i<sis.length;i++) {
      if (sis[i].getAttribute("onclick") && sis[i].getAttribute("onclick").indexOf(pid)>=0) {
        sis[i].classList.add("active"); break;
      }
    }
  }
  initCharts(t);
}

function pn(t, pid, el) {
  document.querySelectorAll(".pt").forEach(function(e){e.classList.remove("active")});
  if (el) el.classList.add("active");
  sp(t, pid);
}

function tst(msg) {
  var t = document.getElementById("tst");
  t.textContent = msg;
  t.className = "tst show";
  setTimeout(function(){t.classList.remove("show");}, 3000);
}

function initCharts(t) {
  if (charts[t]) return;
  charts[t] = true;
  
  if (t === "p") {
    var ccomp = document.getElementById("ccomp");
    if (ccomp) {
      new Chart(ccomp, {
        type:"bar",
        data:{labels:["鹏程","星辰","华通","顺捷","鑫安"],
          datasets:[{label:"给附率%",data:[34,52,91,67,42],
            backgroundColor:["#52C41A","#52C41A","#ff4d4f","#fa8c16","#52C41A"]}]
        },
        options:{responsive:true,plugins:{legend:{display:false}}}
      );
    }
    var ctrend = document.getElementById("ctrend");
    if (ctrend) {
      new Chart(ctrend, {
        type:"line",
        data:{labels:["10月","11月","12月","1月","2月","3月"],
          datasets:[{label:"给付额(万元)",data:[280,310,290,340,360,384],
            borderColor:"#1677FF",backgroundColor:"rgba(22,119,255,.1)",fill:true,tension:.4}]
        },
        options:{responsive:true}
      });
    }
    var crisk = document.getElementById("crisk");
    if (crisk) {
      new Chart(crisk, {
        type:"radar",
        data:{labels:["给附率","评分","续约年限","挂靠比例","赔付速度"],
          datasets:[
            {label:"鹏程",data:[85,78,90,95,88],backgroundColor:"rgba(22,119,255,.2)",borderColor:"#1677FF"},
            {label:"华通",data:[30,45,70,50,60],backgroundColor:"rgba(255,77,79,.2)",borderColor:"#ff4d4f"}
          ]
        },
        options:{responsive:true}
      });
    }
  }
  
  if (t === "e") {
    var eesc = document.getElementById("eesc");
    if (eesc) {
      new Chart(eesc, {
        type:"bar",
        data:{labels:["一分司","二分司","三分司","四分司"],
          datasets:[{label:"评分",data:[82,78,75,71],backgroundColor:"#52C41A"}]
        },
        options:{responsive:true,plugins:{legend:{display:false}}}
      );
    }
    var eddist = document.getElementById("eddist");
    if (eddist) {
      new Chart(eddist, {
        type:"doughnut",
        data:{labels:["优秀(90+)","良好(80+)","一般(70+)","较差(60+)","差(<60)"],
          datasets:[{data:[320,1100,1400,480,110],
            backgroundColor:["#52C41A","#73d13d","#fa8c16","#ff7a45","#ff4d4f"]}]
        },
        options:{responsive:true}
      });
    }
    var estrend = document.getElementById("estrend");
    if (estrend) {
      new Chart(estrend, {
        type:"line",
        data:{labels:["10月","11月","12月","1月","2月","3月"],
          datasets:[{label:"均分",data:[75,76,74,77,76.2,78.5],
            borderColor:"#52C41A",backgroundColor:"rgba(82,196,26,.1)",fill:true,tension:.4}]
        },
        options:{responsive:true}
      });
    }
  }
  
  if (t === "d") {
    var dschart = document.getElementById("dschart");
    if (dschart) {
      new Chart(dschart, {
        type:"radar",
        data:{labels:["安全驾驶","事故记录","合规记录"],
          datasets:[{label:"张伟",data:[85,90,95],backgroundColor:"rgba(250,140,22,.2)",borderColor:"#FA8C16"}]
        },
        options:{responsive:true,scales:{r:{min:0,max:100}}}
      );
    }
    var dstrend = document.getElementById("dstrend");
    if (dstrend) {
      new Chart(dstrend, {
        type:"line",
        data:{labels:["10月","11月","12月","1月","2月","3月"],
          datasets:[{label:"评分",data:[72,74,76,75,76,78],
            borderColor:"#FA8C16",backgroundColor:"rgba(250,140,22,.1)",fill:true,tension:.4}]
        },
        options:{responsive:true}
      });
    }
  }
}

st("p");
</script>
</body>
</html>
'''
with open(path, 'a', encoding='utf-8') as f:
    f.write(js)
print('JS written')
size = os.path.getsize(path)
print('File size:', size)
with open(path, encoding='utf-8') as f:
    content = f.read()
ch_lines = sum(1 for l in content.split('\n') if any('\u4e00' <= c <= '\u9fff' for c in l))
print('Chinese lines:', ch_lines)
print('Has DOCTYPE:', '<!DOCTYPE' in content)
print('Has chart.js:', 'chart.js' in content)
print('Has t-p:', '"t-p"' in content)
print('Complete:', '</html>' in content)
