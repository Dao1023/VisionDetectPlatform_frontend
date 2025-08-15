import os

html_files = [f for f in os.listdir() if f.endswith('.html') and f != 'index.html']
html_files.sort()

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(f'''<!DOCTYPE html>
<html>
<head>
    <title>文件列表</title>
    <style>
        body {{ font-family: sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }}
        li {{ padding: 5px; }}
        a {{ color: #0366d6; }}
    </style>
</head>
<body>
    <h1>共 {len(html_files)} 个HTML文件</h1>
    <ul>
        {"".join(f'<li><a href="{file}">{file}</a></li>' for file in html_files)}
    </ul>
</body>
</html>''')

print("✅ 已生成 index.html")