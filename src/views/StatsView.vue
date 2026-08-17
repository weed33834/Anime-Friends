<template>
  <div class="container">
    <h1 class="section-title">数据<span class="grad">统计</span></h1>

    <div class="stats-grid">
      <div class="card stat-card">
        <div class="stat-num">{{ characters.length }}</div>
        <div class="stat-label">收录角色</div>
      </div>
      <div class="card stat-card">
        <div class="stat-num">{{ questions.length }}</div>
        <div class="stat-label">测试题目</div>
      </div>
      <div class="card stat-card">
        <div class="stat-num">{{ dimensions.length }}</div>
        <div class="stat-label">人格维度</div>
      </div>
      <div class="card stat-card">
        <div class="stat-num">{{ seriesCount }}</div>
        <div class="stat-label">覆盖作品</div>
      </div>
    </div>

    <h2 class="sub-title">人格维度 <span class="muted">均值 / 标准差</span></h2>
    <div class="table-wrap card">
      <table class="tbl">
        <thead>
          <tr><th>维度</th><th>均值</th><th>标准差</th><th>分布</th></tr>
        </thead>
        <tbody>
          <tr v-for="(d, i) in dimensions" :key="d.key">
            <td class="td-name">{{ d.label }}</td>
            <td>{{ GM[i].toFixed(1) }}</td>
            <td>{{ GS[i].toFixed(1) }}</td>
            <td class="td-dist"><i :style="{ width: distWidth(i) }"></i></td>
          </tr>
        </tbody>
      </table>
    </div>

    <h2 class="sub-title">作品分布</h2>
    <div class="table-wrap card">
      <table class="tbl">
        <thead>
          <tr><th>作品</th><th>角色数</th><th>平均特质</th></tr>
        </thead>
        <tbody>
          <tr v-for="s in seriesStats" :key="s.series">
            <td class="td-name">{{ s.series }}</td>
            <td>{{ s.count }}</td>
            <td>{{ s.avg.toFixed(1) }}</td>
          </tr>
        </tbody>
      </table>
    </div>

    <h2 class="sub-title">浏览热度 <span class="muted">Top 5</span></h2>
    <div class="hot-row card" v-for="(it, i) in hotTop" :key="it.c.id">
      <span class="hot-rank">{{ i + 1 }}</span>
      <span class="hot-name">{{ it.c.name }}</span>
      <span class="muted">{{ it.c.series }}</span>
      <span class="hot-count">{{ it.n }} 次</span>
    </div>
    <p v-if="!hotTop.length" class="muted empty">暂无浏览数据</p>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { characters, dimensions, GM, GS } from '@/utils/match'
import { loadStats } from '@/utils/stats'

const seriesCount = computed(() => new Set(characters.map(c => c.series)).size)

const seriesStats = computed(() => {
  const map = {}
  characters.forEach(c => {
    if (!map[c.series]) map[c.series] = { series: c.series, count: 0, sum: 0 }
    map[c.series].count++
    map[c.series].sum += c.traits.reduce((a, b) => a + b, 0) / c.traits.length
  })
  return Object.values(map).map(s => ({ ...s, avg: s.sum / s.count })).sort((a, b) => b.count - a.count)
})

const hotTop = computed(() => {
  const s = loadStats()
  return Object.entries(s)
    .map(([id, n]) => { const c = characters.find(x => x.id === id); return c ? { c, n } : null })
    .filter(Boolean).sort((a, b) => b.n - a.n).slice(0, 5)
})

function distWidth(i) {
  const sd = GS[i] || 1
  return Math.max(6, Math.min(100, Math.round(sd * 2.4))) + '%'
}
</script>

<style scoped>
.stats-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 14px; margin-bottom: 26px; }
.stat-card { text-align: center; padding: 20px 10px; }
.stat-num { font-size: 34px; font-weight: 900; background: linear-gradient(135deg, var(--primary), var(--primary-2)); -webkit-background-clip: text; background-clip: text; color: transparent; }
.stat-label { margin-top: 4px; font-size: 13px; color: var(--text-muted); }
.sub-title { margin: 30px 0 14px; font-size: 18px; }
.sub-title .muted { font-size: 13px; font-weight: 400; }
.table-wrap { overflow-x: auto; padding: 4px 6px; }
.tbl { width: 100%; border-collapse: collapse; font-size: 14px; }
.tbl th { text-align: left; padding: 10px 14px; color: var(--text-muted); font-weight: 600; font-size: 12px; border-bottom: 1px solid var(--border); white-space: nowrap; }
.tbl td { padding: 10px 14px; border-bottom: 1px solid rgba(255,255,255,0.05); white-space: nowrap; }
.td-name { font-weight: 700; }
.td-dist { width: 120px; }
.td-dist i { display: block; height: 6px; border-radius: 999px; background: linear-gradient(90deg, var(--primary), var(--primary-2)); }
.hot-row { display: flex; align-items: center; gap: 14px; padding: 12px 16px; margin-bottom: 10px; }
.hot-rank { width: 28px; height: 28px; flex: none; display: flex; align-items: center; justify-content: center; border-radius: 8px; background: var(--bg-2); color: var(--primary-2); font-weight: 800; }
.hot-name { font-weight: 700; flex: 1; }
.hot-count { color: var(--text-muted); font-size: 13px; }
.empty { text-align: center; padding: 30px 0; }
</style>
