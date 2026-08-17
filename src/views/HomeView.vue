<template>
  <div class="container home">
    <section class="hero">
      <div class="home-badge">88位角色 · 12维性格 · 36道精选题</div>
      <h1 class="home-title">Anime<span class="grad"> Friends</span></h1>
      <p class="home-desc">
        穿越彩虹闪烁的次元之门，回答36道精心设计的性格测试题，我们将从88位人气galgame与动漫角色中，
        用余弦相似度混合欧氏距离算法，找到与你灵魂共鸣的她。
      </p>
      <div class="home-buttons">
        <button class="btn btn-primary" @click="goQuiz">开始测试</button>
        <button class="btn btn-ghost" @click="go('/gallery')">角色图鉴</button>
      </div>
      <div class="home-stats">
        <div class="home-stat" v-for="s in statCards" :key="s.label">
          <div class="home-stat-num">{{ s.num }}</div>
          <div class="home-stat-label">{{ s.label }}</div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRouter } from 'vue-router'
import { characters, questions } from '@/utils/match'
import { useQuizStore as useQuiz } from '@/stores/quiz'

const router = useRouter()
const go = (p) => router.push(p)
const goQuiz = () => { useQuiz().start(); router.push('/quiz') }
const seriesCount = computed(() => new Set(characters.map(c => c.series)).size)
const statCards = computed(() => [
  { num: characters.length, label: '人气角色' },
  { num: 12, label: '性格维度' },
  { num: questions.length, label: '精选题目' },
  { num: seriesCount.value, label: '收录作品' }
])
</script>

<style scoped>
.home { min-height: calc(100vh - 160px); display: flex; align-items: center; justify-content: center; text-align: center; }
.hero { max-width: 720px; padding: 30px 0; }
.home-badge { display: inline-block; padding: 6px 16px; border-radius: 999px; font-size: 13px; letter-spacing: 0.5px; color: #c9b8ff; background: rgba(124,92,255,0.14); border: 1px solid rgba(124,92,255,0.4); margin-bottom: 22px; }
.home-title { font-size: clamp(44px, 8vw, 76px); font-weight: 900; line-height: 1.12; letter-spacing: 1px; }
.home-title .grad { background: var(--grad); -webkit-background-clip: text; background-clip: text; color: transparent; filter: drop-shadow(0 6px 24px rgba(124,92,255,0.35)); }
.home-desc { margin: 20px auto 30px; font-size: 15px; line-height: 1.85; color: var(--text-dim); max-width: 560px; }
.home-buttons { display: flex; gap: 14px; justify-content: center; flex-wrap: wrap; }
.home-stats { display: flex; justify-content: center; gap: 34px; margin-top: 44px; flex-wrap: wrap; }
.home-stat-num { font-size: 30px; font-weight: 800; background: var(--grad); -webkit-background-clip: text; background-clip: text; color: transparent; }
.home-stat-label { font-size: 13px; color: var(--text-dim); margin-top: 4px; }
</style>
