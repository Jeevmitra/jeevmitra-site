import datetime
import random

EMOTIONS = [
    "प्यासा पक्षी",
    "अकेला कुत्ता",
    "घायल गाय",
    "छाया में आराम करता जानवर",
    "मानव और जानवर की मित्रता",
    "छोटे बच्चों और बेज़ुबानों का संबंध"
]

SLOGANS = {
    "प्यासा पक्षी": [
        "थोड़ा सा पानी, एक जान बचा सकता है।",
        "इन गर्म हवाओं में एक कटोरी जीवन है।"
    ],
    "अकेला कुत्ता": [
        "वो चुप है, पर भूख चिल्ला रही है।",
        "एक रोटी और थोड़ी दया – यही उसकी ज़िंदगी है।"
    ],
    "घायल गाय": [
        "ज़ख्म दिखते हैं, दर्द नहीं।",
        "चुपचाप सहने वालों को आवाज़ दो।"
    ],
    "छाया में आराम करता जानवर": [
        "सुकून की छाया भी सेवा है।",
        "धूप से नहीं, दया से ठंडक मिलती है।"
    ],
    "मानव और जानवर की मित्रता": [
        "ये रिश्ता खून का नहीं, करुणा का है।",
        "मित्र वही, जो मौन को समझे।"
    ],
    "छोटे बच्चों और बेज़ुबानों का संबंध": [
        "मासूमियत को मासूमियत से पहचान मिलती है।",
        "बच्चा और पिल्ला – दोनों को प्यार चाहिए।"
    ]
}

def decide_emotion():
    index = datetime.datetime.now().day % len(EMOTIONS)
    return EMOTIONS[index]

def pick_slogan(emotion):
    return random.choice(SLOGANS.get(emotion, ["सेवा सबसे बड़ा धर्म है।"]))

def think_today():
    emotion = decide_emotion()
    slogan = pick_slogan(emotion)
    return {
        "emotion": emotion,
        "slogan": slogan
    }

if __name__ == "__main__":
    today_thought = think_today()
    print("🧠 AI Thought for Today")
    print("Emotion:", today_thought['emotion'])
    print("Slogan:", today_thought['slogan'])
