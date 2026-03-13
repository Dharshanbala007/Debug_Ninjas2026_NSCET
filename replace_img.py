import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

with open("nscetlogo.txt", "r", encoding="utf-8") as f:
    new_b64 = f.read().strip()

# Replace only the first occurrence (which is the NSCET logo)
def repl(match):
    return f'src="data:image/png;base64,{new_b64}"'

new_html = re.sub(r'src="data:image/png;base64,([^"]+)"', repl, html, count=1)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(new_html)

print("Replacement successful.")
