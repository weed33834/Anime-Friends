import { defineStore } from 'pinia'
import { ref } from 'vue'
import { questions, shuffle } from '@/utils/match'

const KEY = 'af_quiz_v1'

function load() {
  try { return JSON.parse(localStorage.getItem(KEY) || 'null') } catch (e) { return null }
}
function save(state) {
  try { localStorage.setItem(KEY, JSON.stringify(state)) } catch (e) {}
}

export const useQuizStore = defineStore('quiz', () => {
  const order = ref([])        // 打乱后的题目索引
  const answers = ref([])      // 每题所选选项下标（null=未答）
  const idx = ref(0)           // 当前题号（0-based）
  const finished = ref(false)

  // 每次状态变化都落盘，刷新/分享链接后不丢结果
  function persist() {
    save({ order: order.value, answers: answers.value, idx: idx.value, finished: finished.value })
  }

  function start() {
    const n = questions.length
    order.value = shuffle([...Array(n).keys()])
    answers.value = Array(n).fill(null)
    idx.value = 0
    finished.value = false
    persist()
  }

  // 从本地存储恢复（用于刷新 / 直接进入结果页）
  function restore() {
    const s = load()
    if (!s || !Array.isArray(s.order) || s.order.length !== questions.length) return false
    order.value = s.order
    answers.value = s.answers && s.answers.length === questions.length ? s.answers : Array(questions.length).fill(null)
    idx.value = s.idx || 0
    finished.value = !!s.finished
    return true
  }

  function answer(optIdx) {
    answers.value[idx.value] = optIdx
    persist()
  }

  function next() {
    if (idx.value < questions.length - 1) { idx.value++; persist(); return false }
    finished.value = true
    persist()
    return true
  }

  function prev() {
    if (idx.value > 0) { idx.value--; persist() }
  }

  function goto(i) { idx.value = i; persist() }

  // 还原为按原始顺序排列的答案数组
  function rawAnswers() {
    const raw = Array(questions.length).fill(null)
    order.value.forEach((qIdx, i) => { raw[qIdx] = answers.value[i] })
    return raw
  }

  return { order, answers, idx, finished, start, restore, answer, next, prev, goto, rawAnswers }
})
