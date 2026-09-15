import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def create_logo():
    # Logo dimensions: 200x60
    img = Image.new('RGBA', (200, 60), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Outer rounded box
    draw.rounded_rectangle([2, 2, 198, 58], radius=10, fill=(133, 195, 182), outline=(55, 113, 103), width=2)
    
    # Inner dark teal icon box
    draw.rounded_rectangle([8, 8, 52, 52], radius=6, fill=(76, 139, 128), outline=(40, 90, 80), width=1)
    
    try:
        font_big = ImageFont.truetype("arialbd.ttf", 26)
        font_small = ImageFont.truetype("arialbd.ttf", 14)
        font_text = ImageFont.truetype("arialbd.ttf", 15)
        font_sub = ImageFont.truetype("arialbd.ttf", 14)
    except:
        font_big = font_small = font_text = font_sub = ImageFont.load_default()
        
    # Draw 'A B C' logo mark inside square
    # A (large)
    draw.text((12, 12), "A", fill=(255, 255, 255), font=font_big)
    # B (superscript)
    draw.text((32, 11), "B", fill=(255, 255, 255), font=font_small)
    # C (subscript)
    draw.text((34, 30), "C", fill=(255, 255, 255), font=font_small)
    
    # Text on right: Logo Điện tử / ABC
    draw.text((62, 12), "Logo Điện tử", fill=(0, 0, 0), font=font_text)
    draw.text((95, 30), "ABC", fill=(0, 0, 0), font=font_sub)
    
    img.save("logo.png")
    print("Created logo.png")

def create_s24ultra():
    # 400x400 image inside rounded border container
    img = Image.new('RGB', (400, 400), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # Outer card frame (as seen in screenshot)
    draw.rounded_rectangle([5, 5, 395, 395], radius=16, fill=(250, 252, 253), outline=(180, 180, 180), width=2)
    
    # Background sparkles/stars
    sparkles = [(40, 80), (360, 90), (30, 250), (370, 260), (350, 310)]
    for sx, sy in sparkles:
        draw.text((sx, sy), "✦", fill=(160, 170, 180), font=ImageFont.load_default())
        
    # Phone shadow at base
    draw.ellipse([80, 360, 320, 380], fill=(220, 225, 230))
    
    # Left phone view / S-Pen
    # S-Pen
    draw.rounded_rectangle([75, 180, 83, 350], radius=4, fill=(120, 130, 140))
    draw.polygon([(75, 350), (83, 350), (79, 362)], fill=(90, 100, 110))
    
    # Left phone (back view)
    draw.rounded_rectangle([95, 120, 215, 360], radius=8, fill=(88, 108, 118), outline=(60, 80, 90), width=2)
    # Camera lenses on back
    cameras = [(115, 145), (115, 180), (115, 215), (145, 145), (145, 180)]
    for cx, cy in cameras:
        draw.ellipse([cx-10, cy-10, cx+10, cy+10], fill=(20, 25, 30), outline=(160, 170, 180), width=2)
        draw.ellipse([cx-5, cy-5, cx+5, cy+5], fill=(40, 50, 60))
        
    # Right phone (front display view)
    draw.rounded_rectangle([205, 100, 335, 360], radius=8, fill=(15, 20, 25), outline=(160, 170, 180), width=2)
    # Screen wallpaper (geometric polygon pattern)
    draw.polygon([(207, 102), (333, 102), (333, 358)], fill=(60, 85, 95))
    draw.polygon([(207, 102), (280, 358), (207, 358)], fill=(120, 150, 160))
    draw.polygon([(240, 140), (333, 200), (280, 358)], fill=(190, 210, 220))
    # Front camera hole
    draw.ellipse([267, 106, 273, 112], fill=(0, 0, 0))
    
    # Samsung logo on back phone
    try:
        font_sm = ImageFont.truetype("arial.ttf", 10)
    except:
        font_sm = ImageFont.load_default()
    draw.text((130, 310), "SAMSUNG", fill=(140, 160, 170), font=font_sm)

    img.save("s24ultra.jpg", quality=95)
    print("Created s24ultra.jpg")

def create_similar_images():
    # iPhone 15 Pro (60x60)
    img1 = Image.new('RGB', (60, 60), (240, 240, 245))
    d1 = ImageDraw.Draw(img1)
    d1.rounded_rectangle([10, 5, 50, 55], radius=6, fill=(70, 75, 80))
    # Camera bump
    d1.rounded_rectangle([14, 9, 32, 27], radius=4, fill=(55, 60, 65))
    d1.ellipse([16, 11, 22, 17], fill=(20, 20, 20))
    d1.ellipse([24, 11, 30, 17], fill=(20, 20, 20))
    d1.ellipse([16, 19, 22, 25], fill=(20, 20, 20))
    img1.save("iphone15.jpg", quality=95)

    # Xiaomi 14 Pro (60x60)
    img2 = Image.new('RGB', (60, 60), (240, 245, 240))
    d2 = ImageDraw.Draw(img2)
    d2.rounded_rectangle([10, 5, 50, 55], radius=6, fill=(60, 90, 75))
    # Square camera island
    d2.rounded_rectangle([14, 9, 34, 29], radius=3, fill=(25, 35, 30))
    d2.ellipse([16, 11, 23, 18], fill=(10, 15, 10))
    d2.ellipse([25, 11, 32, 18], fill=(10, 15, 10))
    d2.ellipse([16, 20, 23, 27], fill=(10, 15, 10))
    d2.ellipse([25, 20, 32, 27], fill=(10, 15, 10))
    img2.save("xiaomi14.jpg", quality=95)

    # Galaxy Z Fold5 (60x60)
    img3 = Image.new('RGB', (60, 60), (245, 240, 245))
    d3 = ImageDraw.Draw(img3)
    d3.rounded_rectangle([10, 5, 40, 55], radius=5, fill=(180, 190, 200))
    d3.rounded_rectangle([41, 5, 50, 55], radius=2, fill=(40, 50, 60))
    # Vertical camera strip
    d3.rounded_rectangle([14, 9, 22, 33], radius=4, fill=(30, 35, 40))
    d3.ellipse([15, 11, 21, 17], fill=(10, 10, 10))
    d3.ellipse([15, 18, 21, 24], fill=(10, 10, 10))
    d3.ellipse([15, 25, 21, 31], fill=(10, 10, 10))
    img3.save("zfold5.jpg", quality=95)

    print("Created iPhone, Xiaomi, and Z Fold5 thumbnails")

if __name__ == "__main__":
    create_logo()
    create_s24ultra()
    create_similar_images()
