import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

js_start = content.find('<script>')
js_end = content.find('</script>', js_start)
js_code = content[js_start:js_end]

# 检查 typewriterText
if 'const typewriterText' in js_code or 'let typewriterText' in js_code:
    print('[OK] typewriterText defined')
else:
    print('[ERROR] typewriterText NOT defined!')
    idx = js_code.find('typewriterText')
    if idx != -1:
        print('Usage at:', js_code[max(0,idx-50):idx+50])

# 检查括号匹配 - Ink 类
if 'class InkExplosion' in js_code:
    print('[OK] InkExplosion class found')
if 'class InkVortex' in js_code:
    print('[OK] InkVortex class found')
if 'class InkRaindrop' in js_code:
    print('[OK] InkRaindrop class found')

# 检查 initInkInteractions
if 'function initInkInteractions()' in js_code:
    print('[OK] initInkInteractions found')

# 检查语法 - 查找未闭合的大括号
open_braces = js_code.count('{')
close_braces = js_code.count('}')
print(f'Braces: open={open_braces}, close={close_braces}')
if open_braces != close_braces:
    print('[ERROR] Brace mismatch!')
