// 挑战模式核心逻辑：关卡定义、计分、每日挑战、分享卡绘制
import { characters, questions, dimensions } from '@/utils/match'

export const TOTAL_LEVELS = 8

// 每关题目数：4 题起，每关 +1，封顶 10
export function questionsForLevel(level) {
  return Math.min(4 + (level - 1), 10)
}

// 每关目标角色：确定性映射（level*11 % 88，88=8*11，保证 8 关各不相同）
export function targetForLevel(level) {
  return characters[(level * 11) % characters.length]
}

// 可复现伪随机（mulberry32），保证同一关每次抽题一致、公平可重复
function mulberry32(seed) {
  let a = seed >>> 0
  return function () {
    a |= 0; a = (a + 0x6d2b79f5) | 0
    let t = Math.imul(a ^ (a >>> 15), 1 | a)
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296
  }
}
function seededShuffle(arr, seed) {
  const rnd = mulberry32(seed)
  const a = arr.slice()
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(rnd() * (i + 1))
    ;[a[i], a[j]] = [a[j], a[i]]
  }
  return a
}

// 取本关题目子集（按关卡 seed 确定性抽取）
export function levelQuestions(level) {
  const n = questionsForLevel(level)
  return seededShuffle([...Array(questions.length).keys()], level * 1000 + 7).slice(0, n)
}

// 预计算每个角色每道题的「理想选项」：与其 12 维特质最一致的选项下标。
// 挑战得分 = 玩家答对的题占比，直接、可通关、技巧含量高。
const IDEAL = {}
characters.forEach(c => {
  IDEAL[c.id] = questions.map(q => {
    let best = 0, bs = -1e9
    q.o.forEach((o, oi) => {
      if (!o.s) return
      let sc = 0
      dimensions.forEach((d, i) => { sc += (o.s[d] || 0) * c.traits[i] })
      if (sc > bs) { bs = sc; best = oi }
    })
    return best
  })
})

// 计分：玩家在本题集中答对「角色理想选项」的比例（0-100）
export function scoreLevel(rawAnswers, target) {
  const key = IDEAL[target.id]
  let hit = 0, total = 0
  rawAnswers.forEach((ans, qi) => {
    if (ans == null) return
    total++
    if (ans === key[qi]) hit++
  })
  return total === 0 ? 0 : Math.round((hit / total) * 100)
}

// 星级：≥85 三星，≥70 二星，≥55 一星（过关），否则 0
export function starsFor(score) {
  if (score >= 85) return 3
  if (score >= 70) return 2
  if (score >= 55) return 1
  return 0
}

// 每日挑战：按当天日期做种子
export function todayStr() {
  const d = new Date()
  return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}`
}
function hashStr(s) {
  let h = 2166136261
  for (let i = 0; i < s.length; i++) { h ^= s.charCodeAt(i); h = Math.imul(h, 16777619) }
  return h >>> 0
}
export function dailyTarget() {
  return characters[hashStr('daily-' + todayStr()) % characters.length]
}
export function dailyQuestions() {
  return seededShuffle([...Array(questions.length).keys()], hashStr('dq-' + todayStr())).slice(0, 5)
}

// 分享卡：在给定 canvas 上绘制战绩图，返回 Promise<boolean>（图片是否成功绘制）
export function drawShareCard(canvas, { title, score, stars, charName, line, imgUrl }) {
  return new Promise((resolve) => {
    const W = 600, H = 800
    canvas.width = W; canvas.height = H
    const ctx = canvas.getContext('2d')
    const g = ctx.createLinearGradient(0, 0, W, H)
    g.addColorStop(0, '#1a1140'); g.addColorStop(1, '#0b1020')
    ctx.fillStyle = g; ctx.fillRect(0, 0, W, H)

    function drawText() {
      ctx.textAlign = 'center'
      ctx.fillStyle = '#ffffff'; ctx.font = 'bold 38px sans-serif'
      ctx.fillText(title, W / 2, 460)
      ctx.fillStyle = '#ff6ec7'; ctx.font = 'bold 92px sans-serif'
      ctx.fillText(score + '%', W / 2, 575)
      ctx.fillStyle = '#ffd76a'; ctx.font = '44px sans-serif'
      ctx.fillText('★'.repeat(stars) + '☆'.repeat(3 - stars), W / 2, 638)
      ctx.fillStyle = 'rgba(242,244,255,0.9)'; ctx.font = '24px sans-serif'
      ctx.fillText(charName, W / 2, 690)
      ctx.fillStyle = 'rgba(242,244,255,0.62)'; ctx.font = '18px sans-serif'
      wrapText(line || '', W / 2, 728, W - 90, 28)
      ctx.fillStyle = 'rgba(242,244,255,0.4)'; ctx.font = '16px sans-serif'
      ctx.fillText('Anime Friends · 娱乐向性格匹配', W / 2, 782)
    }
    function wrapText(text, x, y, maxW, lh) {
      const chars = (text || '').split('')
      let line = '', yy = y
      for (const ch of chars) {
        if (ctx.measureText(line + ch).width > maxW) { ctx.fillText(line, x, yy); line = ch; yy += lh }
        else line += ch
      }
      ctx.fillText(line, x, yy)
    }

    const r = 150, cx = W / 2, cy = 250
    const img = new Image()
    img.crossOrigin = 'anonymous'
    img.onload = () => {
      ctx.save()
      ctx.beginPath(); ctx.arc(cx, cy, r, 0, Math.PI * 2); ctx.closePath(); ctx.clip()
      ctx.drawImage(img, cx - r, cy - r * 1.2, r * 2, r * 2.4)
      ctx.restore()
      drawText(); resolve(true)
    }
    img.onerror = () => { drawText(); resolve(false) }
    img.src = imgUrl
  })
}
