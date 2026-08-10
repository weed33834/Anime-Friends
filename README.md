# Anime Friends

> 穿越彩虹闪烁的次元之门，找到与你灵魂共鸣的她。

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live-brightgreen)](https://weed33834.github.io/Anime-Friends/)
[![Stars](https://img.shields.io/github/stars/weed33834/Anime-Friends?style=social)](https://github.com/weed33834/Anime-Friends/stargazers)

## 在线体验

**GitHub Pages:** https://weed33834.github.io/Anime-Friends/

**秒哒平台:** https://app-dlcivqqgr30h.appmiaoda.com

## 项目简介

一款基于 **88 位人气 galgame 与动漫角色**、**12 维性格精准匹配**的互动 Web 应用。通过回答 36 道精心设计的性格测试题，系统将为你匹配出最契合的二次元角色，并提供详细的匹配分析和角色介绍。

### 核心特性

- **88 位角色库** - 覆盖 46 部经典作品
- **12 维性格匹配** - 温柔/活力/独立/俏皮/忠诚/傲娇/优雅/成熟/神秘/主动/感性/社交
- **36 道精选题** - 每题配有情景 emoji，深度洞察性格
- **混合匹配算法** - 余弦相似度 + 欧氏距离混合计算
- **丰富结果展示** - 命运邂逅故事 / 相处日常 / 潜在情敌 / 分享功能
- **多页面体验** - 测试 / 图鉴 / 排行 / 对比 / 统计
- **深色星空风格** - 粒子动效 + 粉紫渐变配色
- **移动端适配** - 全平台流畅体验
- **本地图片** - 所有角色图片随仓库部署，无需外部 CDN

## 收录作品

涵盖 Fate/stay night、Clannad、新世纪福音战士、Re:从零开始的异世界生活、
命运石之门、四月是你的谎言、龙与虎、物语系列、辉夜大小姐想让我告白、
我的青春恋爱物语果然有问题、紫罗兰永恒花园、DARLING in the FRANXX、
鬼灭之刃、刀剑神域、魔法少女小圆、约会大作战、五等分的新娘、
租借女友、我推的孩子、间谍过家家、凉宫春日的忧郁、冰菓、灼眼的夏娜、
某科学的超电磁炮、叛逆的鲁路修、零之使魔、绯弹的亚里亚、罪恶王冠、
缘之空、声之形、俺妹、天才麻将少女、无职转生、点兔、School Days、
我的朋友很少、黄昏少女×失忆、游魂、Kanon、Angel Beats!、Charlotte、
路人女主的养成方法、更衣人偶坠入爱河、堀与宫村、轻音少女等 46 部作品。

## 技术栈

- **纯静态单文件 HTML** - 零外部 JS 依赖
- **Canvas 粒子动画** - 星空背景效果
- **Canvas 雷达图** - 12 维性格可视化对比
- **localStorage** - 浏览统计持久化
- **CSS 动画** - 页面切换/卡片悬浮/流光效果
- **本地图片资源** - 88 张角色立绘随仓库部署

## 部署方式

### GitHub Pages（推荐）

本仓库已配置 GitHub Actions 自动部署，访问链接即可：
**https://weed33834.github.io/Anime-Friends/**

### 本地预览

```bash
# 直接双击打开 index.html
# 或使用任意静态服务器
python3 -m http.server 8000
```

## 角色数据

每个角色包含 14 个字段的完整数据：
- 姓名、出处作品、角色标签
- 外貌描述（详细外貌描写）
- 性格介绍（150-200 字深度分析）
- 12 维性格评分（0-100）
- 角色立绘图片（本地 images/ 目录）
- 经典台词
- 声优信息
- 生日
- 口癖 / 招牌动作
- 代表色（hex）
- 好感度台词

## 算法说明

匹配采用**余弦相似度 60% + 归一化欧氏距离 40%**的混合算法：

```
匹配分 = 0.6 * cosSim(用户, 角色) + 0.4 * normEuclidean(用户, 角色)
```

- **余弦相似度**：衡量性格方向的相似性
- **欧氏距离**：衡量性格强度的差异
- 最终百分比 0-100%，越高越匹配

## 文件结构

```
.
├── index.html          # 主应用文件（单文件，163KB）
├── images/             # 88 张角色立绘图片
│   ├── saber.jpg
│   ├── rin.jpg
│   └── ...
├── README.md           # 项目说明
├── LICENSE             # MIT 许可证
└── .github/
    └── workflows/
        └── static.yml  # GitHub Actions 自动化部署
```

## 许可证

[MIT License](LICENSE)

## 致谢

- 角色图片来源于各大动漫社区，仅供学习和娱乐用途
- 感谢所有创作者和爱好者对二次元文化的贡献
- 本项目为个人学习项目，不涉及商业用途

---

Made with 💗 by [weed33834](https://github.com/weed33834)
