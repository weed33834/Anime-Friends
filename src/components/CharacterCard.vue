<template>
  <div class="char-card card" @click="$emit('open', c)">
    <div class="cc-img" :style="{ backgroundImage: bg }"></div>
    <div class="cc-body">
      <div class="cc-head">
        <div class="cc-name">{{ c.name }}</div>
        <div class="cc-series muted">{{ c.series }}</div>
      </div>
      <div class="cc-tags">
        <span v-for="t in tagList" :key="t" class="pill">{{ t }}</span>
      </div>
      <div class="cc-foot">
        <span v-if="c.ms !== undefined" class="cc-ms">契合 {{ c.ms }}%</span>
        <MatchLevelBadge v-if="c.ms !== undefined" :score="c.ms" />
        <span v-else class="cc-view muted">查看详情</span>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import MatchLevelBadge from './MatchLevelBadge.vue'

const props = defineProps({ c: { type: Object, required: true } })
defineEmits(['open'])
const tagList = computed(() => (props.c.tags || '').split(',').slice(0, 3))
const bg = computed(() => `url(${props.c.image})`)
</script>

<style scoped>
.char-card { overflow: hidden; cursor: pointer; transition: transform var(--tr-mid), box-shadow var(--tr-mid), border-color var(--tr-mid); }
.char-card:hover { transform: translateY(-6px); box-shadow: var(--shadow); border-color: rgba(124,92,255,0.5); }
.cc-img { height: 200px; background-size: cover; background-position: center 22%; }
.cc-body { padding: 12px 14px 14px; }
.cc-head { display: flex; justify-content: space-between; align-items: baseline; gap: 8px; }
.cc-name { font-size: 16px; font-weight: 700; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.cc-series { font-size: 12px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.cc-tags { display: flex; flex-wrap: wrap; gap: 6px; margin: 8px 0 10px; }
.cc-foot { display: flex; justify-content: space-between; align-items: center; }
.cc-ms { font-size: 13px; font-weight: 700; color: var(--primary-2); }
.cc-view { font-size: 12px; }
</style>
