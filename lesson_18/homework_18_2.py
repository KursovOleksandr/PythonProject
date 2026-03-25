import requests
import os

BASE_URL = "http://127.0.0.1:8080"


image_path = "mars_photo_1.jpg"   # треба покласти mars_photo_1.jpg поруч зі скриптом

# POST
with open(image_path, "rb") as img:
    files = {
        "image": (os.path.basename(image_path), img, "image/jpeg")
    }

    response = requests.post(f"{BASE_URL}/upload", files=files)

response.raise_for_status()

upload_data = response.json()
image_url = upload_data["image_url"]

print("Upload success")
print("Image URL:", image_url)

filename = image_url.split("/")[-1]

# GET
headers = {
    "Content-Type": "text"
}

get_response = requests.get(
    f"{BASE_URL}/image/{filename}",
    headers=headers
)

get_response.raise_for_status()

print("\nGET response")
print(get_response.json())

# DELETE
delete_response = requests.delete(
    f"{BASE_URL}/delete/{filename}"
)

delete_response.raise_for_status()

print("\nDELETE response")
print(delete_response.json())