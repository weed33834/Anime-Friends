<template>
  <canvas ref="cv" class="particle-bg"></canvas>
</template>

<script setup>
import { onMounted, onBeforeUnmount, ref } from 'vue'

const cv = ref(null)
let raf = 0
let particles = []

function resize(canvas) {
  canvas.width = window.innerWidth
  canvas.height = window.innerHeight
}

function tick(canvas) {
  const ctx = canvas.getContext('2d')
  ctx.clearRect(0, 0, canvas.width, canvas.height)
  for (const p of particles) {
    p.x += p.vx; p.y += p.vy
    if (p.x < 0 || p.x > canvas.width) p.vx *= -1
    if (p.y < 0 || p.y > canvas.height) p.vy *= -1
    ctx.beginPath()
    ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2)
    ctx.fillStyle = p.color
    ctx.globalAlpha = p.a
    ctx.fill()
  }
  // 连线
  ctx.globalAlpha = 0.5
  for (let i = 0; i < particles.length; i++) {
    for (let j = i + 1; j < particles.length; j++) {
      const a = particles[i], b = particles[j]
      const dx = a.x - b.x, dy = a.y - b.y
      const dist = Math.sqrt(dx * dx + dy * dy)
      if (dist < 130) {
        ctx.strokeStyle = 'rgba(124,92,255,0.18)'
        ctx.lineWidth = 1
        ctx.beginPath(); ctx.moveTo(a.x, a.y); ctx.lineTo(b.x, b.y); ctx.stroke()
      }
    }
  }
  ctx.globalAlpha = 1
  raf = requestAnimationFrame(() => tick(canvas))
}

onMounted(() => {
  const canvas = cv.value
  resize(canvas)
  particles = Array.from({ length: 46 }, () => ({
    x: Math.random() * canvas.width,
    y: Math.random() * canvas.height,
    vx: (Math.random() - 0.5) * 0.5,
    vy: (Math.random() - 0.5) * 0.5,
    r: 1 + Math.random() * 2.2,
    a: 0.25 + Math.random() * 0.5,
    color: Math.random() > 0.5 ? 'rgba(124,92,255,0.8)' : 'rgba(255,110,199,0.7)'
  }))
  window.addEventListener('resize', () => resize(canvas))
  raf = requestAnimationFrame(() => tick(canvas))
})

onBeforeUnmount(() => {
  cancelAnimationFrame(raf)
  window.removeEventListener('resize', resize)
})
</script>

<style scoped>
.particle-bg {
  position: fixed; inset: 0; z-index: 0;
  pointer-events: none;
}
</style>
