import os
from PIL import Image, ImageDraw, ImageFont
import datetime
import random
import subprocess
import traceback

# 🧠 Emotionally Powerful Hindi Slogans for JeevMitra
slogans = [
    "पंछियों के लिए पानी का प्याला रखो 🐦",
    "एक जानवर की मुस्कान, आपकी मेहरबानी से 😇",
    "जीवों की सेवा, सच्ची भक्ति 🕊️",
    "छाया, पानी, और प्यार – यही जीवन है ❤️",
    "प्रकृति की रक्षा करो, पशु-पक्षी तुम्हारे अपने हैं 🌿",
    "जो जीवों से प्रेम करता है, वही सच्चा मानव है 🙏",
    "कुत्तों का साथ, भगवान का आशीर्वाद 🐾",
    "हर जीवन कीमती है – इंसान हो या जानवर 💧",
    "पशु सेवा ही परम सेवा है 🚩",
    "दया का दूसरा नाम – JeevMitra 🤝"
]

def overlay_slogan(image_path, slogan):
    try:
        img = Image.open(image_path).convert("RGBA")
        txt_layer = Image.new("RGBA", img.size, (255,255,255,0))
        draw = ImageDraw.Draw(txt_layer)

        font_size = int(min(img.size)/15)
        try:
            font = ImageFont.truetype("arial.ttf", font_size)
        except:
            font = ImageFont.load_default()

        text_width, text_height = draw.textsize(slogan, font=font)
        x = (img.width - text_width) / 2
        y = img.height - text_height - 30

        # Shadow + Main text
        draw.text((x+2, y+2), slogan, font=font, fill=(0,0,0,180))
        draw.text((x, y), slogan, font=font, fill=(255,255,255,255))

        out = Image.alpha_composite(img, txt_layer).convert("RGB")
        out.save(image_path)
        print(f"[✅] Processed: {image_path}")
        return True

    except Exception as e:
        print(f"[❌] Error processing {image_path}: {e}")
        traceback.print_exc()
        return False

def process_all_images():
    folder = "images/ai"
    if not os.path.exists(folder):
        print("[⛔] Folder does not exist:", folder)
        return False

    files = [f for f in os.listdir(folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    if not files:
        print("[ℹ️] No images found in", folder)
        return False

    any_updated = False
    for file in files:
        path = os.path.join(folder, file)
        slogan = random.choice(slogans)
        if overlay_slogan(path, slogan):
            any_updated = True

    return any_updated

def commit_and_push():
    try:
        subprocess.run(["git", "config", "--global", "user.name", "JeevMitra-AI"])
        subprocess.run(["git", "config", "--global", "user.email", "jeevmitra@bot.com"])
        subprocess.run(["git", "add", "."], check=True)
        result = subprocess.run(["git", "commit", "-m", f"🔄 Auto Image Update: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"], capture_output=True, text=True)

        if "nothing to commit" in result.stdout.lower():
            print("[ℹ️] No new changes to commit.")
        else:
            subprocess.run(["git", "push"], check=True)
            print("[🚀] Changes pushed to GitHub.")

    except subprocess.CalledProcessError as e:
        print("[❌] Git error:", e)
        traceback.print_exc()

if __name__ == "__main__":
    try:
        if process_all_images():
            commit_and_push()
        else:
            print("[⛔] No updates performed.")
    except Exception as e:
        print("[❌] Fatal error occurred:", e)
        traceback.print_exc()
