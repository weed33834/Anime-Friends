import { createRouter, createWebHashHistory } from 'vue-router'

const routes = [
  { path: '/', name: 'home', component: () => import('@/views/HomeView.vue') },
  { path: '/quiz', name: 'quiz', component: () => import('@/views/QuizView.vue') },
  { path: '/result', name: 'result', component: () => import('@/views/ResultView.vue') },
  { path: '/challenge', name: 'challenge', component: () => import('@/views/ChallengeView.vue') },
  { path: '/gallery', name: 'gallery', component: () => import('@/views/GalleryView.vue') },
  { path: '/ranking', name: 'ranking', component: () => import('@/views/RankingView.vue') },
  { path: '/stats', name: 'stats', component: () => import('@/views/StatsView.vue') },
  { path: '/compare', name: 'compare', component: () => import('@/views/CompareView.vue') }
]

export default createRouter({
  history: createWebHashHistory(),
  routes
})
