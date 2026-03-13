import struct

def get_png_size(file_path):
    with open(file_path, "rb") as f:
        data = f.read(24)
        if data[:8] == b'\x89PNG\r\n\x1a\n':
            w, h = struct.unpack('>II', data[16:24])
            print(f"Original Logo: width={w}, height={h}")
        else:
            print("Original Logo is not a valid PNG")

get_png_size("nscetlogo.png")
