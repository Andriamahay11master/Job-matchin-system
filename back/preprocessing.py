import re

def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"http\S+|www\S+", "", text)
    text = re.sub(r"[^a-z\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def load_text(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return clean_text(f.read())
