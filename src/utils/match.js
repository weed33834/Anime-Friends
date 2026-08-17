import { dimensions } from '@/data/dimensions'
import characters from '@/data/characters.json'
import questions from '@/data/questions.json'

// 防 XSS 转义
export function esc(s) {
  return String(s == null ? '' : s)
    .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;').replace(/'/g, '&#39;')
}

// 洗牌（Fisher-Yates）
export function shuffle(arr) {
  const a = arr.slice()
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1))
    ;[a[i], a[j]] = [a[j], a[i]]
  }
  return a
}

// 各维度最大理论得分（按选项上限 ×2 累加，用于归一化）
export const MAXD = (() => {
  const m = {}
  dimensions.forEach(d => { m[d.key] = 0 })
  questions.forEach(q => {
    dimensions.forEach(d => {
      let mx = 0
      q.o.forEach(o => { if (o.s && o.s[d.key] !== undefined && o.s[d.key] > mx) mx = o.s[d.key] })
      m[d.key] += mx * 2
    })
  })
  return m
})()

// 由答题结果计算用户 12 维画像
export function calcUser(ans) {
  const v = {}
  dimensions.forEach(d => { v[d.key] = 50 })
  questions.forEach((q, i) => {
    if (ans[i] === null || ans[i] === undefined) return
    const o = q.o[ans[i]]
    if (!o || !o.s) return
    for (const k in o.s) {
      if (v[k] !== undefined) v[k] += o.s[k] * 2
    }
  })
  dimensions.forEach(d => {
    const maxD = MAXD[d.key] || 50
    v[d.key] = Math.max(0, Math.min(100, 50 + (v[d.key] - 50) / maxD * 50))
  })
  return v
}

// 各角色维度均值/标准差（z-score 标准化基线）
export const GM = []
export const GS = []
dimensions.forEach((d, j) => {
  let s = 0
  characters.forEach(c => { s += c.traits[j] })
  const m = s / characters.length
  GM.push(m)
  let sd = 0
  characters.forEach(c => { sd += (c.traits[j] - m) * (c.traits[j] - m) })
  GS.push(Math.sqrt(sd / characters.length) || 1)
})

function cosSim(a, b) {
  let d = 0, nA = 0, nB = 0
  dimensions.forEach(dim => {
    const av = a[dim.key], bv = b[dim.key]
    d += av * bv; nA += av * av; nB += bv * bv
  })
  return d / (Math.sqrt(nA) * Math.sqrt(nB) || 1)
}

export function eucDist(a, b) {
  let s = 0
  dimensions.forEach(d => { const diff = a[d.key] - b[d.key]; s += diff * diff })
  return Math.sqrt(s)
}

// 匹配分：z-score 标准化后 0.6 余弦 + 0.4 欧氏
export function matchScore(u, c) {
  const cv = {}, uv = {}
  dimensions.forEach((d, i) => {
    cv[d.key] = (c.traits[i] - GM[i]) / GS[i]
    uv[d.key] = (u[d.key] - GM[i]) / GS[i]
  })
  const cs = cosSim(uv, cv)
  const ed = eucDist(uv, cv)
  const ne = Math.max(0, Math.min(1, 1 - ed / (Math.sqrt(dimensions.length) * 6)))
  return Math.round((0.6 * cs + 0.4 * ne) * 100)
}

// 契合度等级：由组件 MatchLevelBadge 独立实现（避免重复维护）
// 全量排名
export function rankAll(u) {
  return characters
    .map(c => ({ ...c, ms: matchScore(u, c) }))
    .sort((a, b) => b.ms - a.ms)
}

export { dimensions, characters, questions }
