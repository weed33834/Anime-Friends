<template>
  <div class="container quiz">
    <template v-if="!store.finished">
      <div class="quiz-top">
        <div class="quiz-progress">
          <div class="quiz-progress-track"><div class="quiz-progress-bar" :style="{ width: pct + '%' }"></div></div>
          <div class="quiz-progress-text muted">{{ store.idx + 1 }} / {{ store.order.length }}</div>
        </div>
        <div class="quiz-grid">
          <button
            v-for="(_, i) in store.order" :key="i"
            class="quiz-dot" :class="{ done: store.answers[i] !== null, cur: i === store.idx }"
            @click="store.goto(i)"
          >{{ i + 1 }}</button>
        </div>
      </div>

      <transition name="page" mode="out-in" :key="store.idx">
        <div class="quiz-card card">
          <div class="quiz-q muted">第 {{ store.idx + 1 }} 题</div>
          <h2 class="quiz-title">{{ q.q }}</h2>
          <div class="quiz-opts">
            <button
              v-for="(o, oi) in q.o" :key="oi"
              class="quiz-opt" :class="{ picked: store.answers[store.idx] === oi }"
              @click="store.answer(oi)"
            >
              <span class="opt-tag">{{ optTag[oi] }}</span>
              <span>{{ o.t }}</span>
            </button>
          </div>
        </div>
      </transition>

      <div class="quiz-actions">
        <button class="btn btn-ghost" :disabled="store.idx === 0" @click="store.prev()">上一题</button>
        <button class="btn btn-primary" :disabled="!canNext" @click="doNext">{{ store.idx === store.order.length - 1 ? '查看结果' : '下一题' }}</button>
      </div>
    </template>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRouter } from 'vue-router'
import { useQuizStore } from '@/stores/quiz'
import { questions } from '@/utils/match'

const store = useQuizStore()
const router = useRouter()
if (!store.order.length) store.start()

const q = computed(() => questions[store.order[store.idx]])
const pct = computed(() => Math.round(((store.idx + 1) / store.order.length) * 100))
const canNext = computed(() => store.answers[store.idx] !== null)
const optTag = ['A', 'B', 'C', 'D', 'E']

function doNext() {
  const done = store.next()
  if (done) router.push('/result')
}
</script>

<style scoped>
.quiz { max-width: 760px; }
.quiz-top { margin-bottom: 20px; }
.quiz-progress { display: flex; align-items: center; gap: 12px; margin-bottom: 14px; }
.quiz-progress-track { flex: 1; height: 8px; border-radius: 99px; background: rgba(255,255,255,0.1); overflow: hidden; }
.quiz-progress-bar { height: 100%; background: var(--grad); border-radius: 99px; transition: width var(--tr-mid); }
.quiz-progress-text { font-size: 13px; min-width: 54px; text-align: right; }
.quiz-grid { display: flex; flex-wrap: wrap; gap: 6px; }
.quiz-dot { width: 28px; height: 28px; border-radius: 8px; font-size: 12px; background: rgba(255,255,255,0.06); border: 1px solid var(--border); transition: all var(--tr-fast); }
.quiz-dot.done { background: rgba(124,92,255,0.35); border-color: rgba(124,92,255,0.6); }
.quiz-dot.cur { background: var(--grad); border-color: transparent; box-shadow: 0 0 12px rgba(255,110,199,0.4); }
.quiz-card { padding: 30px 26px; }
.quiz-q { font-size: 13px; letter-spacing: 2px; margin-bottom: 12px; }
.quiz-title { font-size: 21px; line-height: 1.6; margin-bottom: 24px; }
.quiz-opts { display: flex; flex-direction: column; gap: 10px; }
.quiz-opt {
  display: flex; align-items: center; gap: 12px; text-align: left;
  padding: 13px 16px; border-radius: var(--r-sm); font-size: 14.5px; line-height: 1.55;
  background: rgba(255,255,255,0.05); border: 1px solid var(--border);
  transition: all var(--tr-fast);
}
.quiz-opt:hover { background: var(--bg-card-hover); border-color: rgba(124,92,255,0.5); }
.quiz-opt.picked { background: rgba(124,92,255,0.22); border-color: var(--primary); box-shadow: 0 0 0 1px var(--primary) inset; }
.opt-tag { flex: 0 0 24px; height: 24px; display: inline-flex; align-items: center; justify-content: center; border-radius: 7px; font-size: 12px; font-weight: 700; background: rgba(255,255,255,0.1); }
.quiz-opt.picked .opt-tag { background: var(--grad); color: #fff; }
.quiz-actions { display: flex; justify-content: space-between; margin-top: 20px; }
.quiz-actions .btn:disabled { opacity: 0.4; cursor: not-allowed; transform: none; }
@media (max-width: 640px) {
  .quiz-card { padding: 22px 16px; }
  .quiz-title { font-size: 17px; }
}
</style>
