<template>
  <div class="container">
    <h1 class="section-title">角色<span class="grad">图鉴</span> <span class="muted" style="font-size:15px">共 {{ filtered.length }} 位</span></h1>
    <div class="gallery-tools">
      <input v-model="kw" class="search" placeholder="搜索角色 / 作品 / 标签…" />
      <select v-model="series" class="select">
        <option value="">全部作品</option>
        <option v-for="s in seriesList" :key="s" :value="s">{{ s }}</option>
      </select>
    </div>
    <div class="gallery-grid">
      <CharacterCard v-for="c in filtered" :key="c.id" :c="c" @open="openDetail" />
    </div>
    <p v-if="!filtered.length" class="muted empty">没有匹配的角色</p>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { characters } from '@/utils/match'
import { bumpStat } from '@/utils/stats'
import CharacterCard from '@/components/CharacterCard.vue'

const router = useRouter()
const kw = ref('')
const series = ref('')
const seriesList = computed(() => [...new Set(characters.map(c => c.series))].sort())

const filtered = computed(() => {
  const k = kw.value.trim().toLowerCase()
  return characters.filter(c => {
    if (series.value && c.series !== series.value) return false
    if (!k) return true
    return [c.name, c.series, c.tags, c.description, c.cv].join(' ').toLowerCase().includes(k)
  })
})

function openDetail(c) { bumpStat(c.id); router.push({ path: '/compare', query: { id: c.id } }) }
</script>

<style scoped>
.gallery-tools { display: flex; gap: 12px; margin-bottom: 22px; flex-wrap: wrap; }
.search { flex: 1; min-width: 220px; padding: 11px 16px; border-radius: 999px; background: var(--bg-card); border: 1px solid var(--border); color: var(--text-main); font-size: 14px; outline: none; transition: border-color var(--tr-fast); }
.search:focus { border-color: var(--primary); }
.select { padding: 11px 16px; border-radius: 999px; background: var(--bg-card); border: 1px solid var(--border); color: var(--text-main); font-size: 14px; outline: none; cursor: pointer; }
.gallery-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(210px, 1fr)); gap: 18px; }
.empty { text-align: center; padding: 60px 0; }
</style>
