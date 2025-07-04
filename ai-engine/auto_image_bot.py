
from PIL import Image, ImageDraw, ImageFont

def overlay_slogan(image_path, slogan):
    try:
        img = Image.open(image_path).convert("RGBA")
    except Exception as e:
        print(f"[❌] Error opening image: {e}")
        return  # image processing fail ho to skip karo

    # Transparent layer for slogan overlay
    txt_layer = Image.new("RGBA", img.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(txt_layer)

    # Font size and position settings
    font_size = int(min(img.size) / 15)
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        font = ImageFont.load_default()  # Fallback if arial not found

    # Text position - bottom center
    text_width, text_height = draw.textsize(slogan, font=font)
    x = (img.width - text_width) / 2
    y = img.height - text_height - 30

    # Draw text (black shadow + white text)
    draw.text((x+2, y+2), slogan, font=font, fill=(0, 0, 0, 150))  # shadow
    draw.text((x, y), slogan, font=font, fill=(255, 255, 255, 255))  # main

    # Merge with original image
    final_img = Image.alpha_composite(img, txt_layer)

    # Save as JPG (convert from RGBA to RGB)
    final_img = final_img.convert("RGB")
    final_img.save(image_path)

    print(f"[✅] Image processed successfully: {image_path}")
