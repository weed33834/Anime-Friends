---
AIGC:
    Label: "1"
    ContentProducer: 001191440300708461136T1XGW3
    ProduceID: c94f524fda04838eb9e189b556d1496a_31a3d78e9a4111f18cca525400e6dd8f
    ReservedCode1: 8tf5ar1FzZewGG+q9kMyXk4j8ZkQochAHleAsXyakiJmK+/aQDKH+qKGYlzctijUWk1v0F7rO69NA++WFBXBbsGhqxJ4FBR8Kkt90nESGlthmdUq6N6lM7JOIKYB0j6i+elj4doxx8FXmPCJc8V9Iw4Sdfv7oXENzJIMOdGNRTucYVN+QRa1CYZtgp4=
    ContentPropagator: 001191440300708461136T1XGW3
    PropagateID: c94f524fda04838eb9e189b556d1496a_31a3d78e9a4111f18cca525400e6dd8f
    ReservedCode2: 8tf5ar1FzZewGG+q9kMyXk4j8ZkQochAHleAsXyakiJmK+/aQDKH+qKGYlzctijUWk1v0F7rO69NA++WFBXBbsGhqxJ4FBR8Kkt90nESGlthmdUq6N6lM7JOIKYB0j6i+elj4doxx8FXmPCJc8V9Iw4Sdfv7oXENzJIMOdGNRTucYVN+QRa1CYZtgp4=
---

# Anime Friends — 132位角色12维性格匹配测试

本仓库 v1 为单文件 HTML 版，后原地重构为 Vue3 + Vite 组件化工程（即当前 `src/`），并修复了初版算法缺陷。数据与图片的历次审计记录见 [image-audit-findings.md](image-audit-findings.md)。

## 在线体验

- **国内快速通道（CloudStudio 托管）**：https://7381928abfa44e18b6b70f43954410be.app.workbuddy.link
- GitHub Pages：https://weed33834.github.io/Anime-Friends/

> 国内网络访问 GitHub Pages 不稳定时，请优先使用上方 CloudStudio 链接（国内可直连）。

## 功能

- 132 位人气 galgame 与动漫角色，12 个性格维度（Fate / EVA / Re:Zero / 命运石之门 / 辉夜大小姐 / 春物 / 青春猪头少年 七大系列扩充）
- 36 道测评题目，作答后计算与每位角色的性格契合度
- 结果页展示 Top 角色、雷达图、契合度等级标签
- 图鉴页（Gallery）、排行榜（Ranking）、统计页（Stats）、对比页（Compare）
- 挑战模式（Challenge）：限时答题挑战，见 `src/views/ChallengeView.vue`
- 全维度概率显示与匹配算法

## 与原版相比的修复

| 缺陷 | 原版 | 修复后 |
| --- | --- | --- |
| 用户画像必然饱和 | 原始系数 ×8 导致 81.6% 用户全维度 ≥90 | calcUser 系数 ×2 并归一化，饱和率归零 |
| 高分角色霸榜 | zero_two 独占 97.3% Top1 | 匹配前 z-score 标准化 + 维度最大得分归一化，Top1 去重角色扩至 16 个 |
| XSS 风险 | 未转义用户输入 | 新增 esc() 转义 |
| 契合度展示 | 仅百分比 | 增加等级标签（如 天作之合 / 心动 / 普通等） |

## 技术栈

- Vue 3 + Vue Router + Pinia
- Vite 5
- 纯手写 CSS（tokens.css 设计变量 + base.css）

## 目录结构

```
src/
├── components/     # 组件（CharacterCard / RadarChart / MatchLevelBadge / ParticleBg）
├── data/           # characters.json / questions.json / dimensions.js
├── stores/         # Pinia 状态（quiz.js）
├── styles/         # tokens.css / base.css
├── utils/          # match.js（算法核心）/ stats.js
├── views/          # Home / Quiz / Result / Gallery / Ranking / Stats / Compare
├── App.vue
├── main.js
└── router.js
public/images/      # 132 张角色图（与 characters.json 一一对应，文件名 = 角色 id）
```

## 测试

```bash
npm test         # vitest 单测：匹配算法 / 分享编码 / 数据完整性
```

数据完整性约束（由测试锁定）：`characters.json` 每条的 `image` 必须精确对应 `public/images/` 下的真实文件；`traits` 必须为 12 维且取值 0–100；`id` 与 `name` 不得重复。

## 版权声明

本项目为非商业粉丝作品（仅供学习交流）。角色名称、设定与图片版权归原作者及版权方所有；图片来源为公开网络渠道的粉丝社区素材。如有侵权请通过 [Issues](https://github.com/weed33834/Anime-Friends/issues) 联系，核实后将立即删除相关内容。

## 开发

```bash
npm install
npm run dev      # 本地开发
npm run build    # 产物输出到 dist/
npm run preview  # 预览构建产物
```

## 部署

构建产物位于 `dist/`，可直接部署到任意静态托管（GitHub Pages / Nginx / CDN 等）。

当前部署情况：

| 通道 | 地址 | 说明 |
| --- | --- | --- |
| CloudStudio（国内直连） | https://7381928abfa44e18b6b70f43954410be.app.workbuddy.link | 主力线上通道，内容与仓库同步更新 |
| GitHub Pages | https://weed33834.github.io/Anime-Friends/ | 由 `.github/workflows/static.yml` 自动构建部署（push main 触发） |

## 角色数据来源

角色、题目、维度数据提取自原仓库 [Anime-Friends](https://github.com/weed33834/Anime-Friends)，图片来源于其 GitHub Pages 站点。
*（内容由AI生成，仅供参考）*
