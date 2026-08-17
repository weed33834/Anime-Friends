<template>
  <span class="level-badge" :class="'lv-' + tier">{{ label }}</span>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({ score: { type: Number, required: true } })
const tier = computed(() => props.score >= 85 ? 4 : props.score >= 70 ? 3 : props.score >= 55 ? 2 : 1)
const label = computed(() => ({ 1: '命运交错', 2: '颇有缘分', 3: '高度契合', 4: '灵魂共鸣' }[tier.value]))
</script>

<style scoped>
.level-badge {
  display: inline-block; padding: 3px 10px; border-radius: 999px;
  font-size: 12px; font-weight: 600;
}
.lv-1 { background: rgba(255,92,122,0.16); color: #ff8fa3; border: 1px solid rgba(255,92,122,0.4); }
.lv-2 { background: rgba(255,180,84,0.14); color: #ffca80; border: 1px solid rgba(255,180,84,0.4); }
.lv-3 { background: rgba(61,220,151,0.14); color: #7be8b9; border: 1px solid rgba(61,220,151,0.4); }
.lv-4 { background: linear-gradient(135deg, rgba(124,92,255,0.3), rgba(255,110,199,0.3)); color: #fff; border: 1px solid rgba(255,110,199,0.55); box-shadow: 0 0 14px rgba(124,92,255,0.35); }
</style>
