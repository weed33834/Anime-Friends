import { defineStore } from 'pinia'
import { ref } from 'vue'
import { questions, shuffle } from '@/utils/match'

export const useQuizStore = defineStore('quiz', () => {
  const order = ref([])        // 打乱后的题目索引
  const answers = ref([])      // 每题所选选项下标（null=未答）
  const idx = ref(0)           // 当前题号（0-based）
  const finished = ref(false)

  function start() {
    const n = questions.length
    order.value = shuffle([...Array(n).keys()])
    answers.value = Array(n).fill(null)
    idx.value = 0
    finished.value = false
  }

  function answer(optIdx) {
    answers.value[idx.value] = optIdx
  }

  function next() {
    if (idx.value < questions.length - 1) { idx.value++; return false }
    finished.value = true
    return true
  }

  function prev() {
    if (idx.value > 0) idx.value--
  }

  function goto(i) { idx.value = i }

  // 还原为按原始顺序排列的答案数组
  function rawAnswers() {
    const raw = Array(questions.length).fill(null)
    order.value.forEach((qIdx, i) => { raw[qIdx] = answers.value[i] })
    return raw
  }

  return { order, answers, idx, finished, start, answer, next, prev, goto, rawAnswers }
})
