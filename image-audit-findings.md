# Anime-Friends 角色图片与描述审计报告

## 审计方法
- 逐张读取 `public/images/` 下的角色图
- 与 `src/data/characters.json` 中的 `name/series/description/appearance` 进行比对
- 标记：图片与名称不符、描述与图片/常识不符、外观字段自相矛盾、CV 错误等问题

## 已确认问题汇总

| id | 名称 | 问题类型 | 具体说明 | 建议修正 |
|---|---|---|---|---|
| medusa | 美杜莎 | appearance 错误 | appearance 写"粉色长发"，但 Medusa（Rider）实际为紫色长发；description 内倒是写对了"紫色长发" | appearance 改为"紫色长发" |
| yurippe | 仲村由理 | CV 错误 | CV 写成"樱井孝宏"（男声优），实际为"樱井浩美" | CV 改为"樱井浩美" |
| kotomi2 | 古河早苗 | tags 错误 | tags 为"姐姐,温柔,早苗"，但她是渚的母亲 | tags 改为"母亲,温柔,早苗" |
| makoto | 美坂香里 | 名称错误 | Kanon 中 id=makoto 对应的是泽渡真琴（狐少女），描述/外观均符合泽渡真琴；"美坂香里"是另一个角色（名雪的姐姐） | name 改为"泽渡真琴" |
| shiori | 仓田汐里 | 名称错误 | Kanon 中的 Shiori 是"美坂栞"，不是"仓田汐里" | name 改为"美坂栞" |
| rise | 天天座理世 | description 与 appearance 矛盾 | description 写"金发双马尾"，appearance 写"紫色长发双马尾"；实际为紫色/深紫发 | description 改为"紫色长发双马尾" |
| chizuru | 水原千鹤 | appearance 错误 | appearance 写"棕色短发"，实际为黑色/深色长发 | appearance 改为"黑色长发" |
| amnist | 泉户真白 | appearance 与 description 矛盾 | description 写"银发红瞳"，appearance 写"白发，紫色眼瞳"；实际为白发/银发 + 红瞳 | appearance 改为"银发红瞳" |
| sora | 春日野穹 | appearance 与 description 矛盾 | description 写"银发蓝瞳"，appearance 写"银色双马尾，紫色眼睛"；实际为银发蓝瞳 | appearance 改为"银色双马尾，蓝色眼睛" |

## 已应用修正（2026-08-20）

- `medusa.appearance` 改为"紫色长发，戴眼罩，身穿紫色服饰，气质冷艳"
- `yurippe.cv` 改为"樱井浩美"
- `kotomi2.tags` 改为"母亲,温柔,早苗"
- `makoto.name` 改为"泽渡真琴"
- `shiori.name` 改为"美坂栞"
- `rise.description` 改为与紫色长发设定一致
- `chizuru.appearance` 改为"黑色长发"
- `amnist.appearance` 改为"银发红瞳"
- `sora.appearance` 改为"银色双马尾，蓝色眼睛"
- 删除 `tohka` 角色条目与 `public/images/tohka.jpg`：该文件与 `ai.jpg` MD5 完全相同，且内容确为星野爱（《推しの子》），因此不存在正确的夜刀神十香图片；已移除错误条目，角色数由 88 调整为 87。

## 视觉核对记录

### Batch 1 (saber)
- `saber.jpg`: 已核对，图片为阿尔托莉雅·潘德拉贡，正确。

### 待继续核对
- 其余 86 张角色图尚未完成逐张视觉核对；此前的"Batch 2~7 核对记录"因模型输出被过滤/缓存引用，无法被后续会话验证，已作废，需重新核对。

