<template>
  <div class="container result" v-if="top">
    <div class="result-top">
      <div class="result-info">
        <div class="result-series">{{ top.series }}</div>
        <h2 class="result-name">{{ top.name }}</h2>
        <div class="result-match">
          契合度 {{ top.ms }}% <MatchLevelBadge :score="top.ms" />
        </div>
        <div class="result-tags">
          <span v-for="t in tagList" :key="t" class="pill">{{ t }}</span>
        </div>
        <p class="result-quote">「{{ top.quote }}」</p>
      </div>
      <div class="result-avatar" :style="{ backgroundImage: `url(${top.image})` }"></div>
    </div>

    <div class="result-grid">
      <section class="card panel">
        <h3 class="panel-title">你的性格画像</h3>
        <RadarChart :values="userVals" :show-values="true" />
        <div class="panel-row">
          <span>最强特质</span><strong>{{ strongest.label }} {{ Math.round(strongest.val) }}</strong>
        </div>
      </section>
      <section class="card panel">
        <h3 class="panel-title">角色档案</h3>
        <div class="profile">
          <p>{{ top.description }}</p>
          <div class="profile-meta">
            <div><span class="muted">CV</span>{{ top.cv }}</div>
            <div><span class="muted">生日</span>{{ top.birthday }}</div>
          </div>
          <div class="profile-quote muted">{{ top.catchphrase }}</div>
          <p class="profile-favor">{{ top.favor_quote }}</p>
        </div>
      </section>
    </div>

    <section class="card panel">
      <h3 class="panel-title">潜在情敌分析</h3>
      <p class="muted panel-sub">以下角色也与你高度契合，可能会成为你追求 {{ top.name }} 的竞争对手：</p>
      <div class="rival-grid">
        <div v-for="r in rivals" :key="r.id" class="rival card" @click="goDetail(r)">
          <div class="rival-avatar" :style="{ backgroundImage: `url(${r.image})` }"></div>
          <div class="rival-name">{{ r.name }}</div>
          <div class="rival-score">契合 {{ r.ms }}%</div>
        </div>
      </div>
    </section>

    <section class="card panel">
      <h3 class="panel-title">完整契合榜</h3>
      <div class="rank-list">
        <div v-for="(c, i) in all" :key="c.id" class="rank-row" @click="goDetail(c)">
          <span class="rank-no">{{ i + 1 }}</span>
          <span class="rank-name">{{ c.name }}</span>
          <div class="rank-bar"><div class="rank-fill" :style="{ width: c.ms + '%' }"></div></div>
          <span class="rank-ms">{{ c.ms }}%</span>
        </div>
      </div>
    </section>

    <div class="result-actions">
      <button class="btn btn-primary" @click="retry">重新测试</button>
      <button class="btn btn-ghost" @click="go('/gallery')">浏览全部角色</button>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRouter } from 'vue-router'
import { useQuizStore } from '@/stores/quiz'
import { calcUser, matchScore, rankAll, questions, characters, dimensions } from '@/utils/match'
import { bumpStat } from '@/utils/stats'
import RadarChart from '@/components/RadarChart.vue'
import MatchLevelBadge from '@/components/MatchLevelBadge.vue'

const router = useRouter()
const store = useQuizStore()
const go = (p) => router.push(p)

// 未完成测试直接访问结果页时，先尝试从本地存储恢复；恢复失败才重开
if (!store.finished && !store.restore()) {
  store.start()
  router.replace('/quiz')
}
const goDetail = (c) => router.push({ path: '/compare', query: { id: c.id } })

const userVals = computed(() => {
  const u = calcUser(store.rawAnswers())
  return dimensions.map(d => u[d.key])
})
const all = computed(() => rankAll(calcUser(store.rawAnswers())))
const top = computed(() => all.value[0])
const rivals = computed(() => all.value.slice(1, 4))
const tagList = computed(() => (top.value.tags || '').split(',').slice(0, 4))
const strongest = computed(() => {
  const u = calcUser(store.rawAnswers())
  return dimensions.map(d => ({ label: d.label, val: u[d.key] })).sort((a, b) => b.val - a.val)[0]
})

