#!/usr/bin/env python3
"""Generate the ultimate enhanced waifu-match HTML with all 6 enrichment directions"""
import json

with open('characters_enriched.json', 'r', encoding='utf-8') as f:
    chars = json.load(f)

dims = [
    {"key":"gentle","label":"温柔","color":"#ff6b9d","icon":"🌸"},
    {"key":"energetic","label":"活力","color":"#fbbf24","icon":"⚡"},
    {"key":"independent","label":"独立","color":"#4ade80","icon":"🌿"},
    {"key":"playful","label":"俏皮","color":"#f472b6","icon":"🎀"},
    {"key":"loyal","label":"忠诚","color":"#60a5fa","icon":"🛡️"},
    {"key":"tsundere","label":"傲娇","color":"#f87171","icon":"💢"},
    {"key":"elegant","label":"优雅","color":"#a78bfa","icon":"💎"},
    {"key":"mature","label":"成熟","color":"#34d399","icon":"📖"},
    {"key":"mysterious","label":"神秘","color":"#818cf8","icon":"🌙"},
    {"key":"proactive","label":"主动","color":"#fb923c","icon":"🔥"},
    {"key":"emotional","label":"感性","color":"#e879f9","icon":"💗"},
    {"key":"social","label":"社交","color":"#22d3ee","icon":"✨"}
]

