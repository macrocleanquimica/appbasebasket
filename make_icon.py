from PIL import Image, ImageDraw
S = 1024
bg = (11, 18, 32)
img = Image.new('RGB', (S, S), bg)
d = ImageDraw.Draw(img)
cx = cy = S // 2
R = int(S * 0.31)
box = [cx - R, cy - R, cx + R, cy + R]
d.ellipse(box, fill=(255, 107, 0), outline=(122, 44, 0), width=30)
w = 42
c = (11, 18, 32)
d.line([cx - R, cy, cx + R, cy], fill=c, width=w)
d.line([cx, cy - R, cx, cy + R], fill=c, width=w)
d.arc([cx - R, cy - R, cx + R, cy + R], start=300, end=60, fill=c, width=w)
d.arc([cx - 2 * R, cy - R, cx, cy + R], start=290, end=70, fill=c, width=w)
d.arc([cx, cy - R, cx + 2 * R, cy + R], start=110, end=250, fill=c, width=w)
img.save('resources/icon.png')
print('icon ok', img.size)
