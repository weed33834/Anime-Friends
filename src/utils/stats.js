const KEY = 'waifuViewStats'
export function loadStats() {
  try { return JSON.parse(localStorage.getItem(KEY) || '{}') } catch (e) { return {} }
}
export function bumpStat(id) {
  const s = loadStats()
  s[id] = (s[id] || 0) + 1
  try { localStorage.setItem(KEY, JSON.stringify(s)) } catch (e) {}
  return s
}
export function saveStats(s) {
  try { localStorage.setItem(KEY, JSON.stringify(s)) } catch (e) {}
}
