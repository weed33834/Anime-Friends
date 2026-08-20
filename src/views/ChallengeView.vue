<template>
  <div class="container challenge">
    <!-- ============ 选关 ============ -->
    <template v-if="store.phase === 'select'">
      <h1 class="section-title">挑战<span class="grad">模式</span>
        <span class="stars-total muted">★ {{ store.totalStars() }} / {{ TOTAL_LEVELS * 3 }}</span>
      </h1>
      <p class="muted ch-sub">每关挑战一位角色：答题越契合她，得分越高，得星解锁下一关。</p>

      <div class="level-grid">
        <button v-for="n in TOTAL_LEVELS" :key="n" class="level-card card"
          :class="n <= store.maxUnlocked ? 'open' : 'locked'"
          :disabled="n > store.maxUnlocked" @click="store.startLevel(n)">
          <div class="lv-no">第 {{ n }} 关</div>
          <template v-if="n <= store.maxUnlocked">
            <div class="lv-avatar" :style="{ backgroundImage: `url(${charImg(targetForLevel(n))})` }"></div>
            <div class="lv-name">{{ targetForLevel(n).name }}</div>
            <div class="lv-stars">{{ starStr(n) }}</div>
          </template>
          <div v-else class="lv-lock">🔒 未解锁</div>
        </button>
      </div>

      <div class="daily-card card" :class="{ done: store.dailyDone }"
        @click="!store.dailyDone && store.startDaily()">
        <div class="daily-left">
          <div class="daily-tag">每日挑战</div>
          <div class="daily-name">{{ store.dailyDone ? '今日已完成' : '今日目标：' + dailyTarget().name }}</div>
        </div>
        <div class="daily-right">{{ store.dailyDone ? '得分 ' + store.dailyScore + '%' : '开始 →' }}</div>
      </div>

      <button class="btn btn-ghost btn-sm reset-btn" @click="store.resetProgress()">重置进度</button>
    </template>

    <!-- ============ 答题 ============ -->
    <template v-else-if="store.phase === 'play'">
      <div class="ch-target card">
        <div class="ct-avatar" :style="{ backgroundImage: `url(${charImg(store.target)})` }"></div>
        <div class="ct-info">
          <div class="ct-hint">本关目标</div>
          <div class="ct-name">{{ store.target.name }}</div>
          <div class="ct-series muted">{{ store.target.series }}</div>
          <div class="ct-tip muted">答题越契合她，得分越高（满分 100）</div>
        </div>
      </div>

      <div class="ch-progress">
        <div class="ch-progress-track"><div class="ch-progress-bar" :style="{ width: pct + '%' }"></div></div>
        <div class="ch-progress-text muted">{{ store.idx + 1 }} / {{ store.qOrder.length }}</div>
      </div>

      <div class="ch-card card">
        <div class="ch-q muted">第 {{ store.idx + 1 }} 题</div>
        <h2 class="ch-title">{{ q.q }}</h2>
        <div class="ch-opts">
          <button v-for="(o, oi) in q.o" :key="oi" class="ch-opt"
            :class="{ picked: store.answers[store.idx] === oi }" @click="store.answer(oi)">
            <span class="opt-tag">{{ optTag[oi] }}</span><span>{{ o.t }}</span>
          </button>
        </div>
      </div>

      <div class="ch-actions">
        <button class="btn btn-ghost" :disabled="store.idx === 0" @click="store.prev()">上一题</button>
        <button class="btn btn-primary" :disabled="!canNext" @click="store.next()">
          {{ store.idx === store.qOrder.length - 1 ? '结算' : '下一题' }}</button>
      </div>
    </template>

    <!-- ============ 结算 ============ -->
    <template v-else>
      <div class="result-top card">
        <div class="rt-score">
          <div class="rt-num">{{ store.result.score }}<span>%</span></div>
          <MatchLevelBadge :score="store.result.score" />
          <div class="rt-stars">{{ '★'.repeat(store.result.stars) }}{{ '☆'.repeat(3 - store.result.stars) }}</div>
        </div>
        <div class="rt-info">
          <div class="muted">{{ store.result.daily ? '每日挑战' : '第 ' + store.result.level + ' 关' }} · 目标角色</div>
          <h2 class="rt-name">{{ store.result.target.name }}</h2>
          <div class="muted rt-series">{{ store.result.target.series }}</div>
          <p class="rt-quote">「{{ store.result.target.favor_quote }}」</p>
          <div v-if="store.result.passed" class="rt-pass">🎉 过关！已解锁下一关</div>
          <div v-else-if="!store.result.daily" class="rt-fail">差一点点，再试一次就能过关</div>
        </div>
        <div class="rt-avatar" :style="{ backgroundImage: `url(${charImg(store.result.target)})` }"></div>
      </div>

      <div class="card rt-radar">
        <h3 class="panel-title">{{ store.result.target.name }} 的性格雷达</h3>
        <RadarChart :values="store.result.target.traits" :show-values="true" :title="store.result.target.name" />
      </div>

      <div class="rt-actions">
        <button v-if="store.result.passed && !store.result.daily && store.result.level < TOTAL_LEVELS"
          class="btn btn-primary" @click="store.startLevel(store.result.level + 1)">下一关</button>
        <button class="btn btn-ghost" @click="retry">重试本关</button>
        <button class="btn btn-ghost" @click="store.backToSelect()">返回选关</button>
        <button class="btn btn-ghost" @click="openShare">生成分享卡</button>
      </div>
    </template>

    <!-- 分享卡弹层 -->
    <div v-if="showShare" class="share-mask" @click.self="showShare = false">
      <div class="share-modal card">
        <canvas ref="canvasEl" class="share-canvas"></canvas>
        <div class="share-actions">
          <button class="btn btn-primary btn-sm" @click="downloadShare">保存图片</button>
          <button class="btn btn-ghost btn-sm" @click="showShare = false">关闭</button>
        </div>
        <p v-if="!shareOk" class="muted share-tip">图片加载失败，分享卡降级为文字战绩</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, nextTick } from 'vue'
