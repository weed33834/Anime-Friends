#!/usr/bin/env python3
"""Generate the waifu match HTML app in parts."""

import os

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

# ===== PART 1: CSS =====
CSS = r"""
*{margin:0;padding:0;box-sizing:border-box;-webkit-tap-highlight-color:transparent}
:root{
--pink:#ff6b9d;--pink-light:#ffc2d9;--pink-dark:#e63973;
--purple:#a855f7;--purple-light:#c084fc;--purple-dark:#7c3aed;
--bg-dark:#1a0a2e;--bg-card:#2d1b4e;--bg-card-light:#3d2b5e;
--text:#f0e6ff;--text-dim:#a99bc9;--text-bright:#fff;
--accent:#fbbf24;--success:#4ade80;
--radius:16px;--shadow:0 8px 32px rgba(168,85,247,0.3);
}
html{scroll-behavior:smooth}
body{
font-family:'PingFang SC','Hiragino Sans GB','Microsoft YaHei','Helvetica Neue',sans-serif;
background:linear-gradient(135deg,#1a0a2e 0%,#2d1b4e 50%,#1a0a2e 100%);
color:var(--text);min-height:100vh;overflow-x:hidden;
}
body::before{
content:'';position:fixed;top:0;left:0;width:100%;height:100%;
background:
radial-gradient(circle at 20% 30%,rgba(255,107,157,0.08) 0%,transparent 50%),
radial-gradient(circle at 80% 70%,rgba(168,85,247,0.08) 0%,transparent 50%);
pointer-events:none;z-index:0;
}
#particles{position:fixed;top:0;left:0;width:100%;height:100%;pointer-events:none;z-index:1}
.container{position:relative;z-index:2;max-width:600px;margin:0 auto;padding:20px;min-height:100vh}
.page{display:none;animation:fadeIn 0.5s ease}
.page.active{display:block}
@keyframes fadeIn{from{opacity:0;transform:translateY(20px)}to{opacity:1;transform:translateY(0)}}
.landing{text-align:center;padding:40px 0;min-height:100vh;display:flex;flex-direction:column;justify-content:center;align-items:center}
.landing-logo{font-size:64px;margin-bottom:16px;animation:bounce 2s ease infinite}
@keyframes bounce{0%,100%{transform:translateY(0)}50%{transform:translateY(-10px)}}
.landing h1{
font-size:32px;font-weight:800;
background:linear-gradient(135deg,var(--pink),var(--purple),var(--accent));
-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;
margin-bottom:12px;line-height:1.4;
}
.landing .subtitle{font-size:15px;color:var(--text-dim);margin-bottom:8px;line-height:1.6}
.landing .stats{display:flex;gap:24px;margin:24px 0}
.landing .stat{text-align:center}
.landing .stat-num{font-size:28px;font-weight:800;color:var(--pink)}
.landing .stat-label{font-size:12px;color:var(--text-dim)}
.landing .tags{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin:16px 0 24px}
.landing .tag{padding:4px 12px;border-radius:20px;font-size:12px;background:rgba(168,85,247,0.15);border:1px solid rgba(168,85,247,0.3);color:var(--purple-light)}
.btn{
display:inline-block;padding:14px 40px;border:none;border-radius:30px;
font-size:16px;font-weight:700;cursor:pointer;transition:all 0.3s ease;
background:linear-gradient(135deg,var(--pink),var(--purple));
color:#fff;box-shadow:0 4px 20px rgba(255,107,157,0.4);
}
.btn:hover{transform:translateY(-2px);box-shadow:0 6px 25px rgba(255,107,157,0.5)}
.btn:active{transform:translateY(0)}
.btn-secondary{background:transparent;border:2px solid var(--purple);color:var(--purple-light);box-shadow:none}
.btn-secondary:hover{background:rgba(168,85,247,0.1);box-shadow:0 4px 15px rgba(168,85,247,0.2)}
.quiz-header{display:flex;justify-content:space-between;align-items:center;margin-bottom:20px}
.quiz-progress-text{font-size:14px;color:var(--text-dim)}
.quiz-progress-text span{color:var(--pink);font-weight:700;font-size:18px}
.quiz-dots{display:flex;gap:4px;flex-wrap:wrap;max-width:300px;justify-content:flex-end}
.quiz-dot{width:8px;height:8px;border-radius:50%;background:rgba(255,255,255,0.1);transition:all 0.3s}
.quiz-dot.done{background:var(--pink)}
.quiz-dot.current{background:var(--accent);transform:scale(1.3)}
.progress-bar{width:100%;height:6px;background:rgba(255,255,255,0.08);border-radius:3px;margin-bottom:24px;overflow:hidden}
.progress-fill{height:100%;border-radius:3px;background:linear-gradient(90deg,var(--pink),var(--purple),var(--accent));transition:width 0.5s ease;width:0}
.question-card{background:var(--bg-card);border-radius:var(--radius);padding:28px 20px;box-shadow:var(--shadow);border:1px solid rgba(168,85,247,0.15)}
.question-tag{display:inline-block;padding:4px 14px;border-radius:20px;font-size:11px;background:rgba(251,191,36,0.12);color:var(--accent);margin-bottom:14px;border:1px solid rgba(251,191,36,0.2)}
.question-text{font-size:19px;font-weight:700;line-height:1.5;color:var(--text-bright);margin-bottom:24px}
.options{display:flex;flex-direction:column;gap:12px}
.option{
padding:16px;border-radius:12px;cursor:pointer;transition:all 0.3s ease;
background:var(--bg-card-light);border:2px solid transparent;
font-size:15px;line-height:1.5;color:var(--text);
display:flex;align-items:center;gap:12px;
}
.option:hover,.option.selected{border-color:var(--pink);background:rgba(255,107,157,0.1);transform:translateX(4px)}
.option-icon{width:32px;height:32px;border-radius:50%;background:rgba(168,85,247,0.2);display:flex;align-items:center;justify-content:center;font-size:16px;flex-shrink:0;transition:all 0.3s}
.option.selected .option-icon{background:var(--pink);color:#fff}
.option-text{flex:1}
.result-page{padding:0}
.result-hero{
text-align:center;padding:30px 0 20px;
background:linear-gradient(180deg,rgba(255,107,157,0.1) 0%,transparent 100%);
border-radius:0 0 30px 30px;margin-bottom:20px;
}
.result-label{font-size:14px;color:var(--accent);margin-bottom:8px;font-weight:600;letter-spacing:2px}
.result-title{font-size:26px;font-weight:800;color:var(--text-bright);margin-bottom:20px}
.result-card{
background:var(--bg-card);border-radius:var(--radius);overflow:hidden;
box-shadow:var(--shadow);border:1px solid rgba(168,85,247,0.2);
margin-bottom:20px;
}
.result-image-wrap{width:100%;aspect-ratio:3/4;overflow:hidden;position:relative;background:var(--bg-card-light)}
.result-image-wrap img{width:100%;height:100%;object-fit:cover;object-position:center top}
.result-image-wrap::after{content:'';position:absolute;bottom:0;left:0;width:100%;height:120px;background:linear-gradient(transparent,var(--bg-card))}
.result-name{padding:20px 20px 0;text-align:center}
.result-name-cn{font-size:24px;font-weight:800;color:var(--text-bright);margin-bottom:4px}
.result-name-jp{font-size:14px;color:var(--text-dim)}
.result-series{font-size:13px;color:var(--pink);margin-top:6px}
.result-tags{display:flex;flex-wrap:wrap;gap:6px;padding:12px 20px;justify-content:center}
.result-tag{padding:3px 10px;border-radius:12px;font-size:11px;background:rgba(168,85,247,0.12);border:1px solid rgba(168,85,247,0.2);color:var(--purple-light)}
.result-match-score{padding:0 20px 16px;text-align:center}
.match-ring{display:inline-flex;flex-direction:column;align-items:center}
.match-percent{font-size:36px;font-weight:800;color:var(--accent)}
.match-label{font-size:12px;color:var(--text-dim)}
.result-section{padding:20px;margin-bottom:16px;background:var(--bg-card);border-radius:var(--radius);border:1px solid rgba(168,85,247,0.1)}
.result-section-title{font-size:16px;font-weight:700;color:var(--accent);margin-bottom:12px;display:flex;align-items:center;gap:8px}
.result-section-title::before{content:'';width:4px;height:18px;border-radius:2px;background:var(--pink)}
.result-bio{font-size:14px;line-height:1.8;color:var(--text)}
.result-appearance{font-size:14px;line-height:1.7;color:var(--text-dim)}
.match-analysis{font-size:14px;line-height:1.9;color:var(--text)}
.match-analysis p{margin-bottom:12px}
.match-analysis .highlight{color:var(--pink);font-weight:600}
.match-analysis .accent-text{color:var(--accent);font-weight:600}
.dimension-bars{display:flex;flex-direction:column;gap:10px}
.dim-bar{display:flex;align-items:center;gap:10px}
.dim-label{width:60px;font-size:12px;color:var(--text-dim);text-align:right;flex-shrink:0}
.dim-track{flex:1;height:8px;background:rgba(255,255,255,0.06);border-radius:4px;overflow:hidden}
.dim-fill{height:100%;border-radius:4px;transition:width 1s ease}
.dim-value{width:30px;font-size:11px;color:var(--text-dim);text-align:left}
.other-matches{display:flex;flex-direction:column;gap:12px}
.other-match{display:flex;align-items:center;gap:12px;padding:10px;background:var(--bg-card-light);border-radius:12px;cursor:pointer;transition:all 0.3s}
.other-match:hover{background:rgba(255,107,157,0.08)}
.other-match-img{width:50px;height:60px;border-radius:8px;overflow:hidden;flex-shrink:0;background:var(--bg-dark)}
.other-match-img img{width:100%;height:100%;object-fit:cover;object-position:center top}
.other-match-info{flex:1;min-width:0}
.other-match-name{font-size:14px;font-weight:600;color:var(--text-bright);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.other-match-series{font-size:11px;color:var(--text-dim)}
.other-match-score{font-size:18px;font-weight:800;color:var(--accent);flex-shrink:0}
.result-actions{display:flex;gap:12px;justify-content:center;padding:20px 0 40px;flex-wrap:wrap}
.gallery-header{text-align:center;padding:20px 0}
.gallery-header h2{font-size:24px;font-weight:800;color:var(--text-bright);margin-bottom:6px}
.gallery-header p{font-size:13px;color:var(--text-dim)}
.gallery-filter{display:flex;gap:8px;justify-content:center;margin:16px 0;flex-wrap:wrap}
.filter-btn{padding:6px 16px;border-radius:20px;font-size:13px;border:1px solid rgba(168,85,247,0.2);background:transparent;color:var(--text-dim);cursor:pointer;transition:all 0.3s}
.filter-btn.active,.filter-btn:hover{background:rgba(168,85,247,0.15);color:var(--purple-light);border-color:var(--purple)}
.gallery-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:12px;padding-bottom:40px}
.gallery-item{background:var(--bg-card);border-radius:12px;overflow:hidden;cursor:pointer;transition:all 0.3s;border:1px solid rgba(168,85,247,0.1)}
.gallery-item:hover{transform:translateY(-4px);box-shadow:var(--shadow);border-color:rgba(255,107,157,0.3)}
.gallery-item-img{width:100%;aspect-ratio:3/4;overflow:hidden;background:var(--bg-card-light)}
.gallery-item-img img{width:100%;height:100%;object-fit:cover;object-position:center top;transition:transform 0.3s}
.gallery-item:hover .gallery-item-img img{transform:scale(1.05)}
.gallery-item-info{padding:8px}
.gallery-item-name{font-size:13px;font-weight:600;color:var(--text-bright);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.gallery-item-series{font-size:10px;color:var(--text-dim);margin-top:2px}
.modal-overlay{position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,0.8);z-index:100;display:none;align-items:center;justify-content:center;padding:20px}
.modal-overlay.active{display:flex;animation:fadeIn 0.3s}
.modal-content{background:var(--bg-card);border-radius:var(--radius);max-width:400px;width:100%;max-height:85vh;overflow-y:auto;border:1px solid rgba(168,85,247,0.3)}
.modal-img{width:100%;aspect-ratio:3/4;overflow:hidden}
.modal-img img{width:100%;height:100%;object-fit:cover;object-position:center top}
.modal-body{padding:20px}
.modal-close{position:fixed;top:20px;right:20px;width:36px;height:36px;border-radius:50%;background:rgba(0,0,0,0.5);color:#fff;border:none;font-size:20px;cursor:pointer;z-index:101;display:flex;align-items:center;justify-content:center}
.loading{text-align:center;padding:60px 0}
.loading-spinner{width:48px;height:48px;border:4px solid rgba(168,85,247,0.2);border-top-color:var(--pink);border-radius:50%;animation:spin 1s linear infinite;margin:0 auto 16px}
@keyframes spin{to{transform:rotate(360deg)}}
.loading-text{font-size:14px;color:var(--text-dim)}
.share-section{background:var(--bg-card);border-radius:var(--radius);padding:20px;margin:16px 0;text-align:center;border:1px solid rgba(168,85,247,0.1)}
.share-title{font-size:15px;font-weight:600;color:var(--accent);margin-bottom:12px}
.share-text{font-size:13px;color:var(--text-dim);line-height:1.6;margin-bottom:12px}
.share-copy{display:inline-flex;align-items:center;gap:6px;padding:8px 20px;border-radius:20px;font-size:13px;border:1px solid var(--purple);background:transparent;color:var(--purple-light);cursor:pointer;transition:all 0.3s}
.share-copy:hover{background:rgba(168,85,247,0.1)}
.img-fallback{display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,var(--bg-card),var(--bg-card-light));color:var(--text-dim);font-size:12px;text-align:center;padding:20px}
@media(min-width:480px){
.gallery-grid{grid-template-columns:repeat(3,1fr)}
.landing h1{font-size:36px}
}
@media(min-width:768px){
.gallery-grid{grid-template-columns:repeat(4,1fr)}
.container{max-width:650px}
}
"""

