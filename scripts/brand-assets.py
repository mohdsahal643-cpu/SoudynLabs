"""Generate deterministic social and favicon artwork from the supplied logo."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont
import base64
from io import BytesIO

ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'assets/img'
navy='#0F1F3D';raised='#162B52';mist='#C3CAD6';amber='#FFB03B'
mark=Image.open(OUT/'soudyn-mark-2x.webp').convert('RGBA')
for name,size in [('favicon-32.png',32),('apple-touch-icon.png',180),('icon-512.png',512)]:
    image=Image.new('RGBA',(size,size),navy)
    scale=min(size/mark.width,size/mark.height)
    resized=mark.resize((round(mark.width*scale),round(mark.height*scale)),Image.Resampling.LANCZOS)
    image.alpha_composite(resized,((size-resized.width)//2,(size-resized.height)//2))
    image.save(OUT/name)
data=base64.b64encode((OUT/'icon-512.png').read_bytes()).decode()
(OUT/'favicon.svg').write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewBox="0 0 512 512"><image width="512" height="512" href="data:image/png;base64,{data}"/></svg>\n',encoding='ascii')

def font(file,size):
    f=TTFont(ROOT/'assets/fonts'/file);f.flavor=None;data=BytesIO();f.save(data);data.seek(0)
    return ImageFont.truetype(data,size)

canvas=Image.new('RGBA',(1200,630),navy);draw=ImageDraw.Draw(canvas)
logo=Image.open(OUT/'soudyn-logo-source.webp').convert('RGBA');logo=logo.crop(logo.getchannel('A').getbbox())
canvas.alpha_composite(logo,(64,80))
heading=font('outfit-latin-600.woff2',48)
draw.multiline_text((64,240),'Elegant software for\neveryday business\nwork.',font=heading,fill='white',spacing=8)
body=font('source-sans-3-latin-400.woff2',23)
for i,text in enumerate(['Send quotation','Create invoice','Collect documents','Chase payment','Remind customer','Update status']):
    y=105+i*68;draw.rounded_rectangle((710,y,1136,y+54),radius=6,fill=raised,outline='#C3CAD6',width=1)
    draw.ellipse((730,y+23,738,y+31),fill=amber if i==5 else '#AFAFAF')
    draw.text((756,y+12),text,font=body,fill=mist)
canvas.convert('RGB').save(OUT/'og-image.png',optimize=True)
print('Generated favicon set, raster-backed SVG favicon and 1200 x 630 social image.')
