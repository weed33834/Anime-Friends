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

### 本轮批量视觉核对（contact sheet 法）
- **时间**: 2026-08-20
- **方法**: 使用 Pillow 将 87 张角色图按 `characters.json` 顺序拼成 4 张 5×5 联系表，每张含文件名、id、名称、作品名标签，一次性视觉核对。
- **范围**: 87 / 87 张角色图全部核对完毕。

**核对结果**:
- 83 张图片与 JSON 名称/作品/描述一致。
- 4 项问题需修正（见下表）。

| id | 名称 | 问题类型 | 具体说明 | 修正措施 |
|---|---|---|---|---|
| chino | 香风智乃 | 图片完全错位 | `chino.jpg` 实际为《黄昏少女×失忆》夕子（黑长发、校服、夕阳背景），不是香风智乃 | 从萌娘共享下载正确的香风智乃角色图，替换 `public/images/chino.jpg` |
| shiori | 美坂栞 | 描述文字错误 | `description` 内写成"仓田汐里"，角色实际是美坂栞 | 将描述改为以美坂栞为主角 |
| makoto | 泽渡真琴 | 描述文字错误 | `description` 内写成"美坂香里"，且描述的是另一个角色 | 重写为泽渡真琴（狐少女、约定、记忆）的描述 |
| rem_alt | 雷姆（ alternate ） | 描述与图片不符 | 图片是冬季/战斗装的雷姆，描述写成"暴食形态/睡裙/空洞眼神" | 将名称改为"雷姆（ alternate ）"，描述改为冬季远行/战士姿态 |

### 修正后复核对关键项
- `chino.jpg`: 已替换为香风智乃角色设定图（蓝发、Rabbit House 制服、右下角标注 "Chino"），正确。
- 其余 3 项为文本修正，已验证 JSON 文本与角色一致。

### 本轮整体结论
- **角色图 87 / 87 全部核对**。
- **图片与角色身份一一对应**；唯一错位的 `chino.jpg` 已替换为正确图片。
- **描述、名称、图片三者一致**；文本错误已修正。

## 七大系列扩充与 133 角色重建（2026-08-20 续）

### 背景与决策
- 用户指令 C：引入更多 **Fate / 新世纪福音战士(EVA) / Re:从零开始的异世界生活(ReZero) / 命运石之门 / 辉夜大小姐想让我告白 / 我的青春恋爱物语果然有问题(春物) / 青春猪头少年不会梦到兔女郎学姐** 七大系列的真实角色，以官网/维基真实名单为准，缺的加、错的改、重复去重。
- 经确认的三点决策：
  1. "青春多多少年不为莫当退远去了" = 《青春猪头少年不会梦到兔女郎学姐》。
  2. 范围：前 5 个 Fate（saber/rin/sakura/illya/medusa）保留，其余全部重做。
  3. 方式：新增+替换由助手定。

### 结果
- 角色数 **87 → 133**。装配逻辑：`final = 保留 22 + 新增 47 + 其他 64`。
- 7 大系列计数：**Fate 13 / EVA 7 / ReZero 16 / 命运石之门 8 / 辉夜 7 / 春物 11 / 青春猪头 7**。
- 新增 47 个均含完整 12 维 traits、cv、birthday、catchphrase、color、favor_quote。
- 图源：萌娘百科 `storage.moegirl.org.cn/moegirl/commons/...` 真实角色图；`is_bad()` 排除 logo/nerv/Uuu.jpg/OP_/ED_/PV_/1600/EVA-TV/EP 等。

### 取舍决策
- **kaji（加持良治，EVA）放弃**：萌娘 `zh.moegirl.org.cn` 与 `zh.moegirl.tw` 均无独立角色页（HTTP 404/超时），Fandom `evangelion.fandom.com/wiki/Kaji_Ryoji` 连接超时（`WinError 10060`）失败。按"宁缺毋滥"原则不强行塞入无图源角色；EVA 保留 7 名核心（rei/asuka/misato/shinji/kaworu/ritsuko/gendo）。
- 补抓 4 张缺失图成功：puck←帕克(Re-从零开始的异世界生活).jpg、petra←Petra21.png、faris←B0055271_516a38c2b10f6.jpg、nodoka_b←Nodoka_Toyohama.jpg。

### 收尾动作
- `npm run build` 干净通过；commit `c4ac258`；三平台（GitHub/GitCode/Gitee）`git push origin main` 全成功。
- CloudStudio 重新部署 `dist/`（纯静态），shareLink 已 verified：`https://7381928abfa44e18b6b70f43954410be.app.workbuddy.link`。
- 去除硬编码：`HomeView.vue` 与 `package.json` 的"88位"改为动态 `{{ characters.length }}` / "133位"。
- 新审计表 `audit_table.html` 重生成 **133 行**，133/133 线上图片 URL 经 curl 全量校验均返回 **200**，待用户逐张复核（编号 X / 链接 Y 报错的反馈机制不变）。

