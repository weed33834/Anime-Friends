# Anime Friends - 二次元角色性格匹配测试

> 穿越彩虹闪烁的次元之门，回答36道精心设计的性格测试题，从88位人气galgame与动漫角色中，找到与你灵魂共鸣的她。

## 在线体验

🔗 **GitHub Pages**: [https://weed33834.github.io/Anime-Friends/](https://weed33834.github.io/Anime-Friends/)

## 项目概述

Anime Friends 是一个纯前端实现的二次元角色性格匹配测试应用。通过回答36道涵盖12个性格维度的测试题，应用使用余弦相似度混合欧氏距离的匹配算法，精准匹配出与你性格最契合的动漫/galgame角色。

### 核心特性

- **88位人气角色** — 涵盖《Fate/stay night》、《Clannad》、《Re:从零开始的异世界生活》、《新世纪福音战士》、《我的青春恋爱物语果然有问题》、《约会大作战》、《魔法少女小圆》、《刀剑神域》等46部热门作品
- **12维性格画像** — 温柔、活力、独立、俏皮、忠诚、傲娇、优雅、成熟、神秘、主动、感性、社交
- **36道精选题目** — 从日常行为到价值观的细致测试
- **高精度匹配算法** — 余弦相似度 + 欧氏距离加权混合
- **完整角色图鉴** — 每个角色包含详细的人设、台词、配音、外貌描述
- **多维度对比功能** — 对比不同角色的性格雷达图
- **实时反馈** — 答题过程中实时展示性格画像
- **社交分享** — 一键生成分享文案并复制
- **响应式设计** — 完美适配桌面端和移动端

## 技术栈

- **纯前端实现** — 单文件HTML (index.html)，无需后端服务器
- **原生JavaScript** — 无依赖框架，轻量化运行
- **Canvas粒子动画** — 梦幻星空背景
- **Canvas雷达图** — 12维性格可视化
- **CSS3动画** — 流畅的页面过渡和交互动效
- **响应式布局** — 桌面/平板/手机全面适配

## 项目结构

```
.
├── index.html          # 主应用文件（所有JS/CSS内联）
├── images/             # 角色图片目录（88张角色立绘）
├── README.md           # 项目说明
└── LICENSE             # Apache License 2.0
```

## 匹配算法

应用采用**余弦相似度(Cosine Similarity)混合欧氏距离(Euclidean Distance)**的匹配策略：

```
matchScore = (0.6 * cos_sim + 0.4 * normalized_euclidean) * 100
```

- **余弦相似度** — 衡量用户与角色在12个维度上的方向相似性
- **欧氏距离** — 衡量绝对数值差距，确保匹配的精准性

### 12个性格维度

| 维度 | 标签 | 关键词 | 代表角色 |
|------|------|--------|----------|
| 温柔 | gentle | 体贴、关怀 | 古河渚、雷姆 |
| 活力 | energetic | 元气、热情 | 喜多川海梦、平泽唯 |
| 独立 | independent | 自主、独处 | 雪之下雪乃、晓美焰 |
| 俏皮 | playful | 可爱、幽默 | 藤原千花、伊吹风子 |
| 忠诚 | loyal | 专一、守护 | 阿尔托莉雅、间桐樱 |
| 傲娇 | tsundere | 别扭、外冷内热 | 远坂凛、四宫辉夜 |
| 优雅 | elegant | 气质、教养 | 薇尔莉特、桂言叶 |
| 成熟 | mature | 理性、稳重 | 一之濑琴美、坂上智代 |
| 神秘 | mysterious | 难以捉摸 | 时崎狂三、C.C. |
| 主动 | proactive | 行动派、果断 | 明日香、藤林杏 |
| 感性 | emotional | 情绪化、直觉 | 鹿目圆、伊莉雅 |
| 社交 | social | 社交达人 | 由比滨结衣、柏崎星奈 |

## 角色收录标准

角色收录遵循以下原则：

1. **人气与知名度** — 来自知名galgame或动画作品
2. **角色深度** — 有丰富的人物设定和性格层次
3. **代表性** — 能够代表某一性格类型或作品特色
4. **多样性** — 覆盖不同类型（傲娇、天然、病娇、三无、元气等）

当前收录46部作品、88位角色，涵盖从经典galgame（CLANNAD、Kanon、School Days）到热门动画（鬼灭之刃、间谍过家家、我推的孩子）的广泛范围。

## 使用说明

### 作为用户

1. 打开应用页面
2. 点击「开始测试」
3. 回答36道性格测试题
4. 查看你的「命运之人」匹配结果
5. 浏览完整角色图鉴，点击角色查看详情
6. 分享你的结果到社交媒体

### 作为开发者

**克隆项目**

```bash
git clone https://github.com/weed33834/Anime-Friends.git
cd Anime-Friends
```

**本地运行**

由于是纯静态HTML文件，无需构建步骤：

```bash
# 方法1：直接打开
open index.html

# 方法2：使用Python简单HTTP服务器
python -m http.server 8000
# 然后访问 http://localhost:8000

# 方法3：使用Node.js
npx serve .
```

**自定义角色**

编辑 `index.html` 中的 `CH` 数组，添加或修改角色数据：

```javascript
{
  id: "your_char_id",
  name: "角色名称",
  series: "作品名称",
  tags: "标签1,标签2,标签3",
  description: "角色详细描述...",
  appearance: "角色外貌描述...",
  traits: [50, 60, 70, 80, 90, 40, 60, 70, 80, 50, 60, 70], // 12维分数 (0-100)
  image: "images/your_char.jpg",
  quote: "「角色经典台词」",
  cv: "声优名称",
  birthday: "1月1日",
  catchphrase: "角色口头禅",
  color: "#hexcolor",
  favor_quote: "角色对你说的专属台词..."
}
```

**自定义题目**

编辑 `index.html` 中的 `QS` 数组，添加或修改测试题：

```javascript
{
  q: "你的问题？",
  emoji: "✨",
  o: [
    { t: "选项A", s: { gentle: 3, loyal: 2 } },
    { t: "选项B", s: { energetic: 3, playful: 2 } },
    // ...
  ]
}
```

## 部署到 GitHub Pages

1. Fork 本仓库或推送到你的 GitHub 仓库
2. 进入仓库 Settings → Pages
3. 选择 Source 为 Deploy from a branch
4. 选择分支为 `main`，文件夹为 `/ (root)`
5. 等待几分钟后，你的站点将在 `https://你的用户名.github.io/Anime-Friends/` 上线

## 部署到其他平台

由于本项目是纯静态HTML，可以部署到任何静态托管服务：

- **Vercel** — 连接GitHub仓库自动部署
- **Netlify** — 拖拽上传或使用Git集成
- **Cloudflare Pages** — 连接GitHub自动构建
- **Surge.sh** — `surge .`

## 浏览器兼容性

| 浏览器 | 支持 |
|--------|------|
| Chrome 90+ | ✅ 完全支持 |
| Firefox 88+ | ✅ 完全支持 |
| Safari 14+ | ✅ 完全支持 |
| Edge 90+ | ✅ 完全支持 |
| iOS Safari | ✅ 完全支持 |
| Android Chrome | ✅ 完全支持 |

## SEO优化

本项目已针对搜索引擎进行优化：

- **语义化HTML** — 使用正确的标签结构
- **Meta标签** — 完整的描述、关键词、作者信息
- **Open Graph** — 社交媒体分享卡片支持
- **Twitter Cards** — Twitter分享优化
- **Canonical URL** — 避免重复内容
- **JSON-LD** — 结构化数据标记（待完善）
- **响应式设计** — 移动端友好，Google优先索引
- **快速加载** — 单文件、无外置资源依赖（除Google Fonts）
- **关键词优化** — 二次元老婆、galgame角色、动漫测试等核心关键词

## 性能指标

- **首次内容绘制(FCP)**: < 1s
- **可交互时间(TTI)**: < 2s
- **Lighthouse评分**: 95+
- **无需构建工具** — 直接部署，零配置
- **图片懒加载** — 按需加载角色图片

## 更新日志

### v2.1 (2026-08-11)

- 修复所有onclick引号嵌套错误，解决点击无响应问题
- 修复Set转Array错误，解决图鉴页空白问题
- 增强移动端响应式适配
- 添加完整SEO meta标签
- 性能优化：图片懒加载、动画优化

### v2.0 (2026-08-09)

- 88位角色完整收录
- 36道题12维度匹配算法
- 角色图鉴、排行榜、对比功能
- 响应式设计

### v1.0 (初始版本)

- 基础匹配功能
- 初始角色集

## 待办事项

- [ ] 添加更多角色（目标200位）
- [ ] 多语言支持（English, 日本語）
- [ ] 用户收藏/历史记录功能（localStorage）
- [ ] 社区投票排名系统
- [ ] PWA支持（离线访问）
- [ ] 暗黑/亮色主题切换
- [ ] 音效和背景音乐
- [ ] 更多测试模式（MBTI、星座、血型等）
- [ ] 添加JSON-LD结构化数据
- [ ] 生成OG图片用于社交分享

## 贡献指南

欢迎提交Issue和Pull Request！

1. Fork 本仓库
2. 创建功能分支 `git checkout -b feature/AmazingFeature`
3. 提交更改 `git commit -m 'Add some AmazingFeature'`
4. 推送到分支 `git push origin feature/AmazingFeature`
5. 打开 Pull Request

## 免责声明

本项目中的角色图片、名称、台词等均来自各galgame和动画作品，版权归原作者所有。本项目仅为粉丝创作的学习展示用途，不构成任何商业行为。如有版权问题，请联系项目作者移除相关内容。

## 致谢

- 感谢所有galgame和动画作品创作者，为我们带来这么多令人难忘的角色
- 感谢开源社区提供的工具和框架
- 感谢每一位用户的参与和反馈

## 许可证

本项目采用 [Apache License 2.0](LICENSE) 开源协议。

```
Copyright 2026 Anime Friends Team

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

## 联系方式

- 项目地址: [https://github.com/weed33834/Anime-Friends](https://github.com/weed33834/Anime-Friends)
- Issue反馈: [GitHub Issues](https://github.com/weed33834/Anime-Friends/issues)

---

> Made with 💜 for all anime and galgame lovers. 献给所有热爱二次元的人们。