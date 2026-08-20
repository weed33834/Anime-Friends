// 纯前端结果分享：把匹配结果编码进 URL，打开链接即可看到对方的结果，无需任何后端。
//
// 编码载荷（紧凑，UTF-8 安全）：
// {
//   v: 1,
//   n: 昵称(可选, 最长 20),
//   t: [[角色id, 契合度], ...top3],
//   d: [12 个维度值 0-100]
// }
// 经 base64url 编码后作为 #/result?share=xxx 的查询参数。

function b64urlEncode(str) {
  const bytes = new TextEncoder().encode(str)
  let bin = ''
  bytes.forEach((b) => (bin += String.fromCharCode(b)))
  const b64 = btoa(bin)
  return b64.replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '')
}

function b64urlDecode(s) {
  s = s.replace(/-/g, '+').replace(/_/g, '/')
  while (s.length % 4) s += '='
  const bin = atob(s)
  const bytes = new Uint8Array(bin.length)
  for (let i = 0; i < bin.length; i++) bytes[i] = bin.charCodeAt(i)
  return new TextDecoder().decode(bytes)
}

// 把结果编码为 base64url 字符串
export function encodeResult({ name, top, dims }) {
  const payload = {
    v: 1,
    n: (name || '').toString().slice(0, 20),
    t: (top || [])
      .filter((c) => c && c.id != null)
      .slice(0, 3)
      .map((c) => [c.id, Math.round(c.ms ?? 0)]),
    d: (dims || []).slice(0, 12).map((v) => Math.round(Number(v) || 0)),
  }
  return b64urlEncode(JSON.stringify(payload))
}

// 从 URL 参数解码；任何损坏/非法输入都返回 null（上层据此回退到普通模式）
export function decodeResult(param) {
  const p = Array.isArray(param) ? param[0] : param
  if (!p || typeof p !== 'string') return null
  try {
    const obj = JSON.parse(b64urlDecode(p))
    if (!obj || obj.v !== 1 || !Array.isArray(obj.t) || !Array.isArray(obj.d)) return null
    return {
      name: typeof obj.n === 'string' ? obj.n : '',
      top: obj.t
        .filter((x) => Array.isArray(x) && x.length >= 2)
        .map(([id, ms]) => ({ id, ms: Number(ms) || 0 })),
      dims: obj.d.map(Number),
    }
  } catch (e) {
    return null
  }
}
