import { describe, it, expect } from 'vitest'
import { encodeResult, decodeResult } from '@/utils/share'

describe('结果分享编码', () => {
  const dims = [10, 20, 30, 40, 50, 60, 70, 80, 90, 55, 45, 35]
  const top = [
    { id: 'saber', ms: 88.4 },
    { id: 'rei', ms: 76 },
    { id: 'misato', ms: 71.9 },
  ]

  it('编码后可无损解码', () => {
    const code = encodeResult({ name: '测试用户', top, dims })
    const out = decodeResult(code)
    expect(out.name).toBe('测试用户')
    expect(out.top).toEqual([
      { id: 'saber', ms: 88 },
      { id: 'rei', ms: 76 },
      { id: 'misato', ms: 72 },
    ])
    expect(out.dims).toEqual(dims.map(Math.round))
  })

  it('昵称截断到 20 字符', () => {
    const out = decodeResult(encodeResult({ name: 'x'.repeat(50), top: [], dims }))
    expect(out.name).toHaveLength(20)
  })

  it('损坏/非法输入安全返回 null', () => {
    expect(decodeResult('')).toBeNull()
    expect(decodeResult('not-base64!!!')).toBeNull()
    expect(decodeResult(Buffer.from(JSON.stringify({ v: 99 })).toString('base64'))).toBeNull()
    expect(decodeResult(null)).toBeNull()
  })
})
