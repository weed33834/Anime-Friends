import { describe, it, expect } from 'vitest'
import { esc, shuffle, MAXD, calcUser, GM, GS, matchScore, rankAll, dimensions, characters, questions } from '@/utils/match'

describe('esc XSS 转义', () => {
  it('转义全部危险字符', () => {
    expect(esc(`<img src=x onerror="alert('1')">&`)).toBe(
      '&lt;img src=x onerror=&quot;alert(&#39;1&#39;)&quot;&gt;&amp;'
    )
  })
  it('null/undefined 安全', () => {
    expect(esc(null)).toBe('')
    expect(esc(undefined)).toBe('')
  })
})

describe('shuffle', () => {
  it('返回等长排列且元素不增不减', () => {
    const src = [...Array(50).keys()]
    const out = shuffle(src)
    expect(out).toHaveLength(src.length)
    expect([...out].sort((a, b) => a - b)).toEqual(src)
  })
})

describe('MAXD 归一化基数', () => {
  it('每个维度都有正的最大理论分', () => {
    for (const d of dimensions) {
      expect(MAXD[d.key]).toBeGreaterThan(0)
    }
  })
})

describe('calcUser 用户画像', () => {
  const N = questions.length
  it('全未答时各维度为基准 50', () => {
    const v = calcUser(Array(N).fill(null))
    for (const d of dimensions) expect(v[d.key]).toBe(50)
  })
  it('任意作答组合下所有维度都在 [0,100]（防饱和回归）', () => {
    for (let i = 0; i < N; i++) {
      for (let o = 0; o < questions[i].o.length; o++) {
        const ans = Array(N).fill(null)
        ans[i] = o
        const v = calcUser(ans)
        for (const d of dimensions) {
          expect(v[d.key]).toBeGreaterThanOrEqual(0)
          expect(v[d.key]).toBeLessThanOrEqual(100)
        }
      }
    }
  })
  it('全选首项/末项整卷作答也在界内', () => {
    for (const pick of [0, questions.map(q => q.o.length - 1)]) {
      const ans = Array(N).fill(null).map((_, i) => (Array.isArray(pick) ? pick[i] : pick))
      const v = calcUser(ans)
      for (const d of dimensions) {
        expect(v[d.key]).toBeGreaterThanOrEqual(0)
        expect(v[d.key]).toBeLessThanOrEqual(100)
      }
    }
  })
})

describe('角色基线统计', () => {
  it('GM/GS 覆盖 12 维且 GS>0', () => {
    expect(GM).toHaveLength(dimensions.length)
    expect(GS).toHaveLength(dimensions.length)
    for (const s of GS) expect(s).toBeGreaterThan(0)
  })
})

describe('matchScore 匹配分', () => {
  const user = calcUser(Array(questions.length).fill(null).map((_, i) => i % questions[i].o.length))
  it('对所有角色输出 0-100 整数', () => {
    for (const c of characters) {
      const ms = matchScore(user, c)
      expect(Number.isInteger(ms)).toBe(true)
      expect(ms).toBeGreaterThanOrEqual(0)
      expect(ms).toBeLessThanOrEqual(100)
    }
  })
  it('确定性：同样输入得分一致', () => {
    expect(matchScore(user, characters[0])).toBe(matchScore(user, characters[0]))
  })
})

describe('rankAll 全量排名', () => {
  it('长度一致且按分数降序', () => {
    const user = calcUser(Array(questions.length).fill(0))
    const ranked = rankAll(user)
    expect(ranked).toHaveLength(characters.length)
    for (let i = 1; i < ranked.length; i++) {
      expect(ranked[i - 1].ms).toBeGreaterThanOrEqual(ranked[i].ms)
    }
  })
})
