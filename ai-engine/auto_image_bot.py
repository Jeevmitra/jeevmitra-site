        
import os
import random
import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

def download_random_image():
    try:
        search_urls = [
            "https://source.unsplash.com/800x600/?animal",
            "https://source.unsplash.com/800x600/?dog",
            "https://source.unsplash.com/800x600/?bird",
            "https://source.unsplash.com/800x600/?nature,animal",
            "https://source.unsplash.com/800x600/?wildlife"
        ]
        url = random.choice(search_urls)
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            image = Image.open(BytesIO(response.content)).convert("RGB")
            filename = "images/ai/auto_" + str(random.randint(1000, 9999)) + ".jpg"
            image.save(filename)
            return filename
        else:
            print("⚠️ Failed to fetch image.")
    except Exception as e:
        print("❌ Error fetching image:", e)
    return None

def overlay_slogan(image_path, slogan):
    try:
        image = Image.open(image_path).convert("RGB")
        draw = ImageDraw.Draw(image)
        font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
        font_size = int(image.width / 18)

        try:
            font = ImageFont.truetype(font_path, font_size)
        except:
            font = ImageFont.load_default()

        text_width, text_height = draw.textsize(slogan, font=font)
        x = (image.width - text_width) // 2
        y = image.height - text_height - 40

        for dx in range(-2, 3):
            for dy in range(-2, 3):
                draw.text((x+dx, y+dy), slogan, font=font, fill="black")

        draw.text((x, y), slogan, font=font, fill="white")
        image.save(image_path)

    except Exception as e:
        print("❌ Error overlaying slogan:", e)

if __name__ == "__main__":
    slogans = [
        "प्रेम ही सच्ची सेवा है 🐾",
        "जीवों से करों प्यार, जीवन होगा उद्धार ❤️",
        "मूक जीवों की रक्षा करें 🌱",
        "परिंदों को पानी दें, पुण्य कमाएं 🕊️",
        "भूखे कुत्तों को भोजन, सबसे बड़ा धर्म 🙏",
        "जहाँ दया है, वहीं ईश्वर है 🌼"
    ]

    slogan = random.choice(slogans)
    downloaded_image = download_random_image()

    if downloaded_image:
        overlay_slogan(downloaded_image, slogan)
        print(f"✅ Done: {downloaded_image}")
    else:
        print("⚠️ No image processed.")
