import base64
import struct
import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

matches = re.findall(r'src="data:image/png;base64,([^"]+)"', html)
print(f"Found {len(matches)} images")

for i, b64 in enumerate(matches):
    try:
        data = base64.b64decode(b64)
        if data[:8] == b'\x89PNG\r\n\x1a\n':
            w, h = struct.unpack('>II', data[16:24])
            print(f"Image {i}: width={w}, height={h}")
        else:
            print(f"Image {i}: not a valid PNG")
    except Exception as e:
        print(e)
