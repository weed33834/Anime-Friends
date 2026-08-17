<template>
  <div class="radar-wrap">
    <svg :viewBox="viewBox" class="radar" role="img" :aria-label="title">
      <!-- 网格 -->
      <g v-for="level in levels" :key="level">
        <polygon
          :points="polyPoints(level)"
          fill="none" stroke="rgba(255,255,255,0.10)" stroke-width="1"
        />
      </g>
      <!-- 轴线 -->
      <line
        v-for="(d, i) in dims" :key="d.key"
        :x1="cx" :y1="cy" :x2="pt(d, 100).x" :y2="pt(d, 100).y"
        stroke="rgba(255,255,255,0.08)"
      />
      <!-- 数据多边形 -->
      <polygon :points="dataPoints" fill="rgba(124,92,255,0.30)" stroke="#8b6cff" stroke-width="2" />
      <!-- 顶点 -->
      <circle v-for="(d, i) in dims" :key="'v' + d.key"
        :cx="pt(d, values[i]).x" :cy="pt(d, values[i]).y" r="3" fill="#ff6ec7" />
      <!-- 维度标签 -->
      <text
        v-for="(d, i) in dims" :key="'t' + d.key"
        :x="pt(d, 118).x" :y="pt(d, 118).y" text-anchor="middle" dominant-baseline="middle"
        class="radar-label"
      >{{ d.label }}</text>
    </svg>
    <div v-if="showValues" class="radar-values">
      <span v-for="(d, i) in dims" :key="d.key" class="rv-pill">{{ d.label }} {{ Math.round(values[i]) }}</span>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { dimensions } from '@/data/dimensions'

const props = defineProps({
  values: { type: Array, required: true },   // 与 dimensions 对齐的 12 个值
  size: { type: Number, default: 320 },
  showValues: { type: Boolean, default: false },
  title: { type: String, default: '' }
})

const cx = 160, cy = 150, r = 100
const viewBox = '0 0 320 300'
const dims = dimensions
const levels = [25, 50, 75, 100]

function pt(d, val) {
  const i = dimensions.findIndex(x => x.key === d.key)
  const ang = (Math.PI * 2 * i) / dimensions.length - Math.PI / 2
  return { x: cx + Math.cos(ang) * (r * val / 100), y: cy + Math.sin(ang) * (r * val / 100) }
}
function polyPoints(level) {
  return dimensions.map(d => { const p = pt(d, level); return p.x + ',' + p.y }).join(' ')
}
const dataPoints = computed(() => {
  return dimensions.map((d, i) => { const p = pt(d, props.values[i] ?? 0); return p.x + ',' + p.y }).join(' ')
})
</script>

<style scoped>
.radar-wrap { display: flex; flex-direction: column; align-items: center; gap: 10px; }
.radar { width: 100%; max-width: 360px; }
.radar-label { fill: rgba(242,244,255,0.75); font-size: 11px; }
.radar-values { display: flex; flex-wrap: wrap; gap: 6px; justify-content: center; }
.rv-pill { font-size: 11px; padding: 3px 8px; border-radius: 999px; background: rgba(124,92,255,0.15); border: 1px solid rgba(124,92,255,0.3); }
</style>