import { useChallengeStore } from '@/stores/challenge'
import { questions } from '@/utils/match'
import { targetForLevel, dailyTarget, TOTAL_LEVELS, drawShareCard } from '@/utils/challenge'
import MatchLevelBadge from '@/components/MatchLevelBadge.vue'
import RadarChart from '@/components/RadarChart.vue'

const store = useChallengeStore()
const optTag = ['A', 'B', 'C', 'D', 'E']

const q = computed(() => questions[store.qOrder[store.idx]])
const pct = computed(() => Math.round(((store.idx + 1) / store.qOrder.length) * 100))
const canNext = computed(() => store.answers[store.idx] !== null)

function charImg(c) { return import.meta.env.BASE_URL + c.image }
function starStr(n) {
  const b = store.best[String(n)]
  return b ? '★'.repeat(b.stars) + '☆'.repeat(3 - b.stars) + ' ' + b.score + '%' : '未挑战'
}
function retry() {
  if (store.result.daily) store.startDaily()
  else store.startLevel(store.result.level)
}

// 分享卡
const showShare = ref(false)
const shareOk = ref(true)
const canvasEl = ref(null)
async function openShare() {
  showShare.value = true
  shareOk.value = true
  await nextTick()
  const r = store.result
  shareOk.value = await drawShareCard(canvasEl.value, {
    title: r.daily ? '每日挑战战绩' : '第 ' + r.level + ' 关战绩',
    score: r.score,
    stars: r.stars,
    charName: r.target.name,
    line: r.target.favor_quote,
    imgUrl: charImg(r.target)
  })
}
function downloadShare() {
  const c = canvasEl.value
  if (!c) return
  const a = document.createElement('a')
  a.download = 'anime-friends-challenge.png'
  a.href = c.toDataURL('image/png')
  a.click()
}
</script>

