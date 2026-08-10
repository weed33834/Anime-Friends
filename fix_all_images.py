#!/usr/bin/env python3
"""Fix all problematic character images"""
import json

with open('characters_enriched.json', 'r', encoding='utf-8') as f:
    chars = json.load(f)

# All replacement URLs - verified good quality
replacements = {
    # Download errors / timeouts
    'kuroneko': 'http://imgs.aixifan.com/newUpload/51387580_bf833e6e07604029897a2c2c777f4bac.jpeg',
    'eru': 'http://bkimg.cdn.bcebos.com/pic/fd039245d688d43f10d39c567d1ed21b0ef43b1f',
    'louise': 'http://gips1.baidu.com/it/u=1067081701,2642560764&fm=3074&app=3074&f=JPEG',
    'aria': 'http://imgs.aixifan.com/newUpload/74239842_88c3702e9caf406b9f9cd0a02fc152a3.jpeg',
    
    # Low resolution / wrong orientation
    'misato': 'http://i0.hdslb.com/bfs/new_dyn/3736e1557dc2cf71d6aec4619a98662a347470220.png@1192w.webp',
    'ayu': 'http://bkimg.cdn.bcebos.com/pic/37d3d539b6003af346a509da352ac65c1038b669',
    'kotonoha': 'http://bkimg.cdn.bcebos.com/pic/738b4710b912c8fcab37a26bfc039245d788214b',
    'shana': 'http://img2.huashi6.com/images/resource/thumbnail/2023/11/05/141534_93454414895.jpg?imageMogr2/quality=100/interlace=1/thumbnail/2000x',
    'makoto': 'http://gips0.baidu.com/it/u=1920275902,2738618676&fm=3074&app=3074&f=JPEG',
    'chizuru': 'http://b0.bdstatic.com/ugc/fbtBjm1Q4qMaqWIRrpmx2Aa5b1c57ac3ca1cb09d7f5f743618e679.jpg@h_1280',
    'nezuko': 'http://gips2.baidu.com/it/u=1344379572,1479101649&fm=3074&app=3074&f=JPEG',
    'asuna': 'http://b0.bdstatic.com/ugc/CzOWc7KIUh_jjLhnHkbd5Ad7775ef76f67d477a81d5cbca63c1a0c.jpg@h_1280',
    'ai': 'http://bkimg.cdn.bcebos.com/pic/9922720e0cf3d7ca7bcb72d04249a9096b63f6240344',
    'shouko': 'http://n.sinaimg.cn/sinakd20121/0/w1920h2880/20240606/c2a2-02880bb09aad22c0a6d52003c5bec2eb.jpg',
}

updated = 0
for c in chars:
    if c['id'] in replacements:
        c['image'] = replacements[c['id']]
        updated += 1
        print(f"Updated: {c['name']} ({c['id']})")

with open('characters_enriched.json', 'w', encoding='utf-8') as f:
    json.dump(chars, f, ensure_ascii=False, indent=2)

print(f"\nTotal updated: {updated} characters")
print("Saved to characters_enriched.json")
