#!/usr/bin/env python3
"""Generate the complete enhanced waifu matcher HTML application"""

import json

with open('/home/work/dumate/ba849ae564f04117b0c123c600d87806/workspace/ses_01aa3bfb9ffezurCsuzN0y3Th7/waifu-match/characters_final.json', 'r', encoding='utf-8') as f:
    characters = json.load(f)

# 36 questions covering 12 dimensions
# Each option maps to dimension scores
questions = [
    {"q": "当朋友难过时，你通常会怎么做？", "options": [
        {"text": "静静陪伴，听对方倾诉", "scores": {"gentle": 3, "mature": 1, "social": -1}},
        {"text": "讲笑话或做鬼脸逗对方开心", "scores": {"energetic": 3, "playful": 2, "proactive": 1}},
        {"text": "冷静分析问题并给出建议", "scores": {"independent": 2, "mature": 3, "mysterious": 1}},
        {"text": "拉对方出去运动或吃美食散心", "scores": {"energetic": 2, "proactive": 3, "social": 2}}
    ]},
    {"q": "你更喜欢怎样的相处模式？", "options": [
        {"text": "温柔体贴，照顾对方的情绪", "scores": {"gentle": 3, "loyal": 1, "emotional": 2}},
        {"text": "打打闹闹，像伙伴一样轻松", "scores": {"playful": 3, "energetic": 2, "social": 1}},
        {"text": "各自独立，有事才联系", "scores": {"independent": 3, "mature": 2, "mysterious": 1}},
        {"text": "时刻陪伴，保持紧密联系", "scores": {"loyal": 3, "proactive": 2, "emotional": 2}}
    ]},
    {"q": "看到路边受伤的小动物，你会？", "options": [
        {"text": "心疼地想带它去治疗", "scores": {"gentle": 3, "emotional": 2, "loyal": 1}},
        {"text": "蹲下来逗它玩，让它开心", "scores": {"playful": 3, "energetic": 1, "social": 1}},
        {"text": "观察一下，默默离开", "scores": {"independent": 2, "mysterious": 3, "mature": 1}},
        {"text": "拍照分享到社交平台求助", "scores": {"social": 3, "proactive": 2, "energetic": 1}}
    ]},
    {"q": "你的理想周末是怎样度过的？", "options": [
        {"text": "宅在家里看书或打游戏", "scores": {"independent": 3, "mysterious": 1, "mature": 1}},
        {"text": "出门运动、爬山或探索城市", "scores": {"energetic": 3, "proactive": 2, "playful": 1}},
        {"text": "约朋友聚会、唱K、逛街", "scores": {"social": 3, "energetic": 1, "playful": 2}},
        {"text": "学习新技能或充电提升", "scores": {"mature": 3, "independent": 2, "elegant": 1}}
    ]},
    {"q": "面对突如其来的表白，你的反应是？", "options": [
        {"text": "脸红心跳，不知所措", "scores": {"tsundere": 3, "emotional": 2, "gentle": 1}},
        {"text": "直接回应，喜欢就接受不喜欢就拒绝", "scores": {"proactive": 3, "independent": 2, "mature": 1}},
        {"text": "装作没听见或者岔开话题", "scores": {"tsundere": 2, "mysterious": 2, "playful": 1}},
        {"text": "认真思考对方是否合适自己", "scores": {"mature": 3, "independent": 2, "elegant": 1}}
    ]},
    {"q": "你最向往的生活场景是？", "options": [
        {"text": "和爱人一起做饭、看夕阳", "scores": {"gentle": 3, "loyal": 2, "emotional": 2}},
        {"text": "在世界各地冒险旅行", "scores": {"energetic": 3, "proactive": 2, "mysterious": 1}},
        {"text": "安静的图书馆或咖啡馆一角", "scores": {"elegant": 3, "independent": 2, "mysterious": 2}},
        {"text": "热闹的派对，和朋友一起嗨", "scores": {"social": 3, "energetic": 2, "playful": 2}}
    ]},
    {"q": "你认为自己的性格更偏向？", "options": [
        {"text": "温柔内敛，不爱争抢", "scores": {"gentle": 3, "elegant": 1, "mysterious": 1}},
        {"text": "活泼外向，喜欢热闹", "scores": {"energetic": 3, "social": 2, "playful": 2}},
        {"text": "理性冷静，独来独往", "scores": {"independent": 3, "mature": 2, "mysterious": 1}},
        {"text": "古灵精怪，出其不意", "scores": {"playful": 3, "mysterious": 2, "proactive": 1}}
    ]},
    {"q": "当朋友遇到困难时，你会？", "options": [
        {"text": "第一时间赶到身边支持", "scores": {"loyal": 3, "gentle": 2, "proactive": 2}},
        {"text": "帮忙想办法解决问题", "scores": {"independent": 2, "mature": 3, "proactive": 1}},
        {"text": "用幽默化解紧张气氛", "scores": {"playful": 3, "social": 2, "energetic": 1}},
        {"text": "默默关注，需要时才出手", "scores": {"mysterious": 3, "independent": 2, "tsundere": 1}}
    ]},
    # === New questions (9-12: mysterious, proactive, emotional, social) ===
    {"q": "当你面对未知的挑战时，你的第一反应是？", "options": [
        {"text": "心跳加速，但暗暗期待", "scores": {"emotional": 2, "proactive": 2, "energetic": 1}},
        {"text": "冷静评估风险后再决定", "scores": {"mature": 3, "independent": 2, "mysterious": 1}},
        {"text": "不管三七二十一先冲再说", "scores": {"energetic": 3, "proactive": 3, "playful": 1}},
        {"text": "感到一种说不清的兴奋和不安", "scores": {"mysterious": 3, "emotional": 2, "tsundere": 1}}
    ]},
    {"q": "你认为一段关系中最重要的是什么？", "options": [
        {"text": "彼此信任，无条件支持", "scores": {"loyal": 3, "gentle": 2, "emotional": 1}},
        {"text": "保持个人空间和独立性", "scores": {"independent": 3, "mature": 2, "mysterious": 1}},
        {"text": "每天都有新鲜感和惊喜", "scores": {"playful": 3, "proactive": 2, "energetic": 1}},
        {"text": "心灵的深层共鸣和理解", "scores": {"emotional": 3, "mysterious": 2, "elegant": 1}}
    ]},
    {"q": "在一个雨天，你最想做什么？", "options": [
        {"text": "泡杯热茶，听雨声发呆", "scores": {"elegant": 3, "emotional": 2, "mysterious": 1}},
        {"text": "冲进雨里淋个痛快", "scores": {"energetic": 3, "playful": 2, "proactive": 1}},
        {"text": "给想念的人打个电话", "scores": {"emotional": 3, "social": 2, "loyal": 1}},
        {"text": "窝在被窝里看恐怖小说", "scores": {"mysterious": 3, "independent": 2, "tsundere": 1}}
    ]},
    {"q": "如果你能拥有一个超能力，你会选择？", "options": [
        {"text": "读心术，看穿别人的想法", "scores": {"mysterious": 3, "emotional": 2, "tsundere": 1}},
        {"text": "瞬间移动，想去哪就去哪", "scores": {"energetic": 3, "proactive": 2, "playful": 1}},
        {"text": "时间暂停，让自己独处", "scores": {"independent": 3, "mysterious": 2, "mature": 1}},
        {"text": "治愈之力，帮助所有受伤的人", "scores": {"gentle": 3, "loyal": 2, "emotional": 2}}
    ]},
    {"q": "你面对压力时通常如何应对？", "options": [
        {"text": "找朋友倾诉，寻求安慰", "scores": {"social": 3, "emotional": 2, "gentle": 1}},
        {"text": "独自消化，静待好转", "scores": {"independent": 3, "mature": 2, "mysterious": 1}},
        {"text": "疯狂运动或打游戏发泄", "scores": {"energetic": 3, "proactive": 2, "playful": 1}},
        {"text": "分析压力源，制定解决计划", "scores": {"mature": 3, "independent": 2, "elegant": 1}}
    ]},
    {"q": "如果要送礼物给重要的人，你会选择？", "options": [
        {"text": "亲手制作的心意之作", "scores": {"gentle": 3, "emotional": 2, "loyal": 1}},
        {"text": "对方一直想要的惊喜大礼", "scores": {"proactive": 3, "playful": 2, "social": 1}},
        {"text": "一本有深度的书或唱片", "scores": {"elegant": 3, "mature": 2, "mysterious": 1}},
        {"text": "一起去某个特别的地方", "scores": {"emotional": 2, "proactive": 2, "mysterious": 2}}
    ]},
    {"q": "你最向往的旅行目的地是？", "options": [
        {"text": "历史悠久的欧洲古城", "scores": {"elegant": 3, "mature": 2, "mysterious": 1}},
        {"text": "热带海岛，阳光沙滩", "scores": {"energetic": 3, "social": 2, "playful": 1}},
        {"text": "人迹罕至的极地或沙漠", "scores": {"mysterious": 3, "independent": 2, "mature": 1}},
        {"text": "和朋友们一起的热闹主题乐园", "scores": {"social": 3, "playful": 2, "energetic": 1}}
    ]},
    {"q": "你认为自己的最大魅力在于？", "options": [
        {"text": "温暖治愈的笑容", "scores": {"gentle": 3, "emotional": 2, "social": 1}},
        {"text": "独特神秘的气质", "scores": {"mysterious": 3, "elegant": 2, "independent": 1}},
        {"text": "永不服输的冲劲", "scores": {"proactive": 3, "energetic": 2, "playful": 1}},
        {"text": "什么场合都能聊得来的社交力", "scores": {"social": 3, "playful": 2, "mature": 1}}
    ]},
    # === Questions 17-24 (deeper scenarios) ===
    {"q": "你最讨厌别人对你做什么？", "options": [
        {"text": "无视你的付出和感受", "scores": {"loyal": 3, "gentle": 2, "emotional": 1}},
        {"text": "限制你的自由和选择", "scores": {"independent": 3, "proactive": 2, "energetic": 1}},
        {"text": "对你撒谎和不信任", "scores": {"mature": 3, "mysterious": 2, "tsundere": 1}},
        {"text": "在众人面前让你难堪", "scores": {"tsundere": 3, "elegant": 2, "social": 1}}
    ]},
    {"q": "深夜睡不着时，你通常会？", "options": [
        {"text": "回忆过去，想很多有的没的", "scores": {"emotional": 3, "mysterious": 2, "gentle": 1}},
        {"text": "刷手机看视频打发时间", "scores": {"social": 2, "playful": 2, "energetic": 1}},
        {"text": "思考人生，规划未来", "scores": {"mature": 3, "independent": 2, "elegant": 1}},
        {"text": "起来做点事情，不想浪费时间", "scores": {"proactive": 3, "energetic": 2, "independent": 1}}
    ]},
    {"q": "你觉得理想的爱情是什么样的？", "options": [
        {"text": "细水长流，相濡以沫", "scores": {"gentle": 3, "loyal": 2, "mature": 1}},
        {"text": "轰轰烈烈，刻骨铭心", "scores": {"emotional": 3, "proactive": 2, "energetic": 1}},
        {"text": "心有灵犀，不言而喻", "scores": {"mysterious": 3, "elegant": 2, "emotional": 1}},
        {"text": "互相成就，共同成长", "scores": {"independent": 3, "mature": 2, "proactive": 1}}
    ]},
    {"q": "你更欣赏哪种类型的角色？", "options": [
        {"text": "温柔善良，为他人着想", "scores": {"gentle": 3, "loyal": 2, "emotional": 1}},
        {"text": "酷酷的，带着神秘感", "scores": {"mysterious": 3, "tsundere": 2, "elegant": 1}},
        {"text": "开朗活泼，元气满满", "scores": {"energetic": 3, "social": 2, "playful": 1}},
        {"text": "冷静理智，实力强大", "scores": {"mature": 3, "independent": 2, "mysterious": 1}}
    ]},
    {"q": "当你在人群中时，你通常？", "options": [
        {"text": "主动和周围人聊天", "scores": {"social": 3, "proactive": 2, "energetic": 1}},
        {"text": "安静待在角落观察", "scores": {"mysterious": 3, "independent": 2, "mature": 1}},
        {"text": "找熟人聊天，不主动搭话", "scores": {"tsundere": 2, "gentle": 2, "emotional": 1}},
        {"text": "成为话题中心，活跃气氛", "scores": {"playful": 3, "social": 2, "proactive": 1}}
    ]},
    {"q": "你最怕失去什么？", "options": [
        {"text": "重要的人的信任", "scores": {"loyal": 3, "gentle": 2, "emotional": 1}},
        {"text": "自由选择的权利", "scores": {"independent": 3, "proactive": 2, "energetic": 1}},
        {"text": "内心深处的秘密", "scores": {"mysterious": 3, "tsundere": 2, "independent": 1}},
        {"text": "和朋友们的关系", "scores": {"social": 3, "emotional": 2, "playful": 1}}
    ]},
    {"q": "你认为什么最能打动你？", "options": [
        {"text": "默默为你付出的小细节", "scores": {"gentle": 3, "emotional": 2, "loyal": 1}},
        {"text": "出其不意的浪漫惊喜", "scores": {"playful": 3, "proactive": 2, "energetic": 1}},
        {"text": "深层次的精神共鸣", "scores": {"mysterious": 3, "elegant": 2, "mature": 1}},
        {"text": "在关键时刻的坚定守护", "scores": {"loyal": 3, "mature": 2, "tsundere": 1}}
    ]},
    {"q": "如果世界末日了，你最后想做什么？", "options": [
        {"text": "和最爱的人在一起度过", "scores": {"emotional": 3, "loyal": 2, "gentle": 1}},
        {"text": "做自己一直想做但没做的事", "scores": {"proactive": 3, "energetic": 2, "playful": 1}},
        {"text": "安静地看最后的风景", "scores": {"mysterious": 3, "elegant": 2, "independent": 1}},
        {"text": "和所有朋友开个末日派对", "scores": {"social": 3, "playful": 2, "energetic": 1}}
    ]},
    # === Questions 25-36 (even deeper, covering all 12 dims) ===
    {"q": "你对待承诺的态度是？", "options": [
        {"text": "一旦承诺就会用生命去守护", "scores": {"loyal": 3, "mature": 2, "gentle": 1}},
        {"text": "视情况而定，灵活处理", "scores": {"playful": 2, "independent": 2, "proactive": 1}},
        {"text": "不轻易承诺，但说到做到", "scores": {"mysterious": 2, "mature": 3, "tsundere": 1}},
        {"text": "承诺是一种浪漫的表达", "scores": {"emotional": 3, "gentle": 2, "elegant": 1}}
    ]},
    {"q": "你的房间是什么风格？", "options": [
        {"text": "温馨整洁，充满生活气息", "scores": {"gentle": 3, "emotional": 2, "social": 1}},
        {"text": "简约冷色，干净利落", "scores": {"mature": 3, "mysterious": 2, "independent": 1}},
        {"text": "色彩缤纷，充满个性", "scores": {"playful": 3, "energetic": 2, "proactive": 1}},
        {"text": "书籍满架，文艺气息", "scores": {"elegant": 3, "mysterious": 2, "mature": 1}}
    ]},
    {"q": "当你生气时，你的表现是？", "options": [
        {"text": "沉默不语，独自消化", "scores": {"mysterious": 3, "independent": 2, "mature": 1}},
        {"text": "直接表达不满，当场解决", "scores": {"proactive": 3, "energetic": 2, "social": 1}},
        {"text": "嘴上说没事，其实很在意", "scores": {"tsundere": 3, "emotional": 2, "loyal": 1}},
        {"text": "用行动证明自己的态度", "scores": {"independent": 3, "mature": 2, "elegant": 1}}
    ]},
    {"q": "你最向往哪种超自然体验？", "options": [
        {"text": "和精灵对话，感受自然之力", "scores": {"mysterious": 3, "emotional": 2, "gentle": 1}},
        {"text": "穿越时空，改变历史", "scores": {"proactive": 3, "mysterious": 2, "energetic": 1}},
        {"text": "进入梦境，探索潜意识", "scores": {"mysterious": 3, "elegant": 2, "emotional": 1}},
        {"text": "获得读心能力，看透人心", "scores": {"tsundere": 2, "mysterious": 3, "social": 1}}
    ]},
    {"q": "你觉得什么样的笑容最迷人？", "options": [
        {"text": "温暖如阳光的微笑", "scores": {"gentle": 3, "emotional": 2, "social": 1}},
        {"text": "带着自信的爽朗大笑", "scores": {"energetic": 3, "proactive": 2, "playful": 1}},
        {"text": "若隐若现的神秘微笑", "scores": {"mysterious": 3, "elegant": 2, "mature": 1}},
        {"text": "害羞时偷笑的样子", "scores": {"tsundere": 3, "emotional": 2, "gentle": 1}}
    ]},
    {"q": "你最想拥有的技能是？", "options": [
        {"text": "烹饪出治愈人心的美食", "scores": {"gentle": 3, "social": 2, "emotional": 1}},
        {"text": "战斗能力，保护重要的人", "scores": {"loyal": 3, "proactive": 2, "energetic": 1}},
        {"text": "洞察一切的分析能力", "scores": {"mature": 3, "mysterious": 2, "independent": 1}},
        {"text": "让任何人都开心的社交术", "scores": {"social": 3, "playful": 2, "proactive": 1}}
    ]},
    {"q": "你的手机里最多的APP是？", "options": [
        {"text": "社交软件，随时和朋友聊天", "scores": {"social": 3, "playful": 2, "energetic": 1}},
        {"text": "阅读和学习类APP", "scores": {"mature": 3, "independent": 2, "elegant": 1}},
        {"text": "游戏和娱乐类APP", "scores": {"playful": 3, "energetic": 2, "proactive": 1}},
        {"text": "摄影和艺术类APP", "scores": {"emotional": 3, "mysterious": 2, "elegant": 1}}
    ]},
    {"q": "你认为最强的力量是？", "options": [
        {"text": "温柔，能融化一切", "scores": {"gentle": 3, "emotional": 2, "loyal": 1}},
        {"text": "意志，永不放弃", "scores": {"loyal": 3, "proactive": 2, "mature": 1}},
        {"text": "智慧，运筹帷幄", "scores": {"mature": 3, "mysterious": 2, "independent": 1}},
        {"text": "勇气，直面恐惧", "scores": {"proactive": 3, "energetic": 2, "playful": 1}}
    ]},
    {"q": "你更喜欢哪个季节？", "options": [
        {"text": "春天，万物生长的季节", "scores": {"gentle": 3, "emotional": 2, "playful": 1}},
        {"text": "夏天，充满活力的季节", "scores": {"energetic": 3, "social": 2, "proactive": 1}},
        {"text": "秋天，沉静优雅的季节", "scores": {"elegant": 3, "mature": 2, "mysterious": 1}},
        {"text": "冬天，安静神秘的季节", "scores": {"mysterious": 3, "independent": 2, "tsundere": 1}}
    ]},
    {"q": "你的口头禅类型是？", "options": [
        {"text": "鼓励和温暖的话", "scores": {"gentle": 3, "emotional": 2, "social": 1}},
        {"text": "毒舌和吐槽", "scores": {"tsundere": 3, "playful": 2, "social": 1}},
        {"text": "冷静的分析和判断", "scores": {"mature": 3, "independent": 2, "mysterious": 1}},
        {"text": "神秘又意味深长的话", "scores": {"mysterious": 3, "elegant": 2, "emotional": 1}}
    ]},
    {"q": "你的理想职业是？", "options": [
        {"text": "教师或心理咨询师，帮助他人", "scores": {"gentle": 3, "emotional": 2, "social": 1}},
        {"text": "探险家或运动员，挑战极限", "scores": {"energetic": 3, "proactive": 2, "playful": 1}},
        {"text": "科学家或研究员，探索未知", "scores": {"mysterious": 3, "independent": 2, "mature": 1}},
        {"text": "艺术家或设计师，创造美", "scores": {"elegant": 3, "emotional": 2, "mysterious": 1}}
    ]},
    {"q": "最后，你希望你的另一半具备什么品质？", "options": [
        {"text": "温柔体贴，永远在你身边", "scores": {"gentle": 3, "loyal": 2, "emotional": 1}},
        {"text": "有趣好玩，每天都不一样", "scores": {"playful": 3, "energetic": 2, "proactive": 1}},
        {"text": "成熟稳重，可以依靠", "scores": {"mature": 3, "independent": 2, "elegant": 1}},
        {"text": "神秘迷人，永远猜不透", "scores": {"mysterious": 3, "tsundere": 2, "elegant": 1}}
    ]},
]

