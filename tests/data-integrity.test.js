import { describe, it, expect } from 'vitest'
import { readFileSync, readdirSync, existsSync } from 'node:fs'
import { resolve } from 'node:path'
import { fileURLToPath } from 'node:url'

const root = resolve(fileURLToPath(import.meta.url), '../..')
const characters = JSON.parse(readFileSync(resolve(root, 'src/data/characters.json'), 'utf8'))
const questions = JSON.parse(readFileSync(resolve(root, 'src/data/questions.json'), 'utf8'))
const imageDir = resolve(root, 'public/images')

describe('角色数据完整性', () => {
  it('角色数与图片数一致（当前 132）', () => {
    expect(characters).toHaveLength(132)
    expect(readdirSync(imageDir)).toHaveLength(132)
  })

  it('id 与 name 全局唯一', () => {
    const ids = characters.map(c => c.id)
    const names = characters.map(c => c.name)
    expect(new Set(ids).size).toBe(ids.length)
    expect(new Set(names).size).toBe(names.length)
  })

  it('traits 均为 12 维、数值、0-100', () => {
    for (const c of characters) {
      expect(c.traits, `${c.id} traits 缺失`).toHaveLength(12)
      for (const t of c.traits) {
        expect(typeof t).toBe('number')
        expect(Number.isNaN(t)).toBe(false)
        expect(t).toBeGreaterThanOrEqual(0)
        expect(t).toBeLessThanOrEqual(100)
      }
    }
  })

  it('每个角色的 image 精确对应真实文件（扩展名也须一致）', () => {
    for (const c of characters) {
      const f = c.image.replace(/^images\//, '')
      expect(existsSync(resolve(imageDir, f)), `${c.id} -> ${c.image} 不存在`).toBe(true)
    }
  })

  it('图片目录无孤儿文件', () => {
    const used = new Set(characters.map(c => c.image.replace(/^images\//, '')))
    const orphans = readdirSync(imageDir).filter(f => !used.has(f))
    expect(orphans).toEqual([])
  })
})

describe('题目数据完整性', () => {
  it('共 36 题，每题至少 2 个选项', () => {
    expect(questions).toHaveLength(36)
    questions.forEach((q, i) => {
      expect(q.o.length, `Q${i} 选项不足`).toBeGreaterThanOrEqual(2)
    })
  })
})