// 浏览计数
bumpStat(top.value?.id)
function retry() { store.start(); router.push('/quiz') }
</script>

<style scoped>
.result { max-width: 900px; }
.result-top { display: flex; gap: 24px; align-items: center; background: var(--bg-card); border: 1px solid var(--border); border-radius: var(--r-lg); padding: 26px; margin-bottom: 18px; }
.result-avatar { width: 168px; height: 224px; border-radius: var(--r-md); background-size: cover; background-position: center 22%; box-shadow: var(--shadow); flex-shrink: 0; border: 2px solid rgba(255,110,199,0.4); }
.result-info { flex: 1; }
.result-series { font-size: 13px; color: var(--primary-2); letter-spacing: 1px; margin-bottom: 6px; }
.result-name { font-size: 32px; font-weight: 900; margin-bottom: 8px; }
.result-match { display: flex; align-items: center; gap: 10px; font-size: 16px; font-weight: 700; color: var(--primary-2); margin-bottom: 12px; }
.result-tags { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 14px; }
.result-quote { font-size: 14px; color: var(--text-dim); font-style: italic; }
.result-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 18px; margin-bottom: 18px; }
.panel { padding: 22px; }
.panel-title { font-size: 18px; font-weight: 700; margin-bottom: 16px; }
.panel-sub { font-size: 13px; margin: -8px 0 14px; }
.panel-row { display: flex; justify-content: space-between; margin-top: 12px; font-size: 14px; }
.profile p { font-size: 14px; line-height: 1.85; color: var(--text-dim); }
.profile-meta { display: flex; gap: 22px; margin: 14px 0; font-size: 14px; }
.profile-meta span { margin-right: 6px; font-size: 12px; }
.profile-quote { font-size: 13px; padding: 10px 14px; border-left: 3px solid var(--primary); background: rgba(124,92,255,0.1); border-radius: 0 10px 10px 0; margin-bottom: 12px; }
.profile-favor { font-size: 13.5px; line-height: 1.8; color: #e8dcff; }
.rival-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; }
.rival { padding: 12px; text-align: center; cursor: pointer; transition: transform var(--tr-fast); }
.rival:hover { transform: translateY(-4px); }
.rival-avatar { width: 74px; height: 96px; margin: 0 auto 8px; border-radius: 10px; background-size: cover; background-position: center 22%; }
.rival-name { font-size: 14px; font-weight: 700; }
.rival-score { font-size: 12px; color: var(--primary-2); margin-top: 3px; }
.rank-list { display: flex; flex-direction: column; gap: 6px; max-height: 420px; overflow-y: auto; padding-right: 6px; }
.rank-row { display: flex; align-items: center; gap: 12px; padding: 8px 10px; border-radius: 10px; cursor: pointer; transition: background var(--tr-fast); }
.rank-row:hover { background: var(--bg-card-hover); }
.rank-no { width: 26px; font-weight: 800; color: var(--text-dim); font-size: 13px; }
.rank-name { width: 120px; font-size: 14px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.rank-bar { flex: 1; height: 8px; border-radius: 99px; background: rgba(255,255,255,0.08); overflow: hidden; }
.rank-fill { height: 100%; background: var(--grad); border-radius: 99px; }
.rank-ms { width: 48px; text-align: right; font-size: 13px; font-weight: 700; color: var(--primary-2); }
.result-actions { display: flex; gap: 12px; justify-content: center; margin-top: 22px; flex-wrap: wrap; }
@media (max-width: 700px) {
  .result-top { flex-direction: column-reverse; }
  .result-grid, .rival-grid { grid-template-columns: 1fr; }
  .result-avatar { width: 130px; height: 172px; }
}
</style>
