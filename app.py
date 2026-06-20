from fastapi import FastAPI, HTTPException
import json
import os

app = FastAPI(
    title="Diagram Symbol API",
    version="1.0.0"
)

METADATA_FILE = "outputs/metadata/symbols.json"


def load_symbols():
    """
    Load symbols from metadata file
    """

    if not os.path.exists(METADATA_FILE):
        return []

    with open(METADATA_FILE, "r") as f:
        return json.load(f)


def save_symbols(symbols):
    """
    Save symbols back to metadata file
    """

    with open(METADATA_FILE, "w") as f:
        json.dump(
            symbols,
            f,
            indent=4
        )


@app.get("/")
def home():

    return {
        "message": "Diagram Symbol API",
        "status": "running"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "PDF Symbol Extractor API"
    }

@app.get("/symbols")
def get_symbols():

    return load_symbols()


@app.get("/symbols/{symbol_id}")
def get_symbol(symbol_id: str):

    symbols = load_symbols()

    for symbol in symbols:

        if symbol["symbol_id"] == symbol_id:
            return symbol

    raise HTTPException(
        status_code=404,
        detail="Symbol not found"
    )


@app.put("/symbols/{symbol_id}")
def update_symbol(
    symbol_id: str,
    properties: dict
):

    symbols = load_symbols()

    for symbol in symbols:

        if symbol["symbol_id"] == symbol_id:

            symbol["properties"].update(
                properties
            )

            save_symbols(symbols)

            return {
                "message": "Symbol updated",
                "symbol": symbol
            }

    raise HTTPException(
        status_code=404,
        detail="Symbol not found"
    )