<template>
  <div class="container">
    <h1 class="section-title">角色<span class="grad">榜单</span></h1>

    <div class="tab-bar">
      <button class="tab" :class="{ on: tab === 'hot' }" @click="tab = 'hot'">浏览热度</button>
      <button class="tab" :class="{ on: tab === 'dim' }" @click="tab = 'dim'">维度高分</button>
    </div>

    <!-- 浏览热度榜 -->
    <template v-if="tab === 'hot'">
      <p v-if="!hotList.length" class="muted empty">暂无浏览记录，去 <router-link to="/gallery" class="grad">图鉴</router-link> 逛逛吧</p>
      <div class="rank-list">
        <div v-for="(it, i) in hotList" :key="it.c.id" class="rank-row card" @click="open(it.c)">
          <div class="rank-no" :class="{ top: i < 3 }">{{ i + 1 }}</div>
          <div class="rank-img" :style="{ backgroundImage: `url(${it.c.image})` }"></div>
          <div class="rank-info">
            <div class="rank-name">{{ it.c.name }} <span class="muted">{{ it.c.series }}</span></div>
            <div class="rank-bar"><i :style="{ width: barWidth(it.n) }"></i></div>
          </div>
          <div class="rank-count">{{ it.n }} 次</div>
        </div>
      </div>
    </template>

    <!-- 维度高分榜 -->
    <template v-else>
      <div class="dim-tools">
        <select v-model="dim" class="select">
          <option v-for="d in dimensions" :key="d.key" :value="d.key">{{ d.label }}</option>
        </select>
      </div>
      <div class="rank-list">
        <div v-for="(it, i) in dimList" :key="it.c.id" class="rank-row card" @click="open(it.c)">
          <div class="rank-no" :class="{ top: i < 3 }">{{ i + 1 }}</div>
          <div class="rank-img" :style="{ backgroundImage: `url(${it.c.image})` }"></div>
          <div class="rank-info">
            <div class="rank-name">{{ it.c.name }} <span class="muted">{{ it.c.series }}</span></div>
            <div class="dim-val">{{ dimLabel }} <b>{{ Math.round(it.v) }}</b></div>
          </div>
        </div>
      </div>
    </template>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { characters, dimensions } from '@/utils/match'
import { loadStats, bumpStat } from '@/utils/stats'

const router = useRouter()
const tab = ref('hot')
const dim = ref(dimensions[0].key)

const hotList = computed(() => {
  const s = loadStats()
  const arr = Object.entries(s).map(([id, n]) => {
    const c = characters.find(x => x.id === id)
    return c ? { c, n } : null
  }).filter(Boolean).sort((a, b) => b.n - a.n).slice(0, 20)
  return arr
})

const dimLabel = computed(() => dimensions.find(d => d.key === dim.value)?.label || '')

const dimList = computed(() => {
  const j = dimensions.findIndex(d => d.key === dim.value)
  return characters
    .map(c => ({ c, v: c.traits[j] }))
    .sort((a, b) => b.v - a.v)
    .slice(0, 10)
})

function barWidth(n) {
  const mx = hotList.value.length ? Math.max(...hotList.value.map(x => x.n)) : 1
  return Math.max(4, Math.round(n / mx * 100)) + '%'
}

function open(c) { bumpStat(c.id); router.push({ path: '/compare', query: { id: c.id } }) }
</script>

<style scoped>
.tab-bar { display: flex; gap: 10px; margin-bottom: 22px; }
.tab { padding: 9px 22px; border-radius: 999px; background: var(--bg-card); border: 1px solid var(--border); color: var(--text-muted); font-size: 14px; cursor: pointer; transition: all var(--tr-fast); }
.tab.on { background: linear-gradient(135deg, var(--primary), var(--primary-2)); color: #fff; border-color: transparent; box-shadow: 0 4px 18px rgba(124,92,255,0.35); }
.rank-list { display: flex; flex-direction: column; gap: 12px; }
.rank-row { display: flex; align-items: center; gap: 16px; padding: 12px 16px; cursor: pointer; transition: transform var(--tr-mid), border-color var(--tr-mid); }
.rank-row:hover { transform: translateX(4px); border-color: rgba(124,92,255,0.5); }
.rank-no { width: 34px; height: 34px; flex: none; display: flex; align-items: center; justify-content: center; border-radius: 10px; background: var(--bg-2); color: var(--text-muted); font-weight: 800; font-size: 15px; }
.rank-no.top { background: linear-gradient(135deg, #ffd76a, #ff8b3d); color: #1b1033; }
.rank-img { width: 56px; height: 56px; flex: none; border-radius: 12px; background-size: cover; background-position: center 22%; }
.rank-info { flex: 1; min-width: 0; }
.rank-name { font-weight: 700; font-size: 15px; margin-bottom: 7px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.rank-name .muted { font-weight: 400; font-size: 12px; }
.rank-bar { height: 6px; border-radius: 999px; background: var(--bg-2); overflow: hidden; }
.rank-bar i { display: block; height: 100%; border-radius: 999px; background: linear-gradient(90deg, var(--primary), var(--primary-2)); }
.rank-count { flex: none; font-size: 13px; color: var(--text-muted); }
.dim-tools { margin-bottom: 18px; }
.dim-val { font-size: 13px; color: var(--text-muted); }
.dim-val b { color: var(--primary-2); font-size: 15px; margin-left: 6px; }
.empty { text-align: center; padding: 60px 0; }
</style>