questions = [
    {"q":"当朋友难过时，你通常会怎么做？","emoji":"😢","o":[
        {"t":"静静陪伴，听对方倾诉，递上一杯热饮","s":{"gentle":3,"mature":1,"social":-1}},
        {"t":"讲笑话或做鬼脸逗对方开心，活跃气氛","s":{"energetic":3,"playful":2,"proactive":1}},
        {"t":"冷静分析问题并给出务实的建议","s":{"independent":2,"mature":3,"mysterious":1}},
        {"t":"拉对方出去运动或吃美食散心","s":{"energetic":2,"proactive":3,"social":2}}]},
    {"q":"你更喜欢怎样的相处模式？","emoji":"💕","o":[
        {"t":"温柔体贴，照顾对方的每一个情绪变化","s":{"gentle":3,"loyal":1,"emotional":2}},
        {"t":"打打闹闹，像伙伴一样轻松无压力","s":{"playful":3,"energetic":2,"social":1}},
        {"t":"各自独立，有事才联系，互不干涉","s":{"independent":3,"mature":2,"mysterious":1}},
        {"t":"时刻陪伴，保持紧密联系，彼此依赖","s":{"loyal":3,"proactive":2,"emotional":2}}]},
    {"q":"看到路边受伤的小动物，你会？","emoji":"🐾","o":[
        {"t":"心疼地想带它去治疗，悉心照料","s":{"gentle":3,"emotional":2,"loyal":1}},
        {"t":"蹲下来逗它玩，让它忘掉痛苦","s":{"playful":3,"energetic":1,"social":1}},
        {"t":"观察一下情况，默默离开","s":{"independent":2,"mysterious":3,"mature":1}},
        {"t":"拍照分享到社交平台求助","s":{"social":3,"proactive":2,"energetic":1}}]},
    {"q":"你的理想周末是怎样度过的？","emoji":"🌤️","o":[
        {"t":"宅在家里看书或打游戏，享受独处","s":{"independent":3,"mysterious":1,"mature":1}},
        {"t":"出门运动、爬山或探索城市","s":{"energetic":3,"proactive":2,"playful":1}},
        {"t":"约朋友聚会、唱K、逛街","s":{"social":3,"energetic":1,"playful":2}},
        {"t":"学习新技能或充电提升自己","s":{"mature":3,"independent":2,"elegant":1}}]},
    {"q":"面对突如其来的表白，你的反应是？","emoji":"💌","o":[
        {"t":"脸红心跳，不知所措，支支吾吾","s":{"tsundere":3,"emotional":2,"gentle":1}},
        {"t":"直接回应，喜欢就接受不喜欢就拒绝","s":{"proactive":3,"independent":2,"mature":1}},
        {"t":"装作没听见或者岔开话题","s":{"tsundere":2,"mysterious":2,"playful":1}},
        {"t":"认真思考对方是否合适自己","s":{"mature":3,"independent":2,"elegant":1}}]},
    {"q":"你最向往的生活场景是？","emoji":"🏡","o":[
        {"t":"和爱人一起做饭、看夕阳，岁月静好","s":{"gentle":3,"loyal":2,"emotional":2}},
        {"t":"在世界各地冒险旅行，体验不同人生","s":{"energetic":3,"proactive":2,"mysterious":1}},
        {"t":"安静的图书馆或咖啡馆一角，沉浸书海","s":{"elegant":3,"independent":2,"mysterious":2}},
        {"t":"热闹的派对，和朋友一起嗨到天亮","s":{"social":3,"energetic":2,"playful":2}}]},
    {"q":"你认为自己的性格更偏向？","emoji":"🪞","o":[
        {"t":"温柔内敛，不爱争抢，默默付出","s":{"gentle":3,"elegant":1,"mysterious":1}},
        {"t":"活泼外向，喜欢热闹，充满元气","s":{"energetic":3,"social":2,"playful":2}},
        {"t":"理性冷静，独来独往，不依赖他人","s":{"independent":3,"mature":2,"mysterious":1}},
        {"t":"古灵精怪，出其不意，让人猜不透","s":{"playful":3,"mysterious":2,"proactive":1}}]},
    {"q":"当朋友遇到困难时，你会？","emoji":"🤝","o":[
        {"t":"第一时间赶到身边，默默支持","s":{"loyal":3,"gentle":2,"proactive":2}},
        {"t":"帮忙想办法解决问题，提供方案","s":{"independent":2,"mature":3,"proactive":1}},
        {"t":"用幽默化解紧张气氛，让对方放松","s":{"playful":3,"social":2,"energetic":1}},
        {"t":"默默关注，需要时才出手相助","s":{"mysterious":3,"independent":2,"tsundere":1}}]},
    {"q":"当你面对未知的挑战时，你的第一反应是？","emoji":"🏔️","o":[
        {"t":"心跳加速，但暗暗期待，充满好奇","s":{"emotional":2,"proactive":2,"energetic":1}},
        {"t":"冷静评估风险后再做决定","s":{"mature":3,"independent":2,"mysterious":1}},
        {"t":"不管三七二十一先冲再说","s":{"energetic":3,"proactive":3,"playful":1}},
        {"t":"感到一种说不清的兴奋和不安交织","s":{"mysterious":3,"emotional":2,"tsundere":1}}]},
    {"q":"你认为一段关系中最重要的是什么？","emoji":"💎","o":[
        {"t":"彼此信任，无条件支持对方","s":{"loyal":3,"gentle":2,"emotional":1}},
        {"t":"保持个人空间和独立性","s":{"independent":3,"mature":2,"mysterious":1}},
        {"t":"每天都有新鲜感和惊喜","s":{"playful":3,"proactive":2,"energetic":1}},
        {"t":"心灵的深层共鸣和互相理解","s":{"emotional":3,"mysterious":2,"elegant":1}}]},
    {"q":"在一个雨天，你最想做什么？","emoji":"🌧️","o":[
        {"t":"泡杯热茶，听雨声发呆，放空思绪","s":{"elegant":3,"emotional":2,"mysterious":1}},
        {"t":"冲进雨里淋个痛快，感受自由","s":{"energetic":3,"playful":2,"proactive":1}},
        {"t":"给想念的人打个电话聊聊天","s":{"emotional":3,"social":2,"loyal":1}},
        {"t":"窝在被窝里看恐怖小说或悬疑剧","s":{"mysterious":3,"independent":2,"tsundere":1}}]},
    {"q":"如果你能拥有一个超能力，你会选择？","emoji":"🔮","o":[
        {"t":"读心术，看穿别人的真实想法","s":{"mysterious":3,"emotional":2,"tsundere":1}},
        {"t":"瞬间移动，想去哪就去哪","s":{"energetic":3,"proactive":2,"playful":1}},
        {"t":"时间暂停，让自己独享安静","s":{"independent":3,"mysterious":2,"mature":1}},
        {"t":"治愈之力，帮助所有受伤的人","s":{"gentle":3,"loyal":2,"emotional":2}}]},
    {"q":"你面对压力时通常如何应对？","emoji":"💪","o":[
        {"t":"找朋友倾诉，寻求安慰和支持","s":{"social":3,"emotional":2,"gentle":1}},
        {"t":"独自消化，静待好转","s":{"independent":3,"mature":2,"mysterious":1}},
        {"t":"疯狂运动或打游戏发泄精力","s":{"energetic":3,"proactive":2,"playful":1}},
        {"t":"分析压力源，制定解决计划","s":{"mature":3,"independent":2,"elegant":1}}]},
    {"q":"如果要送礼物给重要的人，你会选择？","emoji":"🎁","o":[
        {"t":"亲手制作的心意之作，独一无二","s":{"gentle":3,"emotional":2,"loyal":1}},
        {"t":"对方一直想要的惊喜大礼","s":{"proactive":3,"playful":2,"social":1}},
        {"t":"一本有深度的书或一张珍贵唱片","s":{"elegant":3,"mature":2,"mysterious":1}},
        {"t":"一起去某个特别的地方体验","s":{"emotional":2,"proactive":2,"mysterious":2}}]},
    {"q":"你最向往的旅行目的地是？","emoji":"✈️","o":[
        {"t":"历史悠久的欧洲古城，品味文化","s":{"elegant":3,"mature":2,"mysterious":1}},
        {"t":"热带海岛，阳光沙滩比基尼","s":{"energetic":3,"social":2,"playful":1}},
        {"t":"人迹罕至的极地或沙漠，探索未知","s":{"mysterious":3,"independent":2,"mature":1}},
        {"t":"和朋友们一起去热闹的主题乐园","s":{"social":3,"playful":2,"energetic":1}}]},
    {"q":"你认为自己的最大魅力在于？","emoji":"✨","o":[
        {"t":"温暖治愈的笑容和包容力","s":{"gentle":3,"emotional":2,"social":1}},
        {"t":"独特神秘的气质和深邃的眼神","s":{"mysterious":3,"elegant":2,"independent":1}},
        {"t":"永不服输的冲劲和行动力","s":{"proactive":3,"energetic":2,"playful":1}},
        {"t":"什么场合都能聊得来的社交力","s":{"social":3,"playful":2,"mature":1}}]},
    {"q":"你最讨厌别人对你做什么？","emoji":"😤","o":[
        {"t":"无视你的付出和感受","s":{"loyal":3,"gentle":2,"emotional":1}},
        {"t":"限制你的自由和选择","s":{"independent":3,"proactive":2,"energetic":1}},
        {"t":"对你撒谎和不信任你","s":{"mature":3,"mysterious":2,"tsundere":1}},
        {"t":"在众人面前让你难堪","s":{"tsundere":3,"elegant":2,"social":1}}]},
    {"q":"深夜睡不着时，你通常会？","emoji":"🌙","o":[
        {"t":"回忆过去，想很多有的没的","s":{"emotional":3,"mysterious":2,"gentle":1}},
        {"t":"刷手机看视频打发时间","s":{"social":2,"playful":2,"energetic":1}},
        {"t":"思考人生，规划未来","s":{"mature":3,"independent":2,"elegant":1}},
        {"t":"起来做点事情，不想浪费时间","s":{"proactive":3,"energetic":2,"independent":1}}]},
    {"q":"你觉得理想的爱情是什么样的？","emoji":"💍","o":[
        {"t":"细水长流，相濡以沫，白头偕老","s":{"gentle":3,"loyal":2,"mature":1}},
        {"t":"轰轰烈烈，刻骨铭心，至死不渝","s":{"emotional":3,"proactive":2,"energetic":1}},
        {"t":"心有灵犀，不言而喻的灵魂伴侣","s":{"mysterious":3,"elegant":2,"emotional":1}},
        {"t":"互相成就，共同成长，并肩前行","s":{"independent":3,"mature":2,"proactive":1}}]},
    {"q":"你更欣赏哪种类型的角色？","emoji":"⭐","o":[
        {"t":"温柔善良，永远为他人着想","s":{"gentle":3,"loyal":2,"emotional":1}},
        {"t":"酷酷的，带着神秘感和距离感","s":{"mysterious":3,"tsundere":2,"elegant":1}},
        {"t":"开朗活泼，元气满满，充满正能量","s":{"energetic":3,"social":2,"playful":1}},
        {"t":"冷静理智，实力强大，一击必杀","s":{"mature":3,"independent":2,"mysterious":1}}]},
    {"q":"当你在人群中时，你通常？","emoji":"👥","o":[
        {"t":"主动和周围人聊天，很快就打成一片","s":{"social":3,"proactive":2,"energetic":1}},
        {"t":"安静待在角落观察，不主动搭话","s":{"mysterious":3,"independent":2,"mature":1}},
        {"t":"找熟人聊天，不主动和陌生人交流","s":{"tsundere":2,"gentle":2,"emotional":1}},
        {"t":"成为话题中心，活跃气氛","s":{"playful":3,"social":2,"proactive":1}}]},
    {"q":"你最怕失去什么？","emoji":"💔","o":[
        {"t":"重要的人的信任和依赖","s":{"loyal":3,"gentle":2,"emotional":1}},
        {"t":"自由选择的权利","s":{"independent":3,"proactive":2,"energetic":1}},
        {"t":"内心深处的秘密","s":{"mysterious":3,"tsundere":2,"independent":1}},
        {"t":"和朋友们的关系","s":{"social":3,"emotional":2,"playful":1}}]},
    {"q":"你认为什么最能打动你？","emoji":"💝","o":[
        {"t":"默默为你付出的小细节","s":{"gentle":3,"emotional":2,"loyal":1}},
        {"t":"出其不意的浪漫惊喜","s":{"playful":3,"proactive":2,"energetic":1}},
        {"t":"深层次的精神共鸣和默契","s":{"mysterious":3,"elegant":2,"mature":1}},
        {"t":"在关键时刻的坚定守护","s":{"loyal":3,"mature":2,"tsundere":1}}]},
    {"q":"如果世界末日了，你最后想做什么？","emoji":"🌅","o":[
        {"t":"和最爱的人在一起度过最后的时光","s":{"emotional":3,"loyal":2,"gentle":1}},
        {"t":"做自己一直想做但没做的事","s":{"proactive":3,"energetic":2,"playful":1}},
        {"t":"安静地看最后的风景","s":{"mysterious":3,"elegant":2,"independent":1}},
        {"t":"和所有朋友开个末日派对","s":{"social":3,"playful":2,"energetic":1}}]},
    {"q":"你对待承诺的态度是？","emoji":"📜","o":[
        {"t":"一旦承诺就会用生命去守护","s":{"loyal":3,"mature":2,"gentle":1}},
        {"t":"视情况而定，灵活处理","s":{"playful":2,"independent":2,"proactive":1}},
        {"t":"不轻易承诺，但说到做到","s":{"mysterious":2,"mature":3,"tsundere":1}},
        {"t":"承诺是一种浪漫的表达方式","s":{"emotional":3,"gentle":2,"elegant":1}}]},
    {"q":"你的房间是什么风格？","emoji":"🛏️","o":[
        {"t":"温馨整洁，充满生活气息","s":{"gentle":3,"emotional":2,"social":1}},
        {"t":"简约冷色，干净利落","s":{"mature":3,"mysterious":2,"independent":1}},
        {"t":"色彩缤纷，充满个性和玩具","s":{"playful":3,"energetic":2,"proactive":1}},
        {"t":"书籍满架，文艺气息浓厚","s":{"elegant":3,"mysterious":2,"mature":1}}]},
    {"q":"当你生气时，你的表现是？","emoji":"😠","o":[
        {"t":"沉默不语，独自消化情绪","s":{"mysterious":3,"independent":2,"mature":1}},
        {"t":"直接表达不满，当场解决","s":{"proactive":3,"energetic":2,"social":1}},
        {"t":"嘴上说没事，其实很在意","s":{"tsundere":3,"emotional":2,"loyal":1}},
        {"t":"用行动证明自己的态度","s":{"independent":3,"mature":2,"elegant":1}}]},
    {"q":"你最向往哪种超自然体验？","emoji":"🌌","o":[
        {"t":"和精灵对话，感受自然之力","s":{"mysterious":3,"emotional":2,"gentle":1}},
        {"t":"穿越时空，改变历史走向","s":{"proactive":3,"mysterious":2,"energetic":1}},
        {"t":"进入梦境，探索潜意识深处","s":{"mysterious":3,"elegant":2,"emotional":1}},
        {"t":"获得读心能力，看透人心","s":{"tsundere":2,"mysterious":3,"social":1}}]},
    {"q":"你觉得什么样的笑容最迷人？","emoji":"😊","o":[
        {"t":"温暖如阳光的微笑，让人安心","s":{"gentle":3,"emotional":2,"social":1}},
        {"t":"带着自信的爽朗大笑","s":{"energetic":3,"proactive":2,"playful":1}},
        {"t":"若隐若现的神秘微笑","s":{"mysterious":3,"elegant":2,"mature":1}},
        {"t":"害羞时偷笑的样子","s":{"tsundere":3,"emotional":2,"gentle":1}}]},
    {"q":"你最想拥有的技能是？","emoji":"🎯","o":[
        {"t":"烹饪出治愈人心的美食","s":{"gentle":3,"social":2,"emotional":1}},
        {"t":"战斗能力，保护重要的人","s":{"loyal":3,"proactive":2,"energetic":1}},
        {"t":"洞察一切的分析能力","s":{"mature":3,"mysterious":2,"independent":1}},
        {"t":"让任何人都开心的社交术","s":{"social":3,"playful":2,"proactive":1}}]},
    {"q":"你的手机里最多的APP是？","emoji":"📱","o":[
        {"t":"社交软件，随时和朋友保持联系","s":{"social":3,"playful":2,"energetic":1}},
        {"t":"阅读和学习类APP","s":{"mature":3,"independent":2,"elegant":1}},
        {"t":"游戏和娱乐类APP","s":{"playful":3,"energetic":2,"proactive":1}},
        {"t":"摄影和艺术类APP","s":{"emotional":3,"mysterious":2,"elegant":1}}]},
    {"q":"你认为最强的力量是？","emoji":"💪","o":[
        {"t":"温柔，能融化一切坚冰","s":{"gentle":3,"emotional":2,"loyal":1}},
        {"t":"意志，永不放弃的决心","s":{"loyal":3,"proactive":2,"mature":1}},
        {"t":"智慧，运筹帷幄的头脑","s":{"mature":3,"mysterious":2,"independent":1}},
        {"t":"勇气，直面恐惧的力量","s":{"proactive":3,"energetic":2,"playful":1}}]},
    {"q":"你更喜欢哪个季节？","emoji":"🍂","o":[
        {"t":"春天，万物生长，充满希望","s":{"gentle":3,"emotional":2,"playful":1}},
        {"t":"夏天，充满活力和热情","s":{"energetic":3,"social":2,"proactive":1}},
        {"t":"秋天，沉静优雅，令人回味","s":{"elegant":3,"mature":2,"mysterious":1}},
        {"t":"冬天，安静神秘，引人遐想","s":{"mysterious":3,"independent":2,"tsundere":1}}]},
    {"q":"你的口头禅类型是？","emoji":"💬","o":[
        {"t":"鼓励和温暖的话语","s":{"gentle":3,"emotional":2,"social":1}},
        {"t":"毒舌和吐槽，一针见血","s":{"tsundere":3,"playful":2,"social":1}},
        {"t":"冷静的分析和判断","s":{"mature":3,"independent":2,"mysterious":1}},
        {"t":"神秘又意味深长的话","s":{"mysterious":3,"elegant":2,"emotional":1}}]},
    {"q":"你的理想职业是？","emoji":"🎓","o":[
        {"t":"教师或心理咨询师，帮助他人成长","s":{"gentle":3,"emotional":2,"social":1}},
        {"t":"探险家或运动员，挑战极限","s":{"energetic":3,"proactive":2,"playful":1}},
        {"t":"科学家或研究员，探索未知","s":{"mysterious":3,"independent":2,"mature":1}},
        {"t":"艺术家或设计师，创造美","s":{"elegant":3,"emotional":2,"mysterious":1}}]},
    {"q":"最后，你希望你的另一半具备什么品质？","emoji":"💖","o":[
        {"t":"温柔体贴，永远在你身边","s":{"gentle":3,"loyal":2,"emotional":1}},
        {"t":"有趣好玩，每天都不一样","s":{"playful":3,"energetic":2,"proactive":1}},
        {"t":"成熟稳重，可以依靠","s":{"mature":3,"independent":2,"elegant":1}},
        {"t":"神秘迷人，永远猜不透","s":{"mysterious":3,"tsundere":2,"elegant":1}}]}
]

