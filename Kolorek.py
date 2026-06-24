from PIL import Image
import subprocess
import sys

width = 3440
height = 1440

start = sys.argv[1]

img = Image.new("RGB", (width, height))
pixels = img.load()

if len(sys.argv) == 1 or len(sys.argv)>3:
    print("Usage: wallpaper.py '#RRGGBB'")
    sys.exit(1)
elif len(sys.argv) == 2:
    img = Image.new("RGB",(width,height),start)
else:
    end   = sys.argv[2]
    start = (int(start[1:3],16),int(start[3:5],16),int(start[5:],16))
    end = (int(end[1:3],16),int(end[3:5],16),int(end[5:],16))
    
    for x in range(width):
        t = x / (width - 1)
    
        r = int(start[0] * (1 - t) + end[0] * t)
        g = int(start[1] * (1 - t) + end[1] * t)
        b = int(start[2] * (1 - t) + end[2] * t)
    
        for y in range(height):
            pixels[x, y] = (r, g, b)

output = "/tmp/solid_wallpaper.png"
img.save(output)

# GNOME
subprocess.run([
    "gsettings",
    "set",
    "org.gnome.desktop.background",
    "picture-uri",
    f"file://{output}"
])

subprocess.run([
    "gsettings",
    "set",
    "org.gnome.desktop.background",
    "picture-uri-dark",
    f"file://{output}"
])

print(f"Wallpaper set")
