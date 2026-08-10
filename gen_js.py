#!/usr/bin/env python3
"""Append JavaScript logic and close HTML"""
import os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'index.html')

JS = r"""
// ===== DIMENSION INFO =====
const dimInfo = {
gentle:{name:"温柔",color:"#ff6b9d",desc:"你渴望一份温暖如春的感情，在意的人能用柔软的方式包裹你的疲惫"},
energy:{name:"活力",color:"#fbbf24",desc:"你想要一个让生活永不无聊的伴侣，永远充满热情和正能量"},
independent:{name:"独立",color:"#4ade80",desc:"你欣赏有自我追求的人，互相尊重彼此的独立空间"},
playful:{name:"俏皮",color:"#f472b6",desc:"你喜欢充满乐趣和惊喜的相处方式，生活需要调味剂"},
loyal:{name:"忠诚",color:"#a855f7",desc:"你看重绝对的信任和守护，一旦认定就绝不放手"},
tsundere:{name:"傲娇",color:"#fb7185",desc:"你被嘴硬心软的反差感深深吸引，口是心正是最可爱的告白"},
elegant:{name:"优雅",color:"#c084fc",desc:"你向往知性而从容的气质，在安静中感受彼此的深度"},
mature:{name:"成熟",color:"#60a5fa",desc:"你期待理性而深沉的陪伴，能在风雨中一起前行"}
};

// ===== STATE =====
let currentQ = 0;
let userDims = {gentle:0,energy:0,independent:0,playful:0,loyal:0,tsundere:0,elegant:0,mature:0};
let answers = [];

// ===== PAGE NAVIGATION =====
function showPage(id) {
document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
document.getElementById(id).classList.add('active');
window.scrollTo(0, 0);
}

// ===== QUIZ =====
function startQuiz() {
currentQ = 0;
userDims = {gentle:0,energy:0,independent:0,playful:0,loyal:0,tsundere:0,elegant:0,mature:0};
answers = [];
showPage('page-quiz');
renderQuizDots();
renderQuestion();
}

function renderQuizDots() {
const container = document.getElementById('quizDots');
container.innerHTML = '';
for (let i = 0; i < questions.length; i++) {
const dot = document.createElement('div');
dot.className = 'quiz-dot';
if (i < currentQ) dot.classList.add('done');
if (i === currentQ) dot.classList.add('current');
container.appendChild(dot);
}
}

function renderQuestion() {
const q = questions[currentQ];
document.getElementById('qCurrent').textContent = currentQ + 1;
document.getElementById('qTotal').textContent = questions.length;
document.getElementById('progressFill').style.width = ((currentQ / questions.length) * 100) + '%';

const card = document.getElementById('questionCard');
let html = '<span class="question-tag">' + q.tag + '</span>';
html += '<div class="question-text">' + q.q + '</div>';
html += '<div class="options">';
const icons = ['A','B','C','D'];
q.options.forEach((opt, i) => {
html += '<div class="option" onclick="selectOption(' + i + ')" data-idx="' + i + '">';
html += '<div class="option-icon">' + icons[i] + '</div>';
html += '<div class="option-text">' + opt.text + '</div>';
html += '</div>';
});
html += '</div>';
card.innerHTML = html;
}

function selectOption(idx) {
const card = document.getElementById('questionCard');
const options = card.querySelectorAll('.option');
options.forEach(o => o.classList.remove('selected'));
options[idx].classList.add('selected');

const opt = questions[currentQ].options[idx];
answers.push({qIdx: currentQ, optIdx: idx});
Object.keys(opt.dims).forEach(dim => {
userDims[dim] += opt.dims[dim];
});

setTimeout(() => {
currentQ++;
if (currentQ >= questions.length) {
showResult();
} else {
renderQuizDots();
renderQuestion();
}
}, 350);
}

// ===== MATCHING ALGORITHM =====
function calculateMatches() {
const results = characters.map(char => {
let score = 0;
let totalWeight = 0;
Object.keys(userDims).forEach(dim => {
const userVal = userDims[dim];
const charVal = char.dims[dim];
const diff = Math.abs(userVal - charVal);
const weight = userVal;
score += (10 - diff) * weight;
totalWeight += weight * 10;
});
const matchPercent = totalWeight > 0 ? Math.round((score / totalWeight) * 100) : 0;
return {char, score, matchPercent};
});
results.sort((a, b) => b.score - a.score);
return results;
}

// ===== RESULT =====
function showResult() {
showPage('page-result');
const container = document.getElementById('resultContent');
container.innerHTML = '<div class="loading"><div class="loading-spinner"></div><div class="loading-text">正在匹配你的命运之人...</div></div>';

setTimeout(() => {
const results = calculateMatches();
const best = results[0];
const top5 = results.slice(0, 5);

const char = best.char;
const topDims = Object.entries(userDims).sort((a, b) => b[1] - a[1]).slice(0, 3);
const dimAnalysis = topDims.map(([dim, val]) => {
const info = dimInfo[dim];
const charVal = char.dims[dim];
const matchLevel = charVal >= 7 ? '非常高' : charVal >= 5 ? '很高' : charVal >= 3 ? '不错' : '有待提升';
return {dim, val, info, charVal, matchLevel};
});

let html = '<div class="result-hero">';
html += '<div class="result-label">你的命运之人</div>';
html += '<div class="result-title">最佳匹配结果</div>';
html += '</div>';

html += '<div class="result-card">';
html += '<div class="result-image-wrap"><img src="' + char.image + '" alt="' + char.name + '" onerror="this.style.display=\'none\';this.parentElement.classList.add(\'img-fallback\');this.parentElement.textContent=\'图片加载失败\'"></div>';
html += '<div class="result-name">';
html += '<div class="result-name-cn">' + char.name + '</div>';
html += '<div class="result-name-jp">' + char.nameJp + '</div>';
html += '<div class="result-series">出自《' + char.series + '》</div>';
html += '</div>';
html += '<div class="result-tags">';
char.tags.forEach(t => { html += '<span class="result-tag">' + t + '</span>'; });
html += '</div>';
html += '<div class="result-match-score">';
html += '<div class="match-ring">';
html += '<div class="match-percent">' + best.matchPercent + '%</div>';
html += '<div class="match-label">契合度</div>';
html += '</div>';
html += '</div>';
html += '</div>';

// Match analysis
html += '<div class="result-section">';
html += '<div class="result-section-title">为什么是' + char.nickname + '？</div>';
html += '<div class="match-analysis">';

const dimName1 = dimInfo[topDims[0][0]].name;
const dimName2 = dimInfo[topDims[1][0]].name;
const dimName3 = dimInfo[topDims[2][0]].name;

html += '<p>经过24道题的深度分析，你展现出强烈的<span class="highlight">' + dimName1 + '</span>特质';
if (topDims[1][1] > 0) html += '和<span class="highlight">' + dimName2 + '</span>倾向';
html += '。这正是' + char.nickname + '最能与你产生共鸣的地方。</p>';

html += '<p>' + dimInfo[topDims[0][0]].desc + '。而' + char.nickname + '恰好拥有这种特质——' + char.bio.substring(0, 120) + '...</p>';

const charVal0 = char.dims[topDims[0][0]];
const charVal1 = char.dims[topDims[1][0]];

if (charVal0 >= 7) {
html += '<p>在<span class="accent-text">' + dimName1 + '</span>这个维度上，' + char.nickname + '的属性值高达' + charVal0 + '（满分10），与你的期待完美契合。' + dimInfo[topDims[0][0]].desc + '。</p>';
} else {
html += '<p>在<span class="accent-text">' + dimName1 + '</span>维度上，' + char.nickname + '虽然不是最典型的代表，但她独特的性格组合恰好能给你带来意想不到的互补感。</p>';
}

if (charVal1 >= 6) {
html += '<p>在<span class="accent-text">' + dimName2 + '</span>方面，你们同样有着很高的匹配度。这意味着你们的相处会是自然而舒服的——不需要刻意迁就，就能找到彼此都喜欢的节奏。</p>';
}

html += '<p>最重要的是，' + char.nickname + '的核心魅力在于：<span class="highlight">' + char.tags.slice(0, 3).join('、') + '</span>。这些特质与你内心深处对伴侣的期待高度一致。你们在一起，不会是单方面的付出或索取，而是两个灵魂在恰当的频率上相遇——' + char.nickname + '能懂你的' + dimName1 + '，你也能接住她的' + (charVal0 >= 7 ? dimName1 : dimName2) + '。</p>';

html += '<p>这段关系的模样大概是：' + getRelationshipDesc(topDims, char) + '</p>';

html += '</div>';
html += '</div>';

// Dimension bars
html += '<div class="result-section">';
html += '<div class="result-section-title">维度匹配详情</div>';
html += '<div class="dimension-bars">';
Object.keys(dimInfo).forEach(dim => {
const info = dimInfo[dim];
const userVal = Math.min(10, Math.round(userDims[dim] / 3));
const charVal = char.dims[dim];
html += '<div class="dim-bar">';
html += '<div class="dim-label">' + info.name + '</div>';
html += '<div class="dim-track"><div class="dim-fill" style="width:' + (charVal * 10) + '%;background:' + info.color + '"></div></div>';
html += '<div class="dim-value">' + charVal + '/10</div>';
html += '</div>';
});
html += '</div>';
html += '</div>';

// Character bio
html += '<div class="result-section">';
html += '<div class="result-section-title">角色简介</div>';
html += '<div class="result-bio">' + char.bio + '</div>';
html += '</div>';

// Appearance
html += '<div class="result-section">';
html += '<div class="result-section-title">外貌描述</div>';
html += '<div class="result-appearance">' + char.appearance + '</div>';
html += '</div>';

// Other matches
html += '<div class="result-section">';
html += '<div class="result-section-title">其他推荐角色</div>';
html += '<div class="other-matches">';
for (let i = 1; i < Math.min(5, top5.length); i++) {
const m = top5[i];
const c = m.char;
html += '<div class="other-match" onclick="showCharDetail(' + c.id + ')">';
html += '<div class="other-match-img"><img src="' + c.image + '" alt="' + c.name + '" onerror="this.style.display=\'none\'"></div>';
html += '<div class="other-match-info">';
html += '<div class="other-match-name">' + c.name + '</div>';
html += '<div class="other-match-series">' + c.series + '</div>';
html += '</div>';
html += '<div class="other-match-score">' + m.matchPercent + '%</div>';
html += '</div>';
}
html += '</div>';
html += '</div>';

// Share
html += '<div class="share-section">';
html += '<div class="share-title">分享你的结果</div>';
html += '<div class="share-text">我的命运之人是《' + char.series + '》的' + char.name + '！<br>契合度高达' + best.matchPercent + '%~<br>快来测测你的二次元老婆是谁吧！</div>';
html += '<button class="share-copy" onclick="copyResult(\'' + char.name + '\',' + best.matchPercent + ',\'' + char.series + '\')">复制结果</button>';
html += '</div>';

// Actions
html += '<div class="result-actions">';
html += '<button class="btn" onclick="startQuiz()">重新测试</button>';
html += '<button class="btn btn-secondary" onclick="showGallery()">角色图鉴</button>';
html += '</div>';

container.innerHTML = html;

// Animate dimension bars
setTimeout(() => {
document.querySelectorAll('.dim-fill').forEach(el => {
const w = el.style.width;
el.style.width = '0';
setTimeout(() => { el.style.width = w; }, 50);
});
}, 100);
}, 800);
}

function getRelationshipDesc(topDims, char) {
const dim1 = topDims[0][0];
if (dim1 === 'gentle') return '你们会在一个安静的夜晚相遇，她为你煮一碗热汤，你为她讲一个故事。不需要轰轰烈烈，细水长流就是最好的浪漫。';
if (dim1 === 'energy') return '你们会在一场冒险中相遇，她拉着你冲向未知，你追着她跑遍世界。每一天都是新的故事，每一刻都值得回味。';
if (dim1 === 'independent') return '你们会在一个不经意的瞬间被彼此吸引——不是因为需要对方，而是因为欣赏对方。各自精彩，在一起时更加闪耀。';
if (dim1 === 'tsundere') return '你们的日常大概是：她嘴上说"谁要等你"，手上却在给你倒热茶。你说"真不可爱"，心里却甜得不行。';
if (dim1 === 'loyal') return '她会在你最脆弱的时候出现，不是说什么惊天动地的话，只是安静地站在你身边。而你知道，她会一直在。';
if (dim1 === 'playful') return '你们的相处模式大概是：互相起奇怪的外号，在街上突然开始赛跑，深夜一起看恐怖电影然后一起尖叫。';
if (dim1 === 'elegant') return '你们会在一个下雨的午后相遇，她安静地看书，你安静地看她。不需要太多言语，一个眼神就够了。';
if (dim1 === 'mature') return '你们会在一次深谈中发现彼此是同类——不浮躁、不矫情，用理性经营感情，用深沉包裹热爱。';
return '你们的相遇是命运的安排，相处是灵魂的共鸣。';
}

function copyResult(name, percent, series) {
const text = '我的二次元老婆匹配结果：' + name + '（' + series + '）契合度' + percent + '%！快来测测你的命运之人是谁~';
navigator.clipboard.writeText(text).then(() => {
alert('结果已复制到剪贴板！');
}).catch(() => {
alert('复制失败，请手动选择文本复制。');
});
}

// ===== GALLERY =====
function showGallery() {
showPage('page-gallery');
renderGallery('all');
}

function renderGallery(filter) {
const grid = document.getElementById('galleryGrid');
grid.innerHTML = '';
const filtered = filter === 'all' ? characters : characters.filter(c => c.type === filter);
filtered.forEach(char => {
const item = document.createElement('div');
item.className = 'gallery-item';
item.onclick = () => showCharDetail(char.id);
let imgHtml = '<img src="' + char.image + '" alt="' + char.name + '" onerror="this.style.display=\'none\';this.parentElement.classList.add(\'img-fallback\');this.parentElement.textContent=\'图片加载失败\'">';
item.innerHTML = '<div class="gallery-item-img">' + imgHtml + '</div>'
+ '<div class="gallery-item-info">'
+ '<div class="gallery-item-name">' + char.name + '</div>'
+ '<div class="gallery-item-series">' + char.series + '</div>'
+ '</div>';
grid.appendChild(item);
});
}

function filterGallery(type, btn) {
document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
btn.classList.add('active');
renderGallery(type);
}

function showCharDetail(id) {
const char = characters.find(c => c.id === id);
if (!char) return;
const modal = document.getElementById('modal');
const content = document.getElementById('modalContent');
let html = '<div class="modal-img"><img src="' + char.image + '" alt="' + char.name + '" onerror="this.style.display=\'none\';this.parentElement.classList.add(\'img-fallback\');this.parentElement.textContent=\'图片加载失败\'"></div>';
html += '<div class="modal-body">';
html += '<div style="font-size:20px;font-weight:800;color:var(--text-bright);margin-bottom:4px">' + char.name + '</div>';
html += '<div style="font-size:13px;color:var(--text-dim);margin-bottom:4px">' + char.nameJp + '</div>';
html += '<div style="font-size:13px;color:var(--pink);margin-bottom:12px">出自《' + char.series + '》</div>';
html += '<div style="display:flex;flex-wrap:wrap;gap:6px;margin-bottom:16px">';
char.tags.forEach(t => { html += '<span class="result-tag">' + t + '</span>'; });
html += '</div>';
html += '<div style="font-size:14px;line-height:1.7;color:var(--text)">' + char.bio + '</div>';
html += '<div style="font-size:13px;line-height:1.6;color:var(--text-dim);margin-top:12px;padding-top:12px;border-top:1px solid rgba(168,85,247,0.15)">' + char.appearance + '</div>';
html += '</div>';
content.innerHTML = html;
modal.classList.add('active');
}

function closeModal() {
document.getElementById('modal').classList.remove('active');
}

// ===== PARTICLE BACKGROUND =====
function initParticles() {
const canvas = document.getElementById('particles');
const ctx = canvas.getContext('2d');
let particles = [];
let w, h;

function resize() {
w = canvas.width = window.innerWidth;
h = canvas.height = window.innerHeight;
}
resize();
window.addEventListener('resize', resize);

function createParticles() {
particles = [];
const count = Math.min(40, Math.floor(w * h / 25000));
for (let i = 0; i < count; i++) {
particles.push({
x: Math.random() * w,
y: Math.random() * h,
vx: (Math.random() - 0.5) * 0.3,
vy: (Math.random() - 0.5) * 0.3,
r: Math.random() * 2 + 0.5,
alpha: Math.random() * 0.3 + 0.1,
hue: Math.random() < 0.5 ? 330 : 270
});
}
}
createParticles();

function animate() {
ctx.clearRect(0, 0, w, h);
particles.forEach(p => {
p.x += p.vx;
p.y += p.vy;
if (p.x < 0) p.x = w;
if (p.x > w) p.x = 0;
if (p.y < 0) p.y = h;
if (p.y > h) p.y = 0;
ctx.beginPath();
ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
ctx.fillStyle = 'hsla(' + p.hue + ',70%,70%,' + p.alpha + ')';
ctx.fill();
});
requestAnimationFrame(animate);
}
animate();
}

initParticles();
</script>
</body>
</html>
"""

with open(OUT, 'a', encoding='utf-8') as f:
    f.write(JS)

print(f"JavaScript + HTML close appended. File size: {os.path.getsize(OUT)} bytes")