# Dimension labels
dimensions = [
    {"key": "gentle", "label": "温柔", "color": "#ff6b9d"},
    {"key": "energetic", "label": "活力", "color": "#fbbf24"},
    {"key": "independent", "label": "独立", "color": "#4ade80"},
    {"key": "playful", "label": "俏皮", "color": "#f472b6"},
    {"key": "loyal", "label": "忠诚", "color": "#60a5fa"},
    {"key": "tsundere", "label": "傲娇", "color": "#f87171"},
    {"key": "elegant", "label": "优雅", "color": "#a78bfa"},
    {"key": "mature", "label": "成熟", "color": "#34d399"},
    {"key": "mysterious", "label": "神秘", "color": "#818cf8"},
    {"key": "proactive", "label": "主动", "color": "#fb923c"},
    {"key": "emotional", "label": "感性", "color": "#e879f9"},
    {"key": "social", "label": "社交", "color": "#22d3ee"},
]

# Build the HTML
html = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0,maximum-scale=1.0,user-scalable=no">
<title>二次元老婆匹配器 - 80角色12维度精准匹配</title>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700&family=ZCOOL+KuaiLe&display=swap" rel="stylesheet">
<style>
*{margin:0;padding:0;box-sizing:border-box;-webkit-tap-highlight-color:transparent}
:root{
--pink:#e879f9;--purple:#a855f7;--bg:#0b0a12;--card:#15131f;--card2:#1d1b2e;
--text:#f8f7fc;--dim:#9ca3af;--border:rgba(232,121,249,0.25);
--radius:16px;
}
html{scroll-behavior:smooth}
body{
font-family:'Noto Sans SC',sans-serif;
background:var(--bg);color:var(--text);min-height:100vh;overflow-x:hidden;
}
#particles{position:fixed;top:0;left:0;width:100%;height:100%;z-index:0;pointer-events:none}
.page{display:none;position:relative;z-index:1;min-height:100vh;padding:20px;max-width:800px;margin:0 auto}
.page.active{display:block}
.page-enter{animation:fadeIn .5s ease}
@keyframes fadeIn{from{opacity:0;transform:translateY(20px)}to{opacity:1;transform:translateY(0)}}
.btn{
padding:14px 32px;border:none;border-radius:12px;font-size:16px;font-weight:700;
cursor:pointer;transition:all .3s;display:inline-flex;align-items:center;gap:8px;
font-family:inherit;
}
.btn-primary{
background:linear-gradient(135deg,var(--pink),var(--purple));
color:#fff;box-shadow:0 4px 20px rgba(168,85,247,0.4);
}
.btn-primary:hover{transform:translateY(-2px);box-shadow:0 8px 30px rgba(168,85,247,0.5)}
.btn-ghost{
background:transparent;color:var(--text);
border:1px solid var(--border);
}
.btn-ghost:hover{background:rgba(232,121,249,0.1)}
/* HOME */
.home-hero{text-align:center;padding:40px 0}
.home-badge{
display:inline-block;padding:6px 16px;border-radius:20px;
background:rgba(232,121,249,0.1);border:1px solid var(--border);
font-size:13px;color:var(--pink);margin-bottom:24px;
}
.home-title{
font-family:'ZCOOL KuaiLe',cursive;font-size:42px;line-height:1.3;margin-bottom:16px;
}
.home-title .grad{
background:linear-gradient(135deg,var(--pink),var(--purple));
-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;
}
.home-desc{color:var(--dim);font-size:15px;line-height:1.8;margin-bottom:32px;max-width:500px;margin-left:auto;margin-right:auto}
.home-buttons{display:flex;gap:16px;justify-content:center;flex-wrap:wrap}
/* QUIZ */
.quiz-header{margin-bottom:24px}
.quiz-progress-text{text-align:center;font-size:14px;color:var(--dim);margin-bottom:8px}
.quiz-progress-bar{width:100%;height:6px;background:var(--card);border-radius:3px;overflow:hidden}
.quiz-progress-fill{height:100%;background:linear-gradient(90deg,var(--pink),var(--purple));border-radius:3px;transition:width .3s}
.quiz-card{
background:var(--card);border:1px solid var(--border);border-radius:var(--radius);
padding:32px 24px;margin-bottom:24px;
}
.quiz-question{font-size:20px;font-weight:700;margin-bottom:24px;line-height:1.5}
.quiz-options{display:flex;flex-direction:column;gap:12px}
.quiz-option{
padding:16px;border:1px solid var(--border);border-radius:12px;
background:var(--card2);cursor:pointer;transition:all .2s;
display:flex;align-items:center;gap:12px;font-size:15px;color:var(--text);
font-family:inherit;text-align:left;
}
.quiz-option:hover{border-color:var(--pink);background:rgba(232,121,249,0.05)}
.quiz-option.selected{
border-color:var(--pink);background:rgba(232,121,249,0.15);
box-shadow:0 0 0 1px var(--pink);
}
.quiz-option-letter{
width:32px;height:32px;border-radius:50%;border:2px solid var(--border);
display:flex;align-items:center;justify-content:center;font-weight:700;
flex-shrink:0;transition:all .2s;
}
.quiz-option.selected .quiz-option-letter{
border-color:var(--pink);background:var(--pink);color:#fff;
}
.quiz-nav{display:flex;justify-content:space-between;gap:12px}
/* RESULT */
.result-card{
background:var(--card);border:1px solid var(--border);border-radius:var(--radius);
overflow:hidden;margin-bottom:24px;
}
.result-image-wrap{
width:100%;background:var(--card2);display:flex;align-items:center;
justify-content:center;overflow:hidden;
}
.result-image-wrap img{
max-width:100%;max-height:500px;object-fit:contain;display:block;
}
.result-info{padding:24px}
.result-series{font-size:13px;color:var(--pink);margin-bottom:4px}
.result-name{font-size:28px;font-weight:700;margin-bottom:8px}
.result-match{font-size:36px;font-weight:900;background:linear-gradient(135deg,var(--pink),var(--purple));-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.result-tags{display:flex;gap:8px;flex-wrap:wrap;margin:12px 0}
.result-tag{padding:4px 12px;border-radius:20px;background:rgba(232,121,249,0.1);font-size:12px;color:var(--pink)}
.result-desc{color:var(--dim);font-size:14px;line-height:1.8;margin:16px 0}
.result-analysis{
background:var(--card2);border-radius:12px;padding:20px;margin:16px 0;
border-left:3px solid var(--pink);
}
.result-analysis h3{font-size:16px;margin-bottom:12px;color:var(--pink)}
.result-analysis p{font-size:14px;line-height:1.8;color:var(--text)}
.radar-chart-wrap{display:flex;justify-content:center;margin:24px 0}
.result-recommendations{margin-top:24px}
.result-recommendations h3{font-size:18px;margin-bottom:16px}
.rec-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(140px,1fr));gap:12px}
.rec-card{
background:var(--card2);border:1px solid var(--border);border-radius:12px;
overflow:hidden;cursor:pointer;transition:all .2s;
}
.rec-card:hover{border-color:var(--pink);transform:translateY(-2px)}
.rec-image-wrap{
width:100%;aspect-ratio:3/4;overflow:hidden;background:var(--bg);
}
.rec-image-wrap img{width:100%;height:100%;object-fit:cover}
.rec-info{padding:8px}
.rec-name{font-size:13px;font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.rec-match{font-size:12px;color:var(--pink)}
/* GALLERY */
.gallery-header{display:flex;justify-content:space-between;align-items:center;margin-bottom:24px}
.gallery-title{font-size:24px;font-weight:700}
.gallery-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:16px}
.gallery-card{
background:var(--card);border:1px solid var(--border);border-radius:var(--radius);
overflow:hidden;cursor:pointer;transition:all .2s;
}
.gallery-card:hover{border-color:var(--pink);transform:translateY(-4px);box-shadow:0 8px 30px rgba(168,85,247,0.2)}
.gallery-image-wrap{
width:100%;background:var(--card2);overflow:hidden;
display:flex;align-items:center;justify-content:center;min-height:200px;
}
.gallery-image-wrap img{
max-width:100%;max-height:300px;object-fit:contain;display:block;
}
.gallery-info{padding:12px}
.gallery-name{font-size:14px;font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.gallery-series{font-size:12px;color:var(--dim);margin-top:2px}
/* MODAL */
.modal-overlay{
position:fixed;top:0;left:0;width:100%;height:100%;
background:rgba(0,0,0,0.8);z-index:100;display:none;
align-items:center;justify-content:center;padding:20px;
}
.modal-overlay.active{display:flex}
.modal-content{
background:var(--card);border:1px solid var(--border);border-radius:var(--radius);
max-width:500px;max-height:90vh;overflow-y:auto;width:100%;
}
.modal-image-wrap{
width:100%;background:var(--card2);display:flex;align-items:center;
justify-content:center;overflow:hidden;
}
.modal-image-wrap img{max-width:100%;max-height:400px;object-fit:contain}
.modal-body{padding:24px}
.modal-close{
position:absolute;top:16px;right:16px;width:36px;height:36px;
border-radius:50%;background:rgba(0,0,0,0.5);border:none;color:#fff;
font-size:20px;cursor:pointer;display:flex;align-items:center;justify-content:center;
}
/* MOBILE */
@media(max-width:600px){
.home-title{font-size:32px}
.quiz-card{padding:20px 16px}
.quiz-question{font-size:18px}
.gallery-grid{grid-template-columns:repeat(2,1fr)}
.rec-grid{grid-template-columns:repeat(2,1fr)}
.result-image-wrap img{max-height:350px}
}
.watermark{position:fixed;bottom:12px;right:12px;font-size:11px;color:rgba(255,255,255,0.3);z-index:50}
</style>
</head>
<body>
<canvas id="particles"></canvas>

<!-- HOME PAGE -->
<div class="page active" id="page-home">
  <div class="home-hero">
    <div class="home-badge">80位经典角色 12维性格精准匹配</div>
    <h1 class="home-title">二次元老婆<span class="grad">匹配器</span></h1>
    <p class="home-desc">穿越霓虹闪烁的次元之门，回答 36 道精心设计的性格测试题，我们将从 80 位人气 galgame 与动漫角色中，用余弦相似度混合加权欧氏距离算法，找到与你灵魂共鸣的她。</p>
    <div class="home-buttons">
      <button class="btn btn-primary" onclick="goQuiz()">开始测试</button>
      <button class="btn btn-ghost" onclick="goGallery()">角色图鉴</button>
    </div>
  </div>
</div>

<!-- QUIZ PAGE -->
<div class="page" id="page-quiz">
  <div class="quiz-header">
    <div class="quiz-progress-text" id="quizProgress">第 1 / 36 题</div>
    <div class="quiz-progress-bar"><div class="quiz-progress-fill" id="quizBar" style="width:2.7%"></div></div>
  </div>
  <div class="quiz-card" id="quizCard"></div>
  <div class="quiz-nav">
    <button class="btn btn-ghost" id="btnPrev" onclick="prevQuestion()">上一题</button>
    <button class="btn btn-primary" id="btnNext" onclick="nextQuestion()">下一题</button>
  </div>
</div>

<!-- RESULT PAGE -->
<div class="page" id="page-result">
  <div id="resultContent"></div>
  <div style="text-align:center;margin-top:24px">
    <button class="btn btn-primary" onclick="goQuiz()">重新测试</button>
    <button class="btn btn-ghost" onclick="goGallery()">角色图鉴</button>
  </div>
</div>

<!-- GALLERY PAGE -->
<div class="page" id="page-gallery">
  <div class="gallery-header">
    <div class="gallery-title">角色图鉴</div>
    <button class="btn btn-ghost" onclick="goHome()">返回首页</button>
  </div>
  <p style="color:var(--dim);font-size:14px;margin-bottom:16px">共 80 位角色 - 点击卡片查看详情</p>
  <div class="gallery-grid" id="galleryGrid"></div>
</div>

<!-- MODAL -->
<div class="modal-overlay" id="modal" onclick="closeModal(event)">
  <div class="modal-content" style="position:relative" onclick="event.stopPropagation()">
    <button class="modal-close" onclick="closeModal()">&times;</button>
    <div id="modalContent"></div>
  </div>
</div>

<div class="watermark">DuMate</div>

<script>
// DATA
const CHARACTERS = ''' + json.dumps(characters, ensure_ascii=False) + ''';
const QUESTIONS = ''' + json.dumps(questions, ensure_ascii=False) + ''';
const DIMENSIONS = ''' + json.dumps(dimensions, ensure_ascii=False) + ''';

// STATE
let currentQ = 0;
let answers = new Array(QUESTIONS.length).fill(null);

// PARTICLES
const canvas=document.getElementById('particles');
const ctx=canvas.getContext('2d');
let particles=[];
function resizeCanvas(){canvas.width=window.innerWidth;canvas.height=window.innerHeight}
resizeCanvas();
window.addEventListener('resize',resizeCanvas);
function initParticles(){
particles=[];
const count=Math.min(80,Math.floor(window.innerWidth/15));
for(let i=0;i<count;i++){
particles.push({
x:Math.random()*canvas.width,y:Math.random()*canvas.height,
r:Math.random()*2+0.5,sx:(Math.random()-0.5)*0.3,sy:(Math.random()-0.5)*0.3,
a:Math.random()*0.5+0.1,c:Math.random()>0.5?'232,121,249':'168,85,247'
});
}
}
initParticles();
function animateParticles(){
ctx.clearRect(0,0,canvas.width,canvas.height);
particles.forEach(p=>{
p.x+=p.sx;p.y+=p.sy;
if(p.x<0)p.x=canvas.width;if(p.x>canvas.width)p.x=0;
if(p.y<0)p.y=canvas.height;if(p.y>canvas.height)p.y=0;
ctx.beginPath();ctx.arc(p.x,p.y,p.r,0,Math.PI*2);
ctx.fillStyle='rgba('+p.c+','+p.a+')';ctx.fill();
});
requestAnimationFrame(animateParticles);
}
animateParticles();

// NAVIGATION
function showPage(id){
document.querySelectorAll('.page').forEach(p=>{p.classList.remove('active','page-enter')});
const page=document.getElementById(id);
page.classList.add('active','page-enter');
window.scrollTo(0,0);
}
function goHome(){showPage('page-home')}
function goQuiz(){currentQ=0;answers.fill(null);showPage('page-quiz');renderQuestion()}
function goGallery(){showPage('page-gallery');renderGallery()}
function goResult(){showPage('page-result');renderResult()}

// QUIZ
function renderQuestion(){
const q=QUESTIONS[currentQ];
const letters=['A','B','C','D'];
let html='<div class="quiz-question">'+(currentQ+1)+'. '+q.q+'</div><div class="quiz-options">';
q.options.forEach((opt,i)=>{
const sel=answers[currentQ]===i?'selected':'';
html+='<button class="quiz-option '+sel+'" onclick="selectOption('+i+')"><div class="quiz-option-letter">'+letters[i]+'</div><span>'+opt.text+'</span></button>';
});
html+='</div>';
document.getElementById('quizCard').innerHTML=html;
document.getElementById('quizProgress').textContent='\\u7b2c '+(currentQ+1)+' / '+QUESTIONS.length+' \\u9898';
document.getElementById('quizBar').style.width=((currentQ+1)/QUESTIONS.length*100)+'%';
document.getElementById('btnPrev').style.visibility=currentQ===0?'hidden':'visible';
document.getElementById('btnNext').textContent=currentQ===QUESTIONS.length-1?'\\u63d0\\u4ea4':'\\u4e0b\\u4e00\\u9898';
}
function selectOption(i){answers[currentQ]=i;renderQuestion()}
function prevQuestion(){if(currentQ>0){currentQ--;renderQuestion()}}
function nextQuestion(){
if(answers[currentQ]===null){alert('\\u8bf7\\u5148\\u9009\\u62e9\\u4e00\\u4e2a\\u9009\\u9879');return}
if(currentQ<QUESTIONS.length-1){currentQ++;renderQuestion()}
else{goResult()}
}

// MATCHING ALGORITHM
function calculateUserVector(){
const vec={};
DIMENSIONS.forEach(d=>vec[d.key]=50);
QUESTIONS.forEach((q,i)=>{
const ans=answers[i];
if(ans===null)return;
const opt=q.options[ans];
if(!opt.scores)return;
for(const[key,val]of Object.entries(opt.scores)){
if(vec[key]!==undefined){vec[key]+=val*8}
}
});
DIMENSIONS.forEach(d=>{vec[d.key]=Math.max(0,Math.min(100,vec[d.key]))});
return vec;
}
function cosineSimilarity(a,b){
let dot=0,normA=0,normB=0;
DIMENSIONS.forEach(d=>{
const av=a[d.key],bv=b[d.key];
dot+=av*bv;normA+=av*av;normB+=bv*bv;
});
return dot/(Math.sqrt(normA)*Math.sqrt(normB)||1);
}
function euclideanDistance(a,b){
let sum=0;
DIMENSIONS.forEach(d=>{
const diff=a[d.key]-b[d.key];
sum+=diff*diff;
});
return Math.sqrt(sum);
}
function maxEuclidean(){
return Math.sqrt(DIMENSIONS.length)*100;
}
function matchCharacter(userVec,char){
const charVec={};
DIMENSIONS.forEach((d,i)=>{charVec[d.key]=char.traits[i]});
const cos=cosineSimilarity(userVec,charVec);
const euc=euclideanDistance(userVec,charVec);
const normEuc=1-euc/maxEuclidean();
const score=0.6*cos+0.4*normEuc;
return Math.round(score*100);
}
function generateAnalysis(userVec,char){
const topDims=[];
const lowDims=[];
DIMENSIONS.forEach((d,i)=>{
const diff=Math.abs(userVec[d.key]-char.traits[i]);
if(userVec[d.key]>70){topDims.push({label:d.label,key:d.key,userVal:userVec[d.key],charVal:char.traits[i]})}
if(userVal<40&&char.traits[i]<40){lowDims.push(d.label)}
});
const topLabels=topDims.slice(0,3).map(d=>d.label).join('\\u3001');
let analysis='\\u4f60\\u7684\\u6027\\u683c\\u5728\\u300c'+topLabels+'\\u300d\\u7ef4\\u5ea6\\u4e0a\\u8868\\u73b0\\u6700\\u4e3a\\u7a81\\u51fa\\uff0c\\u800c'+char.name+'\\u6b63\\u662f\\u4ee5\\u8fd9\\u4e9b\\u7279\\u8d28\\u8457\\u79f0\\u7684\\u89d2\\u8272\\u3002';
analysis+=char.description;
analysis+='\\u4f60\\u4eec\\u7684\\u6838\\u5fc3\\u6c14\\u8d28\\u9ad8\\u5ea6\\u5171\\u9e23\\uff0c\\u5f7c\\u6b64\\u4e4b\\u95f4\\u7684\\u5dee\\u5f02\\u6070\\u597d\\u5f62\\u6210\\u4e86\\u4e92\\u8865\\u3002';
if(topDims.length>0){
analysis+='\\u5728\\u300c'+topDims[0].label+'\\u300d\\u4e0a\\u4f60\\u5f97\\u5206'+topDims[0].userVal+'\\uff0c\\u5979\\u540c\\u6837\\u62e5\\u6709'+topDims[0].charVal+'\\u7684\\u9ad8\\u5206\\uff0c\\u8fd9\\u610f\\u5473\\u7740\\u4f60\\u4eec\\u80fd\\u591f\\u6df1\\u5c42\\u6b21\\u5730\\u7406\\u89e3\\u5f7c\\u6b64\\u7684\\u5185\\u5fc3\\u4e16\\u754c\\u3002';
}
analysis+='\\u4eff\\u4f5b\\u5979\\u5c31\\u662f\\u4e3a\\u4e86\\u4e0e\\u4f60\\u76f8\\u9047\\u800c\\u5b58\\u5728\\u7684\\u3002';
return analysis;
}
function generateUserProfile(userVec){
const sorted=DIMENSIONS.map((d,i)=>({label:d.label,key:d.key,val:userVec[d.key],color:d.color})).sort((a,b)=>b.val-a.val);
let profile='\\u4f60\\u7684\\u6027\\u683c\\u753b\\u50cf\\u5448\\u73b0\\u51fa\\u4ee5\\u300c'+sorted[0].label+'\\u3001'+sorted[1].label+'\\u3001'+sorted[2].label+'\\u300d\\u4e3a\\u4e3b\\u5bfc\\u7684\\u7279\\u8d28\\u3002';
if(sorted[0].val>80){profile+='\\u4f60\\u5728\\u300c'+sorted[0].label+'\\u300d\\u7ef4\\u5ea6\\u4e0a\\u8868\\u73b0\\u6781\\u4e3a\\u7a81\\u51fa\\uff0c\\u8fd9\\u662f\\u4f60\\u6700\\u6838\\u5fc3\\u7684\\u4eba\\u683c\\u9b45\\u529b\\u6240\\u5728\\u3002'}
if(sorted[sorted.length-1].val<40){profile+='\\u76f8\\u5bf9\\u5730\\uff0c\\u300c'+sorted[sorted.length-1].label+'\\u300d\\u662f\\u4f60\\u8f83\\u4e3a\\u5f31\\u7684\\u7ef4\\u5ea6\\uff0c\\u4f46\\u8fd9\\u4e5f\\u6b63\\u662f\\u4f60\\u72ec\\u7279\\u7684\\u4e00\\u9762\\u3002'}
return profile;
}

// RESULT
function renderResult(){
const userVec=calculateUserVector();
const scored=CHARACTERS.map(c=>({...c,matchScore:matchCharacter(userVec,c)}));
scored.sort((a,b)=>b.matchScore-a.matchScore);
const best=scored[0];
const top5=scored.slice(0,5);
const tags=best.tags.split(',');
const analysis=generateAnalysis(userVec,best);
const profile=generateUserProfile(userVec);

let html='<div class="result-card">';
html+='<div class="result-image-wrap"><img src="'+best.image+'" alt="'+best.name+'" onerror="this.src=\\'data:image/svg+xml,<svg xmlns=\\'http://www.w3.org/2000/svg\\' width=\\'300\\' height=\\'400\\'><rect width=\\'100%25\\' height=\\'100%25\\' fill=\\'%2315131f\\'/><text x=\\'50%25\\' y=\\'50%25\\' fill=\\'%23e879f9\\' text-anchor=\\'middle\\' dy=\\'.3em\\' font-size=\\'20\\'>' + best.name + '</text></svg>\\'" loading="lazy"></div>';
html+='<div class="result-info">';
html+='<div class="result-series">'+best.series+'</div>';
html+='<h2 class="result-name">'+best.name+'</h2>';
html+='<div class="result-match">\\u5951\\u5408\\u5ea6 '+best.matchScore+'%</div>';
html+='<div class="result-tags">';
tags.forEach(t=>{html+='<span class="result-tag">'+t+'</span>'});
html+='</div>';
html+='<p class="result-desc">'+best.appearance+'</p>';
html+='</div></div>';

// Analysis
html+='<div class="result-analysis"><h3>\\u4e3a\\u4ec0\\u4e48\\u662f\\u5979\\uff1f</h3><p>'+analysis+'</p></div>';

// User profile
html+='<div class="result-analysis"><h3>\\u4f60\\u7684\\u6027\\u683c\\u753b\\u50cf</h3><p>'+profile+'</p></div>';

// Radar chart
html+='<div class="radar-chart-wrap"><canvas id="radarChart" width="400" height="400"></canvas></div>';

// Top 5
html+='<div class="result-recommendations"><h3>\\u5176\\u4ed6\\u63a8\\u8350\\u89d2\\u8272</h3><div class="rec-grid">';
top5.slice(1).forEach(c=>{
html+='<div class="rec-card" onclick="showCharDetail(\\''+c.id+'\\')">';
html+='<div class="rec-image-wrap"><img src="'+c.image+'" alt="'+c.name+'" onerror="this.style.display=\\'none\\'" loading="lazy"></div>';
html+='<div class="rec-info"><div class="rec-name">'+c.name+'</div><div class="rec-match">'+c.matchScore+'%</div></div>';
html+='</div>';
});
html+='</div></div>';

document.getElementById('resultContent').innerHTML=html;

// Draw radar chart
drawRadarChart(userVec,best);
}

// RADAR CHART
function drawRadarChart(userVec,char){
const canvas=document.getElementById('radarChart');
if(!canvas)return;
const ctx=canvas.getContext('2d');
const cx=200,cy=200,radius=150;
const n=DIMENSIONS.length;
const angleStep=(Math.PI*2)/n;

ctx.clearRect(0,0,400,400);

// Draw grid
for(let level=1;level<=4;level++){
ctx.beginPath();
for(let i=0;i<=n;i++){
const angle=i*angleStep-Math.PI/2;
const r=radius*(level/4);
const x=cx+Math.cos(angle)*r;
const y=cy+Math.sin(angle)*r;
if(i===0)ctx.moveTo(x,y);else ctx.lineTo(x,y);
}
ctx.strokeStyle='rgba(232,121,249,'+(0.1+level*0.05)+')';
ctx.lineWidth=1;
ctx.stroke();
}

// Draw axes and labels
DIMENSIONS.forEach((d,i)=>{
const angle=i*angleStep-Math.PI/2;
const x=cx+Math.cos(angle)*(radius+20);
const y=cy+Math.sin(angle)*(radius+20);
ctx.fillStyle='#9ca3af';
ctx.font='12px Noto Sans SC';
ctx.textAlign='center';
ctx.textBaseline='middle';
ctx.fillText(d.label,x,y);
});

// Draw character polygon
ctx.beginPath();
DIMENSIONS.forEach((d,i)=>{
const angle=i*angleStep-Math.PI/2;
const val=char.traits[i]/100;
const r=radius*val;
const x=cx+Math.cos(angle)*r;
const y=cy+Math.sin(angle)*r;
if(i===0)ctx.moveTo(x,y);else ctx.lineTo(x,y);
});
ctx.closePath();
ctx.fillStyle='rgba(168,85,247,0.15)';
ctx.strokeStyle='rgba(168,85,247,0.8)';
ctx.lineWidth=2;
ctx.fill();
ctx.stroke();

// Draw user polygon
ctx.beginPath();
DIMENSIONS.forEach((d,i)=>{
const angle=i*angleStep-Math.PI/2;
const val=userVec[d.key]/100;
const r=radius*val;
const x=cx+Math.cos(angle)*r;
const y=cy+Math.sin(angle)*r;
if(i===0)ctx.moveTo(x,y);else ctx.lineTo(x,y);
});
ctx.closePath();
ctx.fillStyle='rgba(232,121,249,0.15)';
ctx.strokeStyle='rgba(232,121,249,0.8)';
ctx.lineWidth=2;
ctx.fill();
ctx.stroke();

// Legend
ctx.fillStyle='rgba(232,121,249,0.8)';
ctx.fillRect(20,370,12,12);
ctx.fillStyle='#f8f7fc';
ctx.font='12px Noto Sans SC';
ctx.textAlign='left';
ctx.fillText('\\u4f60\\u7684\\u6027\\u683c',40,378);
ctx.fillStyle='rgba(168,85,247,0.8)';
ctx.fillRect(120,370,12,12);
ctx.fillStyle='#f8f7fc';
ctx.fillText(char.name,140,378);
}

// GALLERY
function renderGallery(){
let html='';
CHARACTERS.forEach(c=>{
html+='<div class="gallery-card" onclick="showCharDetail(\\''+c.id+'\\')">';
html+='<div class="gallery-image-wrap"><img src="'+c.image+'" alt="'+c.name+'" onerror="this.style.display=\\'none\\'" loading="lazy"></div>';
html+='<div class="gallery-info"><div class="gallery-name">'+c.name+'</div><div class="gallery-series">'+c.series+'</div></div>';
html+='</div>';
});
document.getElementById('galleryGrid').innerHTML=html;
}

// MODAL
function showCharDetail(id){
const c=CHARACTERS.find(x=>x.id===id);
if(!c)return;
const tags=c.tags.split(',');
let html='<div class="modal-image-wrap"><img src="'+c.image+'" alt="'+c.name+'" onerror="this.style.display=\\'none\\'" loading="lazy"></div>';
html+='<div class="modal-body">';
html+='<div style="font-size:13px;color:var(--pink);margin-bottom:4px">'+c.series+'</div>';
html+='<h2 style="font-size:24px;margin-bottom:8px">'+c.name+'</h2>';
html+='<div style="display:flex;gap:8px;flex-wrap:wrap;margin-bottom:12px">';
tags.forEach(t=>{html+='<span class="result-tag">'+t+'</span>'});
html+='</div>';
html+='<p style="color:var(--dim);font-size:14px;line-height:1.8;margin-bottom:12px">'+c.appearance+'</p>';
html+='<p style="font-size:14px;line-height:1.8">'+c.description+'</p>';
html+='<h3 style="font-size:14px;margin:16px 0 8px;color:var(--pink)">\\u6027\\u683c\\u7ef4\\u5ea6</h3>';
html+='<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:8px">';
DIMENSIONS.forEach((d,i)=>{
const val=c.traits[i];
html+='<div style="text-align:center"><div style="font-size:12px;color:var(--dim)">'+d.label+'</div><div style="font-size:18px;font-weight:700;color:'+(val>70?'var(--pink)':val>40?'var(--text)':'var(--dim)')+'">'+val+'</div></div>';
});
html+='</div>';
html+='</div>';
document.getElementById('modalContent').innerHTML=html;
document.getElementById('modal').classList.add('active');
}
function closeModal(e){
if(e&&e.target!==document.getElementById('modal'))return;
document.getElementById('modal').classList.remove('active');
}

// INIT
goHome();
</script>
</body>
</html>'''

output_path = '/home/work/dumate/ba849ae564f04117b0c123c600d87806/workspace/ses_01aa3bfb9ffezurCsuzN0y3Th7/waifu-match/index-v2.html'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html)

import os
size = os.path.getsize(output_path)
print(f"Generated index-v2.html: {size} bytes ({size/1024:.1f} KB)")
print(f"Characters: {len(characters)}")
print(f"Questions: {len(questions)}")
print(f"Dimensions: {len(dimensions)}")