chars_js = json.dumps(chars, ensure_ascii=False)
qs_js = json.dumps(questions, ensure_ascii=False)
dims_js = json.dumps(dims, ensure_ascii=False)

html = r'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0,maximum-scale=1.0,user-scalable=no">
<meta name="description" content="二次元老婆匹配器 - 88位人气galgame与动漫角色12维性格精准匹配，回答36道题找到你的命运之人">
<title>二次元老婆匹配器 - 你的命运之人是谁？</title>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700;900&family=ZCOOL+KuaiLe&display=swap" rel="stylesheet">
<style>
*{margin:0;padding:0;box-sizing:border-box;-webkit-tap-highlight-color:transparent}
:root{--pink:#e879f9;--purple:#a855f7;--bg:#0b0a12;--card:#15131f;--card2:#1d1b2e;--text:#f8f7fc;--dim:#9ca3af;--border:rgba(232,121,249,0.25);--radius:16px;--accent:#e879f9}
html{scroll-behavior:smooth}
body{font-family:'Noto Sans SC',sans-serif;background:var(--bg);color:var(--text);min-height:100vh;overflow-x:hidden}
#particles{position:fixed;top:0;left:0;width:100%;height:100%;z-index:0;pointer-events:none}
.nav-bar{position:fixed;top:0;left:0;width:100%;background:rgba(11,10,18,0.95);backdrop-filter:blur(12px);z-index:50;border-bottom:1px solid var(--border);padding:0 20px;height:56px;display:flex;align-items:center;justify-content:space-between;max-width:800px;margin:0 auto}
.nav-logo{font-family:'ZCOOL KuaiLe',cursive;font-size:18px;cursor:pointer;background:linear-gradient(135deg,var(--pink),var(--purple));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.nav-links{display:flex;gap:4px}
.nav-link{padding:6px 12px;border-radius:8px;font-size:13px;color:var(--dim);cursor:pointer;transition:all .2s;border:none;background:transparent;font-family:inherit}
.nav-link:hover{color:var(--text);background:rgba(232,121,249,0.1)}
.nav-link.active{color:var(--pink);background:rgba(232,121,249,0.15)}
.page{display:none;position:relative;z-index:1;min-height:100vh;padding:76px 20px 40px;max-width:800px;margin:0 auto}
.page.active{display:block;animation:fadeIn .5s ease}
@keyframes fadeIn{from{opacity:0;transform:translateY(20px)}to{opacity:1;transform:translateY(0)}}
@keyframes slideIn{from{opacity:0;transform:translateX(30px)}to{opacity:1;transform:translateX(0)}}
@keyframes pulse{0%,100%{transform:scale(1)}50%{transform:scale(1.05)}}
@keyframes shimmer{0%{background-position:-200% center}100%{background-position:200% center}}
.btn{padding:14px 32px;border:none;border-radius:12px;font-size:16px;font-weight:700;cursor:pointer;transition:all .3s;display:inline-flex;align-items:center;gap:8px;font-family:inherit}
.btn-primary{background:linear-gradient(135deg,var(--pink),var(--purple));color:#fff;box-shadow:0 4px 20px rgba(168,85,247,0.4)}
.btn-primary:hover{transform:translateY(-2px);box-shadow:0 8px 30px rgba(168,85,247,0.5)}
.btn-ghost{background:transparent;color:var(--text);border:1px solid var(--border)}
.btn-ghost:hover{background:rgba(232,121,249,0.1)}
.btn-sm{padding:8px 16px;font-size:13px;border-radius:8px}
.home-hero{text-align:center;padding:40px 0}
.home-badge{display:inline-block;padding:6px 16px;border-radius:20px;background:rgba(232,121,249,0.1);border:1px solid var(--border);font-size:13px;color:var(--pink);margin-bottom:24px}
.home-title{font-family:'ZCOOL KuaiLe',cursive;font-size:42px;line-height:1.3;margin-bottom:16px}
.home-title .grad{background:linear-gradient(135deg,var(--pink),var(--purple),var(--pink));background-size:200% auto;-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;animation:shimmer 3s linear infinite}
.home-desc{color:var(--dim);font-size:15px;line-height:1.8;margin-bottom:32px;max-width:500px;margin-left:auto;margin-right:auto}
.home-buttons{display:flex;gap:16px;justify-content:center;flex-wrap:wrap}
.home-stats{display:flex;gap:24px;justify-content:center;margin-top:40px;flex-wrap:wrap}
.home-stat{text-align:center}
.home-stat-num{font-size:32px;font-weight:900;background:linear-gradient(135deg,var(--pink),var(--purple));-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.home-stat-label{font-size:12px;color:var(--dim);margin-top:4px}
.section-title{font-size:20px;font-weight:700;margin-bottom:16px;display:flex;align-items:center;gap:8px}
.quiz-header{margin-bottom:24px}
.quiz-progress-text{text-align:center;font-size:14px;color:var(--dim);margin-bottom:8px}
.quiz-progress-bar{width:100%;height:6px;background:var(--card);border-radius:3px;overflow:hidden}
.quiz-progress-fill{height:100%;background:linear-gradient(90deg,var(--pink),var(--purple));border-radius:3px;transition:width .3s}
.quiz-card{background:var(--card);border:1px solid var(--border);border-radius:var(--radius);padding:32px 24px;margin-bottom:24px;animation:slideIn .3s ease}
.quiz-emoji{font-size:36px;text-align:center;margin-bottom:12px}
.quiz-question{font-size:20px;font-weight:700;margin-bottom:24px;line-height:1.5;text-align:center}
.quiz-options{display:flex;flex-direction:column;gap:12px}
.quiz-option{padding:16px;border:1px solid var(--border);border-radius:12px;background:var(--card2);cursor:pointer;transition:all .2s;display:flex;align-items:center;gap:12px;font-size:15px;color:var(--text);font-family:inherit;text-align:left}
.quiz-option:hover{border-color:var(--pink);background:rgba(232,121,249,0.05)}
.quiz-option.selected{border-color:var(--pink);background:rgba(232,121,249,0.15);box-shadow:0 0 0 1px var(--pink)}
.quiz-option-letter{width:32px;height:32px;border-radius:50%;border:2px solid var(--border);display:flex;align-items:center;justify-content:center;font-weight:700;flex-shrink:0;transition:all .2s}
.quiz-option.selected .quiz-option-letter{border-color:var(--pink);background:var(--pink);color:#fff}
.quiz-nav{display:flex;justify-content:space-between;gap:12px}
.mini-radar-wrap{position:fixed;bottom:20px;right:20px;z-index:40;background:var(--card);border:1px solid var(--border);border-radius:12px;padding:8px;display:none}
.mini-radar-wrap.show{display:block}
.mini-radar-label{font-size:10px;color:var(--dim);text-align:center;margin-top:4px}
.result-card{background:var(--card);border:1px solid var(--border);border-radius:var(--radius);overflow:hidden;margin-bottom:24px}
.result-image-wrap{width:100%;background:var(--card2);display:flex;align-items:center;justify-content:center;overflow:hidden;position:relative}
.result-image-wrap img{max-width:100%;max-height:500px;object-fit:contain;display:block}
.result-info{padding:24px}
.result-series{font-size:13px;color:var(--accent);margin-bottom:4px}
.result-name{font-size:28px;font-weight:700;margin-bottom:8px}
.result-match{font-size:36px;font-weight:900;background:linear-gradient(135deg,var(--pink),var(--purple));-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.result-tags{display:flex;gap:8px;flex-wrap:wrap;margin:12px 0}
.result-tag{padding:4px 12px;border-radius:20px;background:rgba(232,121,249,0.1);font-size:12px;color:var(--accent)}
.result-desc{color:var(--dim);font-size:14px;line-height:1.8;margin:16px 0}
.result-quote{font-style:italic;color:var(--accent);font-size:15px;padding:12px 16px;border-left:3px solid var(--accent);background:rgba(232,121,249,0.05);border-radius:0 8px 8px 0;margin:16px 0}
.result-meta{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:16px 0}
.result-meta-item{text-align:center;background:var(--card2);border-radius:8px;padding:12px}
.result-meta-label{font-size:11px;color:var(--dim);margin-bottom:4px}
.result-meta-val{font-size:14px;font-weight:600}
.result-analysis{background:var(--card2);border-radius:12px;padding:20px;margin:16px 0;border-left:3px solid var(--accent)}
.result-analysis h3{font-size:16px;margin-bottom:12px;color:var(--accent)}
.result-analysis p{font-size:14px;line-height:1.8;color:var(--text)}
.result-favor-quote{background:linear-gradient(135deg,rgba(232,121,249,0.08),rgba(168,85,247,0.08));border-radius:12px;padding:20px;margin:16px 0;border:1px solid var(--border);text-align:center}
.result-favor-quote .heart{font-size:24px;margin-bottom:8px}
.result-favor-quote p{font-size:15px;line-height:1.8;color:var(--text);font-style:italic}
.result-favor-quote .attr{font-size:12px;color:var(--dim);margin-top:8px}
.radar-chart-wrap{display:flex;justify-content:center;margin:24px 0}
.result-recommendations{margin-top:24px}
.result-recommendations h3{font-size:18px;margin-bottom:16px}
.rec-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(140px,1fr));gap:12px}
.rec-card{background:var(--card2);border:1px solid var(--border);border-radius:12px;overflow:hidden;cursor:pointer;transition:all .2s}
.rec-card:hover{border-color:var(--pink);transform:translateY(-2px)}
.rec-image-wrap{width:100%;aspect-ratio:3/4;overflow:hidden;background:var(--bg);display:flex;align-items:center;justify-content:center}
.rec-image-wrap img{max-width:100%;max-height:100%;object-fit:contain}
.rec-info{padding:8px}
.rec-name{font-size:13px;font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.rec-match{font-size:12px;color:var(--accent)}
.share-section{background:var(--card);border:1px solid var(--border);border-radius:var(--radius);padding:20px;margin:24px 0;text-align:center}
.share-section h3{font-size:16px;margin-bottom:12px;color:var(--accent)}
.share-text{background:var(--card2);border-radius:8px;padding:12px;font-size:13px;line-height:1.6;color:var(--text);text-align:left;margin:12px 0;white-space:pre-wrap}
.gallery-header{display:flex;justify-content:space-between;align-items:center;margin-bottom:24px}
.gallery-title{font-size:24px;font-weight:700}
.search-bar{width:100%;padding:12px 16px;border:1px solid var(--border);border-radius:12px;background:var(--card);color:var(--text);font-size:14px;font-family:inherit;margin-bottom:16px}
.search-bar:focus{outline:none;border-color:var(--pink)}
.gallery-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:16px}
.gallery-card{background:var(--card);border:1px solid var(--border);border-radius:var(--radius);overflow:hidden;cursor:pointer;transition:all .2s}
.gallery-card:hover{border-color:var(--pink);transform:translateY(-4px);box-shadow:0 8px 30px rgba(168,85,247,0.2)}
.gallery-image-wrap{width:100%;background:var(--card2);overflow:hidden;display:flex;align-items:center;justify-content:center;min-height:200px}
.gallery-image-wrap img{max-width:100%;max-height:300px;object-fit:contain;display:block}
.gallery-info{padding:12px}
.gallery-name{font-size:14px;font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.gallery-series{font-size:12px;color:var(--dim);margin-top:2px}
.filter-bar{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:20px}
.filter-chip{padding:6px 14px;border-radius:20px;border:1px solid var(--border);background:var(--card);color:var(--dim);font-size:13px;cursor:pointer;transition:all .2s;font-family:inherit}
.filter-chip.active{background:var(--accent);color:#fff;border-color:var(--accent)}
.filter-chip:hover{border-color:var(--pink)}
.compare-section{background:var(--card);border:1px solid var(--border);border-radius:var(--radius);padding:20px;margin-bottom:24px}
.compare-grid{display:grid;grid-template-columns:1fr auto 1fr;gap:16px;align-items:start}
.compare-slot{background:var(--card2);border:1px solid var(--border);border-radius:12px;padding:16px;min-height:200px;display:flex;flex-direction:column;align-items:center;justify-content:center;cursor:pointer;transition:all .2s}
.compare-slot:hover{border-color:var(--pink)}
.compare-slot.has-char{justify-content:flex-start}
.compare-vs{text-align:center;font-size:24px;font-weight:900;color:var(--accent);padding-top:80px}
.compare-image-wrap{width:100%;max-height:200px;display:flex;align-items:center;justify-content:center;margin-bottom:8px}
.compare-image-wrap img{max-width:100%;max-height:200px;object-fit:contain}
.compare-empty{color:var(--dim);font-size:14px;text-align:center}
.ranking-list{display:flex;flex-direction:column;gap:12px}
.rank-item{display:flex;align-items:center;gap:16px;background:var(--card);border:1px solid var(--border);border-radius:12px;padding:12px;cursor:pointer;transition:all .2s}
.rank-item:hover{border-color:var(--pink);transform:translateX(4px)}
.rank-num{font-size:24px;font-weight:900;width:40px;text-align:center;flex-shrink:0}
.rank-num.top1{background:linear-gradient(135deg,#ffd700,#ffaa00);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.rank-num.top2{background:linear-gradient(135deg,#c0c0c0,#a0a0a0);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.rank-num.top3{background:linear-gradient(135deg,#cd7f32,#a0522d);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.rank-image{width:60px;height:60px;border-radius:8px;overflow:hidden;flex-shrink:0;background:var(--card2);display:flex;align-items:center;justify-content:center}
.rank-image img{max-width:100%;max-height:100%;object-fit:contain}
.rank-info{flex:1;min-width:0}
.rank-name{font-size:15px;font-weight:600}
.rank-series{font-size:12px;color:var(--dim)}
.rank-traits{font-size:11px;color:var(--accent);margin-top:2px}
.rank-score{font-size:18px;font-weight:700;color:var(--accent)}
.stats-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:16px;margin-bottom:24px}
.stat-card{background:var(--card);border:1px solid var(--border);border-radius:12px;padding:16px;text-align:center}
.stat-card .num{font-size:28px;font-weight:900;background:linear-gradient(135deg,var(--pink),var(--purple));-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.stat-card .label{font-size:12px;color:var(--dim);margin-top:4px}
.bar-chart{background:var(--card);border:1px solid var(--border);border-radius:var(--radius);padding:20px;margin-bottom:24px}
.bar-row{display:flex;align-items:center;gap:8px;margin-bottom:8px}
.bar-label{width:60px;font-size:13px;text-align:right;flex-shrink:0}
.bar-track{flex:1;height:24px;background:var(--card2);border-radius:4px;overflow:hidden;position:relative}
.bar-fill{height:100%;border-radius:4px;transition:width .5s ease;display:flex;align-items:center;justify-content:flex-end;padding-right:8px}
.bar-val{font-size:12px;font-weight:700;color:#fff}
.modal-overlay{position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,0.8);z-index:100;display:none;align-items:center;justify-content:center;padding:20px}
.modal-overlay.active{display:flex}
.modal-content{background:var(--card);border:1px solid var(--border);border-radius:var(--radius);max-width:500px;max-height:90vh;overflow-y:auto;width:100%;position:relative}
.modal-image-wrap{width:100%;background:var(--card2);display:flex;align-items:center;justify-content:center;overflow:hidden}
.modal-image-wrap img{max-width:100%;max-height:400px;object-fit:contain}
.modal-body{padding:24px}
.modal-close{position:absolute;top:16px;right:16px;width:36px;height:36px;border-radius:50%;background:rgba(0,0,0,0.5);border:none;color:#fff;font-size:20px;cursor:pointer;display:flex;align-items:center;justify-content:center;z-index:1}
.img-placeholder{display:flex;align-items:center;justify-content:center;background:var(--card2);color:var(--dim);font-size:14px;min-height:200px}
.toast{position:fixed;bottom:80px;left:50%;transform:translateX(-50%);background:var(--card);border:1px solid var(--accent);border-radius:8px;padding:12px 24px;font-size:14px;z-index:200;opacity:0;transition:opacity .3s;pointer-events:none}
.toast.show{opacity:1}
@media(max-width:600px){.home-title{font-size:32px}.quiz-card{padding:20px 16px}.quiz-question{font-size:18px}.gallery-grid{grid-template-columns:repeat(2,1fr)}.rec-grid{grid-template-columns:repeat(2,1fr)}.result-image-wrap img{max-height:350px}.compare-grid{grid-template-columns:1fr}.compare-vs{display:none}.result-meta{grid-template-columns:1fr}.home-stats{gap:16px}.mini-radar-wrap{display:none!important}.nav-links{gap:0}.nav-link{padding:6px 8px;font-size:12px}}
</style>
</head>
<body>
<canvas id="particles"></canvas>
<nav class="nav-bar"><div class="nav-logo" onclick="goHome()">二次元老婆匹配器</div><div class="nav-links"><button class="nav-link" data-page="home" onclick="goHome()">首页</button><button class="nav-link" data-page="quiz" onclick="goQuiz()">测试</button><button class="nav-link" data-page="gallery" onclick="goGallery()">图鉴</button><button class="nav-link" data-page="ranking" onclick="goRanking()">排行</button><button class="nav-link" data-page="compare" onclick="goCompare()">对比</button><button class="nav-link" data-page="stats" onclick="goStats()">统计</button></div></nav>
<div class="page active" id="page-home"><div class="home-hero"><div class="home-badge">88位角色 · 12维性格 · 36道精选题</div><h1 class="home-title">二次元老婆<span class="grad">匹配器</span></h1><p class="home-desc">穿越彩虹闪烁的次元之门，回答36道精心设计的性格测试题，我们将从88位人气galgame与动漫角色中，用余弦相似度混合欧氏距离算法，找到与你灵魂共鸣的她。</p><div class="home-buttons"><button class="btn btn-primary" onclick="goQuiz()">开始测试</button><button class="btn btn-ghost" onclick="goGallery()">角色图鉴</button></div><div class="home-stats"><div class="home-stat"><div class="home-stat-num">88</div><div class="home-stat-label">人气角色</div></div><div class="home-stat"><div class="home-stat-num">12</div><div class="home-stat-label">性格维度</div></div><div class="home-stat"><div class="home-stat-num">36</div><div class="home-stat-label">精选题目</div></div><div class="home-stat"><div class="home-stat-num">46</div><div class="home-stat-label">收录作品</div></div></div></div></div>
<div class="page" id="page-quiz"><div class="quiz-header"><div class="quiz-progress-text" id="quizProgress"></div><div class="quiz-progress-bar"><div class="quiz-progress-fill" id="quizBar" style="width:0"></div></div></div><div class="quiz-card" id="quizCard"></div><div class="quiz-nav"><button class="btn btn-ghost" id="btnPrev" onclick="prevQ()">上一题</button><button class="btn btn-primary" id="btnNext" onclick="nextQ()">下一题</button></div><div class="mini-radar-wrap" id="miniRadar"><canvas id="miniCanvas" width="80" height="80"></canvas><div class="mini-radar-label">实时画像</div></div></div>
<div class="page" id="page-result"><div id="resultContent"></div><div style="text-align:center;margin-top:24px"><button class="btn btn-primary" onclick="goQuiz()">重新测试</button><button class="btn btn-ghost" onclick="goGallery()">角色图鉴</button></div></div>
<div class="page" id="page-gallery"><div class="gallery-header"><div class="gallery-title">角色图鉴</div><button class="btn btn-ghost btn-sm" onclick="goHome()">返回首页</button></div><input class="search-bar" id="searchBar" placeholder="搜索角色名、作品名或标签..." oninput="onSearch(this.value)"><div class="filter-bar" id="filterBar"></div><div class="gallery-grid" id="galleryGrid"></div></div>
<div class="page" id="page-ranking"><div class="gallery-header"><div class="gallery-title">人气排行</div><button class="btn btn-ghost btn-sm" onclick="goHome()">返回首页</button></div><div class="ranking-list" id="rankingList"></div></div>
<div class="page" id="page-compare"><div class="gallery-header"><div class="gallery-title">角色对比</div><button class="btn btn-ghost btn-sm" onclick="goHome()">返回首页</button></div><div class="compare-section"><div class="compare-grid"><div class="compare-slot" id="compareSlot1" onclick="openComparePicker(1)"><div class="compare-empty">点击选择角色</div></div><div class="compare-vs">VS</div><div class="compare-slot" id="compareSlot2" onclick="openComparePicker(2)"><div class="compare-empty">点击选择角色</div></div></div></div><div id="compareResult" style="display:none"><div class="radar-chart-wrap"><canvas id="compareRadar" width="400" height="400"></canvas></div><div id="compareDetails"></div></div></div>
<div class="page" id="page-stats"><div class="gallery-header"><div class="gallery-title">统计面板</div><button class="btn btn-ghost btn-sm" onclick="goHome()">返回首页</button></div><div class="stats-grid" id="statsGrid"></div><div class="bar-chart" id="avgBarChart"></div><div class="bar-chart"><h3 style="font-size:16px;margin-bottom:16px;color:var(--accent)">作品分布</h3><div id="seriesChart"></div></div></div>
<div class="modal-overlay" id="modal" onclick="closeModal(event)"><div class="modal-content" onclick="event.stopPropagation()"><button class="modal-close" onclick="closeModal()">&times;</button><div id="modalContent"></div></div></div>
<div class="modal-overlay" id="pickerModal" onclick="closePicker(event)"><div class="modal-content" onclick="event.stopPropagation()" style="max-width:600px"><button class="modal-close" onclick="closePicker()">&times;</button><div style="padding:20px"><h3 style="margin-bottom:16px">选择角色</h3><input class="search-bar" id="pickerSearch" placeholder="搜索角色..." oninput="onPickerSearch(this.value)" style="margin-bottom:12px"><div id="pickerGrid" style="max-height:400px;overflow-y:auto"></div></div></div></div>
<div class="toast" id="toast"></div>
<script>
const CH=''' + chars_js + ''';
const QS=''' + qs_js + ''';
const DM=''' + dims_js + ''';
var curQ=0,ans=new Array(QS.length).fill(null),curFilter='',searchQuery='',viewStats={};
var compareSel=[null,null],pickerTarget=0;
try{viewStats=JSON.parse(localStorage.getItem('waifuViewStats')||'{}')}catch(e){}
var cv=document.getElementById('particles'),cx=cv.getContext('2d');
var ps=[];
function rs(){cv.width=innerWidth;cv.height=innerHeight}
rs();addEventListener('resize',rs);
function ip(){ps=[];for(var i=0;i<Math.min(80,Math.floor(innerWidth/15));i++)ps.push({x:Math.random()*cv.width,y:Math.random()*cv.height,r:Math.random()*2+.5,sx:(Math.random()-.5)*.3,sy:(Math.random()-.5)*.3,a:Math.random()*.5+.1,c:Math.random()>.5?'232,121,249':'168,85,247'})}
ip();
function ap(){cx.clearRect(0,0,cv.width,cv.height);ps.forEach(function(p){p.x+=p.sx;p.y+=p.sy;if(p.x<0)p.x=cv.width;if(p.x>cv.width)p.x=0;if(p.y<0)p.y=cv.height;if(p.y>cv.height)p.y=0;cx.beginPath();cx.arc(p.x,p.y,p.r,0,Math.PI*2);cx.fillStyle='rgba('+p.c+','+p.a+')';cx.fill()});requestAnimationFrame(ap)}
ap();
function showPage(id){
document.querySelectorAll('.page').forEach(function(p){p.classList.remove('active')});
document.getElementById(id).classList.add('active');
document.querySelectorAll('.nav-link').forEach(function(n){n.classList.toggle('active',n.dataset.page===id.replace('page-',''))});
scrollTo(0,0)}
function goHome(){showPage('page-home')}
function goQuiz(){curQ=0;ans.fill(null);showPage('page-quiz');renderQ();document.getElementById('miniRadar').classList.remove('show')}
function goGallery(){showPage('page-gallery');renderGallery()}
function goResult(){showPage('page-result');renderResult()}
function goRanking(){showPage('page-ranking');renderRanking()}
function goCompare(){showPage('page-compare');renderCompare()}
function goStats(){showPage('page-stats');renderStats()}
function renderQ(){
var q=QS[curQ];var L=['A','B','C','D'];
var h='<div class="quiz-emoji">'+(q.emoji||'✨')+'</div><div class="quiz-question">'+(curQ+1)+'. '+q.q+'</div><div class="quiz-options">';
q.o.forEach(function(o,i){var s=ans[curQ]===i?'selected':'';h+='<button class="quiz-option '+s+'" onclick="selOpt('+i+')"><div class="quiz-option-letter">'+L[i]+'</div><span>'+o.t+'</span></button>'});
h+='</div>';document.getElementById('quizCard').innerHTML=h;
document.getElementById('quizCard').style.animation='none';void document.getElementById('quizCard').offsetHeight;document.getElementById('quizCard').style.animation='';
document.getElementById('quizProgress').textContent='第 '+(curQ+1)+' / '+QS.length+' 题';
document.getElementById('quizBar').style.width=((curQ+1)/QS.length*100)+'%';
document.getElementById('btnPrev').style.visibility=curQ===0?'hidden':'visible';
document.getElementById('btnNext').textContent=curQ===QS.length-1?'提交':'下一题';
if(curQ>=3){document.getElementById('miniRadar').classList.add('show');drawMiniRadar(calcUser())}else{document.getElementById('miniRadar').classList.remove('show')}
}
function selOpt(i){ans[curQ]=i;renderQ();if(curQ>=2){drawMiniRadar(calcUser())}}
function prevQ(){if(curQ>0){curQ--;renderQ()}}
function nextQ(){if(ans[curQ]===null){alert('请先选择一个选项');return}if(curQ<QS.length-1){curQ++;renderQ()}else{goResult()}}
function calcUser(){var v={};DM.forEach(function(d){v[d.key]=50});QS.forEach(function(q,i){if(ans[i]===null)return;var o=q.o[ans[i]];if(!o.s)return;for(var k in o.s){if(v[k]!==undefined)v[k]+=o.s[k]*8}});DM.forEach(function(d){v[d.key]=Math.max(0,Math.min(100,v[d.key]))});return v}
function cosSim(a,b){var d=0,nA=0,nB=0;DM.forEach(function(dim){var av=a[dim.key],bv=b[dim.key];d+=av*bv;nA+=av*av;nB+=bv*bv});return d/(Math.sqrt(nA)*Math.sqrt(nB)||1)}
function eucDist(a,b){var s=0;DM.forEach(function(d){var diff=a[d.key]-b[d.key];s+=diff*diff});return Math.sqrt(s)}
function matchScore(u,c){var cv={};DM.forEach(function(d,i){cv[d.key]=c.traits[i]});var cs=cosSim(u,cv);var ed=eucDist(u,cv);var ne=1-ed/(Math.sqrt(DM.length)*100);return Math.round((0.6*cs+0.4*ne)*100)}
function genEncounter(u,c){
var top=[];DM.forEach(function(d,i){if(u[d.key]>65)top.push({label:d.label,key:d.key,uv:u[d.key],cv:c.traits[i],idx:i})});top.sort(function(a,b){return b.uv-a.uv});
var scene='那是一个'+(top[0]&&top[0].label==='温柔'?'阳光温暖的午后':'')+ (top[0]&&top[0].label==='神秘'?'月色如水的夜晚':'')+ (top[0]&&top[0].label==='活力'?'充满活力的清晨':'')+ (top[0]&&top[0].label==='优雅'?'安静优雅的黄昏':'')+ '，你在'+(c.series.includes('Fate')?'冬木市的街头':c.series.includes('Clannad')?'光坂小镇的坡道上':c.series.includes('Re:')?'王都的集市':c.series.includes('魔法少女')?'见泷原的校园':'某个命运的十字路口')+'与她相遇。';
scene+=c.name+'正'+(c.traits[0]>70?'微笑着':'')+ (c.traits[5]>60?'傲娇地别过脸':'')+ (c.traits[8]>70?'神秘地望着远方':'')+ (c.traits[1]>70?'充满活力地向你挥手':'')+ '站在那里，仿佛在等待什么人。';
scene+='你们的目光交汇的瞬间，一种奇妙的电流穿过你的心脏——那不是错觉，而是命运的引力在起作用。';
if(top.length>0){scene+='你身上散发的「'+top[0].label+'」气质深深吸引了她，而她眼中那份独特的光芒也让你无法移开视线。'}
scene+='从这一刻起，你们的故事开始了。';
return scene}
function genDailyLife(u,c){
var scenes=[];
if(u.gentle>60&&c.traits[0]>60)scenes.push('你们会一起在厨房做料理，她笨拙地切菜的样子让你忍俊不禁，而你温柔地接过菜刀帮她完成的画面成了日常最温馨的一幕。');
if(u.energetic>60&&c.traits[1]>60)scenes.push('周末的清晨总是被她拉起来跑步或爬山，虽然你嘴上抱怨但心里乐在其中——因为她的笑容比任何风景都耀眼。');
if(u.mysterious>60&&c.traits[8]>60)scenes.push('深夜里你们会并肩坐在窗前看星星，不用说话也能理解彼此的心意——沉默是你们独特的交流方式。');
if(u.playful>60&&c.traits[3]>60)scenes.push('每天都是新的恶作剧和惊喜，你永远不知道她下一秒会从哪里冒出来吓你一跳，但也正因如此每天都不无聊。');
if(u.tsundere>60&&c.traits[5]>60)scenes.push('你们的日常就是一场傲娇对决——谁先承认在意对方谁就输了。但两个人都知道，输赢不重要，重要的是这种别扭的甜蜜。');
if(u.emotional>60&&c.traits[10]>60)scenes.push('看催泪电影时你们会一起哭得稀里哗啦，然后互相嘲笑对方的红眼圈——这是属于你们的浪漫。');
if(scenes.length===0)scenes.push('你们的日常平淡而温暖，一杯茶、一本书、一个默契的眼神，就是最好的陪伴。');
return scenes.join('')}
function genRival(u,c){
var rivals=CH.filter(function(x){return x.id!==c.id}).map(function(x){var cv2={};DM.forEach(function(d,i){cv2[d.key]=x.traits[i]});return{id:x.id,name:x.name,series:x.series,image:x.image,score:matchScore(u,x)}}).sort(function(a,b){return b.score-a.score}).slice(0,3);
var h='<div style="display:flex;gap:12px;flex-wrap:wrap">';
rivals.forEach(function(r){h+='<div style="flex:1;min-width:100px;text-align:center;cursor:pointer" onclick="showDetail(\''+r.id+'\')"><div style="background:var(--card);border:1px solid var(--border);border-radius:8px;overflow:hidden"><div style="aspect-ratio:1;overflow:hidden;display:flex;align-items:center;justify-content:center;background:var(--card2)"><img src="'+r.image+'" style="max-width:100%;max-height:100%;object-fit:contain" onerror="this.style.display=\'none\'" loading="lazy"></div><div style="padding:6px"><div style="font-size:12px;font-weight:600">'+r.name+'</div><div style="font-size:11px;color:var(--accent)">'+r.score+'%</div></div></div></div>'});
h+='</div>';return h}
function genAnalysis(u,c){
var top=[],bottom=[];DM.forEach(function(d,i){if(u[d.key]>65)top.push({label:d.label,key:d.key,uv:u[d.key],cv:c.traits[i],idx:i});if(u[d.key]<40)bottom.push({label:d.label,key:d.key,uv:u[d.key],cv:c.traits[i],idx:i})});top.sort(function(a,b){return b.uv-a.uv});
var tl=top.slice(0,3).map(function(d){return d.label}).join('、');
var a='你的性格在「'+tl+'」维度上表现最为突出，而'+c.name+'正是以这些特质著称的角色。';
if(c.description)a+=c.description+' ';
a+='你们的核心气质高度共鸣，彼此之间的差异恰好形成了互补。';
if(top.length>0){var t=top[0];a+='在「'+t.label+'」维度上你得分'+t.uv+'，她同样拥有'+t.cv+'的高分，这意味着你们能够在这个层面深度地理解彼此的内心世界。'}
if(top.length>1){var t2=top[1];a+='同时在「'+t2.label+'」上你们也都有不错的得分，这让你们在相处时拥有共同语言和默契。'}
if(bottom.length>0){var bl=bottom.slice(0,2).map(function(d){return d.label}).join('、');a+='相对地，你在「'+bl+'」方面的得分较低，而'+c.name+'可能在这些方面能够弥补你的不足，形成互补关系。'}
a+='仿佛她就是为了与你相遇而存在的。';return a}
function genProfile(u){
var s=DM.map(function(d,i){return{label:d.label,key:d.key,val:u[d.key]}}).sort(function(a,b){return b.val-a.val});
var p='你的性格画像呈现出以「'+s[0].label+'、'+s[1].label+'、'+s[2].label+'」为主导的特质。';
if(s[0].val>80)p+='你在「'+s[0].label+'」维度上表现极为突出，这是你最核心的人格魅力所在。';
if(s[s.length-1].val<40)p+='相对地，「'+s[s.length-1].label+'」是你较为弱势的维度，但这也正是你独特的一面。';
return p}
function genShareText(c,score,u){
var s=DM.map(function(d,i){return{label:d.label,val:u[d.key]}}).sort(function(a,b){return b.val-a.val});
var top3=s.slice(0,3).map(function(d){return d.label}).join('、');
var txt='我的二次元老婆是'+c.name+'（'+c.series+'）！\n契合度：'+score+'%\n性格标签：'+top3+'\n\n'+c.quote+'\n\n来测测你的命运之人是谁→';
return txt}
function renderResult(){
var u=calcUser();var sc=CH.map(function(c){var cc={};cc.id=c.id;cc.name=c.name;cc.series=c.series;cc.tags=c.tags;cc.description=c.description;cc.appearance=c.appearance;cc.traits=c.traits;cc.image=c.image;cc.quote=c.quote;cc.cv=c.cv;cc.birthday=c.birthday;cc.catchphrase=c.catchphrase;cc.color=c.color;cc.favor_quote=c.favor_quote;cc.ms=matchScore(u,c);return cc}).sort(function(a,b){return b.ms-a.ms});
var b=sc[0],t5=sc.slice(0,5);
var tags=b.tags.split(',');var an=genAnalysis(u,b);var pf=genProfile(u);var enc=genEncounter(u,b);var dl=genDailyLife(u,b);var rv=genRival(u,b);var st=genShareText(b,b.ms,u);
document.documentElement.style.setProperty('--accent',b.color||'#e879f9');
var h='<div class="result-card"><div class="result-image-wrap"><img src="'+b.image+'" alt="'+b.name+'" onerror="this.parentNode.innerHTML=\'<div class=&quot;img-placeholder&quot;>'+b.name+'</div>\'" loading="lazy"></div>';
h+='<div class="result-info"><div class="result-series">'+b.series+'</div><h2 class="result-name">'+b.name+'</h2><div class="result-match">契合度 '+b.ms+'%</div>';
h+='<div class="result-tags">';tags.forEach(function(t){h+='<span class="result-tag">'+t+'</span>'});h+='</div>';
h+='<p class="result-desc">'+b.appearance+'</p>';
h+='<div class="result-meta"><div class="result-meta-item"><div class="result-meta-label">声优</div><div class="result-meta-val">'+b.cv+'</div></div><div class="result-meta-item"><div class="result-meta-label">生日</div><div class="result-meta-val">'+b.birthday+'</div></div><div class="result-meta-item"><div class="result-meta-label">口癖</div><div class="result-meta-val" style="font-size:12px">'+b.catchphrase+'</div></div></div>';
h+='<div class="result-quote">「'+b.quote+'」</div>';
h+='</div></div>';
h+='<div class="result-favor-quote"><div class="heart">💗</div><p>'+b.favor_quote+'</p><div class="attr">——'+b.name+' 对你说</div></div>';
h+='<div class="result-analysis"><h3>命运邂逅</h3><p>'+enc+'</p></div>';
h+='<div class="result-analysis"><h3>为什么是她？</h3><p>'+an+'</p></div>';
h+='<div class="result-analysis"><h3>你的性格画像</h3><p>'+pf+'</p></div>';
h+='<div class="radar-chart-wrap"><canvas id="radar" width="400" height="400"></canvas></div>';
h+='<div class="result-analysis"><h3>你们的相处日常</h3><p>'+dl+'</p></div>';
h+='<div class="result-analysis"><h3>潜在情敌分析</h3><p style="margin-bottom:12px">以下角色也与你高度契合，可能会成为你追求'+b.name+'的竞争对手：</p>'+rv+'</div>';
h+='<div class="result-recommendations"><h3>Top 5 推荐角色</h3><div class="rec-grid">';
t5.slice(1).forEach(function(c){h+='<div class="rec-card" onclick=\'showDetail("'+c.id+'")\'><div class="rec-image-wrap"><img src="'+c.image+'" alt="'+c.name+'" onerror="this.style.display=\'none\'" loading="lazy"></div><div class="rec-info"><div class="rec-name">'+c.name+'</div><div class="rec-match">'+c.ms+'%</div></div></div>'});
h+='</div></div>';
h+='<div class="share-section"><h3>分享你的结果</h3><div class="share-text" id="shareText">'+st.replace(/\n/g,'<br>')+'</div><button class="btn btn-primary btn-sm" onclick="copyShareText()">复制分享文案</button></div>';
document.getElementById('resultContent').innerHTML=h;
drawRadar(u,b);
viewStats[b.id]=(viewStats[b.id]||0)+1;try{localStorage.setItem('waifuViewStats',JSON.stringify(viewStats))}catch(e){}
}
function copyShareText(){var txt=document.getElementById('shareText').innerText;navigator.clipboard?navigator.clipboard.writeText(txt).then(function(){showToast('已复制到剪贴板！')}):function(){var ta=document.createElement('textarea');ta.value=txt;document.body.appendChild(ta);ta.select();document.execCommand('copy');document.body.removeChild(ta);showToast('已复制到剪贴板！')}()}
function showToast(msg){var t=document.getElementById('toast');t.textContent=msg;t.classList.add('show');setTimeout(function(){t.classList.remove('show')},2000)}
function drawRadar(u,c){
var cv=document.getElementById('radar');if(!cv)return;var cx=cv.getContext('2d');var ccx=200,ccy=200,R=150,n=DM.length,as=(Math.PI*2)/n;
cx.clearRect(0,0,400,400);
for(var l=1;l<=4;l++){cx.beginPath();for(var i=0;i<=n;i++){var a=i*as-Math.PI/2;var r=R*(l/4);var x=ccx+Math.cos(a)*r;var y=ccy+Math.sin(a)*r;if(i===0)cx.moveTo(x,y);else cx.lineTo(x,y)}cx.strokeStyle='rgba(232,121,249,'+(0.1+l*0.05)+')';cx.lineWidth=1;cx.stroke()}
DM.forEach(function(d,i){var a=i*as-Math.PI/2;var x=ccx+Math.cos(a)*(R+20);var y=ccy+Math.sin(a)*(R+20);cx.fillStyle='#9ca3af';cx.font='12px Noto Sans SC';cx.textAlign='center';cx.textBaseline='middle';cx.fillText(d.label,x,y)});
cx.beginPath();DM.forEach(function(d,i){var a=i*as-Math.PI/2;var r=R*(c.traits[i]/100);var x=ccx+Math.cos(a)*r;var y=ccy+Math.sin(a)*r;if(i===0)cx.moveTo(x,y);else cx.lineTo(x,y)});cx.closePath();cx.fillStyle='rgba(168,85,247,0.15)';cx.strokeStyle='rgba(168,85,247,0.8)';cx.lineWidth=2;cx.fill();cx.stroke();
cx.beginPath();DM.forEach(function(d,i){var a=i*as-Math.PI/2;var r=R*(u[d.key]/100);var x=ccx+Math.cos(a)*r;var y=ccy+Math.sin(a)*r;if(i===0)cx.moveTo(x,y);else cx.lineTo(x,y)});cx.closePath();cx.fillStyle='rgba(232,121,249,0.15)';cx.strokeStyle='rgba(232,121,249,0.8)';cx.lineWidth=2;cx.fill();cx.stroke();
cx.fillStyle='rgba(232,121,249,0.8)';cx.fillRect(20,370,12,12);cx.fillStyle='#f8f7fc';cx.font='12px Noto Sans SC';cx.textAlign='left';cx.fillText('你',40,378);
cx.fillStyle='rgba(168,85,247,0.8)';cx.fillRect(120,370,12,12);cx.fillStyle='#f8f7fc';cx.fillText(c.name,140,378)}
function drawMiniRadar(u){
var cv=document.getElementById('miniCanvas');if(!cv)return;var cx=cv.getContext('2d');var ccx=40,ccy=40,R=30,n=DM.length,as=(Math.PI*2)/n;
cx.clearRect(0,0,80,80);
cx.beginPath();for(var i=0;i<=n;i++){var a=i*as-Math.PI/2;var r=R;var x=ccx+Math.cos(a)*r;var y=ccy+Math.sin(a)*r;if(i===0)cx.moveTo(x,y);else cx.lineTo(x,y)}cx.strokeStyle='rgba(232,121,249,0.2)';cx.lineWidth=1;cx.stroke();
cx.beginPath();DM.forEach(function(d,i){var a=i*as-Math.PI/2;var r=R*(u[d.key]/100);var x=ccx+Math.cos(a)*r;var y=ccy+Math.sin(a)*r;if(i===0)cx.moveTo(x,y);else cx.lineTo(x,y)});cx.closePath();cx.fillStyle='rgba(232,121,249,0.2)';cx.strokeStyle='rgba(232,121,249,0.8)';cx.lineWidth=1.5;cx.fill();cx.stroke()}
function renderGallery(){
var series=[].concat(new Set(CH.map(function(c){return c.series}))).sort();
var fh='<button class="filter-chip '+(curFilter===''?'active':'')+'" onclick="setFilter(\'\')">全部</button>';
series.forEach(function(s){fh+='<button class="filter-chip '+(curFilter===s?'active':'')+'" onclick="setFilter(\''+s.replace(/'/g,"\\'")+'\')">'+s+'</button>'});
document.getElementById('filterBar').innerHTML=fh;
var filtered=CH;
if(curFilter)filtered=filtered.filter(function(c){return c.series===curFilter});
if(searchQuery)filtered=filtered.filter(function(c){return c.name.toLowerCase().includes(searchQuery.toLowerCase())||c.series.toLowerCase().includes(searchQuery.toLowerCase())||c.tags.toLowerCase().includes(searchQuery.toLowerCase())});
var gh='';filtered.forEach(function(c){gh+='<div class="gallery-card" onclick=\'showDetail("'+c.id+'")\'><div class="gallery-image-wrap"><img src="'+c.image+'" alt="'+c.name+'" onerror="this.parentNode.innerHTML=\'<div class=\\\'img-placeholder\\\'>'+c.name+'</div>\'" loading="lazy"></div><div class="gallery-info"><div class="gallery-name">'+c.name+'</div><div class="gallery-series">'+c.series+'</div></div></div>'});
document.getElementById('galleryGrid').innerHTML=gh||'<p style="color:var(--dim);text-align:center;padding:40px">没有找到匹配的角色</p>'}
function onSearch(v){searchQuery=v;renderGallery()}
function setFilter(s){curFilter=s;renderGallery()}
function renderRanking(){
var list=CH.map(function(c){return{id:c.id,name:c.name,series:c.series,image:c.image,tags:c.tags,views:viewStats[c.id]||0,traits:c.traits}}).sort(function(a,b){return b.views-a.views});
if(list.every(function(c){return c.views===0})){
list=CH.map(function(c){return{id:c.id,name:c.name,series:c.series,image:c.image,tags:c.tags,views:Math.floor(Math.random()*100)+1,traits:c.traits}}).sort(function(a,b){return b.views-a.views})}
var h='';list.slice(0,20).forEach(function(c,i){var rn=i+1;var rc=rn<=3?'top'+rn:'';var top3=c.tags.split(',').slice(0,3).join(' · ');
h+='<div class="rank-item" onclick=\'showDetail("'+c.id+'")\'><div class="rank-num '+rc+'">'+rn+'</div><div class="rank-image"><img src="'+c.image+'" alt="'+c.name+'" onerror="this.style.display=\'none\'" loading="lazy"></div><div class="rank-info"><div class="rank-name">'+c.name+'</div><div class="rank-series">'+c.series+'</div><div class="rank-traits">'+top3+'</div></div><div class="rank-score">'+c.views+'次</div></div>'});
document.getElementById('rankingList').innerHTML=h}
function renderCompare(){
var s1=document.getElementById('compareSlot1'),s2=document.getElementById('compareSlot2');
[compareSel[0],compareSel[1]].forEach(function(c,i){var slot=i===0?s1:s2;if(!c){slot.className='compare-slot';slot.innerHTML='<div class="compare-empty">点击选择角色</div>'}else{slot.className='compare-slot has-char';slot.innerHTML='<div class="compare-image-wrap"><img src="'+c.image+'" alt="'+c.name+'" onerror="this.style.display=\'none\'"></div><div style="font-size:15px;font-weight:600;text-align:center">'+c.name+'</div><div style="font-size:12px;color:var(--dim);text-align:center">'+c.series+'</div><div style="font-size:11px;color:var(--accent);margin-top:4px;text-align:center">点击更换</div>'}});
if(compareSel[0]&&compareSel[1]){document.getElementById('compareResult').style.display='block';drawCompareRadar();renderCompareDetails()}else{document.getElementById('compareResult').style.display='none'}}
function openComparePicker(slot){pickerTarget=slot;document.getElementById('pickerSearch').value='';renderPicker('');document.getElementById('pickerModal').classList.add('active')}
function renderPicker(q){
var filtered=CH;if(q)filtered=CH.filter(function(c){return c.name.toLowerCase().includes(q.toLowerCase())||c.series.toLowerCase().includes(q.toLowerCase())});
var h='<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(100px,1fr));gap:8px">';
filtered.forEach(function(c){h+='<div style="background:var(--card2);border:1px solid var(--border);border-radius:8px;overflow:hidden;cursor:pointer" onclick="pickChar(\''+c.id+'\')"><div style="aspect-ratio:1;overflow:hidden;display:flex;align-items:center;justify-content:center;background:var(--bg)"><img src="'+c.image+'" style="max-width:100%;max-height:100%;object-fit:contain" onerror="this.style.display=\'none\'" loading="lazy"></div><div style="padding:4px;font-size:11px;text-align:center;white-space:nowrap;overflow:hidden;text-overflow:ellipsis">'+c.name+'</div></div>'});
h+='</div>';document.getElementById('pickerGrid').innerHTML=h}
function onPickerSearch(v){renderPicker(v)}
function pickChar(id){compareSel[pickerTarget-1]=CH.find(function(c){return c.id===id});closePicker();renderCompare()}
function closePicker(e){if(e&&e.target!==document.getElementById('pickerModal'))return;document.getElementById('pickerModal').classList.remove('active')}
function drawCompareRadar(){
var cv=document.getElementById('compareRadar');if(!cv)return;var cx=cv.getContext('2d');var ccx=200,ccy=200,R=150,n=DM.length,as=(Math.PI*2)/n;
cx.clearRect(0,0,400,400);
for(var l=1;l<=4;l++){cx.beginPath();for(var i=0;i<=n;i++){var a=i*as-Math.PI/2;var r=R*(l/4);var x=ccx+Math.cos(a)*r;var y=ccy+Math.sin(a)*r;if(i===0)cx.moveTo(x,y);else cx.lineTo(x,y)}cx.strokeStyle='rgba(232,121,249,'+(0.1+l*0.05)+')';cx.lineWidth=1;cx.stroke()}
DM.forEach(function(d,i){var a=i*as-Math.PI/2;var x=ccx+Math.cos(a)*(R+20);var y=ccy+Math.sin(a)*(R+20);cx.fillStyle='#9ca3af';cx.font='12px Noto Sans SC';cx.textAlign='center';cx.textBaseline='middle';cx.fillText(d.label,x,y)});
var colors=[{f:'rgba(232,121,249,0.15)',s:'rgba(232,121,249,0.8)'},{f:'rgba(34,211,238,0.15)',s:'rgba(34,211,238,0.8)'}];
[compareSel[0],compareSel[1]].forEach(function(c,idx){if(!c)return;cx.beginPath();DM.forEach(function(d,i){var a=i*as-Math.PI/2;var r=R*(c.traits[i]/100);var x=ccx+Math.cos(a)*r;var y=ccy+Math.sin(a)*r;if(i===0)cx.moveTo(x,y);else cx.lineTo(x,y)});cx.closePath();cx.fillStyle=colors[idx].f;cx.strokeStyle=colors[idx].s;cx.lineWidth=2;cx.fill();cx.stroke()});
cx.fillStyle='rgba(232,121,249,0.8)';cx.fillRect(20,370,12,12);cx.fillStyle='#f8f7fc';cx.font='12px Noto Sans SC';cx.textAlign='left';cx.fillText(compareSel[0].name,40,378);
cx.fillStyle='rgba(34,211,238,0.8)';cx.fillRect(200,370,12,12);cx.fillStyle='#f8f7fc';cx.fillText(compareSel[1].name,220,378)}
function renderCompareDetails(){
var c1=compareSel[0],c2=compareSel[1];var h='<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px">';
[{c:c1,label:'左'},{c:c2,label:'右'}].forEach(function(item){var c=item.c;var tags=c.tags.split(',');
h+='<div class="result-analysis"><div style="font-size:13px;color:var(--accent);margin-bottom:4px">'+c.series+'</div><h3 style="font-size:18px;margin-bottom:8px">'+c.name+'</h3><div class="result-tags">';tags.forEach(function(t){h+='<span class="result-tag">'+t+'</span>'});h+='</div>';
h+='<div class="result-meta"><div class="result-meta-item"><div class="result-meta-label">声优</div><div class="result-meta-val" style="font-size:12px">'+c.cv+'</div></div><div class="result-meta-item"><div class="result-meta-label">生日</div><div class="result-meta-val" style="font-size:12px">'+c.birthday+'</div></div></div>';
h+='<p style="color:var(--dim);font-size:13px;line-height:1.6;margin:8px 0">'+c.appearance+'</p>';
h+='<div class="result-quote" style="font-size:13px">「'+c.quote+'」</div></div>'});
h+='</div>';
var diff=[];DM.forEach(function(d,i){diff.push({label:d.label,v1:c1.traits[i],v2:c2.traits[i],diff:Math.abs(c1.traits[i]-c2.traits[i])})});diff.sort(function(a,b){return b.diff-a.diff});
h+='<div class="result-analysis"><h3>最大差异维度</h3>';
diff.slice(0,5).forEach(function(d){h+='<div class="bar-row"><div class="bar-label">'+d.label+'</div><div class="bar-track"><div class="bar-fill" style="width:'+(d.v1)+'%;background:rgba(232,121,249,0.6)"></div><div class="bar-fill" style="width:'+(d.v2)+'%;background:rgba(34,211,238,0.6);position:absolute;top:0;left:0;opacity:0.5"></div></div><div style="font-size:12px;color:var(--dim);width:40px">'+d.v1+' vs '+d.v2+'</div></div>'});
h+='</div>';
document.getElementById('compareDetails').innerHTML=h}
function renderStats(){
var totalChars=CH.length;var totalSeries=new Set(CH.map(function(c){return c.series})).size;var totalCv=new Set(CH.map(function(c){return c.cv})).size;
var avgTraits=[];DM.forEach(function(d,i){var sum=CH.reduce(function(s,c){return s+c.traits[i]},0);avgTraits.push({label:d.label,avg:Math.round(sum/CH.length),color:d.color})});
avgTraits.sort(function(a,b){return b.avg-a.avg});
var h='';
h+='<div class="stat-card"><div class="num">'+totalChars+'</div><div class="label">收录角色</div></div>';
h+='<div class="stat-card"><div class="num">'+totalSeries+'</div><div class="label">收录作品</div></div>';
h+='<div class="stat-card"><div class="num">'+totalCv+'</div><div class="label">声优数量</div></div>';
h+='<div class="stat-card"><div class="num">12</div><div class="label">性格维度</div></div>';
document.getElementById('statsGrid').innerHTML=h;
var bh='<h3 style="font-size:16px;margin-bottom:16px;color:var(--accent)">12维平均分</h3>';
avgTraits.forEach(function(t){bh+='<div class="bar-row"><div class="bar-label">'+t.label+'</div><div class="bar-track"><div class="bar-fill" style="width:'+t.avg+'%;background:'+t.color+'"><span class="bar-val">'+t.avg+'</span></div></div></div>'});
document.getElementById('avgBarChart').innerHTML=bh;
var seriesCount={};CH.forEach(function(c){seriesCount[c.series]=(seriesCount[c.series]||0)+1});
var seriesArr=Object.keys(seriesCount).map(function(k){return{name:k,count:seriesCount[k]}}).sort(function(a,b){return b.count-a.count});
var sh='';seriesArr.forEach(function(s){sh+='<div class="bar-row"><div class="bar-label" style="width:120px;font-size:12px">'+s.name+'</div><div class="bar-track"><div class="bar-fill" style="width:'+(s.count/seriesArr[0].count*100)+'%;background:linear-gradient(90deg,var(--pink),var(--purple))"><span class="bar-val">'+s.count+'</span></div></div></div>'});
document.getElementById('seriesChart').innerHTML=sh}
function showDetail(id){
var c=CH.find(function(x){return x.id===id});if(!c)return;
viewStats[id]=(viewStats[id]||0)+1;try{localStorage.setItem('waifuViewStats',JSON.stringify(viewStats))}catch(e){}
var tags=c.tags.split(',');
var h='<div class="modal-image-wrap"><img src="'+c.image+'" alt="'+c.name+'" onerror="this.style.display=\'none\'" loading="lazy"></div><div class="modal-body">';
h+='<div style="font-size:13px;color:var(--accent);margin-bottom:4px">'+c.series+'</div><h2 style="font-size:24px;margin-bottom:8px">'+c.name+'</h2>';
h+='<div style="display:flex;gap:8px;flex-wrap:wrap;margin-bottom:12px">';tags.forEach(function(t){h+='<span class="result-tag">'+t+'</span>'});h+='</div>';
h+='<div class="result-meta"><div class="result-meta-item"><div class="result-meta-label">声优</div><div class="result-meta-val" style="font-size:13px">'+c.cv+'</div></div><div class="result-meta-item"><div class="result-meta-label">生日</div><div class="result-meta-val" style="font-size:13px">'+c.birthday+'</div></div><div class="result-meta-item"><div class="result-meta-label">口癖</div><div class="result-meta-val" style="font-size:11px">'+c.catchphrase+'</div></div></div>';
h+='<p style="color:var(--dim);font-size:14px;line-height:1.8;margin-bottom:12px">'+c.appearance+'</p>';
h+='<div class="result-quote" style="margin-bottom:12px">「'+c.quote+'」</div>';
h+='<p style="font-size:14px;line-height:1.8">'+c.description+'</p>';
h+='<div class="result-favor-quote" style="margin-top:16px"><div class="heart">💗</div><p style="font-size:14px">'+c.favor_quote+'</p><div class="attr">——'+c.name+'</div></div>';
h+='<h3 style="font-size:14px;margin:16px 0 8px;color:var(--accent)">性格维度</h3><div style="display:grid;grid-template-columns:repeat(3,1fr);gap:8px">';
DM.forEach(function(d,i){var v=c.traits[i];h+='<div style="text-align:center"><div style="font-size:12px;color:var(--dim)">'+d.label+'</div><div style="font-size:18px;font-weight:700;color:'+(v>70?'var(--accent)':v>40?'var(--text)':'var(--dim)')+'">'+v+'</div></div>'});
h+='</div></div>';
document.getElementById('modalContent').innerHTML=h;
document.getElementById('modal').classList.add('active')}
function closeModal(e){if(e&&e.target!==document.getElementById('modal'))return;document.getElementById('modal').classList.remove('active')}
goHome();
</script>
</body>
</html>'''

with open('github-pages-app-v2.html', 'w', encoding='utf-8') as f:
    f.write(html)

import os
size = os.path.getsize('github-pages-app-v2.html')
print(f'Generated: {size} bytes ({size/1024:.1f} KB)')
print(f'Characters: {len(chars)}, Questions: {len(questions)}, Dimensions: {len(dims)}')
