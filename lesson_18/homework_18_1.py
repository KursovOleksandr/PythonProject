import requests

BASE_URL = "https://images-api.nasa.gov"

# Пошук зображень
search_url = f"{BASE_URL}/search"
search_params = {
    "q": "Curiosity rover Mars", # пошуковий запит
    "media_type": "image", # тільки зображення
    "page_size": 20 # щоб було з чого вибрати
}

search_response = requests.get(search_url, params=search_params)
search_response.raise_for_status()

data = search_response.json()

# Витягуємо nasa_id
items = data.get("collection", {}).get("items", [])
nasa_ids = []

for item in items:
    data_block = item.get("data", [])
    if data_block:
        nasa_id = data_block[0].get("nasa_id")
        if nasa_id:
            nasa_ids.append(nasa_id)

print(f"Знайдено nasa_id: {nasa_ids[:5]}")

# asset + пошук JPG
def get_jpg_url(nasa_id):
    asset_url = f"{BASE_URL}/asset/{nasa_id}"
    response = requests.get(asset_url)
    response.raise_for_status()

    asset_data = response.json()
    items = asset_data.get("collection", {}).get("items", [])

    for item in items:
        href = item.get("href", "")
        if href.lower().endswith(".jpg"):
            return href

    return None

# завантаження
def download_image(url, filename):
    response = requests.get(url)
    response.raise_for_status()

    with open(filename, "wb") as f:
        f.write(response.content)

# логіка
downloaded = 0

for nasa_id in nasa_ids:
    jpg_url = get_jpg_url(nasa_id)

    if jpg_url:
        filename = f"mars_photo_{downloaded + 1}.jpg"
        print(f"Скачуємо: {jpg_url}")

        download_image(jpg_url, filename)
        downloaded += 1

    if downloaded == 2:
        break

print("Готово! Завантажено 2 зображення.")