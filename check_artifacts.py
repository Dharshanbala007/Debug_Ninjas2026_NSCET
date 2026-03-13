import struct
import glob
import os

artifact_dir = r"C:\Users\dhars\.gemini\antigravity\brain\245234ac-06fd-4167-a18f-18112b5bb84e"

for file_path in glob.glob(os.path.join(artifact_dir, "*.png")):
    with open(file_path, "rb") as f:
        data = f.read(24)
        if data[:8] == b'\x89PNG\r\n\x1a\n':
            w, h = struct.unpack('>II', data[16:24])
            print(f"File {os.path.basename(file_path)}: width={w}, height={h}")
        else:
            print(f"File {os.path.basename(file_path)}: not a valid PNG")
