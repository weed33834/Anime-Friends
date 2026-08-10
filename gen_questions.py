#!/usr/bin/env python3
"""Append questions data to index.html"""
import os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'index.html')

questions = [
{"tag":"日常","q":"深夜加班回家，推开门的那一刻，你最希望看到什么场景？","options":[
{"text":"暖黄的灯光下，她端着热汤等你回来，柔声说'辛苦了'","dims":{"gentle":3,"loyal":2}},
{"text":"她蹦跳着冲过来，兴奋地说'你终于回来啦！快来看我今天的战利品！'","dims":{"energy":3,"playful":2}},
{"text":"她正专注地看书，抬头看你一眼说'回来了？饭在桌上，自己热一下'","dims":{"independent":2,"mature":3}},
{"text":"她背对你说'才没有等你呢'，但你注意到桌上的饭菜还是热的","dims":{"tsundere":3,"loyal":1}}]},

{"tag":"早晨","q":"周末早晨醒来，你希望身边的她是怎样的状态？","options":[
{"text":"已经悄悄起来做好了早餐，正温柔地看着你睡醒","dims":{"gentle":3,"mature":1}},
{"text":"像猫咪一样蜷缩在你怀里，赖床不肯起来","dims":{"playful":3,"gentle":1}},
{"text":"早就出门晨跑了，留了张纸条说'记得吃早饭'","dims":{"independent":3,"energy":2}},
{"text":"嘴上嘟囔着'好困'，却还是挣扎着起来给你做早饭","dims":{"tsundere":3,"loyal":2}}]},

{"tag":"冲突","q":"两个人吵架了，你希望她会怎么做？","options":[
{"text":"主动来跟你道歉，红着眼眶拉着你的手说'对不起'","dims":{"gentle":3,"loyal":2}},
{"text":"给你发一堆搞笑表情包破冰，假装什么都没发生","dims":{"playful":3,"energy":2}},
{"text":"冷静地找你谈，一条条分析问题出在哪里","dims":{"independent":3,"mature":3}},
{"text":"嘴上说'我才不生气'，但表情明显在说'快来哄我'","dims":{"tsundere":3,"playful":1}}]},

{"tag":"生日","q":"你过生日时，最期待她送你什么？","options":[
{"text":"亲手做的礼物，虽然不完美但充满心意","dims":{"gentle":3,"loyal":2}},
{"text":"你们一起去做一件你们都没尝试过的疯狂事情","dims":{"energy":3,"playful":2}},
{"text":"一本你提过很久的书，或者你需要的实用物品","dims":{"mature":3,"independent":1}},
{"text":"嘴上说'随便买的'，但其实是你上次多看了两眼的东西","dims":{"tsundere":3,"loyal":2}}]},

{"tag":"脆弱","q":"在她面前示弱时，你希望她的反应是？","options":[
{"text":"轻轻抱住你，说'没关系的，有我在'","dims":{"gentle":3,"loyal":2}},
{"text":"拍拍你的肩说'走！去吃顿好的就好了！'","dims":{"energy":3,"playful":1}},
{"text":"认真听你倾诉，然后帮你理清思路","dims":{"mature":3,"independent":2}},
{"text":"嘴上说'真没用'，手却已经在帮你倒热水了","dims":{"tsundere":3,"loyal":2}}]},

{"tag":"同居","q":"你心目中理想的同居生活是什么样的？","options":[
{"text":"温馨的房间，两个人一起做饭、看电影、依偎在一起","dims":{"gentle":3,"loyal":2}},
{"text":"充满笑声的家，经常有朋友来聚会，热闹非凡","dims":{"energy":3,"playful":2}},
{"text":"各自有独立空间，偶尔交集，互相尊重彼此的生活节奏","dims":{"independent":3,"mature":2}},
{"text":"日常拌嘴但谁都离不开谁，嘴上嫌弃身体诚实","dims":{"tsundere":3,"playful":2}}]},

{"tag":"心动","q":"你最容易被哪种瞬间击中内心？","options":[
{"text":"她不经意间为你做了件小事，比如帮你整理衣领","dims":{"gentle":3,"loyal":1}},
{"text":"她在人群中笑得灿烂，回头看见你时笑容更亮了","dims":{"energy":3,"playful":1}},
{"text":"她专注做某件事时认真的侧脸，眼神坚定","dims":{"independent":3,"elegant":2}},
{"text":"她嘴上说着'笨蛋'，手却不自觉地牵紧了你","dims":{"tsundere":3,"loyal":2}}]},

{"tag":"价值观","q":"你认为爱情中最重要的是？","options":[
{"text":"相互包容，彼此温暖，让对方感到安心","dims":{"gentle":3,"loyal":2}},
{"text":"一起经历有趣的事，永远保持新鲜感","dims":{"energy":3,"playful":2}},
{"text":"互相尊重彼此的独立人格，共同成长","dims":{"independent":3,"mature":2}},
{"text":"嘴上不说爱，但行动上处处为对方着想","dims":{"tsundere":3,"loyal":2}}]},

{"tag":"穿搭","q":"你希望她的穿衣风格是？","options":[
{"text":"温柔系，碎花裙、针织衫，给人柔软的感觉","dims":{"gentle":3,"elegant":1}},
{"text":"活力系，运动装、短裙，充满青春气息","dims":{"energy":3,"playful":1}},
{"text":"简约干练，衬衫西裤，利落大方","dims":{"independent":3,"mature":2}},
{"text":"有点小个性，带着不经意的性感或可爱","dims":{"tsundere":2,"playful":2}}]},

{"tag":"恐惧","q":"你们一起看恐怖电影时，她会是？","options":[
{"text":"紧紧抓着你的手，但嘴上逞强说不怕","dims":{"tsundere":3,"loyal":1}},
{"text":"比你还怕，直接扑进你怀里","dims":{"gentle":2,"playful":2}},
{"text":"完全不怕，还给你科普恐怖片拍摄手法","dims":{"independent":3,"mature":2}},
{"text":"尖叫着把爆米花洒一地，然后哈哈大笑","dims":{"energy":3,"playful":2}}]},

{"tag":"称呼","q":"你希望她怎么称呼你？","options":[
{"text":"温柔地叫你的名字，语气柔软","dims":{"gentle":3}},
{"text":"给你起一堆奇怪的外号，每天不重样","dims":{"playful":3,"energy":2}},
{"text":"直接叫姓或全名，简洁利落","dims":{"independent":2,"mature":2}},
{"text":"嘴上叫'笨蛋''烦人精'，但语气里满是宠溺","dims":{"tsundere":3,"loyal":1}}]},

{"tag":"生病","q":"你生病的时候，她最可能做的事是？","options":[
{"text":"守在床边寸步不离，亲手熬粥喂你喝","dims":{"gentle":3,"loyal":3}},
{"text":"冲出去买药，回来路上还顺便买了你爱吃的零食","dims":{"energy":3,"playful":1}},
{"text":"查好症状和用药说明，理性地安排你吃药休息","dims":{"independent":2,"mature":3}},
{"text":"嘴上说'谁让你不好好穿衣服'，手上却在帮你量体温","dims":{"tsundere":3,"loyal":2}}]},

{"tag":"未来","q":"对于未来的规划，你希望她是？","options":[
{"text":"愿意和你一起慢慢规划，把两个人的未来编织在一起","dims":{"gentle":3,"loyal":2}},
{"text":"充满期待地畅想各种可能性，每一个计划都有你有她","dims":{"energy":3,"playful":1}},
{"text":"有自己的目标和方向，但也愿意为你们的关系留出空间","dims":{"independent":3,"mature":2}},
{"text":"嘴上说着'谁要跟你过一辈子'，但已经在默默存钱了","dims":{"tsundere":3,"loyal":2}}]},

{"tag":"浪漫","q":"你认为最浪漫的事情是？","options":[
{"text":"在雨中同撑一把伞，她把伞偏向你这边","dims":{"gentle":3,"loyal":2}},
{"text":"说走就走的旅行，两个人在陌生城市迷路也开心","dims":{"energy":3,"playful":2}},
{"text":"深夜长谈，聊到凌晨三点发现彼此灵魂共振","dims":{"independent":2,"mature":3}},
{"text":"她别扭地递给你一封手写信，脸红着说'别看！'","dims":{"tsundere":3,"gentle":1}}]},

{"tag":"社交","q":"你希望她在社交场合是？","options":[
{"text":"安静地待在你身边，偶尔微笑，给你安全感","dims":{"gentle":3,"loyal":2}},
{"text":"全场焦点，热情开朗，和所有人都能聊得来","dims":{"energy":3,"playful":2}},
{"text":"优雅从容，言谈得体，让人忍不住想靠近","dims":{"elegant":3,"mature":2}},
{"text":"表面冷淡不近人情，只有对你才会露出笑容","dims":{"tsundere":3,"loyal":2}}]},

{"tag":"困难","q":"当你们面对困难时，你希望她？","options":[
{"text":"坚定地说'不管发生什么，我都在你身边'","dims":{"loyal":3,"gentle":2}},
{"text":"拍着胸脯说'有什么好怕的！我们一起上！'","dims":{"energy":3,"playful":1}},
{"text":"冷静分析局势，拿出可行的解决方案","dims":{"independent":3,"mature":3}},
{"text":"嘴上说'真麻烦'，但已经在默默帮你处理了","dims":{"tsundere":3,"loyal":2}}]},

{"tag":"告白","q":"你最喜欢的告白方式是？","options":[
{"text":"在樱花飘落的季节，她红着脸轻声说'我喜欢你'","dims":{"gentle":3,"elegant":2}},
{"text":"在游乐园的摩天轮上，她大声喊出'我喜欢你！'","dims":{"energy":3,"playful":2}},
{"text":"在安静的咖啡馆，她认真地看着你的眼睛说'我想和你在一起'","dims":{"mature":3,"independent":2}},
{"text":"她别扭地把情书塞给你，转身就跑，耳朵红透了","dims":{"tsundere":3,"loyal":1}}]},

{"tag":"相处","q":"你希望你们之间的相处模式是？","options":[
{"text":"彼此温柔以待，细水长流地经营每一天","dims":{"gentle":3,"loyal":2}},
{"text":"热热闹闹，打打闹闹，每天都像在冒险","dims":{"energy":3,"playful":2}},
{"text":"互相尊重边界，在各自独立的基础上相爱","dims":{"independent":3,"mature":2}},
{"text":"嘴上互怼不停，但心里都知道对方是最重要的人","dims":{"tsundere":3,"playful":1}}]},

{"tag":"特长","q":"如果她有一项特长，你希望是？","options":[
{"text":"厨艺精湛，能用美食治愈你所有的疲惫","dims":{"gentle":3,"mature":1}},
{"text":"运动全能，拉着你一起挥洒汗水","dims":{"energy":3,"playful":1}},
{"text":"学识渊博，能和你探讨任何话题","dims":{"independent":3,"mature":2}},
{"text":"才艺出众，但只愿意在你面前展示","dims":{"tsundere":2,"elegant":2}}]},

{"tag":"笑容","q":"你希望她的笑容是？","options":[
{"text":"温柔的微笑，像春风拂面，让人心安","dims":{"gentle":3,"elegant":1}},
{"text":"灿烂的大笑，毫无顾忌，感染力十足","dims":{"energy":3,"playful":2}},
{"text":"淡淡的嘴角上扬，带着几分知性","dims":{"mature":3,"elegant":2}},
{"text":"嘴上说着'哼'，嘴角却忍不住上翘","dims":{"tsundere":3,"playful":1}}]},

{"tag":"约会","q":"你心中最理想的约会是？","options":[
{"text":"在家一起做饭、看电影、窝在沙发上聊天","dims":{"gentle":3,"loyal":2}},
{"text":"去游乐园/水族馆/动物园，玩到天黑才回家","dims":{"energy":3,"playful":2}},
{"text":"逛美术馆/博物馆/书店，安静地享受文化氛围","dims":{"elegant":3,"mature":2}},
{"text":"漫无目的地夜游城市，在无人的街道上牵手散步","dims":{"tsundere":2,"independent":2}}]},

{"tag":"品质","q":"你最看重伴侣的哪个品质？","options":[
{"text":"善良温柔，能感知他人的情绪","dims":{"gentle":3,"loyal":1}},
{"text":"乐观开朗，永远充满正能量","dims":{"energy":3,"playful":1}},
{"text":"独立自主，有自己的人生追求","dims":{"independent":3,"mature":2}},
{"text":"嘴硬心软，表面高冷内心炽热","dims":{"tsundere":3,"loyal":2}}]},

{"tag":"表达","q":"你希望她怎么表达爱意？","options":[
{"text":"用行动默默付出，在生活细节中体现关心","dims":{"gentle":3,"loyal":3}},
{"text":"直白热烈地说'我爱你'，丝毫不掩饰","dims":{"energy":3,"playful":2}},
{"text":"用理性的方式表达，比如帮你规划未来","dims":{"mature":3,"independent":2}},
{"text":"从来不说爱，但你就是知道她把你放在第一位","dims":{"tsundere":3,"loyal":2}}]},

{"tag":"总结","q":"最后一题：如果用一个词形容你心中的理想伴侣，你会选？","options":[
{"text":"温暖——像冬日里的暖阳，照亮你的整个世界","dims":{"gentle":3,"loyal":2}},
{"text":"元气——像夏日里的清风，让生活充满活力","dims":{"energy":3,"playful":2}},
{"text":"独立——像秋日里的星空，遥远却令人向往","dims":{"independent":3,"mature":2}},
{"text":"傲娇——像春天里的猫，嘴上不亲你，却总是蹭过来","dims":{"tsundere":3,"playful":1}}]},
]

import json
js = 'const questions = ' + json.dumps(questions, ensure_ascii=False) + ';\n'

with open(OUT, 'a', encoding='utf-8') as f:
    f.write(js)

print(f"Questions appended. File size: {os.path.getsize(OUT)} bytes")
