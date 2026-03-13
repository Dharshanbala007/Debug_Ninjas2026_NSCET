import base64

file_path = r"C:\Users\dhars\.gemini\antigravity\brain\245234ac-06fd-4167-a18f-18112b5bb84e\media__1773380953821.png"
with open(file_path, "rb") as f:
    data = f.read()
    b64 = base64.b64encode(data).decode('utf-8')
    
print("b64 length:", len(b64))

with open("nscetlogo.txt", "w") as out:
    out.write(b64)
