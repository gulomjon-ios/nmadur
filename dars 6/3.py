import re
from pathlib import Path

import requests

url = "https://www.threads.com/@moshinasale/post/C-dIoYRNzD4?hl=ja"

response = requests.get(url, timeout=30)

if response.status_code != 200:
    raise RuntimeError(f"Saytni yuklashda xatolik: {response.status_code}")

html = response.text
image_urls = re.findall(
    r'https?://[^\"\'\s]+(?:jpg|jpeg|png|webp|gif)',
    html,
    flags=re.IGNORECASE,
)

if not image_urls:
    raise RuntimeError("Saytdan rasm linki topilmadi.")

image_url = image_urls[0]
image_response = requests.get(image_url, timeout=30)
image_response.raise_for_status()

if not image_response.headers.get("Content-Type", "").startswith("image/"):
    raise RuntimeError("Topilgan link rasm emas.")

file_path = Path("downloaded_image.jpg")
file_path.write_bytes(image_response.content)

print(f"Rasm yuklandi: {file_path.resolve()}")
print(f"Rasm URL: {image_url}")