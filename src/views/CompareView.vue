<template>
  <div class="container">
    <h1 class="section-title">角色<span class="grad">对比</span></h1>

    <div class="pick-bar">
      <button class="arrow" @click="shift(-1)">‹</button>
      <select class="select" :value="cur.id" @change="pick($event.target.value)">
        <option v-for="c in characters" :key="c.id" :value="c.id">{{ c.name }} · {{ c.series }}</option>
      </select>
      <button class="arrow" @click="shift(1)">›</button>
    </div>

    <div class="detail-grid">
      <div class="card detail-card">
        <div class="detail-img" :style="{ backgroundImage: `url(${cur.image})` }"></div>
        <div class="detail-body">
          <div class="detail-name">{{ cur.name }}</div>
          <div class="muted">{{ cur.series }} · CV {{ cur.cv }}</div>
          <div class="detail-tags">
            <span v-for="t in tagList" :key="t" class="pill">{{ t }}</span>
          </div>
          <p class="detail-desc">{{ cur.description }}</p>
        </div>
      </div>

      <div class="card radar-card">
        <h3 class="radar-title">{{ cur.name }} 的<span class="grad">人格雷达</span></h3>
        <RadarChart :values="cur.traits" :show-values="true" :title="cur.name" />
      </div>
    </div>

    <!-- 与"你"对比 -->
    <template v-if="myTraits">
      <h2 class="sub-title">与「你」的<span class="grad">契合度</span></h2>
      <div class="match-panel card">
        <div class="match-score">
          <div class="ms-num">{{ matchMs }}</div>
          <MatchLevelBadge :score="matchMs" />
          <div class="muted" style="margin-top:6px">z-score 标准化匹配分</div>
        </div>
        <div class="match-radar">
          <RadarChart :values="myTraits" :show-values="false" title="你的画像" />
        </div>
        <div class="match-meta">
          <div class="meta-row"><span class="muted">欧氏距离</span><b>{{ myDist.toFixed(2) }}</b></div>
          <div class="meta-row"><span class="muted">最高契合</span><b class="grad">{{ topMs }}</b></div>
        </div>
      </div>

      <h2 class="sub-title">你的<span class="grad">亲密伙伴</span> <span class="muted">欧氏距离最近 Top 5</span></h2>
      <div class="friend-list">
        <div v-for="(it, i) in friends" :key="it.c.id" class="friend-row card" @click="router.push({ path: '/compare', query: { id: it.c.id } })">
          <span class="friend-rank">{{ i + 1 }}</span>
          <div class="friend-img" :style="{ backgroundImage: `url(${it.c.image})` }"></div>
          <div class="friend-name">{{ it.c.name }} <span class="muted">{{ it.c.series }}</span></div>
          <span class="friend-dist">距离 {{ it.d.toFixed(2) }}</span>
        </div>
      </div>
    </template>
    <div v-else class="card cta-card">
      <p class="muted">完成 <router-link to="/quiz" class="grad">人格测试</router-link> 后，即可查看与角色的契合度、欧氏距离与你的亲密伙伴 Top 5。</p>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { characters, dimensions, calcUser, matchScore, eucDist } from '@/utils/match'
import { useQuizStore } from '@/stores/quiz'
import { bumpStat } from '@/utils/stats'
import RadarChart from '@/components/RadarChart.vue'
import MatchLevelBadge from '@/components/MatchLevelBadge.vue'

const route = useRoute()
const router = useRouter()
const quiz = useQuizStore()

const id = computed(() => route.query.id || characters[0].id)
const cur = computed(() => characters.find(c => c.id === id.value) || characters[0])
const tagList = computed(() => (cur.value.tags || '').split(',').slice(0, 4))

const myTraits = computed(() => {
  if (!quiz.finished) return null
  const u = calcUser(quiz.rawAnswers())
  return dimensions.map(d => u[d.key])
})
const myUser = computed(() => {
  if (!quiz.finished) return null
  return calcUser(quiz.rawAnswers())
})

