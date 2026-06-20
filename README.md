# PDF Symbol Extractor

A Python-based system for extracting symbols from PDF documents and representing them as editable symbol entities with structured metadata. The project processes PDF files, identifies both embedded image symbols and vector-based drawing symbols, generates metadata automatically, and provides REST APIs for managing custom properties.

## Overview

Engineering and technical PDF documents often contain symbols represented as a combination of embedded images, vector drawings, and text annotations. This project extracts visible symbols from PDF files, converts them into individual symbol entities, generates metadata for each extracted symbol, and exposes them through a FastAPI-based backend.

Each extracted symbol can be assigned custom properties such as tags, descriptions, and status information through API endpoints.

## Features

* Extract visible symbols from PDF documents
* Support both raster image symbols and vector drawing symbols
* Automatically generate metadata for extracted symbols
* Store symbol information in JSON format
* Retrieve symbol information through REST APIs
* Assign and update custom properties for symbols
* Health monitoring endpoint
* Interactive API documentation using Swagger UI
* Lightweight and extensible architecture

## System Workflow

```text
PDF Document
      │
      ▼
PDF Analysis
      │
      ▼
Image & Vector Symbol Extraction
      │
      ▼
Metadata Generation
      │
      ▼
JSON Storage
      │
      ▼
FastAPI Backend
```

## Project Structure

```text
pid-symbol-extractor/
│
├── images/
│   ├── swagger-ui.png
│   ├── get-symbol.png
│   └── update-symbol.png
│
├── input/
│   └── Code Breaker.pdf
│
├── outputs/
│   ├── metadata/
│   │   └── symbols.json
│   │
│   └── pages/
│       └── Code Breaker_page_1.png
│
├── .gitignore
├── README.md
├── app.py
├── detect_vector_drawings.py
├── extract_drawings.py
├── extract_symbols.py
├── generate_metadata.py
├── models.py
├── pdf_to_image.py
└── requirements.txt
```

## Architecture

```text
PDF Document
      │
      ▼
PyMuPDF Processing
      │
      ├──────────────┐
      ▼              ▼
Image Extraction   Vector Drawing Extraction
      │              │
      └──────┬───────┘
             ▼
      Symbol Generation
             │
             ▼
      Metadata Generation
             │
             ▼
         symbols.json
             │
             ▼
          FastAPI
```

## Screenshots

### API Documentation

Interactive Swagger UI for testing and exploring API endpoints.

![Swagger UI](images/swagger-ui.png)

---

### Retrieving Extracted Symbols

The `/symbols` endpoint returns all extracted symbols along with their metadata and assigned properties.

![Get Symbols](images/get-symbol.png)

---

### Updating Symbol Properties

Custom properties can be assigned and updated using the PUT endpoint.

Example:

```json
{
    "tag": "PV-1000",
    "status": "active",
    "description": "Pressure Vessel"
}
```

![Update Symbol](images/update-symbol.png)

---

## Installation

```bash
git clone https://github.com/manishmahara23/pid-symbol-extractor.git

cd pid-symbol-extractor

python -m venv .venv

.venv\Scripts\activate

pip install -r requirements.txt
```

## Usage

### 1. Extract Embedded Symbols

```bash
python extract_symbols.py
```

### 2. Extract Vector Drawing Symbols

```bash
python extract_drawings.py
```

### 3. Generate Metadata

```bash
python generate_metadata.py
```

### 4. Run the API

```bash
uvicorn app:app --reload
```

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

## API Endpoints

| Method | Endpoint             | Description                |
| ------ | -------------------- | -------------------------- |
| GET    | /                    | API information            |
| GET    | /health              | Health check               |
| GET    | /symbols             | Retrieve all symbols       |
| GET    | /symbols/{symbol_id} | Retrieve a specific symbol |
| PUT    | /symbols/{symbol_id} | Update symbol properties   |

## Example Metadata

```json
{
    "symbol_id": "shape_0",
    "symbol_type": "engineering_symbol",
    "image_path": "extracted_symbols/shape_0.png",
    "properties": {
        "tag": "",
        "status": "pending",
        "description": ""
    }
}
```

## Technologies Used

* Python
* FastAPI
* PyMuPDF
* Pydantic
* Uvicorn
* JSON

## Challenges

One of the primary challenges was handling symbols represented as vector drawing objects rather than embedded images. The initial implementation extracted only embedded raster images. The extraction pipeline was later extended to analyze vector drawing elements, group related drawing primitives and associated labels, and represent them as complete symbol entities.

## Future Improvements

* Automatic symbol classification
* SVG export support
* Search and filtering capabilities
* Symbol similarity matching
* Database integration

## Author

**Manish Mahara**

B.Tech CSE (AI/ML & Robotics)
DIT University
