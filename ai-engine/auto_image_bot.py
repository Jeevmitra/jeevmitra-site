
import os
import requests
from datetime import datetime

# Daily slogan list
SLOGANS = [
    "हर जानवर में भगवान का अंश होता है। 🙏",
    "बेजुबानों की सेवा ही सच्ची सेवा है। ❤️",
    "प्रेम बांटो, भोजन दो, जीवन दो। 🐾",
    "गर्मी में परिंदों को पानी देना हमारा धर्म है। 🕊️",
    "कुत्तों को दुत्कारो नहीं, दुआओं का हक़दार समझो। 🐶",
    "सेवा करो, संवेदना फैलाओ, जीवन बचाओ। 🌱"
]

# Get today's slogan
today_slogan = SLOGANS[datetime.now().day % len(SLOGANS)]

# Get image from the web (Unsplash API-like)
def fetch_random_animal_image():
    url = "https://source.unsplash.com/600x400/?dog,animal,bird"
    response = requests.get(url)
    return response.url

# Save image to local folder
def save_image(image_url, save_path):
    response = requests.get(image_url)
    with open(save_path, 'wb') as f:
        f.write(response.content)

# Main logic
def main():
    img_url = fetch_random_animal_image()
    now = datetime.now().strftime("%Y-%m-%d")
    img_filename = f"daily_{now}.jpg"
    save_dir = "images/ai/"
    os.makedirs(save_dir, exist_ok=True)
    save_path = os.path.join(save_dir, img_filename)

    save_image(img_url, save_path)

    # Save slogan too
    with open(f"{save_dir}slogan_{now}.txt", "w", encoding='utf-8') as f:
        f.write(today_slogan)

    print(f"✔️ Image and slogan saved for {now}")

if __name__ == "__main__":
    main()
