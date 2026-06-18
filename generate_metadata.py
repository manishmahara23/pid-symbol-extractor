import os
import json

SYMBOL_DIR = "extracted_symbols"
OUTPUT_DIR = "outputs/metadata"

os.makedirs(
    OUTPUT_DIR,
    exist_ok=True
)

symbols = []

if os.path.exists(SYMBOL_DIR):

    image_files = sorted(
        [
            f for f in os.listdir(SYMBOL_DIR)
            if f.lower().endswith(
                (".png", ".jpg", ".jpeg")
            )
        ]
    )

    for idx, file_name in enumerate(
        image_files,
        start=0
    ):

        symbols.append(
            {
                "symbol_id": f"symbol_{idx}",
                "symbol_type": "image",
                "image_path": os.path.join(
                    SYMBOL_DIR,
                    file_name
                ),
                "properties": {}
            }
        )

metadata_path = os.path.join(
    OUTPUT_DIR,
    "symbols.json"
)

with open(
    metadata_path,
    "w"
) as f:

    json.dump(
        symbols,
        f,
        indent=4
    )

print(
    f"Generated metadata for {len(symbols)} symbols"
)

print(
    f"Saved: {metadata_path}"
)