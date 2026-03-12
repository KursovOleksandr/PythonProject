import os
import json
import logging

folder_path = "work_with_json"

logging.basicConfig(
    filename="json_kursov.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

for file_name in os.listdir(folder_path):
    if file_name.endswith(".json"):
        file_path = os.path.join(folder_path, file_name)

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                json.load(f)

        except json.JSONDecodeError as e:
            logging.error(f"Invalid JSON file: {file_name} | Error: {e}")

        except Exception as e:
            logging.error(f"Error processing file: {file_name} | Error: {e}")