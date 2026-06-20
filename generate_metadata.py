import os
import json
import re

OUTPUT_DIR = "extracted_symbols"
METADATA_FILE = "outputs/metadata/symbols.json"


def natural_sort_key(filename):
    return [
        int(text) if text.isdigit() else text.lower()
        for text in re.split(r'(\d+)', filename)
    ]


def generate_metadata():

    metadata_list = []

    os.makedirs(
        os.path.dirname(METADATA_FILE),
        exist_ok=True
    )

    if not os.path.exists(OUTPUT_DIR):
        print(
            f"Error: Directory '{OUTPUT_DIR}' not found."
        )
        return

    files = sorted(
        os.listdir(OUTPUT_DIR),
        key=natural_sort_key
    )

    for filename in files:

        if not (
            filename.lower().endswith(".png")
            or filename.lower().endswith(".jpg")
            or filename.lower().endswith(".jpeg")
        ):
            continue

        symbol_name = os.path.splitext(filename)[0]

        symbol_data = {
            "symbol_id": symbol_name,
            "symbol_type": "engineering_symbol",
            "image_path": os.path.join(
                OUTPUT_DIR,
                filename
            ),
            "properties": {
                "tag": "",
                "status": "pending",
                "description": ""
            }
        }

        metadata_list.append(
            symbol_data
        )

    with open(
        METADATA_FILE,
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(
            metadata_list,
            f,
            indent=4
        )

    print(
        f"Generated metadata for "
        f"{len(metadata_list)} symbols"
    )

    print(
        f"Saved: {METADATA_FILE}"
    )


if __name__ == "__main__":
    generate_metadata()