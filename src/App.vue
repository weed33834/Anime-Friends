<template>
  <ParticleBg />
  <header class="app-header">
    <div class="container header-inner">
      <router-link to="/" class="brand">Anime <span class="grad">Friends</span></router-link>
      <nav class="nav">
        <router-link to="/quiz" class="nav-link">开始测试</router-link>
        <router-link to="/gallery" class="nav-link">角色图鉴</router-link>
        <router-link to="/ranking" class="nav-link">人气排行</router-link>
        <router-link to="/stats" class="nav-link">测试统计</router-link>
      </nav>
    </div>
  </header>
  <main class="app-main">
    <router-view v-slot="{ Component }">
      <transition name="page" mode="out-in">
        <component :is="Component" />
      </transition>
    </router-view>
  </main>
</template>

<script setup>
import ParticleBg from '@/components/ParticleBg.vue'
</script>

<style scoped>
.app-header { position: sticky; top: 0; z-index: 20; backdrop-filter: blur(14px); background: rgba(11,16,32,0.72); border-bottom: 1px solid var(--border); }
.header-inner { display: flex; align-items: center; justify-content: space-between; height: 62px; }
.brand { font-size: 20px; font-weight: 800; letter-spacing: 0.3px; }
.brand .grad { background: var(--grad); -webkit-background-clip: text; background-clip: text; color: transparent; }
.nav { display: flex; gap: 6px; }
.nav-link { padding: 8px 14px; border-radius: 999px; font-size: 14px; color: var(--text-dim); transition: all var(--tr-fast); }
.nav-link:hover { color: var(--text-main); background: var(--bg-card); }
.nav-link.router-link-active { color: #fff; background: rgba(124,92,255,0.24); }
.app-main { position: relative; z-index: 1; padding: 28px 0 70px; }
@media (max-width: 640px) {
  .nav-link { padding: 6px 9px; font-size: 12.5px; }
  .brand { font-size: 17px; }
}
</style>
