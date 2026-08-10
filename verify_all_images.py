#!/usr/bin/env python3
"""Comprehensive image quality check for all 88 characters"""
import json, urllib.request, ssl, os, time
from PIL import Image

with open('characters_enriched.json', 'r', encoding='utf-8') as f:
    chars = json.load(f)

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

os.makedirs('img_verify', exist_ok=True)

results = []
for i, c in enumerate(chars):
    url = c['image']
    name = c['name']
    char_id = c['id']
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        resp = urllib.request.urlopen(req, timeout=15, context=ctx)
        data = resp.read()
        size = len(data)
        
        ext = '.jpg'
        content_type = resp.headers.get('Content-Type', '')
        if 'png' in content_type.lower(): ext = '.png'
        elif 'webp' in content_type.lower(): ext = '.webp'
        elif 'gif' in content_type.lower(): ext = '.gif'
        
        filepath = f'img_verify/{i:03d}_{char_id}{ext}'
        with open(filepath, 'wb') as f:
            f.write(data)
        
        # Analyze image
        img = Image.open(filepath)
        w, h = img.size
        aspect = w / h if h > 0 else 0
        
        # Quality assessment
        issues = []
        if size < 15000: issues.append('TOO_SMALL')
        if w < 400 or h < 400: issues.append('LOW_RES')
        if aspect > 2.0: issues.append('TOO_WIDE')
        if aspect < 0.4: issues.append('TOO_TALL')
        if w > 3000 and h > 3000: issues.append('TOO_BIG')
        
        status = 'OK' if not issues else 'WARN'
        
        results.append({
            'id': char_id, 'name': name, 'series': c['series'],
            'url': url, 'size': size, 'width': w, 'height': h,
            'aspect': round(aspect, 2), 'status': status, 'issues': issues
        })
        
        marker = '✅' if status == 'OK' else '⚠️'
        print(f"{marker} {i:3d} {name:20s} {w}x{h} {size/1024:7.1f}KB aspect:{aspect:.2f} {issues}")
        
    except Exception as e:
        results.append({
            'id': char_id, 'name': name, 'series': c['series'],
            'url': url, 'size': 0, 'width': 0, 'height': 0,
            'aspect': 0, 'status': 'ERROR', 'issues': [str(e)]
        })
        print(f"❌ {i:3d} {name:20s} ERROR: {e}")
    
    if (i + 1) % 10 == 0:
        print(f"--- Progress: {i+1}/88 ---")
    time.sleep(0.2)

# Summary
print(f"\n{'='*80}")
print(f"Total: {len(results)}")
ok_count = sum(1 for r in results if r['status'] == 'OK')
warn_count = sum(1 for r in results if r['status'] == 'WARN')
error_count = sum(1 for r in results if r['status'] == 'ERROR')
print(f"OK: {ok_count}, WARN: {warn_count}, ERROR: {error_count}")

print(f"\nCharacters with issues:")
for r in results:
    if r['status'] != 'OK':
        print(f"  {r['id']:20s} ({r['name']}) - {r['issues']} - {r['url'][:80]}")

# Save report
with open('img_verify_report.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"\nReport saved to img_verify_report.json")