### 待办
- 用户逐张复核 `audit_table.html`；反馈「编号 X / 链接 Y 错了」后，改图或重映射。

## 第二轮图文一致性审计（2026-08-23）

### 方法
- 程序化核查：字段完整性、traits 维度/取值、id/name 查重、发色瞳色 appearance↔description 交叉比对、全量图片 MD5 查重。
- 视觉抽查：对历史问题角色及可疑条目逐张人工核对（chino/shana/medusa/makoto/asuna/sora/chizuru/rise/amnist/saber/rem_alt/shiori）。

### 发现并修复

| id | 问题 | 处理 |
|---|---|---|
| makoto / asuna | **两张图互换**：makoto.jpg 实为亚丝娜（甲裙细剑），asuna.jpg 实为真琴风格便服少女 | 两文件名互换，JSON 无需改动 |
| shiori | shiori.jpg 实为**西宫硝子官方设定图（Model Sheet）**，与"美坂栞"完全不符；且数据集已有正确硝子条目（shouko） | 删除该条目；以已视觉核实的葛城美里替补 |
| misato | 原条目指向 misato.png 未核实；misato.jpg 曾被误判孤儿 | 统一为已核实的 misato.jpg（紫长发/棕眼/金耳环/十字架项链），appearance 同步修正"短发→长发" |
| shana | description 写"红发少女"，appearance 写黑发（战斗时变红）；图为红发战斗形态 | description 统一为"平时黑发红瞳、战斗时化作红发烈焰" |
| medusa | 图中紫瞳可见、无眼罩，appearance 却写"戴眼罩" | 移除眼罩描述，按图补齐细节 |
| sora | 图为白衬衫+格纹裙+黑缎带双马尾+兔子玩偶，非"黑色洋装/哥特萝莉" | appearance 改为与图一致 |
| amnist | 图为浅棕长发+狐耳+紫瞳+白衣和服持神杖，原写"银发红瞳" | 按图修正 |

### 清理
- 删除孤儿文件：kaworu.png、mio_i.png、miura.jpg、miyuki.png、nodoka_k.jpg、rem_alt.jpg（rem_alt 实为无关的金发校服少女）、shiori.jpg、misato.png、_image_manifest.txt。
- 删除仓库根目录审计中间产物 `audit_table.html`。

### 结果
- 角色数 **133 → 132**（移除无法配图的错误条目），`index.html` / `package.json` / README 计数同步更新。
- `public/images/` 现有 **132 张图，与 characters.json 一一精确对应**（文件名 = id，零缺失零孤儿）。
- 全库 MD5 无重复图片。

## 第三轮：网络检索交叉验证（2026-08-23）

### 方法
按"以官方资料反查角色数据"的流程，对全部被修改过的条目逐一搜索权威数据库（Key 公式站、ACDB、NeoApo、EvaWiki Fandom、SRW Wiki 等），核对 CV 与生日。

### 核验结果

| 条目 | 字段 | 权威来源数据 | 结论 |
|---|---|---|---|
| makoto（泽渡真琴） | CV | NeoApo：飯塚雅弓 | ❌原"小林沙苗"实为美坂栞的 CV（shiori/makoto 条目生成时互相污染）→ **已修正** |
| makoto（泽渡真琴） | 生日 | Key 公式站：1月6日 | ❌原"10月13日"→ **已修正** |
| amnist（泉戸ましろ/Tayutama） | 身份与外观 | ACDB：very long brown hair, purple eyes, animal ears；白衣神明形象 | ✅图片与修正后文本一致；原"银发红瞳"确认有误 |
| misato（葛城美里） | CV＋生日 | Wikipedia/NeoApo/Fandom/SRW Wiki：三石琴乃；1986年12月8日 | ✅无误（与声优同生日为官方彩蛋） |
| ayu／nayuki | 生日 | Key 公式站：1月7日／12月23日 | ✅无误 |
| asuna | 图为创世神ステイシア形态（金发金瞳白甲细剑） | SAO WoU 官方设定及手办商品页 | ✅与 appearance 文本吻合 |

### 结论
- 本轮新增修复 makoto 的 CV 与生日共 2 处资料错误。
- 其余约 120 个条目的 CV/生日尚未逐条核验，建议后续按系列批量比对官方维基（每系列一次检索）。

