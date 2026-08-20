import { defineStore } from 'pinia'
import { ref } from 'vue'
import { questions } from '@/utils/match'
import {
  TOTAL_LEVELS, targetForLevel, levelQuestions, scoreLevel, starsFor,
  todayStr, dailyTarget, dailyQuestions
} from '@/utils/challenge'

const KEY = 'af_challenge_v1'
function load() {
  try { return JSON.parse(localStorage.getItem(KEY) || 'null') } catch (e) { return null }
}
function save(s) {
  try { localStorage.setItem(KEY, JSON.stringify(s)) } catch (e) {}
}

export const useChallengeStore = defineStore('challenge', () => {
  // —— 持久化进度 ——
  const prog = load() || {}
  const maxUnlocked = ref(prog.maxUnlocked || 1)
  const best = ref(prog.best || {})            // { [level]: { score, stars } }
  const dailyDate = ref(prog.dailyDate || '')
  const dailyDone = ref(prog.dailyDate === todayStr())
  const dailyScore = ref(prog.dailyScore || 0)

  function persist() {
    save({ maxUnlocked: maxUnlocked.value, best: best.value, dailyDate: dailyDate.value, dailyScore: dailyScore.value })
  }

  // —— 当前对局（不持久化，答完即结算） ——
  const mode = ref(null)        // 'level' | 'daily'
  const levelNum = ref(1)
  const qOrder = ref([])        // 本局题目原始下标
  const target = ref(null)      // 目标角色
  const answers = ref([])       // 本局每题所选选项下标
  const idx = ref(0)
  const phase = ref('select')    // select | play | result
  const result = ref(null)       // { score, stars, passed, target, daily, level }

  function startLevel(n) {
    if (n > maxUnlocked.value) return
    mode.value = 'level'; levelNum.value = n
    target.value = targetForLevel(n)
    qOrder.value = levelQuestions(n)
    answers.value = Array(qOrder.value.length).fill(null)
    idx.value = 0; phase.value = 'play'; result.value = null
  }
  function startDaily() {
    mode.value = 'daily'; levelNum.value = 0
    target.value = dailyTarget()
    qOrder.value = dailyQuestions()
    answers.value = Array(qOrder.value.length).fill(null)
    idx.value = 0; phase.value = 'play'; result.value = null
  }
  function answer(optIdx) { answers.value[idx.value] = optIdx }
  function next() {
    if (idx.value < qOrder.value.length - 1) { idx.value++; return false }
    return finish()
  }
  function prev() { if (idx.value > 0) idx.value-- }
  function goto(i) { idx.value = i }

  function rawAnswers() {
    const raw = Array(questions.length).fill(null)
    qOrder.value.forEach((qIdx, i) => { raw[qIdx] = answers.value[i] })
    return raw
  }

  function finish() {
    const score = scoreLevel(rawAnswers(), target.value)
    const stars = starsFor(score)
    const isDaily = mode.value === 'daily'
    const passed = !isDaily && stars >= 1
    if (isDaily) {
      dailyDate.value = todayStr(); dailyDone.value = true; dailyScore.value = score
    } else {
      const key = String(levelNum.value)
      const prevBest = best.value[key]
      if (!prevBest || score > prevBest.score) best.value[key] = { score, stars }
      else if (stars > prevBest.stars) best.value[key] = { score: prevBest.score, stars }
      // 过关且非最后一关，则解锁下一关
      if (passed && levelNum.value < TOTAL_LEVELS && levelNum.value + 1 > maxUnlocked.value) {
        maxUnlocked.value = levelNum.value + 1
      }
    }
    result.value = { score, stars, passed, target: target.value, daily: isDaily, level: levelNum.value }
    phase.value = 'result'
    persist()
    return true
  }

  function backToSelect() { phase.value = 'select'; mode.value = null; result.value = null }
  function resetProgress() {
    maxUnlocked.value = 1; best.value = {}; dailyDate.value = ''; dailyDone.value = false; dailyScore.value = 0
    persist()
  }
  function totalStars() {
    return Object.values(best.value).reduce((a, b) => a + (b.stars || 0), 0)
  }

  return {
    maxUnlocked, best, dailyDone, dailyScore, mode, levelNum, qOrder, target, answers, idx, phase, result,
    startLevel, startDaily, answer, next, prev, goto, finish, backToSelect, resetProgress, totalStars
  }
})