const matchMs = computed(() => myUser.value ? matchScore(myUser.value, cur.value) : 0)
const myDist = computed(() => {
  if (!myUser.value) return 0
  const a = traitsObj(myUser.value)
  const b = traitsObj(cur.value)
  return eucDist(a, b)
})

const friends = computed(() => {
  if (!myUser.value) return []
  return characters
    .map(c => ({ c, d: eucDist(traitsObj(myUser.value), traitsObj(c)) }))
    .sort((a, b) => a.d - b.d)
    .slice(0, 5)
})

const topMs = computed(() => {
  if (!myUser.value) return '-'
  return Math.max(...characters.map(c => matchScore(myUser.value, c))) + '%'
})

function traitsObj(c) {
  const o = {}
  dimensions.forEach((d, i) => { o[d.key] = c.traits[i] })
  return o
}

function pick(v) { bumpStat(v); router.push({ path: '/compare', query: { id: v } }) }
function shift(delta) {
  const i = characters.findIndex(c => c.id === id.value)
  const next = characters[(i + delta + characters.length) % characters.length]
  bumpStat(next.id)
  router.push({ path: '/compare', query: { id: next.id } })
}
</script>

<style scoped>
.pick-bar { display: flex; align-items: center; gap: 12px; margin-bottom: 20px; }
.pick-bar .select { flex: 1; }
.arrow { width: 40px; height: 40px; border-radius: 12px; background: var(--bg-card); border: 1px solid var(--border); color: var(--text-main); font-size: 20px; cursor: pointer; transition: border-color var(--tr-fast); }
.arrow:hover { border-color: var(--primary); }
.detail-grid { display: grid; grid-template-columns: 340px 1fr; gap: 18px; margin-bottom: 8px; }
@media (max-width: 860px) { .detail-grid { grid-template-columns: 1fr; } }
.detail-card { overflow: hidden; }
.detail-img { height: 320px; background-size: cover; background-position: center 22%; }
.detail-body { padding: 18px 20px; }
.detail-name { font-size: 24px; font-weight: 900; margin-bottom: 4px; }
.detail-tags { display: flex; flex-wrap: wrap; gap: 6px; margin: 12px 0; }
.detail-desc { font-size: 14px; line-height: 1.7; color: var(--text-muted); margin: 0; }
.radar-card { padding: 22px 20px; display: flex; flex-direction: column; justify-content: center; }
.radar-title { margin: 0 0 14px; font-size: 17px; }
.sub-title { margin: 30px 0 14px; font-size: 18px; }
.sub-title .muted { font-size: 13px; font-weight: 400; }
.match-panel { display: grid; grid-template-columns: 200px 1fr 200px; gap: 20px; align-items: center; padding: 24px; }
@media (max-width: 860px) { .match-panel { grid-template-columns: 1fr; text-align: center; } }
.match-score { text-align: center; }
.ms-num { font-size: 52px; font-weight: 900; background: linear-gradient(135deg, var(--primary), var(--primary-2)); -webkit-background-clip: text; background-clip: text; color: transparent; margin-bottom: 10px; }
.match-radar { min-width: 0; }
.match-meta { display: flex; flex-direction: column; gap: 14px; font-size: 14px; }
.meta-row { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px dashed var(--border); padding-bottom: 8px; }
.meta-row b { font-size: 16px; }
.friend-list { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 12px; }
.friend-row { display: flex; align-items: center; gap: 12px; padding: 10px 14px; cursor: pointer; transition: border-color var(--tr-mid); }
.friend-row:hover { border-color: rgba(124,92,255,0.5); }
.friend-rank { width: 26px; height: 26px; flex: none; display: flex; align-items: center; justify-content: center; border-radius: 8px; background: var(--bg-2); color: var(--primary-2); font-weight: 800; font-size: 13px; }
.friend-img { width: 44px; height: 44px; flex: none; border-radius: 10px; background-size: cover; background-position: center 22%; }
.friend-name { flex: 1; font-weight: 700; font-size: 14px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.friend-name .muted { font-weight: 400; font-size: 11px; }
.friend-dist { flex: none; font-size: 12px; color: var(--text-muted); }
.cta-card { padding: 30px; text-align: center; }
</style>