# ===== PART 2: HTML structure =====
HTML_HEAD = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>二次元老婆匹配器 - 你的命运之人是谁？</title>
<style>
""" + CSS + """
</style>
</head>
<body>
<canvas id="particles"></canvas>
<div class="container">

<!-- Landing Page -->
<div class="page active" id="page-landing">
<div class="landing">
<div class="landing-logo">\u2740</div>
<h1>\u4e8c\u6b21\u5143\u8001\u5a46\u5339\u914d\u5668</h1>
<p class="subtitle">48\u4f4d\u4eba\u6c14galgame\u4e0e\u52a8\u6f2b\u89d2\u8272</p>
<p class="subtitle">\u56de\u7b5424\u9053\u7075\u9b42\u62f7\u95ee\uff0c\u627e\u5230\u4f60\u7684\u547d\u8fd0\u4e4b\u4eba</p>
<div class="stats">
<div class="stat"><div class="stat-num">48</div><div class="stat-label">\u89d2\u8272</div></div>
<div class="stat"><div class="stat-num">24</div><div class="stat-label">\u95ee\u9898</div></div>
<div class="stat"><div class="stat-num">8</div><div class="stat-label">\u7ef4\u5ea6</div></div>
</div>
<div class="tags">
<span class="tag">Galgame</span>
<span class="tag">\u52a8\u6f2b</span>
<span class="tag">\u50b2\u5a07</span>
<span class="tag">\u6cbb\u6108\u7cfb</span>
<span class="tag">\u5143\u6c14</span>
<span class="tag">\u4e09\u65e0</span>
<span class="tag">\u75c5\u5a07</span>
<span class="tag">\u4eba\u59bb</span>
</div>
<button class="btn" onclick="startQuiz()">\u5f00\u59cb\u5339\u914d \u2728</button>
<p class="subtitle" style="margin-top:16px;font-size:12px">\u00a9 \u4e8c\u6b21\u5143\u8001\u5a46\u5339\u914d\u5668 \u00b7 \u4ec5\u4f9b\u5a31\u4e50</p>
</div>
</div>

