import os
import requests
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

# 📍 Config
SAVE_DIR = "images/ai"
SLOGANS = [
    "बेजुबानों की सेवा, सबसे बड़ी मानवता है ❤️",
    "गर्मी में पानी दो, दुआएँ पाओ 🐦",
    "हर जानवर एक भावना है, वस्तु नहीं 🙏",
    "कृपा करो, करुणा बाँटो 🐾",
    "कुत्ते आपके दोस्त हैं, दुश्मन नहीं 🐶"
]

def get_today_slogan():
    return SLOGANS[datetime.now().day % len(SLOGANS)]

def fetch_image():
    url = "https://source.unsplash.com/800x600/?dog,animal"
    response = requests.get(url)
    return response.url

def download_image(url, save_path):
    data = requests.get(url).content
    with open(save_path, "wb") as f:
        f.write(data)

def overlay_slogan(image_path, slogan)
    if not os.path.exists(image_path) or os.path.getsize(image_path) < 1000:
        print(f"Skipping: {image_path} seems to be invalid or empty")
        return
    img = Image.open(image_path)
    img.verify()
    img = Image.open(image_path)
except Exception as e:
    print(f"Skipping image due to error: {e}")
    return 
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("DejaVuSans-Bold.ttf", 28)
    except:
        font = ImageFont.load_default()

    # Calculate text position
    margin = 20
    width, height = img.size
    text_width, text_height = draw.textsize(slogan, font=font)
    x = (width - text_width) // 2
    y = height - text_height - margin

    # Black background rectangle
    draw.rectangle([x - 10, y - 10, x + text_width + 10, y + text_height + 10], fill=(0, 0, 0, 160))
    draw.text((x, y), slogan, font=font, fill="white")

    img.save(image_path)

def main():
    os.makedirs(SAVE_DIR, exist_ok=True)
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"{today}.jpg"
    filepath = os.path.join(SAVE_DIR, filename)

    img_url = fetch_image()
    download_image(img_url, filepath)

    slogan = get_today_slogan()
    overlay_slogan(filepath, slogan)

    print(f"✅ Saved {filename} with slogan: {slogan}")

if __name__ == "__main__":
    main()