<style scoped>
.challenge { max-width: 900px; }
.stars-total { font-size: 15px; font-weight: 600; margin-left: 14px; color: #ffd76a; }
.ch-sub { margin: -6px 0 22px; font-size: 14px; }

/* 选关 */
.level-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(180px, 1fr)); gap: 16px; margin-bottom: 20px; }
.level-card { padding: 18px; text-align: center; cursor: pointer; transition: transform var(--tr-fast), border-color var(--tr-fast); }
.level-card.open:hover { transform: translateY(-4px); border-color: rgba(124,92,255,0.5); }
.level-card.locked { opacity: 0.5; cursor: not-allowed; }
.lv-no { font-size: 13px; color: var(--text-dim); margin-bottom: 10px; }
.lv-avatar { width: 84px; height: 104px; margin: 0 auto 10px; border-radius: 12px; background-size: cover; background-position: center 22%; border: 2px solid rgba(255,110,199,0.4); }
.lv-name { font-size: 15px; font-weight: 700; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.lv-stars { font-size: 12px; color: #ffd76a; margin-top: 4px; }
.lv-lock { padding: 30px 0; font-size: 15px; color: var(--text-dim); }

.daily-card { display: flex; align-items: center; justify-content: space-between; padding: 18px 22px; cursor: pointer; margin-bottom: 18px; transition: border-color var(--tr-fast); }
.daily-card:not(.done):hover { border-color: rgba(124,92,255,0.5); }
.daily-card.done { opacity: 0.7; cursor: default; }
.daily-tag { display: inline-block; padding: 3px 10px; border-radius: 999px; background: var(--grad); color: #fff; font-size: 12px; font-weight: 700; margin-bottom: 6px; }
.daily-name { font-size: 15px; font-weight: 700; }
.daily-right { font-size: 15px; font-weight: 700; color: var(--primary-2); }
.reset-btn { margin: 4px auto 0; display: block; }

/* 答题 */
.ch-target { display: flex; align-items: center; gap: 16px; padding: 16px 18px; margin-bottom: 18px; }
.ct-avatar { width: 64px; height: 80px; border-radius: 10px; background-size: cover; background-position: center 22%; flex: none; border: 2px solid rgba(255,110,199,0.4); }
.ct-hint { font-size: 12px; color: var(--primary-2); letter-spacing: 1px; }
.ct-name { font-size: 20px; font-weight: 800; }
.ct-series { font-size: 12px; }
.ct-tip { font-size: 12px; margin-top: 4px; }

.ch-progress { display: flex; align-items: center; gap: 12px; margin-bottom: 14px; }
.ch-progress-track { flex: 1; height: 8px; border-radius: 99px; background: var(--bg-2); overflow: hidden; }
.ch-progress-bar { height: 100%; background: var(--grad); border-radius: 99px; transition: width var(--tr-mid); }
.ch-progress-text { font-size: 13px; min-width: 54px; text-align: right; }

.ch-card { padding: 26px 22px; }
.ch-q { font-size: 13px; letter-spacing: 2px; margin-bottom: 12px; }
.ch-title { font-size: 20px; line-height: 1.6; margin-bottom: 22px; }
.ch-opts { display: flex; flex-direction: column; gap: 10px; }
.ch-opt { display: flex; align-items: center; gap: 12px; text-align: left; padding: 13px 16px; border-radius: var(--r-sm); font-size: 14.5px; line-height: 1.55; background: var(--bg-card); border: 1px solid var(--border); transition: all var(--tr-fast); }
.ch-opt:hover { background: var(--bg-card-hover); border-color: rgba(124,92,255,0.5); }
.ch-opt.picked { background: rgba(124,92,255,0.22); border-color: var(--primary); box-shadow: 0 0 0 1px var(--primary) inset; }
.opt-tag { flex: 0 0 24px; height: 24px; display: inline-flex; align-items: center; justify-content: center; border-radius: 7px; font-size: 12px; font-weight: 700; background: var(--bg-2); }

.ch-actions { display: flex; justify-content: space-between; margin-top: 20px; }
.ch-actions .btn:disabled { opacity: 0.4; cursor: not-allowed; transform: none; }

/* 结算 */
.result-top { display: flex; gap: 20px; align-items: center; padding: 24px; margin-bottom: 18px; }
.rt-score { text-align: center; flex: none; width: 160px; }
.rt-num { font-size: 52px; font-weight: 900; background: var(--grad); -webkit-background-clip: text; background-clip: text; color: transparent; }
.rt-num span { font-size: 24px; }
.rt-stars { color: #ffd76a; font-size: 22px; margin-top: 6px; letter-spacing: 2px; }
.rt-info { flex: 1; min-width: 0; }
.rt-name { font-size: 26px; font-weight: 900; margin: 4px 0 2px; }
.rt-series { font-size: 13px; }
.rt-quote { font-size: 13px; color: var(--text-dim); font-style: italic; margin: 10px 0; }
.rt-pass { font-size: 14px; color: var(--ok); font-weight: 700; }
.rt-fail { font-size: 14px; color: var(--warn); font-weight: 700; }
.rt-avatar { width: 110px; height: 144px; border-radius: var(--r-md); background-size: cover; background-position: center 22%; flex: none; border: 2px solid rgba(255,110,199,0.4); box-shadow: var(--shadow); }
.rt-radar { padding: 20px; margin-bottom: 18px; }
.panel-title { font-size: 17px; font-weight: 700; margin-bottom: 14px; text-align: center; }
.rt-actions { display: flex; gap: 12px; justify-content: center; flex-wrap: wrap; }

/* 分享卡 */
.share-mask { position: fixed; inset: 0; background: rgba(0,0,0,0.7); display: flex; align-items: center; justify-content: center; z-index: 50; padding: 20px; }
.share-modal { padding: 18px; max-width: 92vw; text-align: center; }
.share-canvas { width: 300px; max-width: 80vw; height: auto; border-radius: 12px; }
.share-actions { display: flex; gap: 10px; justify-content: center; margin-top: 14px; }
.share-tip { font-size: 12px; margin-top: 8px; }

@media (max-width: 640px) {
  .result-top { flex-direction: column-reverse; text-align: center; }
  .rt-score { width: auto; }
  .rt-avatar { width: 92px; height: 120px; }
}
</style>