<!-- Quiz Page -->
<div class="page" id="page-quiz">
<div class="quiz-header">
<div class="quiz-progress-text">\u7b2c <span id="qCurrent">1</span> / <span id="qTotal">24</span> \u9898</div>
<div class="quiz-dots" id="quizDots"></div>
</div>
<div class="progress-bar"><div class="progress-fill" id="progressFill"></div></div>
<div class="question-card" id="questionCard"></div>
</div>

<!-- Result Page -->
<div class="page" id="page-result">
<div class="result-page" id="resultContent"></div>
</div>

<!-- Gallery Page -->
<div class="page" id="page-gallery">
<div class="gallery-header">
<h2>\u89d2\u8272\u56fe\u9274</h2>
<p>\u5171 48 \u4f4d\u89d2\u8272 \u00b7 \u70b9\u51fb\u67e5\u770b\u8be6\u60c5</p>
</div>
<div class="gallery-filter">
<button class="filter-btn active" onclick="filterGallery('all',this)">\u5168\u90e8</button>
<button class="filter-btn" onclick="filterGallery('galgame',this)">Galgame</button>
<button class="filter-btn" onclick="filterGallery('anime',this)">\u52a8\u6f2b</button>
</div>
<div class="gallery-grid" id="galleryGrid"></div>
</div>

</div>

<!-- Modal -->
<div class="modal-overlay" id="modal">
<button class="modal-close" onclick="closeModal()">\u00d7</button>
<div class="modal-content" id="modalContent"></div>
</div>
"""

# Write part 1
with open(os.path.join(OUT_DIR, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(HTML_HEAD)

print("Part 1 (CSS + HTML structure) written successfully")
print(f"File size so far: {os.path.getsize(os.path.join(OUT_DIR, 'index.html'))} bytes")
